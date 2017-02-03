class Patient():

    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__location = None
        self.__ailments = set()
        self.__treatments = set()

    def set_name(self, firstname, lastname):
        self.__first_name = firstname
        self.__last_name = lastname

    def get_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_location(self):
        return self.__location

    def get_ailments(self):
        return self.__ailments

    def add_ailment(self, ailment):
        return self.__ailments.add(ailment)

    def remove_ailment(self, ailment):
        self.__ailments.remove(ailment)

    def add_treatment(self, treatment):
        self.__treatments.add(treatment)

    def get_treatments(self):
        return self.__treatments


class Doctor():

    def __init__(self):
        self.__first_name = None
        self.__last_name = None

    def set_name(self, firstname, lastname):
        self.__first_name = firstname
        self.__last_name = lastname

    def diagnose_patient(self, patient, ailment):
        patient.add_ailment(ailment)

    def treat_patient(self, patient, ailment, treatment):
        patient.remove_ailment(ailment)
        patient.add_treatment(treatment)





if __name__ == "__main__":
    joe = Patient()
    joe.set_name("Joe", "Shepherd")

    brenda = Doctor()
    brenda.set_name("Brenda", "Long")

    brenda.diagnose_patient(joe, "Hypertension")
    brenda.diagnose_patient(joe, "ACL tear")

    brenda.treat_patient(joe, "Hypertension", "Xanax")

    print("Ailments for {}: {}".format(joe.get_name(), joe.get_ailments()))
    print("Treatments for {}: {}".format(joe.get_name(), joe.get_treatments()))

