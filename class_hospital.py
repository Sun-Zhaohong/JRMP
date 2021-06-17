########################################################################
########################################################################
# Ready for experiments
# Update 2020.07.14
########################################################################
########################################################################

import numpy as np

########################################################################
#   Hospital class
########################################################################


class Hospital:
    """A Hospital supports the following functions:

    ** Setup: Initialization **
        __init__(self, h_id, capacity, cap) : only hospital_id is necessary
 
    ** Setup: Add one contract to priority_ordering ** 
        add_priority_ordering(self, contract)
        
    ** Setup: Randomize priority_ordering from a list of integers ** 
        reset_priority_ordering(self, list_of_integers)
        
    ** Algorithm: Clear applicant pool for each iteration **       
        clear_applicant_pool(self)
    
    ** Algorithm: Add one proposal from some doctor to applicant_pool **
        add_applicant_pool(self, contract)
        
    ** Algorithm: (GDA-RH) Hospital chooses contracts by priority up to capacity **
        choose_from_applicant_pool_capacity(self) 
    
    ** Algorithm: (ADA) Hospital chooses contracts by priority up to artificial_cap **
        choose_from_applicant_pool_artificial_cap(self)
        
    ** Algorithm: Hospital notifies doctors about acceptance and rejection **       
        feedback_to_doctor(self):
    """

    def __init__(self, h_id, capacity=10, cap=8):
        """
        Create a new hospital instance. Only hospital_ID is necessary when initialization.   
        
        Members: 
            hospital_id : an integer 
            
            capacity : an integer
            artificial_cap : an integer

            weight : an integer
            associated_region_id : an integer

            priority_ordering : a list of contracts
            applicant_pool : a list of contracts

            current_match_contract : a list of contracts
            current_match_total_number : an integer

            final_ranking : a list of integers   
        """
        self._hospital_id = h_id
        
        self._capacity = capacity
        self._artificial_cap = cap
        
        self._weight = -1
        self._associated_region_id = -1

        # for algorithm_choice_function_hospitals
        self._priority_ordering = [None] * 0
        self._applicant_pool = [None] * 0

        self._current_match_contract = [None] * 0
        self._current_match_total_number = 0
               
        # for outcome_analysis
        self._final_ranking = [None] * 0
        
    ########################################################################
    # methods on hospital_id 
    # update on 2020.07.24
    ########################################################################
    
    # Necessary: get hospital_id
    def get_hospital_id(self):
        """
        Return hospital_id
        """
        return self._hospital_id
    
    # Optional: set a new hospital_id
    def set_hospital_id(self, new_id):
        """
        Set a new ID
        
        Parameter: an integer
        """
        self._hospital_id = new_id
        
    ########################################################################
    # methods on capacity
    # update on 2020.07.24
    ########################################################################
    
    # Necessary: get capacity
    def get_capacity(self):
        """
        Return capacity
        """
        return self._capacity

    # Optional: set a new capacity
    def set_capacity(self, capacity):
        """
        Set a new capacity
        
        Parameter: an integer
        """
        self._capacity = capacity

    ########################################################################
    # methods on artificial_cap
    # update on 2020.07.24
    ########################################################################
    
    # Necessary: get artificial_cap
    def get_artificial_cap(self):
        """
        Return artificial_cap
        """
        return self._artificial_cap

    # Optional: set a new artificial_cap
    def set_artificial_cap(self, cap):
        """
        Set a new artificial_cap
        
        Parameter: an integer
        """
        self._artificial_cap = cap
        
    ########################################################################
    # methods on weight
    # update on 2020.07.24
    ########################################################################
    
    # Optional: get weight
    def get_weight(self):
        """
        Return weight
        """
        return self._weight

    # Optional: set a new weight
    def set_weight(self, weight):
        """
        Set a new weight
        
        Parameter: an integer
        """
        self._weight = weight
        
    ########################################################################
    # methods on associated_region_id
    # update on 2020.07.24
    ########################################################################
    
    # Necessary: get associated_region_id
    def get_associated_region_id(self):
        """
        Return associated_region_id
        """
        return self._associated_region_id

    # optional: set a new associated_region_id
    def set_associated_region_id(self, r_id):
        """
        Set a new associated_region_id
        
        Parameter: an integer
        """
        self._associated_region_id = r_id      
  
    ########################################################################
    # methods on priority_ordering
    # update on 2020.07.24
    ########################################################################

    # Important: Add one contract to self._priority_ordering
    def add_priority_ordering(self, contract):
        """
        This function is called by market when initializing priority profile of hospitals.
        
        """
        # check whether the contract has been added to self._priority_ordering
        if contract not in self._priority_ordering:
            self._priority_ordering.append(contract)

    # Necessary: reset self._priority_ordering in according with a list of integers 
    def reset_priority_ordering_from_integers(self, list_of_integers):
        """
        This function is called by market when randomizing priority profile of hospitals.
        
        Warn: self._priority_ordering cannot be empty!
        """
        if len(list_of_integers) != len(self._priority_ordering):
            raise Exception("Check the length of input list! It should be the same as the priority ordering")
            
        new_ordering = [None] * 0
        
        for i in list_of_integers:
            new_ordering.append(self._priority_ordering[i])
            
        self._priority_ordering = new_ordering

    # Optional: clear self._priority_ordering
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
    # update on 2020.07.24
    ########################################################################
    
    # Optional: return applicant_pool
    def get_applicant_pool(self):
        """
        Return applicant_pool
        """
        return self._applicant_pool
    
    # Necessary: Add one contract to self._applicant_pool
    def add_applicant_pool(self, contract):
        """
        This function is called by market during Algorithm after doctors propose contracts. 
        It assigns proposals from doctors to corresponding hospitals. 
        
        """
        h_id = contract.get_hospital_id()
        
        if self._hospital_id != h_id:
            raise Exception("Check hospital_id of the contract! It should be the same as self._hospital_id.")
            
        # check whether the contract has been added to self._applicant_pool
        if contract not in self._applicant_pool:
            self._applicant_pool.append(contract)           

    # Necessary: sort applicant_pool by self._priority_ordering
    def sort_applicant_pool_by_priority(self):
        """
        This function is called by self.choose_from_applicant_pool() when hospital chooses contracts. 
       
        """
        tmp_list = sorted(self._applicant_pool, key=lambda x: self._priority_ordering.index(x))
        self._applicant_pool = tmp_list            

    # Necessary: Clear applicant pool
    def clear_applicant_pool(self):
        """
        This function is called by market during Algorithm - choice function of hospitals
        in the beginning of each iteration of choice functions of hospitals.
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
    # update on 2020.07.24
    ########################################################################

    # Optional: return current_match_contract
    def get_current_match_contract(self):
        """
        return a list of contracts
        """
        return self._current_match_contract
    
    # Necessary: return current_match_total_number
    def get_current_match_total_number(self):
        """
        return total_number of current matched contracts
        """
        return self._current_match_total_number

    # Optional: reset current_match_contract from a list of contracts
    def reset_current_match_contract(self, list_contracts):
        """
        Reset current_match_contract from a list of contracts
        
        parameter : a list of contracts
        """
        
        # clear_current_match_contract first
        self.clear_current_match_contract()
        
        for contract in list_contracts:
            self._current_match_contract.append(contract)
            
        # Update current_match_total_number
        self._current_match_total_number = len(list_contracts)
        
    # Necessary: clear current_match_contract
    def clear_current_match_contract(self):
        """
        This function is called before each iteration of choice function of hospitals.
        """
        self._current_match_contract.clear()
        
        # Update current_match_total_number
        self._current_match_total_number = 0
        
    # Optional: print current_match_contract
    def print_current_match_contract(self):
        """
        print current_match_contract
        
        Warn: Contract class must support print
        """
        for contract in self._current_match_contract:
            print(contract)  
            
    ########################################################################
    # methods: final_ranking
    # update: 2020.07.24
    ########################################################################
    
    # Necessary: return final_ranking
    def get_final_ranking(self):
        """
        This function is called when analyzing final outcome.
        """
        return self._final_ranking
    
    # Necessary: add the position of given contract to self._final_ranking
    def add_contract_final_ranking(self, contract):
        """
        This function is called by market.initialize_market_current_match()
        """
        pos = self._priority_ordering.index(contract)
        if pos not in self._final_ranking:
            self._final_ranking.append(pos)

    # Necessary: clear final_ranking
    def clear_final_ranking(self):
        """
       This function is called by market.initialize_market_current_match()
        
        """
        self._final_ranking.clear()
 
    # optional: print final ranking
    def print_final_ranking(self):
        """
        print_final_ranking
        
        """
        print(self._final_ranking)
           
    ########################################################################
    # Methods for Algorithm - Choice function of hospital
    # update: 2020.07.24
    ########################################################################
    
    # Necessary: (GDA-RH) Choose contracts from applicant_pool up to capacity
    def choose_from_applicant_pool_capacity(self):
        """
        This function is called by GDA-RH as choice function of hospital
        
        """
        # Sort applicant_pool first
        self.sort_applicant_pool_by_priority()
        
        # Clear current_match_contract
        self.clear_current_match_contract()
        
        count = 0

        if count < self._capacity:  
            for contract in self._applicant_pool:
                self._current_match_contract.append(contract)
                count += 1
                # check whether the number of currently matched contracts reaches hospital capacity
                if count == self._capacity:           
                    break
        
        # Update current_match_total_number
        self._current_match_total_number = len(self._current_match_contract)
                
    # Necessary: (ADA) Choose contracts from applicant_pool to artificial_cap
    def choose_from_applicant_pool_artificial_cap(self):
        """
        This function is called by ADA as choice function of hospital.
        
        """
        
        # Sort applicant_pool first
        self.sort_applicant_pool_by_priority()
                
        # Clear current_match_contract
        self.clear_current_match_contract()
        
        count = 0
        
        if count < self._artificial_cap:
            for contract in self._applicant_pool:
                self._current_match_contract.append(contract)
                count += 1
                # check whether the number of currently matched contracts reaches hospital artificial_cap
                if count == self._artificial_cap:          
                    break
        
        # Update current_match_total_number
        self._current_match_total_number = len(self._current_match_contract)
                    
    # Necessary: feedback_to_doctors that whether proposals are accepted or rejected
    def feedback_to_doctor(self, display_procedure=False):
        """
        This function is called by choice function of hospitals after hospitals select contracts.

        """
        for contract in self._applicant_pool:
            d = contract.get_doctor()
            
            if contract in self._current_match_contract:
                d.proposal_accepted()
            else:
                d.proposal_rejected()
                
                if display_procedure:
                    print("doctor", d.get_doctor_id(), "rejected by hospital", self.get_hospital_id())  

        
