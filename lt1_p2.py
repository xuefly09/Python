# -*- coding: utf-8 -*-
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from heapq import heappop, heappush

class Simulator(object):
    "simulating the environment"
    def __init__(self):
        # current time
        self.currenttime = 0
        # events in the simulated process
        self.queue = []
        # process in the simulation(arrival, serve)
        self.processes = []
    "initialize(reset) the state"
    def reset(self):
        self.currenttime = 0
        self.queue = []
        for p in self.processes:
            p.reset()
            p.activate()
    "using data struct heap to simulate the process of events"
    def schedule(self, delay, event):
        heappush(self.queue, (self.currenttime + delay, event))
    # the newst timestamp
    def peek(self):
        return self.queue[0][0]
    
    "excute the event"
    def _step(self):
        self.currenttime, event = heappop(self.queue)
        event()
        
    def step(self):
        if not self.queue:
            raise RuntimeError('no generators defined')
        self._step()
    
    "the function run() is like controller, whihc begin the whole simulation"
    def run(self, until=1000):
        if not self.queue:
            raise RuntimeError('no generators defined')
        while self.currenttime < until:
            self._step()

class Process(object):
    "class process simulates a single request"
    
    # out = the service
    def __init__(self, sim, dist, out):
        self.sim = sim
        self.sim.processes.append(self)
        if not callable(dist):
            raise TypeError('dist must be callable')
        self.dist = dist
        self.out = out
        self.reset()
        self.activate()
        
    def reset(self):
        pass
    
    def activate(self):
        raise NotImplementedError

class Monitor(object):
    "gathering the information and data"
    
    def __init__(self, sim):
        self.sim = sim
        self.reset()
        
    def reset(self):
        self.last = 0
        # list of the real time between two events Tq
        self.dt = []
        # list of Q in the queue
        self.Qt = []
        # list of the state of server(idle or busy)
        self.Ut = []
    
    def observe(self, queue, server):
        self.dt.append(self.sim.currenttime - self.last)
        self.last = self.sim.currenttime
        self.Qt.append(queue)
        self.Ut.append(server)

# Decorator for methods
def monitor(func):
    def new_func(self, *args, **kwargs):
        if self.mon:
            self.mon.observe(self.queue, self.busy)
        return func(self, *args, **kwargs)
    return new_func

class Generator(Process):
    "request generator"
    
    def __init__(self, sim, dist, out=None):
        if not out or not isinstance(out, Resource):
            raise TypeError('no resource connected')
        super(Generator, self).__init__(sim, dist, out)
        
    def activate(self):
        delay = self.dist()
        "grab a request"
        sim.schedule(delay, self.out.seize)
        delay = self.dist()
        "ready to grab next requests"
        sim.schedule(delay, self.activate)

class Resource(Process):
    "simulation of the resource(service) of the M/M/1"
    
    "defaulty, set capacity=1(one request served per timeS) and queue_size wiht inf, dist is a functioin that will set the Ts"
    def __init__(self, sim, dist, capacity=1, queue_size=float('inf'), out=None, mon=None):
        if out and not isinstance(out, Resource):
            raise TypeError('no resource connected')
        self.queue_size = queue_size
        self.capacity = capacity
        # monitor
        self.mon = mon
        super(Resource, self).__init__(sim, dist, out)
    
    "initialize the state of the service"
    def reset(self):
        self.queue = 0
        self.busy = 0
        if self.mon:
            self.mon.reset()
    
    def activate(self):
        pass
    
    "action when a birth event generated"
    @monitor
    def seize(self):
        # Serve or enqueue
        if self.busy < self.capacity:
            self.busy += 1
            sim.schedule(self.dist(), self.release)
        elif self.queue < self.queue_size:
            self.queue += 1
            
    "action when a death event generated"
    @monitor
    def release(self):
        if self.out:
            sim.schedule(0, self.out.seize)
        # Serve another or halt
        if self.queue:
            self.queue -= 1
            sim.schedule(self.dist(), self.release)
        else:
            self.busy -= 1

def exp(lamda):
    rannum = random.uniform(0, 1)
    res = (-1.0/lamda)*math.log(rannum)
    return res

def MM1_simulation(lamda, ts, sim):
    la = lamda
    mu = 1/ts
    rho = la/mu
    
    "service time"
    exp_service = partial(exp, mu)
    "arrival interval time"
    exp_arrival = partial(exp, la)
    
    sim = sim
    
    mon = Monitor(sim)
    server = Resource(sim, exp_service, mon=mon)
    gen = Generator(sim, exp_arrival, out=server)
    
    
    sim.run(until=1000)
    
    ### Figures
    dt = np.array(mon.dt)
    Ut = np.array(mon.Ut)
    Qt = np.array(mon.Qt)
    
    axis = plt.subplot()
    axis.set_title('M/M/1, $\lambda={}, \mu={}$'.format(la, mu))
    
    t = dt.cumsum()
    axis.step(t, Ut, label='Instantaneous server utilisation')
    axis.step(t, Qt, label='Instantaneous queue utilisation')
    N_average_t = ((Ut + Qt) * dt).cumsum() / t
    axis.plot(t, N_average_t, label='Average system utilisation')
    axis.axhline(rho/(1-rho), linewidth=2, color='black', ls='--', label='Theoretical average')
    
    axis.set_xlabel('time')
    axis.set_ylabel('number of customers')
    axis.legend()
    
    plt.show()


if __name__ == "__main__":
    
    
    sim = Simulator()
    print("Simulation of a)\n")
    MM1_simulation(5, 0.15, sim)
    sim = Simulator()
    print("Simulation of d)\n")
    MM1_simulation(6, 0.15, sim)
    sim = Simulator()
    print("Simulation of e)\n")
    MM1_simulation(6, 0.2, sim)
    