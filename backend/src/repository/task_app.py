from models.task_app import Tasks
from database.db import get_connection
from psycopg2 import extras

from models.employee import Employee
class TasksRepository:
    
    dbconnection = get_connection() 
    
    def get_one(self, id):
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from task_app where id = %s', (id,))
        task = self.__compound_task(cursor.fetchone())
        cursor.close()
        return task

    def get_list(self):
        task_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from task_app')
        rows = cursor.fetchall()
        for row in rows:
            task_list.append(self.__compound_task(row))
        
        cursor.close()
        
        if len(task_list) == 0 or None :
            return []
        
        return task_list
    
    def get_my_tasks(self, id):
        task_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('Select * FROM task_app WHERE employee_id = %s ORDER BY due_date', (id,))
        rows = cursor.fetchall()
        for row in rows:
            task_list.append(self.__compound_task(row))
        
        cursor.close()
        
        if len(task_list) == 0 or None :
            return []
        
        return task_list
    
    def get_company_tasks(self, id):
        task_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute("""
                       SELECT users.id, users.name, users.surname, task_app.* FROM users JOIN task_app 
                       ON users.id = task_app.employee_id AND task_app.company_id = %s ORDER BY due_date ASC;
                       """, (id,))
        rows = cursor.fetchall()
        for row in rows:
            task_list.append(self.__compound_task(row, "company_tasks"))
        
        cursor.close()
        
        if len(task_list) == 0 or None :
            return []
        
        return task_list
    
    def create(self, task:Tasks):
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('insert into task_app (id, employee_id, assigned_by_id, company_id, title, description, due_date, is_completed)values (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (
                           task.id,
                           task.employee_id,
                           task.assigned_by_id,
                           task.company_id,
                           task.title,
                           task.description,
                           task.due_date,
                           task.is_completed
                           
                       ))
        self.dbconnection.commit()
        cursor.close()
        
    def update(self, type, id):
        cursor = self.dbconnection.cursor()
        if type == 'done':
            cursor.execute('UPDATE task_app SET is_completed=True WHERE id = %s;', (id))
            self.dbconnection.commit()
            cursor.close()
        elif type == 'content':
            pass
        
    def delete(self, id):
        cursor = self.dbconnection.cursor()
        cursor.execute('delete from task_app where id = %s', (id,))
        self.dbconnection.commit()
        cursor.close()
        
    def __compound_task(self, row, type=None):
        if row is None:
            return None

        task = Tasks(
            row['id'],
            row['employee_id'],
            row['assigned_by_id'],
            row['company_id'],
            row['title'],
            row['description'],
            row['due_date'],
            row['is_completed']
        )
        if type is not None:
            employee = Employee(
                row['employee_id'],
                row['name'],
                row['surname']
            )
            emp_info = employee.no_id_json()
            task_info = task.to_JSON()
            task_info.update(emp_info)
            print(task_info)
            return task_info
        else:
            print(task.to_JSON())
            return task.to_JSON()