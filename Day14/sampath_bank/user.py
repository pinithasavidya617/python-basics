class User:
    def __init__(self,name, age, nic):
        self.__name = name
        self.__age = age
        self.__nic = nic

    def set_age(self, age):  # setters
        self.__age = age

    def get_age(self):  # getters
        return self.__age

    def set_nic(self, nic):
        self.__nic = nic

    def get_nic(self):
        return self.__nic

    def set_name(self, name):
        self.__name = name

    def get_name(self): #boilerplate code
        return self.__name

    def __str__(self): #default behavior is returning memory location
        return f" Username: {self.__name}  User Age: {self.__age} NIC: {self.__nic}"

