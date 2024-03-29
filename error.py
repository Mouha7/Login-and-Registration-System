import re

class User:
    def __init__(self, name, lastname, email, password) -> None:
        self.__name = name
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__state = False
    
    def get_name(self):
        return self.__name
    def get_lastname(self):
        return self.__lastname
    def get_fullname(self):
        return self.__name + " " + self.__lastname
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    
    def set_name(self, new_name):
        self.__name = new_name
    def set_lastname(self, new_lastname):
        self.__lastname = new_lastname
    def set_email(self, new_email):
        self.__email = new_email
    def set_password(self, new_password):
        self.__password = new_password
    def set_state(self, new_state):
        self.__state = new_state

class Signup(User):
    def __init__(self, name, lastname, email, password, password_conf) -> None:
        super().__init__(name, lastname, email, password)
        self.__password_conf = password_conf
    
    def inscription(self):
        self.__lastname = input("Nom : ")
        self.__name = input("Prénom : ")
        self.__email = input("E-mail : ")
        self.__password = input("Password : ")
        self.__password_conf = input("Confirme Password : ")

def main():
    u = User
    s = Signup
    s.inscription(u)

if __name__ == '__main__':
    main()