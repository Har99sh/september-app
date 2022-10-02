from flask import Blueprint, make_response
from models.company import Company
from database.db import get_connection


company = Blueprint('company', __name__, url_prefix="/company")

@company.get('/')
def get_companies():
    try:
        connection = get_connection()
        company_list = []
        with connection.cursor() as cursor:
                cursor.execute("SELECT id, name, cif, email, telephone FROM companies ORDER BY name ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                    company = Company(row[0], row[1], row[2], row[3], row[4], )
                    company_list.append(company.to_JSON())
        
        connection.close()
        return make_response(company_list)
    except Exception as ex:
        raise Exception(ex)

@company.get('/<id>')
def get_one_company(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, cif, email, telephone FROM companies WHERE id = %s", (id,))
            row = cursor.fetchone()
            one_company = None
            if row is not None:
               one_company = Company(id=row[0], name=row[1], cif=row[2], email=row[3], telephone=row[4])
               one_company = one_company.to_JSON()
            
        
        connection.close()
        return one_company
    except Exception as ex:
        raise Exception(ex)

