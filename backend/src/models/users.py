from flask_login import UserMixin

class Users(UserMixin):

    def __init__(self, id, name, surname, email, password, company_id, dni, is_admin) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.company_id = company_id
        self.dni = dni
        self.is_admin = is_admin
       
    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password, 
            'company_id' : self.company_id,
            'dni' : self.dni,
            'is_admin' : self.is_admin, 

        }
    
    def to_JSON_no_pass(self):
        return{
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'company_id' : self.company_id,
            'dni' : self.dni,
            'is_admin' : self.is_admin,

        }