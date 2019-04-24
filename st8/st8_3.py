# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:45:54 2017

@author: Jiafei Xue
"""
import threading
import logging
import json
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Data")

class imuData(object):
    def __init__(self, hjson):
        self.xgyro = hjson['xgyro']
        self.zmag = hjson["zmag"]
        self.ygyro = hjson["ygyro"]
        self.xmag = hjson["xmag"]
        self.diff_pressure = hjson["diff_pressure"]
        self.zacc = hjson["zacc"]
        self.xacc = hjson["xacc"]
        self.yacc = hjson["yacc"]
        self.abs_pressure = hjson["abs_pressure"]
        self.fields_updated = hjson["fields_updated"]
        self.zgyro = hjson["zgyro"]
        self.pressure_alt = hjson["pressure_alt"]
        self.mavpackettype = hjson["mavpackettype"]
        self.ymag = hjson["ymag"]
        self.time_usec = hjson["time_usec"]
        self.temperature = hjson["temperature"]

class gpsData(object):
    def __init__(self, hjson):
        self.vx = hjson["vx"]
        self.lon = hjson["lon"]
        self.time_boot_ms = hjson["time_boot_ms"]
        self.hdg = hjson["hdg"]
        self.relative_alt = hjson["relative_alt"]
        self.vy = hjson["vy"]
        self.lat = hjson["lat"]
        self.mavpackettype = hjson["mavpackettype"]
        self.alt = hjson["alt"]
        self.vz = hjson["vz"]

class dataDistributor(object):
    def __init__(self, imuFile, gpsFile):
        self.imu = imuFile
        self.gps = gpsFile

    def loadData(self):
        file = open(self.imu)
        words = file.read().split('\n')
        file.close()
        self.imuList = [imuData for n in range(len(words))]
        i = 0
        for st in words:
            nimu = imuData(json.loads(st))
            self.imuList[i] = nimu
            i += 1
        file = open(self.gps)
        words = file.read().split('\n')
        file.close()
        self.gpsList = [gpsData for n in range(len(words))]
        i = 0
        for st in words:
            ngps = gpsData(json.loads(st))
            self.gpsList[i] = ngps
            i += 1
        
    def getData(self, index, tag):
        if tag == 1:
            return self.imuList[index]
        else:
            return self.getData[index]


class dataPublisher(object):
    def __init__(self, condition, topic):
        self.topic = topic
        self.subscriber = None
        self.topic = topic
        self.condition = condition
        
    def publish(self, data):
        self.edata = data
        self.condition.acquire()
        self._write_data()
        self._notify_subscriber()
        self.condition.notify_all()
        self.condition.release()
        
    def _notify_subscriber(self):
        if self.subscriber:
            self.subscribe()
            
    def subscribe(self, callback):
        self.subscriber = callback
    
    def _write_data(self):
        return

class imuPublisher(dataPublisher):
    def __init__(self, condition, topic):
        super(imuPublisher, self).__init__(condition, topic)
        
    def _write_data(self):
        strres = ""
        strtopic = ""
        if self.topic == 1:
            strtopic = "Accelerometer\n"
            strres = "time_usec: \n" + str(self.edata.time_usec) + "\nxacc:" + str(self.edata.xacc) + "\nyacc: " + str(self.edata.yacc) + "\nzacc: " + str(self.edata.zacc)
        else:
            strtopic = "Gyroscope\n"
            strres = "time_usec: \n" + str(self.edata.time_usec) + "\nxgyro:" + str(self.edata.xgyro) + "\nygyro: " + str(self.edata.ygyro) + "\nzgyro: " + str(self.edata.zgyro)
        logger.info("Data Publish {} {}".format(strtopic, strres))
        
class gpsPublisher(dataPublisher):
    def __init__(self, condition, topic):
        super(gpsPublisher, self).__init__(condition, topic)
        
    def _write_data(self):
        strres = ""
        strtopic = "Position\n"
        if self.topic == 1:
            strres = "time_boot_ms: \n" + str(self.edata.time_boot_ms) + "\nlat:" + str(self.edata.lat) + "\nlon: " + str(self.edata.lon)
        logger.info("Data Publish {} {}".format(strtopic, strres))    

class dataSubscriber(threading.Thread):
    def __init__(self, condition, data, topic, publisher):
        self.blockTime = 0
        self.timeStamp = 0
        self.lastTst = 0
        self.index = 0
        self.pub = publisher
        self.topic = topic
        self.condition = condition
        self.edata = data
        self.message_ready = False
        super(dataSubscriber, self).__init__()
        
    def treatData(self, data):
        self.pub.publish(data)
        
    def setTimestamp(self, data):
        return
        
    def run(self):
        while True:
            self.condition.acquire()
            while True:
                if self.condition.acquire():
                    data = self.edata[self.index]
                    self.index += 1
                    self.setTimestamp(data)
                    logger.info("Subscribe: {} {}".format(threading.current_thread().name, self.topic))
                    self.treatData(data)
                    self.message_ready = False
                    break
            self.condition.wait(self.blockTime)
            
    def callback(self):
        self.message_ready = True

class imuDts(dataSubscriber):
    def __init__(self, condition, data, topic, publisher):
        super(imuDts, self).__init__(condition, data, topic, publisher)
        
    def treatData(self, data):
        self.pub.publish(self.edata[self.index])
        
    def setTimestamp(self, data):
        if self.lastTst == 0:
            self.blockTime = 20000/1000000
        else:
            self.timeStamp = data.time_usec
            self.blockTime = (self.timeStamp-self.lastTst)/1000000
        self.lastTst = self.timeStamp

class gpsDts(dataSubscriber):
    def __init__(self, condition, data, topic, publisher):
        super(gpsDts, self).__init__(condition, data, topic, publisher)
        
    def treatData(self, data):
        self.pub.publish(self.edata[self.index])
        
    def setTimestamp(self, data):
        if self.lastTst == 0:
            self.blockTime = 20/1000
        else:
            self.timeStamp = data.time_boot_ms
            self.blockTime = (self.timeStamp-self.lastTst)/1000
        self.lastTst = self.timeStamp

class dataCollector(object):
    def __init__(self):
        self.timeImu = []
        self.timeGps = []
        self.xgyro = []
        self.ygyro = []
        self.zgyro = []
        self.xacc = []
        self.yacc = []
        self.zacc = []
        self.lon = []
        self.lat = []
        
       
if __name__ == "__main__":

    # Everything runs forever, get ready to killall python
    allData = dataDistributor("st_8-imu.txt", "st_8-gps.txt")
    allData.loadData()
    
    dataCol = dataCollector()
    
    
    ct = 0
    for imuD in allData.imuList:
        dataCol.timeImu.append(imuD.time_usec - ct)
        dataCol.xgyro.append(imuD.xgyro)
        dataCol.ygyro.append(imuD.ygyro)
        dataCol.zgyro.append(imuD.zgyro)
        dataCol.xacc.append(imuD.xacc)
        dataCol.yacc.append(imuD.yacc)
        dataCol.zacc.append(imuD.zacc)
        ct = imuD.time_usec
        
    ct = 0
    for gpsD in allData.gpsList:
        dataCol.timeGps.append(gpsD.time_boot_ms - ct)
        dataCol.lon.append(gpsD.lon)
        dataCol.lat.append(gpsD.lat)
        ct = gpsD.time_boot_ms
    
    tm = np.array(dataCol.timeImu)
    roll = np.array(dataCol.xgyro)
    pitch = np.array(dataCol.ygyro)
    yaw = np.array(dataCol.zgyro)
    x = np.array(dataCol.xacc)
    y = np.array(dataCol.yacc)
    z = np.array(dataCol.zacc)
    lon = np.array(dataCol.lon)
    lat = np.array(dataCol.lat)
    
    angSp = "degrees/second"
    axis = plt.subplot()
    
    
    t = tm.cumsum()
    axis.step(t, roll, label='Instantaneous roll')
    axis.step(t, pitch, label='Instantaneous pitch')
    axis.step(t, pitch, label='Instantaneous yaw')
    axis.set_xlabel('time')
    axis.set_ylabel('angular speeds') 
    axis.legend()
    plt.show()
    
    t = tm.cumsum()
    axis = plt.subplot()
    axis.step(t, x, label='Instantaneous x acceleration')
    axis.step(t, y, label='Instantaneous y acceleration')
    axis.step(t, z, label='Instantaneous z acceleration')
    axis.set_xlabel('time')
    axis.set_ylabel('acceleration') 
    axis.legend()
    plt.show()
    
    tm = np.array(dataCol.timeGps)
    t = tm.cumsum()
    plt.plot(lon, lat)
    plt.show()
    
    
    condition1 = threading.Condition()
    condition2 = threading.Condition()
    condition3 = threading.Condition()
    pubImu1 = imuPublisher(condition1, 1)
    pubImu2 = imuPublisher(condition2, 2)
    pubGps = gpsPublisher(condition3, 1)
    subImuAccelerometer = imuDts(condition1, allData.imuList, "Accelerometer", pubImu1)
    subImuGyroscope = imuDts(condition2, allData.imuList, "Gyroscope", pubImu2)
    subGpsPosition = gpsDts(condition3, allData.gpsList, "GpsPosition", pubGps)
    subImuAccelerometer.start()
    subImuGyroscope.start()
    subGpsPosition.start()
    
    



























