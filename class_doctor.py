########################################################################
########################################################################
# Ready for Experiment
# Update on 2020.07.13
########################################################################
########################################################################

import numpy as np

########################################################################
#   Doctor class
########################################################################


class Doctor:
    """A Doctor Class supports the following functions:

    ** Setup : Initialization **
        __init__(self, d_id) : a doctor_id is necessary
    
    ** Setup : Add one contract to preference_ordering ** 
        add_preference_ordering(self, contract)
        
    ** Setup : Randomize preference_ordering from a list of integers ** 
        reset_preference_ordering_from_integers(self, list_of_integers)
        
    ** Algorithm: Doctor proposes contract **
        doctor_propose()
        
    ** Algorithm: Hospital or region rejects proposal  **
        proposal_rejected() : called by hospital or region
    
    ** Algorithm: Hospital or region accepts proposal **
        proposal_accepted() : called by hospital or region
    """

    ########################################################################
    # __init__ method
    
    ########################################################################
    def __init__(self, d_id):
        """
        Create a new doctor instance. Only doctor_ID is necessary when initialization.

        Members: 
            doctor_ID: an integer

            preference_ordering: a list of contracts

            current_proposal_pos: an integer indicating the position of current proposal

            current_match_pos: an integer indicating the position of current match

            current_match_contract: an instance of contract 
        """
        self._doctor_id = d_id

        self._preference_ordering = [None] * 0

        self._current_proposal_pos = 0

        self._current_match_pos = -1

        self._current_match_contract = None

    ########################################################################
    # methods on doctor_id
    # Update on 2020.07.24
    ########################################################################

    # Optional: return doctor_id
    def get_doctor_id(self):
        """
        Return ID
        """
        return self._doctor_id

    ########################################################################
    # methods on preference_ordering
    # Update on 2020.07.24
    #########################################################################
        
    # Necessary: add one contract to preference ordering
    def add_preference_ordering(self, contract):
        """
        Append the given contract to self._preference_ordering

        Parameter: an instance of contract
        
        Warn: the contract must be associated with the doctor
        """
        # check whether the contract is associated with the doctor
        if contract.get_doctor_id() != self._doctor_id:
            raise Exception("Check contract! It should be consistent with doctor ID!")
        else:
            # check whether the contract has been added
            if contract not in self._preference_ordering:
                self._preference_ordering.append(contract)

    # Necessary: create a new preference ordering from list_of_integers
    def reset_preference_ordering_from_integers(self, list_of_integers):
        """
        Create a new preference ordering that is consistent with list_of_integers

        Parameter: a list of integers

        Warn : self._preference_ordering cannot be empty when calling this method
        """
        if len(list_of_integers) != len(self._preference_ordering):
            raise Exception("Check the length of preference ordering!")
            
        # create an empty ordering to store the new preference ordering    
        new_ordering = [None] * 0
        
        for i in range(0, len(list_of_integers)):
            new_ordering.append(self._preference_ordering[list_of_integers[i]])
            
        self._preference_ordering = new_ordering
            
    # Optional: return preference_ordering
    def get_preference_ordering(self):
        """
        Return preference_ordering
        """
        return self._preference_ordering
    
    # Optional: clear preference_ordering
    def clear_preference_ordering(self):
        """
        Clear preference_ordering
        """
        self._preference_ordering.clear()

    # Optional: print preference_ordering
    def print_preference_ordering(self):
        """
        Print preference ordering

        Warn: Contract class must support __str__() method
        """
        for m in range(0, len(self._preference_ordering)):
            print(self._preference_ordering[m])

    ########################################################################
    # methods on current_proposal_pos 
    # Update on 2020.07.24
    ########################################################################
    
    # Optional: return current_proposal_pos
    def get_current_proposal_pos(self):
        """
        Return current_proposal_pos
        """
        return self._current_proposal_pos
    
    # Optional: set a new current_proposal_pos
    def set_current_proposal_pos(self, pos):
        """
        Set current_proposal_pos to be a new position
        
        Parameter: an integer
        """
        self._current_proposal_pos = pos

    # Optional: check whether proposal_pool is empty or not
    def proposal_pool_is_empty(self):
        """
        Check whether proposal_pool is empty or not

        Depending on whether current_proposal_pos is larger than the length of preference_ordering
        """
        if self._current_proposal_pos >= len(self._preference_ordering):
            return True
        else:
            return False
        
    ########################################################################
    # methods on current_match_pos
    # Update on 2020.07.24
    ######################################################################## 
        
    # Optional: return current_match_pos
    def get_current_match_pos(self):
        """
        Return current_match_pos
        
        Note: When current_match_pos = len(self._proposal_pool), doctor is unmatched 
        """
        return self._current_match_pos

    # Optional: set current_match_pos
    def set_current_match_pos(self, pos):
        """
        Set current_match_pos to be some position
        
        Parameter: an integer
        
        Note: When current_match_pos = len(self._proposal_pool), doctor is unmatched 
        """
        self._current_match_pos = pos
        
    ########################################################################
    # methods on current_match_contract
    # Update on 2020.07.24
    ########################################################################
    
    # Optional: return current_match_contract
    def get_current_match_contract(self):
        """
        Return currently matched contract or None when unmatted
        """
        return self._current_match_contract

    # Optional: set current_match_contract
    def set_current_match_contract(self, contract):
        """
        Set current_match_contract to the given contract.
        
        Parameter: an instance of Contract
        """
        self._current_match_contract = contract
        
    ########################################################################
    # Method for Algorithm - Initailization of the market
    # Update on 2020.07.24
    ########################################################################
    
    # Necessary: Reset current_proposal_pos, current_match_pos, current_match_contract
    def initialize_proposal_and_current_match_pos(self):
        """
        Initialize self._current_proposal_pos, self._current_match_pos, self._current_match_contract
        """
        self._current_proposal_pos = 0
        self._current_match_pos = -1
        self._current_match_contract = None
        
    ########################################################################
    # Method for Algorithm - Choice function of doctors
    # Update on 2020.07.24
    ########################################################################
    
    # Necessary: doctor proposes a new contract
    def doctor_propose(self, display_procedure=False):
        """
        Propose a new contract with respect to current_proposal_pos.

        Warn: Check whether the proposal_pool is empty first.
        """
        if self.proposal_pool_is_empty():
            self._current_match_contract = None
            self._current_match_pos = len(self._preference_ordering)
            return None
        else:
            if display_procedure:
                print("doctor", self._doctor_id, "proposes", print(self._preference_ordering[self._current_proposal_pos]))
                
            return self._preference_ordering[self._current_proposal_pos]  
        
    ########################################################################
    # Methods for Algorithm - Accepted or rejected by hospital / region 
    # Update on 2020.07.24
    ########################################################################
    
    # Necessary: Invoked when proposal is rejected.
    def proposal_rejected(self):
        """
        Modify attriubtes when current proposal is rejected as follows: 
        
        current_proposal_pos points to next position.

        current_match_pos points to the end of the proposal pool.

        current_match_contract is set to None.
        """
        self._current_proposal_pos += 1
        self._current_match_pos = len(self._preference_ordering)
        self.set_current_match_contract(None)

    # Necessary: Invoked when proposal is accepted.
    def proposal_accepted(self):
        """
        Modify attriubtes when current proposal is accepted as follows: 

        current_proposal_pos remains the same.

        current_match_pos points to current position.

        current_match_contract is set to current contract.
        """
        self._current_match_pos = self._current_proposal_pos
        self.set_current_match_contract(self._preference_ordering[self._current_match_pos])


        
        
        