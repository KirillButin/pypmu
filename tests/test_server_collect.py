import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading

SLEEP_TIME = 1.0/100



def test_client_single_pmu():
    
    pmu = create_pmu(9006)  
    pmu.ieee_data_sample.set_freq(1)

    cnt = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:                       
            pmu.send(pmu.ieee_data_sample)             
            
    pmu.join()

def test_client_2_pmus():
    
    pmus = [create_pmu(port) for port in [9007, 9008]]
    
    for i, pmu in enumerate(pmus):
        pmu.ieee_data_sample.set_freq(i+1)

    
    cnt = 0
    while True:
        sleep(SLEEP_TIME)        
        for pmu in pmus:                    
            pmu.send(pmu.ieee_data_sample)             
            
    for pmu in pmus:            
        pmu.join()


def test_client_10_pmus():
    
    nSources = 4
    pmus = [create_pmu(port, log_level='DEBUG') for port in range(9009, 9009+nSources)]
   # pmus = [create_pmu(port) for port in range(9009, 9009+nSources)]
    
    for i, pmu in enumerate(pmus):
        pmu.ieee_data_sample.set_freq(i+1)

    
    cnt = 0
    while True:
       # sleep(SLEEP_TIME)        
        for pmu in pmus:                    
            pmu.send(pmu.ieee_data_sample)             
            
    for pmu in pmus:            
        pmu.join()



if __name__ == "__main__":

    test_list = [
      #  test_client_single_pmu, 
      #  test_client_2_pmus,
        test_client_10_pmus
        ]

    threads = list()

  
    for test in test_list:
        x = threading.Thread(target=test)
        threads.append(x)
        x.start()
    
    
        

    for index, thread in enumerate(threads):        
        thread.join()
        
   
