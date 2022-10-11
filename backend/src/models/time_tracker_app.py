class TimeTracker():
    
    def __init__(self, id, sign_in, sign_out, total_hours, work_day, employee_id, company_id) -> None:
        self.id = id
        self.sign_in = sign_in
        self.sign_out = sign_out
        self.total_hours = total_hours
        self.work_day = work_day
        self.employee_id = employee_id
        self.company_id = company_id
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'sign_in': self.sign_in,
            'sign_out': self.sign_out,
            'total_hours': self.total_hours,
            'work_day': self.work_day,
            'employee_id': self.employee_id,
            'company_id': self.company_id
        }
        