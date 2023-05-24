import os
import time
import datetime as dt
import random
from dotenv import load_dotenv
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar


def configure():
    load_dotenv()
    return


def ding():
    os.system("afplay " + "ding.mp3")
    return


def initialize_calendar():
    configure()
    global gc
    gc = GoogleCalendar(calendar=os.getenv("cal"), credentials_path="credentials.json")
    return


def log_event(name, start, end, desc):
    block = Event(
        name, start=start, end=end, desc=desc, color_id=random.randrange(1, 12)
    )
    gc.add_event(block)
    print("Interval successfully logged.")
    return


def log_response_query(name, start, end, desc):
    log_response = input(
        "Would you like to log this interval on Google Calendar? (Yes or No)"
    ).lower()
    if "yes" in log_response:
        log_event(name, start, end, desc)
    return


def report_block(study_sequence, seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    study_sequence.append(f"{int(hours)}:{int(minutes)}:{seconds:.2f}")


def traditional():
    pomodoro_time = float(
        input("How long, in minutes, would you like each study block to be? ")
    )
    rest_time = float(input("How long, in minutes, would you like your breaks to be? "))

    while True:
        desc = input("Please enter a description of your Study Block: ")
        input(
            f"Press Enter/Return to start the your {pomodoro_time} minute study block."
        )
        start = dt.datetime.now()
        print(f"Your study block has begun! {start.strftime('%X')}")
        time.sleep(pomodoro_time * 60)
        ding()
        end = dt.datetime.now()
        print(f"Your study block has ended! {end.strftime('%X')}")
        log_response_query("Pomodoro Session", start, end, desc)
        input(f"Press Enter/Return to start your {rest_time} minute break.")
        start = dt.datetime.now()
        print(f"Your break has begun! {start.strftime('%X')}")
        time.sleep(rest_time * 60)
        ding()
        end = dt.datetime.now()
        print(f"Your break has ended! {end.strftime('%X')}")
        log_response_query("Break", start, end, "Break")
        if "n" in input("Would you like to continue studying? (Yes or No)").lower():
            break
    return


def personal():
    study_sequence = []

    while True:
        desc = input("Please enter what you're doing: ")
        input("Press Enter/Return to start studying. ")
        timer_start = time.time()
        start = dt.datetime.now()
        print(f"Your study block has begun! {start.strftime('%X')}")
        input("Press Enter/Return when you're done studying. ")
        end = dt.datetime.now()
        timer_end = time.time()
        print(f"Your study block has ended! {end.strftime('%X')}")
        log_response_query("Pomodoro Session", start, end, desc)
        report_block(study_sequence, timer_end - timer_start)
        if "n" in input("Would you like to continue studying? (Yes or No)").lower():
            break
        input("Press Enter/Return to start a break.")
        timer_start = time.time()
        start = dt.datetime.now()
        print(f"Your break has begun! {start.strftime('%X')}")
        input("Press Enter/Return to end your break.")
        end = dt.datetime.now()
        timer_end = time.time()
        print(f"Your break has ended! {end.strftime('%X')}")
        log_response_query("Break", start, end, "Break")
        report_block(study_sequence, timer_end - timer_start)
        print("Your study sequence thus far is:", study_sequence)
        if "n" in input("Would you like to continue studying? (Yes or No)").lower():
            break
    return


# Program Start

sequence_choice = input(
    """Would you like to develop a personalized study sequence, or follow a traditional study sequence? 
Please respond either 'personal' or 'traditional': """
).lower()

initialize_calendar()

traditional() if "trad" in sequence_choice else personal()

print("Congratulations on studying!")
