class Employee():

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
    def to_JSON(self):
        return { 
            'id': self.id,
            'name': self.name,
            "surname": self.surname
        }
    def no_id_json(self):
        return {
            'name': self.name,
            'surname': self.surname
        }
    