class Users():

    def __init__(self, id, name=None, surname=None, email=None, password=None) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password 
        }