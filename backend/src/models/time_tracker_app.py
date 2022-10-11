class TimeTracker():
    
    def __init__(self, id, work_day, sign_in, sign_out, employee_id) -> None:
        self.id = id
        self.work_day = work_day
        self.sign_in = sign_in
        self.sign_out = sign_out
        self.employee_id = employee_id
    
    def to_JSON(self):
        return{
            'id': self.id, 
            'work_day': self.work_day,
            'sign_in': self.sign_in,
            'sign_out': self.sign_out,
            'employee_id': self.employee_id
        }
        