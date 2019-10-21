import flask
import json
import requests
import sqlalchemy
import easygui as eg
import sqlite3 as sql

URL = "http://maps.googleapis.com/maps/api/geocode/json"
cust_id = "Magnus.johan.larsen+7@gmail.com"


def main():

    db_file_dirs = "C:\\Users\\natha\\OneDrive\\Documents\\Citrus_Gruppendatabase_test.db3"

    db_results = get_db_data(db_file_dirs)

    json_response = get_serial_json(db_results)


def get_db_data(db_file_dirs):

    sql_queries = get_sql_queries()

    connection = sql.connect(db_file_dirs)
    conn = connection.cursor()
    conn.execute(sql_queries)
    results = conn.fetchall()
    print(results)
    conn.close()
    connection.close()
    return results


def get_sql_queries():

    sql_query_1 = """select * from Customer_Form where email is '%s'""" % cust_id
    return sql_query_1


def get_serial_json(db_results):


    return


if __name__ == '__main__':
    main()
