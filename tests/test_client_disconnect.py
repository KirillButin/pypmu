import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading

SLEEP_TIME = 1.0/100



def test_ConnectDisconnect():
    '''do no send anything except cfg and header'''
    pmu = create_pmu_forC37Test(9994)  

    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:   
           # del pmu
            return




if __name__ == "__main__":

    test_list = [     
        test_ConnectDisconnect,
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
        
   
