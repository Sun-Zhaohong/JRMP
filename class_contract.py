########################################################################
# Ready for experiments
# Update 2020.07.24
########################################################################


########################################################################
#   contract class
########################################################################

class Contract:
    """
    A contract instance consists of a doctor instance and a hospital instance.
    """
    def __init__(self, doctor, hospital):
        """
        A doctor instance and a hospital are necessary when initialization.

        Member:
            doctor: a doctor instance
            school: a hospital instance

            doctor_id: an integer
            hospital_id: an integer 
        """
        self._doctor = doctor
        self._hospital = hospital
        self._doctor_id = doctor.get_doctor_id()
        self._hospital_id = hospital.get_hospital_id()

    def get_doctor(self):
        return self._doctor

    def get_hospital(self):
        return self._hospital

    def get_doctor_id(self):
        return self._doctor_id

    def get_hospital_id(self):
        return self._hospital_id

    def __str__(self):
        return "(d" + str(self.get_doctor_id()) + ",h" + str(self.get_hospital_id()) + ")"




