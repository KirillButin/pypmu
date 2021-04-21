import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading
import numpy as np

SLEEP_TIME = 1.0/70

SIGNAL_DURATION = 10
DT = 0.02
PI2 = np.pi * 2

def gen_single_harmonic():
    """Single harmonic."""
    f = 1.0

    ts = np.arange(0, 1.0/f, DT)
    #ts = np.arange(0, 100, DT)
    xs = np.cos(PI2 * f * ts)
    return xs, ts


def TestWorkFlow1Source1Method():
    
    pmu = create_pmu(10001)  
    
    cnt = 0
        
    xs, ts = gen_single_harmonic()
    pos = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:                       
            pmu.send(pmu.ieee_data_sample)             
            pmu.ieee_data_sample.set_freq(int(1000*xs[pos]))
            pos += 1
            if (pos >= len(xs)):
                pos = 0
            
    pmu.join()

def TestWorkFlow2Sources1Method():
    
    pmu = create_pmu(10002)  
    
    cnt = 0
        
    xs, ts = gen_single_harmonic()
    xs2, ts2 = gen_single_harmonic()

    pos = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:                       
            pmu.send(pmu.ieee_data_sample)             
            pmu.ieee_data_sample.set_freq(int(1000*xs[pos]))
            pos += 1
            if (pos >= len(xs)):
                pos = 0
            
    pmu.join()


def TestWorkFlow1Source1MethodDEF():
    
    pmu = create_pmu(10003)  
    
    cnt = 0
        
    xs, ts = gen_single_harmonic()
    pos = 0
    while True:
        sleep(SLEEP_TIME)        
        if pmu.clients:                       
            df = DataFrame(7,  # PMU_ID
            ("ok", True, "timestamp", False, False, False, 0, "<10", 0),  # STAT WORD - Check DataFrame set_stat()
            [(14635, 0), (-7318, -12676), (-7318, 12675), (1092, 0)],  # PHASORS (3 - v, 1 - i)
            0,  # Frequency deviation from nominal in mHz
            0,  # Rate of Change of Frequency
            [int(2000*xs[pos]), int(20000*xs[pos]), 10000],  # Analog Values
            [0x3c12],  # Digital status word
            pmu.cfg2)  # Data Stream Configuration
            df.set_freq(int(1000*xs[pos]))
            pmu.send(df)     
            
            #pmu.ieee_data_sample.set_freq(int(1000*xs[pos]))
            pos += 1
            if (pos >= len(xs)):
                pos = 0
            
    pmu.join()


if __name__ == "__main__":

    test_list = [
       # TestWorkFlow1Source1Method,        
      #  TestWorkFlow2Sources1Method,        

        TestWorkFlow1Source1MethodDEF
           
        ]

    threads = list()

  
    for test in test_list:
        x = threading.Thread(target=test)
        threads.append(x)
        x.start()    
        

    for index, thread in enumerate(threads):        
        thread.join()
        
   
