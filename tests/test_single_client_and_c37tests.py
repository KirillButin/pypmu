import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading

SLEEP_TIME = 1.0/1000


def test_client_1():
   
    pmu = create_pmu(9001, log_level="DEBUG")
   # pmu = create_pmu(9001)
    
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
      #  sleep(SLEEP_TIME)
        
        if pmu.clients:
            #print("send")
   
            pmu.send(pmu.ieee_data_sample)
            #  if cnt%1000 == 0:
            #      print(cnt)

    pmu.join()

def test_client_disconnectNoDataForSomeTime():
    '''sends 2 frames in a row without delay'''
    pmu = create_pmu(9002, log_level = "DEBUG")  

    cnt = 0

    while True:
        if pmu.clients:                   
            for step in range(100):
                sleep(SLEEP_TIME)        
                if pmu.clients:                   
                    pmu.send(pmu.ieee_data_sample)  
            break
    
    sleep(10)

    while True:
      #  sleep(SLEEP_TIME)        
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


def test_client_no_data():
    '''do no send anything except cfg and header'''
    pmu = create_pmu(9004)  

    pmu.join()


def test_client_glued2():
    '''sends 2 frames in a row without delay'''
    pmu = create_pmu(9005)  

    cnt = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:       
            pmu.ieee_data_sample.set_freq(1)
            pmu.send(pmu.ieee_data_sample)  
            pmu.send(pmu.ieee_command_sample)
            pmu.ieee_data_sample.set_freq(2)
            pmu.send(pmu.ieee_data_sample)             
                
            break
        
    pmu.join()


def test_client_2_pmu_in_one():
    
    n = 2
    pmu, cfg = create_pmu_set(n, 9006)  
        
    df = DataFrame(7,  # PMU_ID
                   [("ok", True, "timestamp", False, False, False, 0, "<10", 0)]*n,  # STAT WORD - Check DataFrame set_stat()
                   [[(14635, 0), (-7318, -12676), (-7318, 12675), (1092, 0)]]*n,  # PHASORS (3 - v, 1 - i)
                   [i*100 + 2500 for i in range(n)],  # Frequency deviation from nominal in mHz
                   [0]*n,  # Rate of Change of Frequency
                   [[100, 1000, 10000]]*n,  # Analog Values
                   [[0x3c12]]*n,  # Digital status word
                   cfg)  # Data Stream Configuration

    
    pmu.run()

    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:
            pmu.send(df)

    pmu.join()




def test_RecieveCfg():
    '''do no send anything except cfg and header'''
    pmu = create_pmu_forC37Test(9991)  

    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:
             pmu.send(pmu.ieee_data_sample)   
             




if __name__ == "__main__":

    test_list = [
        test_client_1, 
      #  test_client_disconnectNoDataForSomeTime,
        #test_client_glued,
        #test_client_no_data,
        #test_client_glued2,
        #test_client_2_pmu_in_one,
        #test_RecieveCfg,
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
        
   

#[WinError 10054] Удаленный хост принудительно разорвал существующее подключение
#2021-03-04 12:46:55,934 WARNING [7] - Message not received completely <- (127.0.0.1:54833)
#b'\xaaA\x00\x12\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01T\x98\xaaA\x00\x12\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x14\x1c'