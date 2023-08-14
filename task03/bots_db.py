"""
Task_3 Version 0.4

! edit config.py !

All DB methods working fine
But not integrated in class CaptchSolver yet
"""


from config import *
import mysql.connector as SQLC

#connect to Database
def connect_mydb():
    mydb = SQLC.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
    return mydb

# def create_db(mydb, name):
#     mydb.cursor().execute(f'CREATE DATABASE {name}')

# def create_table(mydb, name):
#     sql = (
#        f'CREATE TABLE `{DB_NAME}`.`{name}` ('
#        '`id_bot` INT NOT NULL,'
#        '`solve_method` VARCHAR(45) NULL,'
#         'PRIMARY KEY (`id_bot`));'
#     )
#     mydb.cursor().execute(sql)
#     print( f"Table {name} created.")

#add new bot in DB
def db_add_bot(mydb, id_bot, solve_method):
    mycursor = mydb.cursor()
    sql = f"INSERT INTO {TABLE_NAME} (id_bot, solve_method) VALUES (%s, %s)"
    val = (id_bot, solve_method)
    mycursor.execute(sql, val)  
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# return int=bot_id or None if does not exist
def db_get_bot(mydb, id_bot):
    mycursor = mydb.cursor()
    sql = f"SELECT * FROM {TABLE_NAME} WHERE id_bot ='{id_bot}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    return myresult 
