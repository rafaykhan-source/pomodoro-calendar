import os
from random import randrange
import time
import datetime
import random
from dotenv import load_dotenv
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

def configure():
  load_dotenv()
  
  

# Initializing Google Calendar & sound
configure()
study_calendar = GoogleCalendar(calendar=os.getenv('TOKEN'))
ding = "ding.mp3"

def log_session(type, start, end, desc):
  block = Event(type,
                start=start,
                end=end,
                description=desc,
                color_id=random.randrange(1, 12))
  study_calendar.add_event(block)
  print("Interval successfully logged.")
  return

# Determining Pomodoro Sequence
sequence_time = float(input("How many hours, in total, would you like to study for? This will be used to develop the study sequence. "))
pomodoro_time = float(input("How long, in minutes, would you like each study block to be? "))
rest_time = float(input("How long, in minutes, would you like your breaks to be? "))

for i in range(round(sequence_time*60/(pomodoro_time+rest_time))):
    desc = input("Please enter a description of your Study Block: ")
    input(f"Press Enter/Return to start the your {pomodoro_time} minute study block.")
    start_time = datetime.datetime.now()
    print(f"Your study block has begun! {start_time.strftime('%X')}")
    time.sleep(pomodoro_time*60)
    os.system("afplay " + ding)
    end_time = datetime.datetime.now()
    print(f"Your study block has ended! {end_time.strftime('%X')}")
    log_response = input("Would you like to log this interval on Google Calendar? (Yes or No)").lower()
    if 'yes' in log_response: log_session("Pomodoro Session", start_time, end_time, desc)
    input(f"Press Enter/Return to start your {rest_time} minute break.")
    start_time = datetime.datetime.now()
    print(f"Your break has begun! {start_time.strftime('%X')}")
    time.sleep(rest_time*60)
    os.system("afplay " + ding)
    end_time = datetime.datetime.now()
    print(f"Your break has ended! {end_time.strftime('%X')}")
    log_response = input("Would you like to log this interval on Google Calendar? (Yes or No)").lower()
    if 'yes' in log_response: log_session("Break", start_time, end_time, "Break")
    if 'n' in input("Would you like to continue studying? (Yes or No)").lower(): break
print("Congratulations on studying!")
