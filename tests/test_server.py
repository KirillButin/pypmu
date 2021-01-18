import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading

SLEEP_TIME = 1.0/100


def test_client_1():
    pmu = create_pmu(9001)
    
    #df = DataFrame(7,  # PMU_ID
    #            ("ok", True, "timestamp", False, False, False, 0, "<10", 0),  # STAT WORD - Check DataFrame set_stat()
    #            [(14635, 0), (-7318, -12676), (-7318, 12675), (1092, 0)],  # PHASORS (3 - v, 1 - i)
    #            2500,  # Frequency deviation from nominal in mHz
    #            0,  # Rate of Change of Frequency
    #            [100, 1000, 10000],  # Analog Values
    #            [0x3c12],  # Digital status word
    #            pmu.cfg2)  # Data Stream Configuration

    cnt = 0
    while True:
        sleep(SLEEP_TIME)
        
        if pmu.clients:
            #print("send")
   
            pmu.send(pmu.ieee_data_sample)
            #  if cnt%1000 == 0:
            #      print(cnt)

    pmu.join()


def test_client_2():
    pmu = create_pmu(9002, "DEBUG")    

    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:                           
            pmu.send(pmu.ieee_data_sample)            

    pmu.join()


def test_client_glued():
    '''sends 2 frames in a row without delay'''
    pmu = create_pmu(9003)  

    cnt = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:               
            for i in range(2):
                pmu.ieee_data_sample.set_freq(i)
                pmu.send(pmu.ieee_data_sample)  
                
            break

    pmu.join()



if __name__ == "__main__":

    test_list = [
        test_client_1, 
        test_client_2,
        test_client_glued
        ]

    threads = list()

  #  x = threading.Thread(target=test_client_1, args=(index,))
  
    for test in test_list:
        x = threading.Thread(target=test)
        threads.append(x)
        x.start()
    
    #x = threading.Thread(target=test_client_1)
    #threads.append(x)
    #x.start()

    #x = threading.Thread(target=test_client_2)
    #threads.append(x)
    #x.start()
        

    for index, thread in enumerate(threads):        
        thread.join()
        
   
