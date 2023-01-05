import config
import mysql.connector

def db_init():
   global sh
   global sh_cursor
   
   sh = mysql.connector.connect(
   host=config.host,
   user=config.username,
   password=config.password,
   database=config.db
   )
   
   sh_cursor = sh.cursor()
   return

def store_pomodoro(title: str, desc: str, start: str, end: str):
   sh_cursor.execute(f"""
                     INSERT INTO studyHistory
                     VALUES ();""")
   return