from models.time_tracker_app import TimeTracker
from database.db import get_connection
from psycopg2 import extras

class TimeTrackerRepository:
    
    dbconnection = get_connection()
      
    def get_time_tracker_list(self, id):
        time_tracker_list = []
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from shift_tracker WHERE company_id  = %s', (id,))
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
        cursor.execute('insert into shift_tracker (id, work_day, sign_in, employee_id) values (%s, %s, %s, %s)',
                       (
                           timeTracker.id,
                           timeTracker.work_day,
                           timeTracker.sign_in,
                           timeTracker.employee_id,
                       ))
        self.dbconnection.commit()
        cursor.close()
       

    def checkout(self, work_day, employee_id):
        cursor = self.dbconnection.cursor()
        cursor.execute('UPDATE shift_tracker SET sign_out = now() where work_day = %s and employee_id = %s', (work_day, employee_id,))
        self.dbconnection.commit()
        cursor.close()
            
    def get_one_day_timetracker(self, id, day):
        cursor = self.dbconnection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('Select * FROM shift_tracker WHERE employee_id = %s AND work_day = %s', (id, day,))
        time_tracker = self.__compound_timeTracker(cursor.fetchone())
        cursor.close()
        return time_tracker



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

    