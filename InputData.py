TRACE_ON = True        # Set to true to trace a simulation replication
DECI = 5                # the decimal point to round the numbers to in the trace file
# simulation settings
SIM_DURATION = 100000   # (hours) a large number to me sure the simulation will be terminated eventually but

HOURS_OPEN = 20         # hours the urgent cares open
N_PCP = 10                # number of primary-care physicians
MEAN_ARRIVAL_TIME = 1/60       # mean patients inter-arrival time (hours)
MEAN_EXAM_DURATION = 10/60       # mean of exam duration (hours)
MEAN_MH_CONSULT = 20/60         # mean duration of mental health consultation
PROB_DEPRESSION = 0.1           # probability that a patient is diagnosed with depression
