########################################################################
########################################################################
# Ready for experiments
# Update 2020.07.16
########################################################################
########################################################################

import numpy as np

########################################################################
#   Region class
########################################################################


class Region:
    """A Region supports the following functions:

    ** Setup: Initialization **
        __init__(self, r_id, capacity=100) : only region_id is necessary
 
    ** Setup: Add one contract to priority_ordering ** 
        add_priority_ordering(self, contract)
        
    ** Setup: Randomize priority_ordering from a list of integers ** 
        reset_priority_ordering(self, list_of_integers)
        
    ** Algorithm: Clear applicant pool for each iteration **       
        clear_applicant_pool(self)
    
    ** Algorithm: (GDA-RO) Add one proposal from some doctor to applicant_pool **
        add_applicant_pool(self, contract)
        
    ** Algorithm: (GDA-RH) Add a list of proposals to applicant_pool **
        add_applicant_pool_list_of_contracts(self, list_of_contracts) 
        
    ** Algorithm: (GDA-RH) Hospital chooses contracts by priority up to capacity **
        choose_from_applicant_pool_capacity(self) 
    
    ** Algorithm: (ADA) Hospital chooses contracts by priority up to artificial_cap **
        choose_from_applicant_pool_artificial_cap(self)
        
    ** Algorithm: Region notifies doctors about acceptance and rejection **       
        feedback_to_doctor(self):
    """

    def __init__(self, r_id, num_h):
        """
        Create a new region instance. Only region_ID is necessary when initialization.   
        
        Members: 
            region_id : an integer 
            capacity : an integer
                        
            associated_hospitals_bool : a dictionary {school_id: Bool}           
            associated_hospitals_capacity : a dictionary {school_id: Integer}           
            associated_hospitals_artificial_cap : a dictionary {school_id: Integer}
            
            priority_ordering : a list of contracts
            
            applicant_pool : a list of contracts

            current_match_contract : a dictionary {school_id: list}
            current_match_total_number : an integer
   
        """
        self._region_id = r_id
        self._capacity = 0
            
        self._associated_hospitals_bool = {i:False for i in range(num_h)}
        self._associated_hospitals_capacity = {i:-1 for i in range(num_h)}
        self._associated_hospitals_artificial_cap = {i:-1 for i in range(num_h)}
                       
        self._priority_ordering = [None] * 0

        self._applicant_pool = [None] * 0
        
        self._current_match_contract = {i:[None] * 0 for i in range(num_h)}
        self._current_match_total_number = 0
        
    ########################################################################
    # methods on region_id 
    # update on 2020.07.24
    ########################################################################
    
    # Optional: get region_id
    def get_region_id(self):
        """
        Return an integer of region_id
        """
        return self._region_id
    
    # Optional: set a new region_id
    def set_region_id(self, new_id):
        """
        Set a new region_id
        
        Parameter: an integer
        """
        self._region_id = new_id
        
    ########################################################################
    # methods on capacity
    # update on 2020.07.24
    ########################################################################
    
    # Optional: get capacity
    def get_capacity(self):
        """
        Return an integer of capacity
        """
        return self._capacity

    # Optional: set a new capacity
    def set_capacity(self, capacity):
        """
        Set a new regional capacity
        
        Parameter: an integer
        """
        self._capacity = capacity

    ########################################################################
    # methods on associated_hospitals_bool 
    # update on 2020.07.24
    ########################################################################
    
    # Necessary: add one hospital to associated_hospitals & associated_hospitals_capacity & associated_hospitals_artificial_cap
    def add_associated_hospitals_all_for_one_hospital(self, hospital):
        """
        add one hospital to the dictionary of associated_hospitals & associated_hospitals_capacity & associated_hospitals_artificial_cap 
        
        Parameter: an instance of hospital
        
        Warn: Call this function only if capacity and artifical_cap is assigned
        """
        
        h_id = hospital.get_hospital_id()
        capacity = hospital.get_capacity()
        cap = hospital.get_artificial_cap()
        
        self._associated_hospitals_bool[h_id] = True
        self._associated_hospitals_capacity[h_id] = capacity
        self._associated_hospitals_artificial_cap[h_id] = cap    
        
    # Optional: get associated_hospitals_bool
    def get_associated_hospitals_bool(self):
        """
        Return a dictionary of associated_hospitals_bool {hospital_id: bool}
        """
        return self._associated_hospitals_bool
    
    # Optional: set associated_hospitals_bool for one hospital
    def set_associated_hospitals_bool_for_one_hospital(self, h_id, bool_value=True):
        """
        Set associated_hospitals_bool for one hospital with {h_id: bool_value}
        
        Parameters: 
            h_id : an integer
            bool_value : True or False
        """
        # Check whether h_id is one of the keys 
        if self._associated_hospitals_bool.has_key(h_id):
            self._associated_hospitals_bool[h_id] = bool_value  
        else:
            raise Exception("Check h_id!")
    
    # Optional: set associated_hospitals_bool for all hospitals
    def set_associated_hospitals_bool_for_all_hospitals(self, list_of_bool):
        """
        set associated_hospitals_bool for all hospitals {h_id: bool_value}
        
        Parameter: a list of bool values
        """
        if len(list_of_bool) == len(self._associated_hospitals_bool):
            for i in range (len(list_of_bool)):
                self._associated_hospitals_bool[i] = list_of_bool[i]  
        else:
            raise Exception("Check the length of list_of_bool.")    

    # Optional: set associated_hospitals_bool from a dictionary
    def set_associated_hospitals_bool_from_dictionary(self, dict_of_bool):
        """
        set associated_hospitals_bool from a dictionary {h_id: bool_value}
        
        Parameter: a dict of bool values
        """
        self._associated_hospitals_bool.update(dict_of_bool)
           
    ########################################################################
    # methods on associated_hospitals_capacity 
    # update - 2020.07.17
    ######################################################################## 
   
    # Optional: get associated_hospitals_capacity
    def get_associated_hospitals_capacity(self):
        """
        Return a dictionary of associated_hospitals_capacity {hospital_id: capacity}
        """
        return self._associated_hospitals_capacity
    
    # Optional: set associated_hospitals_capacity for one hospital
    def set_associated_hospitals_capacity_for_one_hospital(self, h_id, capacity):
        """
        Set associated_hospitals_capacity for one hospital with {h_id: capacity}
        
        Parameters: 
            h_id : an integer
            capacity : an integer
        """
        # Check whether h_id is one of the keys 
        if self._associated_hospitals_capacity.has_key(h_id):
            self._associated_hospitals_capacity[h_id] = capacity
        else:
            raise Exception("Check h_id!")
    
    # Optional: set associated_hospitals_capacity for all hospitals
    def set_associated_hospitals_capacity_for_all_hospitals(self, list_of_capacity):
        """
        set associated_hospitals_capacity for all hospitals {h_id: capacity}
        
        Parameter: a list of integers
        """
        if len(list_of_capacity) == len(self._associated_hospitals_capacity):
            for i in range (len(list_of_capacity)):
                self._associated_hospitals_capacity[i] = list_of_capacity[i]  
        else:
            raise Exception("Check the length of list_of_integers.")    

    # Optional: set associated_hospitals_capacity from a dictionary
    def set_associated_hospitals_capacity_from_dictionary(self, dict_of_capacity):
        """
        set associated_hospitals_capacity from a dictionary {h_id: capacity}
        
        Parameter: a dict of integers
        """
        self._associated_hospitals_capacity.update(dict_of_capacity)
        
    ########################################################################
    # methods on associated_hospitals_artificial_cap
    # update - 2020.07.16
    ######################################################################## 
    
    # Optional: get associated_hospitals_artificial_cap
    def get_associated_hospitals_artificial_cap(self):
        """
        Return a dictionary of associated_hospitals_artificial_cap {hospital_id: artificial_cap}
        """
        return self._associated_hospitals_artificial_cap
    
    # Optional: set associated_hospitals_artificial_cap for one hospital
    def set_associated_hospitals_artificial_cap_for_one_hospital(self, h_id, artificial_cap):
        """
        Set associated_hospitals_cartificial_cap for one hospital with {h_id: artificial_cap}
        
        Parameters: 
            h_id : an integer
            artificial_cap : an integer
        """
        # Check whether h_id is one of the keys 
        if self._associated_hospitals_artificial_cap.has_key(h_id):
            self._associated_hospitals_artificial_cap[h_id] = artificial_cap
        else:
            raise Exception("Check h_id!")
    
    # Optional: set associated_hospitals_artificial_cap for all hospitals
    def set_associated_hospitals_artificial_cap_for_all_hospitals(self, list_of_artificial_cap):
        """
        set associated_hospitals_artificial_cap for all hospitals {h_id: artificial_cap}
        
        Parameter: a list of integers
        """
        if len(list_of_artificial_cap) == len(self._associated_hospitals_artificial_cap):
            for i in range (len(list_of_artificial_cap)):
                self._associated_hospitals_artificial_cap[i] = list_of_artificial_cap[i]  
        else:
            raise Exception("Check the length of list_of_artificial_cap.")    

    # Optional: set associated_hospitals_artificial_cap from a dictionary
    def set_associated_hospitals_artificial_cap_from_dictionary(self, dict_of_artificial_cap):
        """
        set associated_hospitals_artificial_cap from a dictionary {h_id: artificial_cap}
        
        Parameter: a dict of integers
        """
        self._associated_hospitals_artificial_cap.update(dict_of_artificial_cap)         

    ########################################################################
    # methods on priority_ordering
    # update - 2020.07.16
    ########################################################################

    # Optional: Get priority_ordering
    def get_priority_ordering(self):
        """
        Return priority ordering
        """
        return self._priority_ordering
    
    
    # Necessary: Add one contract to priority ordering
    def add_priority_ordering(self, contract):
        """
        Add one contract to priority_ordering
        
        Parameter: an instance of Contract class
        """
        self._priority_ordering.append(contract)

    # Necessary: reset priority ordering 
    def reset_priority_ordering(self, list_of_integers):
        """
        Reset priority ordering in according with a list of integers 
        
        Parameter: a list of integers
        
        Warn 1: only invoked after creating a non-empty priority ordering
        
        Warn 2: list_of_integers must start from 0
        """
        if len(list_of_integers) != len(self._priority_ordering):
            raise Exception("Check the length of input list! It should be the same as the priority ordering")
            
        new_ordering = [None] * 0
        
        for i in list_of_integers:
            new_ordering.append(self._priority_ordering[i])
            
        self._priority_ordering = new_ordering

    # Optional: clear priority ordering
    def clear_priority_ordering(self):
        """
        Clear priority ordering
        """        
        self._priority_ordering.clear()

    # Optional: print priority ordering
    def print_priority_ordering(self):
        """
        Print priority ordering
        
        Warn: Contract class must support print
        """
        for m in range(0, len(self._priority_ordering)):
            print(self._priority_ordering[m])
    
    ########################################################################
    # methods on applicant_pool
    # update - 2020.07.16
    ########################################################################

    # Optional: return applicant_pool
    def get_applicant_pool(self):
        """
        Return a list of contracts stored in the applicant_pool
        """
        return self._applicant_pool
    
    # Necessary: Add one contract to applicant_pool
    def add_applicant_pool(self, contract):
        """
        Add one contract to applicant pool.
        
        Paramter: an instance of Contract class
        """
        h_id = contract.get_hospital_id()
        
        # check whether the contract is related to the region
        if self._associated_hospitals_bool[h_id] != True:
            raise Exception("Check hospital_id of the contract! It is not related to the region.")
            
        self._applicant_pool.append(contract)
        
    # Necessary: Add a list of contracts to applicant_pool
    def add_applicant_pool_list_of_contracts(self, list_of_contracts):
        """
        Add a list of contracts to applicant pool.
        
        Paramter: a list of instances of Contract class
        """
        for contract in list_of_contracts:
            h_id = contract.get_hospital_id()
            
            # check whether the contract is related to the region
            if self._associated_hospitals_bool[h_id] != True:
                raise Exception("Check hospital_id of the contract! It is not related to the region.")

            self._applicant_pool.append(contract)
        
    # Important: sort applicant_pool by priority_ordering
    def sort_applicant_pool_by_priority(self):
        """
        Sort applicant_pool by priority_ordering
        
        Warn: Only invoked after creating a non-empty applicant pool
        """
        tmp_list = sorted(self._applicant_pool, key=lambda x: self._priority_ordering.index(x))
        self._applicant_pool = tmp_list            

    # Necessary: Clear applicant pool
    def clear_applicant_pool(self):
        """
        Clear applicant pool in the beginning of each iteration.
        """
        self._applicant_pool.clear()

    # Optional: display applicant_pool
    def print_applicant_pool(self):
        """
        print proposal pool
        
        Warn: Contract class must support print
        """
        for m in range(0, len(self._applicant_pool)):
            print(self._applicant_pool[m])

    ########################################################################
    # methods on current_match_contract & current_match_total_number
    # update: 2020.07.16
    ########################################################################

    # Optional: return current_match_contract
    def get_current_match_contract(self):
        """
        return a dictionary of current_match_contract
        """
        return self._current_match_contract
    
    # Optional: return current_match_total_number
    def get_current_match_total_number(self):
        """
        return an integer of current_match_total_number
        """
        return self._current_match_total_number

    # Important: add one contract to current_match_contract
    def add_current_match_contract(self, contract):
        """
        add one contract to current_match_contract
        
        parameter : an instance of contract
        """
        h_id = contract.get_hospital_id()
        self._current_match_contract[h_id].append(contract)
            
        # Update current_match_total_number
        self._current_match_total_number += 1
        
    # Important: clear current_match_contract
    def clear_current_match_contract(self):
        """
        Clear current_match_contract
        
        Warn: must clear current_match_contract for next iteration.
        """
        for key in self._current_match_contract:
            self._current_match_contract[key].clear()
        
        # Update current_match_total_number
        self._current_match_total_number = 0
        
    # Optional: print current_match_contract
    def print_current_match_contract(self):
        """
        print current_match_contract
        
        Warn: Contract class must support print
        """
        for key in self._current_match_contract:
            if self._associated_hospitals_bool[key]:
                print("hospital", key, "length", len(self._current_match_contract[key]))
                for contract in self._current_match_contract[key]:
                    print(contract)         
        
    ########################################################################
    # Interface for Algorithm
    # update 2020.07.23
    ########################################################################
    
    # Necessary: (GDA-R) Choose contracts from applicant_pool up to capacity
    def choose_from_applicant_pool(self):
        """
        Choose contracts from applicant_pool by priority_ordering without exceeding regional capacity
        
        Round 1: up to hospital artificial_cap
        
        Round 2: up to hospital capacity
        """
        # Sort applicant_pool first
        self.sort_applicant_pool_by_priority()
        
        # Clear current_match_contract
        self.clear_current_match_contract()
        
        # Round 1: self._associated_hospitals_capacity[h_id] < artificial_cap
        for contract in self._applicant_pool:
            if self._current_match_total_number < self._capacity:  
                h_id = contract.get_hospital_id() 

                if len(self._current_match_contract[h_id]) < self._associated_hospitals_artificial_cap[h_id]:
                    if contract in self._current_match_contract[h_id]:
                        pass
                    else:
                        self._current_match_contract[h_id].append(contract)
                        self._current_match_total_number += 1        
            else:         
                break
  
        # Round 2:  self._associated_hospitals_capacity[h_id] < capacity
        for contract in self._applicant_pool:

            if self._current_match_total_number < self._capacity:          
                h_id = contract.get_hospital_id()
            
                if len(self._current_match_contract[h_id]) < self._associated_hospitals_capacity[h_id]:
                    
                    # check the contract has been inserted
                    if contract in self._current_match_contract[h_id]:
                        pass
                    else:
                        
                        self._current_match_contract[h_id].append(contract)
                        self._current_match_total_number += 1        
            else:         
                break
  
        
    # Necessary: feedback_to_doctors that whether proposals are accepted or rejected
    def feedback_to_doctor(self, display=False):
        """
        Feedback to doctors that whether proposals are accepted or rejected
        """
        for contract in self._applicant_pool:
            d = contract.get_doctor()
            h_id = contract.get_hospital_id()
            
            if contract in self._current_match_contract[h_id]:
                d.proposal_accepted()
            else:
                d.proposal_rejected()
                
                if display:
                    print("doctor", d.get_doctor_id(), "rejected by region", self.get_region_id())
                                   

    



