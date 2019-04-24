import hashlib
import threading
import time
import random
import string
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("st6")

class POW(object):
    def __init__(self, message, difficulty = 1):
        self.message = message
        self.difficulty = difficulty
        #How many hashes will be calculated per block
        self.block_size = 100000
        #The current block number
        self.block = 0 

        #Once the POW is found by a worker thread the hash found is save here
        self.hash = None
        #Once POW is found the nonce used by the worker thread is saved here
        self.nonce = None

    def get_next_block(self):
        if not self.hash:
            self.block += self.block_size
        return self.block

    def valid_prefix(self, hash):
        """Determine if the hash is prepended by the right number of zeros"""
        return hash[:self.difficulty] == "".join(['0'] * self.difficulty)

    def create(self, parallelize):
        "create threads"
        workers = []
        for i in range(parallelize):
            t = threading.Thread(target = self.worker, args = (), name = 'thread-' + str(i))
            t.start()
            workers.append(t)
        "wait for all threads"
        for w in workers:
            w.join()
        "if failed to find a valid hash, start searching again"
        while self.nonce == None and self.hash == None:
            self.create(parallelize)
        """ Create and return the hash and nonce as POW. The parallelizable argument 
        specifies the number of worker threads to invoke. 
        
        Implement me!
        
        """
        return (self.hash, self.nonce)

    def worker(self):
        cnounce = None
        cmessage = None
        hashfn = hashlib.sha256
        "this is a critical section"
        lock = threading.Lock()
        lock.acquire()
        cblock = self.get_next_block()
        lock.release()
        for i in range(self.block_size):      
           if self.nonce == None and self.hash == None:
               cnounce = str(cblock+i)
               cmessage = self.message + cnounce
               cmessage = cmessage.encode("utf-8")
               cmessage = hashfn(cmessage).hexdigest()
               flag_res = self.valid_prefix(cmessage)
               "this is the critical section"
               if(flag_res):
                   if self.nonce == None and self.hash == None:
                       lock.acquire()
                       self.nonce = cnounce
                       self.hash = cmessage
                       logger.info("Main thread name = {}".format(threading.current_thread().name))
                       lock.release()
                       return
                   else:
                       return
           else:
               return
        """
        Implement me!

        Loop until a nonce is found that creates a valid POW. 
        First request the next block, and then iterate over block size. 
        Compute the nonce, which is the block + current iteration and 
        then set the nonce as the suffix to the original message. Generate the SHA256 
        of the message+nonce and test whether the hash is valid, if so 
        update the class hash and nonce and stop iterating. 

        """

def main():
    # Message to generate a POW for
    message = "Attack at dawn"
    # Number of zeros that the hexdigest of the hash must start with
    difficulty = 5
    pow = POW(message, difficulty)
    hash, nonce = pow.create(parallelize=5)
    print ("Message:", message, "Pow", hash, "found with nonce", nonce)


if __name__ == "__main__":
    main()



