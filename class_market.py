########################################################################
########################################################################
# Ready for experiments
# Update 2020.07.25
########################################################################
########################################################################

import numpy as np
import func

from class_doctor import *
from class_hospital import *
from class_region import *
from class_contract import *
from class_outcome import *
########################################################################
#   Market class
########################################################################

class Market:
    """A Market supports the following functions:

    ** Setup: Create doctors, hospitals, regions **
    
        __init__(self, num_doctor, num_hospital, num_region) 
        
    ** Setup: Create a set of contracts **
    
        create_list_contracts(self)
        
    ** Setup: Determine quotas for hospitals and regions **
    
        assign_capacity_vector_to_hospitals(self, hospital_capacity_vector)
        assign_artificial_cap_vector_to_hospitals(self, artificial_cap_vector)
        assign_capacity_vector_to_regions(self, regional_capacity_vector)
             
    ** Setup: Relate hospitals with regions **
    
        relate_hospitals_with_regions(self, list_of_integers)
               
    ** Setup: Initialize preference & priority profile **
    
        initialize_preference_and_priority_profile(self)
        
    ** Setup: randomize preference & priority profile **
         
        randomize_preference_profile_doctors(preference_profile)
        
        randomize_priority_profile_hospitals(priority_hospital_profile)
        
        randomize_priority_profile_regions()
    """

    def __init__(self, num_doctor, num_hospital, num_region):
        """
        Create a new market instance incluing a list of doctors, a list of hospitals and a list of regions 
        
        Members: 
            list_doctors : a list of Doctor instances        
            list_hospitals : a list of Hospital instances           
            list_regions : a list of Region instances           
            list_contracts : a list of Contract instances
        """
        self._list_doctors = [Doctor(i) for i in range(num_doctor)]
        self._list_hospitals = [Hospital(i) for i in range(num_hospital)]
        self._list_regions = [Region(i, num_hospital) for i in range(num_region)]
        self._list_contracts = [None] * 0
        
    ########################################################################
    # methods on list_doctors
    # update 2020.07.25
    ########################################################################
    
    # Necessary: get self._list_doctors
    def get_list_doctors(self):
        """
        Return a list of instances of Doctor class
        """
        return self._list_doctors
    
    # optional: print self._list_doctors_id
    def print_list_doctors_id(self):
        for doctor in self._list_doctors:
            print("doctor_id is", doctor.get_doctor_id())      
            
    ########################################################################
    # methods on list_hospitals
    # update 2020.07.25
    ########################################################################
    
    # Necessary: get self._list_hospitals
    def get_list_hospitals(self):
        """
        Return a list of instances of Hospital class
        """
        return self._list_hospitals
    
    # Optional: print self._list_doctors_id
    def print_list_hospitals_id(self):
        for hospital in self._list_hospitals:
            print("hospital_id is", hospital.get_hospital_id())  
            
    ########################################################################
    # methods on list_regions
    # update 2020.07.25
    ########################################################################
    
    # Necessary: get self._list_regions
    def get_list_regions(self):
        """
        Return a list of instances of Region class
        """
        return self._list_regions
    
    # Optional: print self._list_regions_id
    def print_list_regions_id(self):
        for region in self._list_regions:
            print("region_id is", region.get_region_id())  
            
    ########################################################################
    # methods on list_contracts
    # update 2020.07.25
    ########################################################################

    # Important: create a set of contracts
    def create_list_contracts(self):
        """
        This function is called in the Phase of Initialization.
        
        """
        for doctor in self._list_doctors:
            for hospital in self._list_hospitals:
                self._list_contracts.append(Contract(doctor, hospital))

    # Necessary: return list_contracts
    def get_list_contracts(self):
        """
        Return a list of instances of Contract class
        """
        return self._list_contracts
    
    # optional: print self._list_contracts
    def print_list_contracts(self):
        for contract in self._list_contracts:
            print(contract)
            
    ########################################################################
    # Methods for Initializtion - Set quotas for hospitals and regions
    # update 2020.07.25
    ######################################################################## 
    
    # Helper: set capacity_and_artificial_cap for hospitals
    def set_capacity_and_artificial_cap_for_hospitals(self, hospital_capacity_vector, artificial_cap_vector):
        """        
        This is a helper function, part of self.set_quotas_for_hospitals_and_regions(). 
        
        """        
        # check the length of hospital_capacity_vector, which should be equal to num_hospitals
        if len(hospital_capacity_vector) != len(self._list_hospitals):
            raise Exception("Check the length of hospital_capacity_vector! It should be equal to num_hospitals.")   
            
        # check the length of artificial_cap_vector, which should be equal to num_hospitals
        if len(artificial_cap_vector) != len(self._list_hospitals):
            raise Exception("Check the length of artificial_cap_vector! It should be equal to num_hospitals.")  
            
        for i in range(len(self._list_hospitals)):
            self._list_hospitals[i].set_capacity(hospital_capacity_vector[i])    
            self._list_hospitals[i].set_artificial_cap(artificial_cap_vector[i])  
            
    # Helper: relate hospitals with regions
    def relate_hospitals_with_regions(self, list_of_integers):
        """
        This is a helper function, part of self.set_quotas_for_hospitals_and_regions(). 
        
        """
        # check the length of list_of_integers, which should be equal to num_hospitals
        if len(list_of_integers) != len(self._list_hospitals):
            raise Exception("Check the length of list_of_integers! It should be equal to num_hospitals.")  

        for i in range(len(list_of_integers)):
            r_id = list_of_integers[i]

            # check whether region_id is valid, which should be in the range [0, num_regions)
            if r_id < 0 and r_id >= len(self._list_regions):
                raise Exception("Check the region_id! It should be in the range [0, num_regions).")  
            else:                
                # Assign region_id to corresponding hosptial
                self._list_hospitals[i].set_associated_region_id(r_id)
                
                # Assign hosptial to corresponding region's associated_hospitals
                self._list_regions[r_id].add_associated_hospitals_all_for_one_hospital(self._list_hospitals[i])          
                
    # Helper: set capacity for regions
    def set_capacity_for_regions(self, regional_capacity_vector):
        """
        This is a helper function, part of self.set_quotas_for_hospitals_and_regions(). 
        
        """
        # check the length of regional_capacity_vector, which should be equal to num_regions
        if len(regional_capacity_vector) != len(self._list_regions):
            raise Exception("Check the length of regional_capacity_vector! It should be equal to num_regions.")  

        for i in range(len(regional_capacity_vector)):
            self._list_regions[i].set_capacity(regional_capacity_vector[i])
            
    # Important: set quotas for hospitals and regions
    def set_quotas_for_hospitals_and_regions(self, hos_factor=1.2, cap_factor=1.0, reg_factor=1.1, mode="evenly", sort=False):
        """
        This function is called in the phase of Initialization, that calls three helper functions above.
         
        Warn: Don't change the order of implementing helper functions. 
      
        """       
        number_doctors = len(self._list_doctors)
        number_hospitals = len(self._list_hospitals)
        number_regions = len(self._list_regions)
        
        # create vectors for hospital_capacity, artificial_cap, assign_hospitals_to_region, regional_capacity
        hospital_capacity_vector = func.genVector_hospital_capacity(number_doctors, number_hospitals, hos_factor)
        artificial_cap_vector = func.genVector_hospital_artifical_cap(number_doctors, number_hospitals, cap_factor)
        assign_hospitals_to_regions_vector = func.genVector_assign_hospitals_to_regions(number_hospitals, number_regions, mode, sort)
        regional_capacity_vector = func.genVector_region_capacity(number_doctors, number_hospitals, assign_hospitals_to_regions_vector, reg_factor)
        
        # set quotas for hospitals
        self.set_capacity_and_artificial_cap_for_hospitals(hospital_capacity_vector, artificial_cap_vector) 
        
        # relate hospitals with regions
        self.relate_hospitals_with_regions(assign_hospitals_to_regions_vector)
        
        # set quotas for regions
        self.set_capacity_for_regions(regional_capacity_vector)
                               
    ########################################################################
    # Methods for Initializtion - Random preference_profile and priority_profile 
    # update 2020.07.25
    ########################################################################                 
    
    # Helper: Initialize preference_profile and priority_profile 
    def initialize_preference_and_priority_profile(self):
        """
        This is a helper function, part of self.create_preference_and_priority_profile().
        """
        
        for contract in self._list_contracts:
            d_id = contract.get_doctor_id()
            h_id = contract.get_hospital_id()
            
            # add each contract to corresponding doctor._preference_ordering / hospital._priority_ordering
            self._list_doctors[d_id].add_preference_ordering(contract)
            self._list_hospitals[h_id].add_priority_ordering(contract)
            
            # add each contract to all regions
            for region in self._list_regions:
                region.add_priority_ordering(contract)        
          
        # old version add each contract to corresponding doctor / hospital / region
        # difficult to create regional_priority_profile by mallow model
        if False:
            for contract in self._list_contracts:
                d_id = contract.get_doctor_id()
                h_id = contract.get_hospital_id()
                r_id = contract.get_hospital().get_associated_region_id()

                self._list_doctors[d_id].add_preference_ordering(contract)
                self._list_hospitals[h_id].add_priority_ordering(contract)
                self._list_regions[r_id].add_priority_ordering(contract)
       
    # Helper:  Clear preference_profile and priority_profile             
    def clear_preference_and_priority_profile(self):
        """
        This is a helper function, part of self.create_preference_and_priority_profile().
        """
        
        # initalize preference_ordering for each doctor
        for doctor in self._list_doctors:
            doctor.clear_preference_ordering()
            
        # initalize prirority_ordering for each hospital
        for hospital in self._list_hospitals:
            hospital.clear_priority_ordering()
        
        # initalize prirority_ordering for each region
        for region in self._list_regions:
            region.clear_priority_ordering()           
    
    # Helper: set preference_profile for doctors
    def set_preference_profile_doctors(self, preference_profile):
        """
        This is a helper function, part of self.create_preference_and_priority_profile()
        
        """      
        for i in range(len(self._list_doctors)):
            self._list_doctors[i].reset_preference_ordering_from_integers(preference_profile[i])
            
    # Helper: set priority profile for hospitals            
    def set_priority_profile_hospitals(self, priority_hospital_profile):
        """
        This is a helper function, part of self.create_preference_and_priority_profile()
        
        """     
        for i in range(len(self._list_hospitals)):
            self._list_hospitals[i].reset_priority_ordering_from_integers(priority_hospital_profile[i])

    # Helper: set priority profile for regions           
    def set_priority_profile_regions(self, priority_region_profile):
        """
       This is a helper function, part of self.create_preference_and_priority_profile()
        
        """
        for i in range(len(self._list_regions)):   
            self._list_regions[i].reset_priority_ordering(priority_region_profile[i])  

    # Important:  Randomize preference profile & priority profile for all agents 
    def create_preference_and_priority_profile(self, mallow_para_doctor, mallow_para_hospital, mallow_para_region):
        """
        This function is called in the phase of Initialization, that calls five helper functions above.
        
        """    
        # clear_preference_and_priority_profile()
        self.clear_preference_and_priority_profile()
        
        # initialize_preference_and_priority_profile()
        self.initialize_preference_and_priority_profile()
        
        # create preference_ profile, priority_hospital_profile & priority_region_profile by mallow_model:
        preference_profile = func.genPref(len(self._list_doctors), len(self._list_hospitals), mallow_para_doctor)
        priority_hospital_profile = func.genPref(len(self._list_hospitals), len(self._list_doctors), mallow_para_hospital)
        priority_region_profile = func.genPref(len(self._list_regions), len(self._list_doctors) * len(self._list_hospitals), mallow_para_region)
        
        # randomize preference & priority profile:
        self.set_preference_profile_doctors(preference_profile)
        self.set_priority_profile_hospitals(priority_hospital_profile)
        self.set_priority_profile_regions(priority_region_profile)
                    
    ########################################################################
    # Helper functions for Algorithm : GDA-RH, GDA-RO & ADA
    # update 2020.07.25
    ########################################################################      

     # Helper: initalize market current_match
    def initialize_market_current_match(self):
        """
        This is a helper function, part of self.GDA-RH(), self.GDA-RO & self.ADA()
        
        """
        # initalize proposal_pos and current_match_pos for each doctor
        for doctor in self._list_doctors:
            doctor.initialize_proposal_and_current_match_pos()
            
        # clear current_match_contract & final_ranking for each hospital
        for hospital in self._list_hospitals:
            hospital.clear_current_match_contract()
            hospital.clear_final_ranking()
        
        # initalize current match for each region
        for region in self._list_regions:
            region.clear_current_match_contract() 
    
    # Helper: Choice function of doctors
    def doctors_propose(self, display_procedure = False):       
        """
        This is a helper function, part of self.GDA-RH(), self.GDA-RO & self.ADA()
        
        Return a list of contracts chosen by doctors.
        """
        list_proposals_doctors = []
        
        for doctor in self._list_doctors:
            contract = doctor.doctor_propose()
            if contract != None:
                list_proposals_doctors.append(contract)
         
        if display_procedure:
            print("proposals by doctors")
            for contract in list_proposals_doctors:
                print("doctor", contract.get_doctor_id(), "proposes", contract)

        return list_proposals_doctors  
    
    # Helper: Choice function of hospitals for ADA only
    def hospitals_choose_ADA(self, list_proposals, display_procedure = False):      
        """
        This is a helper function, part of self.ADA()
        
        Return a list of contracts chosen by hospitals in ADA

        """
        
        list_hospitals_chosen_contracts = []
        
        # clear hospitals applicant_pool
        for hospital in self._list_hospitals:
            hospital.clear_applicant_pool()
        
        # assign proposals to corresponding hospitals
        for contract in list_proposals:
            h_id = contract.get_hospital_id()
            self._list_hospitals[h_id].add_applicant_pool(contract)
            
        # hospitals choose contracts 
        for hospital in self._list_hospitals:
            hospital_chosen_proposals = []
            
            # each hospital chooses contracts by priority up to artificial_cap
            hospital.choose_from_applicant_pool_artificial_cap()
            
            # feedback_to_doctors that whether proposals are accepted or rejected
            hospital.feedback_to_doctor(display_procedure)
            
            # store all contracts chosen by hospitals
            hospital_chosen_contracts = hospital.get_current_match_contract()
            list_hospitals_chosen_contracts += hospital_chosen_contracts
            
            if display_procedure:
                print("contracts chosen by hospitals", hospital.get_hospital_id())
                hospital.print_current_match_contract()
        
        return list_hospitals_chosen_contracts 
    
    # Helper: Choice function of hospitals for GDA-RH only
    def hospitals_choose_GDA_RH(self, list_proposals, display_procedure = False):      
        """
        This is a helper function, part of self.GDA_RH()
        
        Return a list of contracts chosen by hospitals in GDA-RH
        
        """
        
        list_hospitals_chosen_contracts = []
        
        # clear hospitals applicant_pool
        for hospital in self._list_hospitals:
            hospital.clear_applicant_pool()
        
        # assign proposals to corresponding hospitals
        for contract in list_proposals:
            h_id = contract.get_hospital_id()
            self._list_hospitals[h_id].add_applicant_pool(contract)
            
        # hospitals choose contracts 
        for hospital in self._list_hospitals:
            hospital_chosen_proposals = []
            
            # each hospital chooses contracts by priority up to capacity
            hospital.choose_from_applicant_pool_capacity()
            
            # feedback_to_doctors that whether proposals are accepted or rejected
            hospital.feedback_to_doctor(display_procedure)
            
            # store all contracts chosen by hospitals
            hospital_chosen_contracts = hospital.get_current_match_contract()
            list_hospitals_chosen_contracts += hospital_chosen_contracts
        
            # display contracts chosen by hospitals
            if display_procedure:
                print("contracts chosen by hospitals", hospital.get_hospital_id())
                hospital.print_current_match_contract()
            
        return list_hospitals_chosen_contracts    
    
    # Helper: Choice function of hospitals for GDA-RH & GDA-RO
    def regions_choose_GDA_R(self, list_proposals, display_procedure = False):       
        """
        This is a helper function, part of self.GDA_RH() & self.GDA_RO()
        
        """   
        
        # clear regions applicant_pool
        for region in self._list_regions:
            region.clear_applicant_pool() 
        
        # assign proposals to corresponding regions
        for contract in list_proposals:
            h_id = contract.get_hospital_id()
            r_id = self._list_hospitals[h_id].get_associated_region_id()
            self._list_regions[r_id].add_applicant_pool(contract)
                
        # regions choose contracts 
        for region in self._list_regions:
            
            # each hospital chooses contracts by priority up to capacity
            region.choose_from_applicant_pool()
            
            # feedback_to_doctors that whether proposals are accepted or rejected
            region.feedback_to_doctor(display_procedure)
            
            # display contracts chosen by regions
            if display_procedure:
                print("contracts chosen by region", region.get_region_id())
                region.print_current_match_contract()
    
    # helper: set final_ranking for_hospitals
    def set_final_ranking_hospitals(self):
        """
        This is a helper function, part of self.GDA-RH(), self.GDA-RO & self.ADA()
        
        Warn: for GDA-RH, the current_match_contract may be wrong, because it is not refined by regions!
            for GDA-RO, the current_match_contract is empty!
            
        """
        # compute the final outcome from doctor.get_current_match_contract()
        final_outcome = []
        for doctor in self.get_list_doctors():
            contract = doctor.get_current_match_contract()
            if contract != None:
                final_outcome.append(contract)
        
        # update final_ranking for hospitals from final outcome
        for contract in final_outcome:
            h_id = contract.get_hospital_id()
            self._list_hospitals[h_id].add_contract_final_ranking(contract)
                
        # pad all vacant positions with number_doctors        
        for hospital in self.get_list_hospitals():
            num_padding = hospital.get_capacity() - len(hospital._final_ranking)
            for i in range (num_padding):
                hospital._final_ranking.append(len(self._list_doctors))
    
    ########################################################################
    # Algorithm : GDA-RH
    # update 2020.07.25
    ########################################################################    
    
    # Important : GDA_RH   
    def GDA_RH(self, display_procedure = False):
        """
        Implementation of GDA-RH
        """        
        
        Termination = False
        round = 0
        
        # initialize current_match for the market:
        self.initialize_market_current_match()
        
        while not Termination:        
            round += 1
            
            # display detailed procedure of GDA-RH
            if display_procedure:
                print("*" * 20, "GDA-RH round", round)    
                
            # Doctors propose contracts
            list_doctor_proposals = self.doctors_propose(display_procedure)
            
            # Hospitals Choose Contracts
            list_hospitals_chosen_contracts = self.hospitals_choose_GDA_RH(list_doctor_proposals, display_procedure)
            
            # Regions Choose Contracts
            self.regions_choose_GDA_R(list_hospitals_chosen_contracts, display_procedure)
            
            # Determine termination
            Termination = True
            for doctor in self.get_list_doctors():
                if doctor.get_current_match_pos() != doctor.get_current_proposal_pos():
                    if not doctor.proposal_pool_is_empty():
                        Termination = False
                        
        # update the final outcome
        self.set_final_ranking_hospitals() 
        
        # print the final outcome by GDA-RH
        if display_procedure:
            print("*" * 20, "Final outcome by GDA-RH in", round, "round", "*" * 20)
            for doctor in self.get_list_doctors():
                print("doctor",doctor.get_doctor_id(),"current_match_pos",doctor.get_current_match_pos(),doctor.get_current_match_contract())
                
    ########################################################################
    # Algorithm : GDA-RO
    # update 2020.07.25
    ########################################################################    
    
    # Important : GDA-RO     
    def GDA_RO(self, display_procedure = False):
        
        Termination = False
        round = 0
        
        # initialize current_match for the market:
        self.initialize_market_current_match()        
        
        while not Termination:        
            round += 1
            
            # display detailed procedure of GDA-RO
            if display_procedure:
                print("*" * 20, "GDA-RO round", round)
                        
            # Doctors propose contracts
            list_doctor_proposals = self.doctors_propose(display_procedure)
            
            # Regions choose contracts
            self.regions_choose_GDA_R(list_doctor_proposals, display_procedure)
            
            # Determine termination
            Termination = True
            for doctor in self.get_list_doctors():
                if doctor.get_current_match_pos() != doctor.get_current_proposal_pos():
                    if not doctor.proposal_pool_is_empty():
                        Termination = False
        
        # update the final outcome
        self.set_final_ranking_hospitals() 
        
        # print the final outcome by GDA-RO
        if display_procedure:
            print("*" * 20, "Final outcome by GDA-RO in", round, "round", "*" * 20)
            for doctor in self.get_list_doctors():
                print("doctor",doctor.get_doctor_id(),"current_match_pos",doctor.get_current_match_pos(),doctor.get_current_match_contract())
            
    ########################################################################
    # Algorithm : ADA
    # update 2020.07.25
    ########################################################################    
    
    # Important : ADA    
    def ADA(self, display_procedure = False):
        
        Termination = False
        round = 0
        
        # initialize current_match for the market:
        self.initialize_market_current_match()
        
        while not Termination:        
            round += 1
            
            # display detailed procedure of ADA
            if display_procedure:
                print("*" * 20, "ADA round", round)
            
            # Doctors propose contracts
            list_doctor_proposals = self.doctors_propose(display_procedure)
            
            # Hospitals choose contracts by ADA
            self.hospitals_choose_ADA(list_doctor_proposals, display_procedure)
            
            # Determine termination
            Termination = True
            for doctor in self.get_list_doctors():
                if doctor.get_current_match_pos() != doctor.get_current_proposal_pos():
                    if not doctor.proposal_pool_is_empty():
                        Termination = False
        
        # update the final outcome
        self.set_final_ranking_hospitals() 
        
        # print the final outcome by ADA
        if display_procedure:
            print("*" * 20, "Final outcome by ADA in", round, "round", "*" * 20)
            for doctor in self.get_list_doctors():
                print("doctor",doctor.get_doctor_id(),"current_match_pos",doctor.get_current_match_pos(),doctor.get_current_match_contract())              
    

    
    
    
    
    
    
        