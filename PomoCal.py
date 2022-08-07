import os
import time
import datetime
from dotenv import load_dotenv
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

def configure():
  load_dotenv()

# Initializing Google Calendar & sound
configure()
study_calendar = GoogleCalendar(calendar=os.getenv('TOKEN'))
file = "ding.mp3"
# Determining Pomodoro Sequence
sequence_time = float(input("About how long, in minutes, would you like to study for? This will be used to develop the study sequence. "))
pomodoro_time = float(input("How long, in minutes, would you like each study block to be? "))
rest_time = float(input("How long, in minutes, would you like your breaks to be? "))

for i in range(round(sequence_time/(pomodoro_time+rest_time))):
    description = input("Please enter a description of your Study Block: ")
    input(f"Press Enter/Return to start the your {pomodoro_time} minute study block.")
    study_start_time = datetime.datetime.now()
    print(f"Your study block has begun! {study_start_time.strftime('%X')}")
    time.sleep(pomodoro_time*60)
    os.system("afplay " + file)
    study_end_time = datetime.datetime.now()
    print(f"Your study block has ended! {study_end_time.strftime('%X')}")
    input(f"Press Enter/Return to start your {rest_time} minute break.")
    break_start_time = datetime.datetime.now()
    print(f"Your break has begun! {break_start_time.strftime('%X')}")
    time.sleep(rest_time*60)
    os.system("afplay " + file)
    break_end_time = datetime.datetime.now()
    print(f"Your break has ended! {break_start_time.strftime('%X')}")
    log_response = input("Would you like to log this interval on Google Calendar? (Yes or No)").lower()
    if 'yes' in log_response:
        study_block = Event('Pomodoro Session',
                start=study_start_time,
                end=study_end_time,
                description=description,
                color_id=1)
        study_calendar.add_event(study_block)
        break_block = Event('Break',
                start=break_start_time,
                end=break_end_time,
                color_id=4)
        study_calendar.add_event(break_block)
        print("Interval successfully logged.")
    if 'n' in input("Would you like to continue studying? (Yes or No)").lower(): break
print("Congratulations on studying!")

