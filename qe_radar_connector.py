from qe_radar_toolkit import *

class DevSimulator (object):

    def __init__(self):

    def simulate(self, pulse, measure, example):
        #Runs the provided configuration into the simulator and returns a normalised signal as a float
        
        #Keyword arguments:
        #pulse -- paired list with start and end of pulse in us (0-500,000)
        #measure -- list with start and end of the measurement window in us (0-500 000) and phase in radians
        #example -- id of example chosen for the simulation (0-999)
        return dev_sim(pulse, measure, example)

    def mass_simulate(self, configurations):

        for tar in configurations:
            i = 0
            result = []
            if len(tar[0]) == len(tar[1]):
                while i < len(tar[0]):
                    sig = dev_sim(tar[0][i], tar[1][i], tar[2])
                    result.append(sig)
                    i += 1
            results.append([result, tar[2]])
        return results

    #Directly calls dev_data() in qe_radar
    def dataset(self, example):
        #Requests the Rabi, Detuning, and Time of Flight for the chosen example target.
        return dev_data(example)

    def mass_dataset(self):
        results = []
        i = 0
        while i < 1000:
            results.append(dev_data(i))
            i += 1
        return results

    def validate_config(self, configs):
        return dev_config(configs)

    def validate_estimate(self, estimates):
        return dev_estimates(estimates)

class TestSimulator(object):

    def simulate(self, pulse, measure, example):
        return test_sim(pulse, measure, example)

    def mass_simulate(self, configurations):
        for tar in configurations:
            i = 0
            result = []
            if len(tar[0]) == len(tar[1]):
                while i < len(tar[0]):
                    sig = test_sim(tar[0][i], tar[1][i], tar[2])
                    result.append(sig)
                    i += 1
            results.append([result, tar[2]])
        return results

    def score(self, configs, estimates):
        error = test_config(configs)
        if error == 0:
            return test_score(estimates)
        return error