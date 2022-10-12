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
    
class EmployeeInfo():
    def __init__(self, employee_id, name, surname, email, company_id, is_admin, contract_info,task_list=[], hour_logs=[]):
        self.employee_id :str = employee_id
        self.name :str= name
        self.surname :str= surname
        self.email :str = email
        self.company_id :str =company_id
        self.is_admin :bool=  is_admin
        self.contract_info :dict = contract_info
        self.task_list :list = task_list
        self.hour_logs :list = hour_logs