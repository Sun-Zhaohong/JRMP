########################################################################
# Ready for experiments
# Update 2020.07.25
########################################################################

import numpy as np

import copy

########################################################################
#   Outcome class
########################################################################

class Outcome:
    """
    An outcome instance consists of two members :
   
        self._doctors_final_pos: a list of integers
        self._hospitals_final_pos: a matrix of integers, with shape num_hospitals by capacity 
    
    """
    def __init__(self, experiment_id):
        """
        """
        self._outcome_id = experiment_id
        self._doctors_final_pos_GDA_RH = [None] * 0
        self._hospitals_final_pos_GDA_RH = [None] * 0        
        
        self._doctors_final_pos_GDA_RO = [None] * 0
        self._hospitals_final_pos_GDA_RO = [None] * 0
        
        self._doctors_final_pos_ADA = [None] * 0
        self._hospitals_final_pos_ADA = [None] * 0
        
    ##############################################################################
    # Methods on experiment_id
    # update on 2020.07.25
    ##############################################################################
    def get_outcome_id(self):
        return self._outcome_id
    
    ##############################################################################
    # Methods on self._doctors_final_pos_GDA_RH & self._hospitals_final_pos_GDA_RH
    # update on 2020.07.25
    ##############################################################################
    
    def get_doctors_final_pos(self, algo="GDA-RH"):
        if algo=="GDA-RH":
            return self._doctors_final_pos_GDA_RH
        if algo=="GDA-RO":
            return self._doctors_final_pos_GDA_RO
        if algo=="ADA":
            return self._doctors_final_pos_ADA
        else:
            raise Exception("Select from GDA-RH, GDA-RO or ADA.") 
            
    def get_hospitals_final_pos(self, algo="GDA-RH"):
        if algo=="GDA-RH":
            return self._hospitals_final_pos_GDA_RH
        if algo=="GDA-RO":
            return self._hospitals_final_pos_GDA_RO
        if algo=="ADA":
            return self._hospitals_final_pos_ADA
        else:
            raise Exception("Select from GDA-RH, GDA-RO or ADA.") 
    
    def set_doctors_and_hospitals_final_pos(self, list_doctors, list_hospitals, algo="GDA-RH"):
        """
        Warn : deep copy ! otherwise they point to the list with different names.
        """
        doctors_final_pos = []
        hospitals_final_pos = []
        
        for doctor in list_doctors:
            doctors_final_pos.append(copy.deepcopy(doctor.get_current_match_pos()))
            
        for hospital in list_hospitals:
            hospitals_final_pos.append(copy.deepcopy(hospital.get_final_ranking()))

        if algo=="GDA-RH":
            self._doctors_final_pos_GDA_RH = doctors_final_pos
            self._hospitals_final_pos_GDA_RH = hospitals_final_pos
            
        if algo=="GDA-RO":
            self._doctors_final_pos_GDA_RO = doctors_final_pos
            self._hospitals_final_pos_GDA_RO = hospitals_final_pos
            
        if algo=="ADA":
            self._doctors_final_pos_ADA = doctors_final_pos
            self._hospitals_final_pos_ADA = hospitals_final_pos
            
    def get_doctors_percentage(self, number_hospitals, algo="GDA-RH"):
  
        doctors_percentage = []
        
        target_percentage_vector = [(i+1) * number_hospitals / 10 for i in range (10)]
        
        if algo=="GDA-RH":
            for i in range (10):
                doctors_percentage.append( np.sum(np.array(self._doctors_final_pos_GDA_RH) < target_percentage_vector[i] ) )
                
        if algo=="GDA-RO":
            for i in range (10):
                doctors_percentage.append( np.sum(np.array(self._doctors_final_pos_GDA_RO) < target_percentage_vector[i] ) )        
                
        if algo=="ADA":
            for i in range (10):
                doctors_percentage.append( np.sum(np.array(self._doctors_final_pos_ADA) < target_percentage_vector[i] ) ) 
                
        return doctors_percentage
                
                
                
                
                
                
        