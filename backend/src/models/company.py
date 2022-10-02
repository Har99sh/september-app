class Company():

    def __init__(self, id, name, cif, email, telephone) -> None:
        self.id = id
        self.name = name
        self.cif = cif
        self.email = email
        self.telephone = telephone
       
    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'cif': self.cif,
            'email': self.email,
            'telephone': self.telephone
        }
    
    def to_JSON_no_pass(self):
        return{
            'id': self.id,
            'name': self.name,
            'cif': self.cif,
            'email': self.email,
            'telephone' : self.telephone
        }