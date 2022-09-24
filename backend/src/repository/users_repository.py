from sqlite3 import Row
from models.users import Users
from database.db import get_connection
from psycopg2 import sql,extras

class UserRepository:

    _dbconection = get_connection() 

    def get(self, id):
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from users where id = %s', (id,))
        user = self.__compound_user(cursor.fetchone())
        cursor.close()
        return user

    def get_by_email(self, email):
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        query = sql.SQL("select {fields} from {table} where email = %s").format(
    fields=sql.SQL(',').join([
        sql.Identifier('id'),
        sql.Identifier('name'),
        sql.Identifier('surname'),
        sql.Identifier('email'),
        sql.Identifier('password'),
        sql.Identifier('company_id'),
        sql.Identifier('dni'),
        sql.Identifier('is_admin'),
    ]),table=sql.Identifier('users'))
        cursor.execute('select * from users where email = %s', (email,))
        user = self.__compound_user(cursor.fetchone())
        cursor.close()
        return user

    def list(self):
        user_list = []
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from users')
        rows = cursor.fetchall()
        for row in rows:
            user_list.append(self.__compound_user(row))
        cursor.close()
        return user_list

    def add(self, user: Users):
        cursor = self._dbconection.cursor()
        cursor.execute('insert into users values (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (
                           user.id,
                           user.name,
                           user.surname,
                           user.email,
                           user.password,
                           user.company_id,
                           user.dni,
                           user.is_admin,
                           
                       ))
        self._dbconection.commit()
        cursor.close()

    def __compound_user(self, row):
        if row is None:
            return None

        print(row)
        user = Users(
            row['id'],
            row['name'],
            row['surname'],
            row['email'],
            row['password'],
            row['company_id'],
            row['dni'],
            row['is_admin']    
        )
        return user