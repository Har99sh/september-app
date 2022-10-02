from models.company import Company
from database.db import get_connection
from psycopg2 import sql,extras

class CompanyRepository:

    _dbconection = get_connection() 

    def get(self, id):
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from companies where id = %s', (id,))
        user = self.__compound_company(cursor.fetchone())
        cursor.close()
        return user

    def get_by_email(self, email):
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        query = sql.SQL("select {fields} from {table} where email = %s").format(
    fields=sql.SQL(',').join([
        sql.Identifier('id'),
        sql.Identifier('name'),
        sql.Identifier('cif'),
        sql.Identifier('email'),
        sql.Identifier('teleophone')
    ]),table=sql.Identifier('companies'))
        cursor.execute('select * from companies where email = %s', (email,))
        company = self.__compound_company(cursor.fetchone())
        cursor.close()
        return company

    def list(self):
        companies_list = []
        cursor = self._dbconection.cursor(cursor_factory=extras.RealDictCursor)
        cursor.execute('select * from companies')
        rows = cursor.fetchall()
        for row in rows:
            companies_list.append(self.__compound_company(row))
        cursor.close()
        return companies_list

    def add(self, company: Company):
        cursor = self._dbconection.cursor()
        cursor.execute('insert into companies (id, name, cif, email, telephone) values (%s, %s, %s, %s, %s)',
                       (
                           company.id,
                           company.name,
                           company.cif,
                           company.email,
                           company.telephone                         
                       ))
        self._dbconection.commit()
        cursor.close()

    def __compound_company(self, row):
        if row is None:
            return None

        print(row)
        company = Company(
            row['id'],
            row['name'],
            row['cif'],
            row['email'],
            row['telephone']
        )
        return company.to_JSON()