class Usuario:
    def __init__(self, id, username, DNI, password, email):
        self.__id = id
        self.__username = username
        self.__DNI = DNI 
        self.__password = password
        self.__email = email

    # Métodos get para cada atributo
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_DNI(self):
        return self.__DNI

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    # Métodos set para cada atributo
    def set_username(self, username):
        self.__username = username

    def set_DNI(self, dni):
        self.__DNI = dni

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    # Representación en string
    def __str__(self):
        return f"Usuario(id={self.__id}, username='{self.__username}', DNI='{self.__DNI}', email='{self.__email}')"