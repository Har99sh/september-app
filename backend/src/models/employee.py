class Employee():

    def __init__(self, id, name, surname):
        self.name = name
        self.id = id
        self.surname = surname
    def to_JSON(self):
        return { 
            'id': self.id,
            'name': self.name,
            "surname": self.surname
        }
    