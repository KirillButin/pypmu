import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from synchrophasor.frame import *
from synchrophasor.pmu import Pmu


 
def create_pmu(port, log_level = "NOTSET", statName = "Station A"):
    
    pmu = Pmu(ip="127.0.0.1", port = port)
    pmu.logger.setLevel(log_level)

    ph_v_conversion = int(300000.0 / 32768 * 100000)  # Voltage phasor conversion factor
    ph_i_conversion = int(15000.0 / 32768 * 100000)  # Current phasor conversion factor   

    cfg = ConfigFrame2(7,  # PMU_ID
                    1000000,  # TIME_BASE
                    1,  # Number of PMUs included in data frame
                    statName,  # Station name
                    7734,  # Data-stream ID(s)
                    (False, False, True, False),  # Data format - Check ConfigFrame2 set_data_format()
                    4,  # Number of phasors
                    3,  # Number of analog values
                    1,  # Number of digital status words
                    ["VA", "VB", "VC", "I1", "ANALOG1", "ANALOG2", "ANALOG3", "BREAKER 1 STATUS",
                    "BREAKER 2 STATUS", "BREAKER 3 STATUS", "BREAKER 4 STATUS", "BREAKER 5 STATUS",
                    "BREAKER 6 STATUS", "BREAKER 7 STATUS", "BREAKER 8 STATUS", "BREAKER 9 STATUS",
                    "BREAKER A STATUS", "BREAKER B STATUS", "BREAKER C STATUS", "BREAKER D STATUS",
                    "BREAKER E STATUS", "BREAKER F STATUS", "BREAKER G STATUS"],  # Channel Names
                    [(ph_v_conversion, "v"), (ph_v_conversion, "v"),
                    (ph_v_conversion, "v"), (ph_i_conversion, "i")],  # Conversion factor for phasor channels
                    [(1, "pow"), (1, "rms"), (1, "peak")],  # Conversion factor for analog channels
                    [(0x0000, 0xffff)],  # Mask words for digital status words
                    50,  # Nominal frequency
                    1,  # Configuration change count
                    50)  # Rate of phasor data transmission)

    
    hf = HeaderFrame(7,  # PMU_ID
                     "Hello I'm nanoPMU!")  # Header Message

    pmu.set_configuration(cfg)
    pmu.set_header(hf)

    pmu.run()

    return pmu


def create_pmu_set(n, port, log_level = "NOTSET"):
    
    pmu = Pmu(ip="127.0.0.1", port = port)
    pmu.logger.setLevel(log_level)

    ph_v_conversion = int(300000.0 / 32768 * 100000)  # Voltage phasor conversion factor
    ph_i_conversion = int(15000.0 / 32768 * 100000)  # Current phasor conversion factor   

    cfg = ConfigFrame2(7,  # PMU_ID
                    1000000,  # TIME_BASE
                    n,  # Number of PMUs included in data frame
                    [f"Station {i}" for i in range(n)],  # Station name
                    [i + 7734 for i in range(n)],  # Data-stream ID(s)
                    [(False, False, True, False) for i in range(n)],  # Data format - Check ConfigFrame2 set_data_format()
                    [4]*n,  # Number of phasors
                    [3]*n,  # Number of analog values
                    [1]*n,  # Number of digital status words
                    [["VA", "VB", "VC", "I1", "ANALOG1", "ANALOG2", "ANALOG3", "BREAKER 1 STATUS",
                    "BREAKER 2 STATUS", "BREAKER 3 STATUS", "BREAKER 4 STATUS", "BREAKER 5 STATUS",
                    "BREAKER 6 STATUS", "BREAKER 7 STATUS", "BREAKER 8 STATUS", "BREAKER 9 STATUS",
                    "BREAKER A STATUS", "BREAKER B STATUS", "BREAKER C STATUS", "BREAKER D STATUS",
                    "BREAKER E STATUS", "BREAKER F STATUS", "BREAKER G STATUS"]]*n,  # Channel Names
                    [[(ph_v_conversion, "v"), (ph_v_conversion, "v"),
                    (ph_v_conversion, "v"), (ph_i_conversion, "i")]]*n,  # Conversion factor for phasor channels
                    [[(1, "pow"), (1, "rms"), (1, "peak")]]*n,  # Conversion factor for analog channels
                    [[(0x0000, 0xffff)]]*n,  # Mask words for digital status words
                    [50]*n,  # Nominal frequency
                    [1]*n,  # Configuration change count
                    50)  # Rate of phasor data transmission)

    
    hf = HeaderFrame(7,  # PMU_ID
                     "Hello I'm nanoPMU!")  # Header Message

    pmu.set_configuration(cfg)
    pmu.set_header(hf)

    pmu.run()

    return pmu, cfg


def create_pmu_forC37Test(port, log_level = "NOTSET", statName = "Station A"):
    
    pmu = Pmu(ip="127.0.0.1", port = port)
    pmu.logger.setLevel(log_level)

    ph_v_conversion = int(300000.0 / 32768 * 100000)  # Voltage phasor conversion factor
    ph_i_conversion = int(15000.0 / 32768 * 100000)  # Current phasor conversion factor   

    cfg = ConfigFrame2(7,  # PMU_ID
                    1000000,  # TIME_BASE
                    1,  # Number of PMUs included in data frame
                    statName,  # Station name
                    7734,  # Data-stream ID(s)
                    (False, False, True, False),  # Data format - Check ConfigFrame2 set_data_format()
                    4,  # Number of phasors
                    3,  # Number of analog values
                    1,  # Number of digital status words
                    ["VA", "VB", "VC", "I1", "ANALOG1", "ANALOG2", "ANALOG3", "BREAKER 1 STATUS",
                    "BREAKER 2 STATUS", "BREAKER 3 STATUS", "BREAKER 4 STATUS", "BREAKER 5 STATUS",
                    "BREAKER 6 STATUS", "BREAKER 7 STATUS", "BREAKER 8 STATUS", "BREAKER 9 STATUS",
                    "BREAKER A STATUS", "BREAKER B STATUS", "BREAKER C STATUS", "BREAKER D STATUS",
                    "BREAKER E STATUS", "BREAKER F STATUS", "BREAKER G STATUS"],  # Channel Names
                    [(ph_v_conversion, "v"), (ph_v_conversion, "v"),
                    (ph_v_conversion, "v"), (ph_i_conversion, "i")],  # Conversion factor for phasor channels
                    [(1, "pow"), (1, "rms"), (1, "peak")],  # Conversion factor for analog channels
                    [(0x0000, 0xffff)],  # Mask words for digital status words
                    50,  # Nominal frequency
                    1,  # Configuration change count
                    50)  # Rate of phasor data transmission)

    
    hf = HeaderFrame(7,  # PMU_ID
                     "Hello I'm nanoPMU!")  # Header Message

    pmu.set_configuration(cfg)
    pmu.set_header(hf)

    pmu.run()

    return pmu

