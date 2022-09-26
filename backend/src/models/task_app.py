class Tasks():

    def __init__(self, id, employee_id, assigned_by_id, company_id, title, description,  due_date, is_completed=False ) -> None:
        self.id = id
        self.employee_id = employee_id
        self.assigned_by_id = assigned_by_id
        self.company_id = company_id
        self.title = title
        self.description = description
        self.due_date = due_date 
        self.is_completed = is_completed

    def to_JSON(self):
        return{
            'id': self.id,
            'employee_id':self.employee_id ,
            'assigned_by_id':self.assigned_by_id,
            'company_id':self.company_id,
            'title':self.title,
            'description':self.description,
            'due_date':self.due_date,
            'is_completed':self.is_completed
        }
