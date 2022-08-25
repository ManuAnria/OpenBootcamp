import time


def isTimeToLeave():

    current_time = time.localtime(time.time())

    if current_time.tm_hour < 19:
        remaining_time = 19 - current_time.tm_hour
        print(f"You have {remaining_time} hours to leave")
    else:
        print("It is time to go home")


isTimeToLeave()
