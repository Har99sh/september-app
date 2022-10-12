from models.employee import Employee, EmployeeInfo
from database.db import get_connection
from psycopg2 import sql,extras


class EmployeeRepository:
    _dbconection = get_connection() 
    def smthn(self):
        return 'smth'
    
    def get_list(self, company_id):
        employee_list = []
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT id, name, surname FROM users WHERE company_id=%s', (company_id,))
        rows = cursor.fetchall()
        
        for row in rows:
            employee_list.append(self.__compound_employee(row))
            
        cursor.close()
        if len(employee_list) == 0:
            return "no emps"
        return employee_list

    def get_employee_info(self, employee_id):
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('SELECT id, name, surname, email, company_id, is_admin FROM users WHERE id = %s', (id,))
        pass

    def __compound_employee(self, row):
        employee = Employee(row["id"],row['name'],row["surname"])
        return employee.to_JSON()