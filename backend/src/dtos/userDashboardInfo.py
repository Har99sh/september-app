
Class UserDashboardInfoDto()

    def __init__(self, id, name, surname, email, company_id, is_admin, contract_info, task_list, hour_logs) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.company_id = company_id
        self.is_admin = is_admin
        self.contract_info: dict=contract_info,
        self.task_list = task_list,
        self.hour_logs = hour_logs

    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'company_id' : self.company_id,
            'is_admin' : self.is_admin, 
            'contract_info' : self.contract_info,
            'task_list' : self.task_list,
            'hour_logs': self.hour_logs
        }