from models.time_tracker_app import TimeTracker
from database.db import get_connection
from psycopg2 import extras

class TimeTrackerRepository:
    
    dbconnection = get_connection()
      
    def get_time_tracker_list(self, id):
        time_tracker_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from shift_tracker WHERE company_id = %s', (id,))
        rows = cursor.fetchall()
        for row in rows:
                time_tracker_list.append(self.__compound_timeTracker(row))
        cursor.close()  
                      
        if len(time_tracker_list) == 0 or None :
            return []                
        return time_tracker_list
    
    def get_my_shift(self, id):
        time_tracker_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('Select * FROM shift_tracker WHERE employee_id = %s', (id,))
        rows = cursor.fetchall()
        for row in rows:
            time_tracker_list.append(self.__compound_timeTracker(row))
        
        cursor.close()
        
        if len(time_tracker_list) == 0 or None :
            return []
        
        return time_tracker_list
    
    def checkin(self, timeTracker:TimeTracker):
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('insert into shift_tracker (id, sign_in, sign_out, total_hours, work_day, employee_id, company_id)values (%s, %s, %s, %s, %s, %s, %s)',
                       (
                           timeTracker.id,
                           timeTracker.sign_in,
                           timeTracker.sign_out,
                           timeTracker.total_hours,
                           timeTracker.work_day,
                           timeTracker.employee_id,
                           timeTracker.company_id                          
                      
                       ))
        self.dbconnection.commit()
        cursor.close()
       

    def checkout(self, id):
        cursor = self.dbconnection.cursor()
        cursor.execute('UPDATE shift_tracker SET sign_out = now() where id = %s', (id,))
        self.dbconnection.commit()
        cursor.close()
            
    
    def __compound_timeTracker(self, row):
        if row is None:
            return None

        timeTracker = TimeTracker(
            row['id'],
            row['sign_in'],
            row['sign_out'],
            row['total_hours'],
            row['work_day'],
            row['employee_id'],
            row['company_id'],           
        )

        return timeTracker.to_JSON()