import numpy as np
import pandas as pd
import matplotlib as mp

generation = 1
number_of_pairs = 1
young_rab = 1
old_rab = 0
total = []

while number_of_pairs <= 10000:
    new_rabs = old_rab * 1
    number_of_pairs = new_rabs + old_rab + young_rab
    old_rab = old_rab + young_rab
    young_rab = new_rabs
    generation += 1
    print ("In generation {} the number of rabit pairs was {}".format(generation,number_of_pairs))
    


while number_of_pairs <= 100000:
    new_rabs = old_rab * 1
    number_of_pairs = new_rabs + old_rab + young_rab
    old_rab = old_rab + young_rab
    young_rab = new_rabs
    generation += 1
    print ("In generation {} the number of rabit pairs was {}".format(generation,number_of_pairs))
    
while i is True:
    rab_1 = 1
    rab_2 = 0
    rab_