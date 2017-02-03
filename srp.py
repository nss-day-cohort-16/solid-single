class Patient():

    def __init__(self):
        self.__first_name = None
        self.__last_name = None
        self.__location = None
        self.__ailments = set()
        self.__treatments = set()

    def get_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_location(self):
        return self.__location

    def get_ailments(self):
        return self.__ailments

    def add_ailment(self, ailment):
        return self.__ailments.add(ailment)

    def provide_treatment(self, ailment, treatment):
        self.__ailments.remove(ailment)
        self.__treatments.add(treatment)


if __name__ == "__main__":
    joe = Patient()
    joe.add_ailment("Back spasms")
    joe.add_ailment("Hypertension")
    print(joe.get_ailments())
    joe.provide_treatment("Hypertension", "Xanax")
    print(joe.get_ailments())
    print(joe.get_location())