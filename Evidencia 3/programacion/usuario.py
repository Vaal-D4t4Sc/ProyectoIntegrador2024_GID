class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f'ID: {self.id}, Username: {self.username}, Contraseña: {self.password}, Email: {self.email}'