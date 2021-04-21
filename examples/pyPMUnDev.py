import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu
from synchrophasor.pmuGen import *
from time import sleep
import threading
import numpy as np

SLEEP_TIME = 1.0/70

"""
pyPMU is custom configured PMU simulator. Code below represents
PMU described in IEEE C37.118.2 - Annex D.
"""




if __name__ == "__main__":

    n = 2
    pmu, cfg = create_pmu_set(n, 10001, "DEBUG")  
        
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
        if pmu.clients:
            pmu.send(df)

    pmu.join()
