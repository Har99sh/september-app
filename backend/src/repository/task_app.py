from models.task_app import Tasks
from database.db import get_connection
from psycopg2 import extras

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
            cursor.execute('UPDATE task_app SET is_completed = True where id = %s;', (id))
            self.dbconnection.commit()
            cursor.close()
        elif type == 'content':
            pass
        
    def delete(self, id):
        cursor = self.dbconnection.cursor()
        cursor.execute('delete from task_app where id = %s', (id,))
        self.dbconnection.commit()
        cursor.close()
        
    def __compound_task(self, row):
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

        return task.to_JSON()