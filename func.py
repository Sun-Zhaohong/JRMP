import numpy as np
import math
import generate_profiles as gp

########################################################################
# Important: generates a vector that assigns each hospital to some region.
def genVector_assign_hospitals_to_regions(number_hospitals, number_regions, mode="evenly", sort_bool=False):
    """
    This function generates region_id evenly s.t. all regions have the same number of hospitals.
    
    Output : a list of integers
    Length : number_hospitals
    Index :  hosptial_id
    Element : region_id
    sort_bool : Bool
    
    """
    
    if mode == "evenly":
        assign_hospitals_to_regions_vector = np.resize(np.arange(number_regions), (number_hospitals, ))
        np.random.shuffle(assign_hospitals_to_regions_vector)
        
    # Warn! ``randomly`` mode only works when number_hospitals / number_regions is large.     
    # Otherwise some region does not have a capacity and it may lead to bugs!
    if mode == "randomly":
        assign_hospitals_to_regions_vector = np.random.randint(low = 0, high = number_regions, size=number_hospitals)

    if sort_bool:
        assign_hospitals_to_regions_vector = np.sort(np.array(assign_hospitals_to_regions_vector))  
        
    return assign_hospitals_to_regions_vector


########################################################################
# Important: generates a vector of capacity for each hospital
def genVector_hospital_capacity(number_doctors, number_hospitals, factor=1.2):
    """
    This function generates the same capacity for all hospitals.
    
    Output : a list of integers
    Length : number_hospitals
    
    """
    
    hospital_capacity_vector = [int(math.ceil(factor * number_doctors / number_hospitals)) for i in range(number_hospitals)]
          
    return hospital_capacity_vector   


########################################################################
# Important: generates a vector of artifical_cap for each hospital
def genVector_hospital_artifical_cap(number_doctors, number_hospitals, factor=1.0):
    """
    This function generates the same capacity for all hospitals.
    
    Output : a list of integers
    Length : number_hospitals
    
    """
    
    hospital_artificial_cap_vector = [int(math.ceil(factor * number_doctors / number_hospitals)) for i in range(number_hospitals)]
          
    return hospital_artificial_cap_vector  


########################################################################
# Important: generates a vector of capacity for each region
def genVector_region_capacity(number_doctors, number_hospitals, assign_hospitals_to_regions_vector, factor=1.1):
    """
    This function generates the same capacity for all hospitals.
    
    Output : a list of integers
    Length : number_hospitals
    
    """
    unique, counts = np.unique(assign_hospitals_to_regions_vector, return_counts=True)
    regional_capacity_vector = [int(math.ceil(factor * number_doctors / number_hospitals)) * item for item in counts]

    return regional_capacity_vector    


########################################################################
# Important: generates a preference / priority ordering by Mallow model 
def genPref(num_rows = 10, num_columns = 5, Mallow_para = 0.5):

    dic = dict((i, i) for i in range(num_columns))

    res = gp.gen_mallows_mix(num_rows, dic, 1, Mallow_para)

    prefs = []
    for i in range(len(res[0])):
        tmp = []
        for k in range(1, len(res[0][i]) + 1):
            for l in res[0][i]:
                if res[0][i][l] == k:
                    tmp.append(l)
                    break
        for j in range(res[1][i]):
            prefs.append(tmp)

    # test only - print generated profile
    #f = open('preferences.txt', 'z')
    #for p in prefs:
    #    f.write(str(p) + '\n')
    #f.close()
    return prefs   
    
########################################################################
# Important: calculate the average welfare of doctors
def average_welfare_docotrs(list_outcomes, parameters):
    
    # retrive parameters
    number_experiments = parameters["number_experiments"]
    number_hospitals = parameters["number_hospitals"]
    hos_factor = parameters["hos_factor"]
    cap_factor = parameters["cap_factor"]
    reg_factor = parameters["reg_factor"]
    mallow_para_doctor = parameters["mallow_para_doctor"]
    mallow_para_hospital = parameters["mallow_para_hospital"]
    mallow_para_region = parameters["mallow_para_region"]
    
    # initialize sum to be zero
    sum_RH = [0 for i in range(10)]
    sum_RO = [0 for i in range(10)]
    sum_ADA = [0 for i in range(10)]

    # update sum
    for outcome in list_outcomes:
        sum_RH = np.array(sum_RH) + np.array(outcome.get_doctors_percentage(number_hospitals, "GDA-RH"))
        sum_RO = np.array(sum_RO) + np.array(outcome.get_doctors_percentage(number_hospitals, "GDA-RO"))
        sum_ADA = np.array(sum_ADA) + np.array(outcome.get_doctors_percentage(number_hospitals, "ADA"))
    
    # store average outcomes
    f = open('outcome.txt', 'a')
    f.write("*"*20 + "hos_f " + str(hos_factor) + " cap_f " + str(cap_factor) + " reg_f " + str(reg_factor) + " mallow_doc " + str(mallow_para_doctor) + " mallow_hos " + str(mallow_para_hospital) + " mallow_reg " + str(mallow_para_region) + "*"*20 + '\n')
    f.write("GDA-RH" + '\n' + str(list(np.array(sum_RH) / number_experiments)) + '\n')
    f.write("GDA-RO" + '\n' + str(list(np.array(sum_RO) / number_experiments)) + '\n')
    f.write("ADA" + '\n' + str(list(np.array(sum_ADA) / number_experiments)) + '\n' + '\n')
    f.close()
    
     # print average outcomes
    print("hos_factor", hos_factor, "cap_factor", cap_factor, "reg_factor", reg_factor, "mallow_doctor", mallow_para_doctor, "mallow_hospital", mallow_para_hospital, "mallow_region", mallow_para_region)
    print("GDA-RH", list(np.array(sum_RH) / number_experiments))   
    print("GDA-RO", list(np.array(sum_RO) / number_experiments))   
    print("ADA   ", list(np.array(sum_ADA) / number_experiments))    
    
