"""
Time_Share

The purpose of this program is to calculate what
would be efficient times to meet in a week based on some input."""

__author__ = "Abdiel Diaz"
# TimeShare - Version 1.03

# === Sources ===
# {https://www.programiz.com/python-programming/datetime/current-datetime}
# === Sources === 


# Compiles utilities and information about the date function.
from datetime import date


def introduction_timeshare():
    """
    This function initiates the interaction with the user.
    It greets the user and gives a list of options.
    """
    # var
    today = date.today()
    user_name = ""
    # var

    print("\nTimeShare is a program that will assist you on"
          " discovering what time slots work best for your team.")

    # Making sure there is valid input.
    valid_input = False
    while not valid_input:
        user_name = input(
            "Before we go into further detail, how can we call you?: ")
        if user_name == "":
            print("\nPlease input your name.")
            valid_input = False
        else:
            valid_input = True

    if user_name:
        # Using the end= parameter pass in the user's name in the prompt
        print("\nThank you ", end=user_name)
        print("\nOne of the first things that we do in this program is to"
              "calculate the current date, and from there, let you decide "
              "what would work best for your team.")

        print("\nLooks like the current date is (month/day/year): ")
        # Separating the time accordingly
        # with character / and the sep= parameter
        print(today.month, today.day, today.year, sep="/")

        user_confirmation = input("Is that correct? Y/N: ")

        if user_confirmation == "Y" or user_confirmation == "y":
            # Using the character % in the function
            # strftime to get the actual date and time.
            # The function strftime was found in programiz.com

            print("Great. Now we know that the current date is",
                  today.strftime("%B %d, %Y"))
            print("We can do quite a lot of things with our time.")
            print("\nThroughout this program, you'll get the chance"
                  " to put in some data, it will mostly be numbers.")

            user_confirmation = input("Ready to start? Y/N: ")
            if user_confirmation == "Y" or user_confirmation == "y":
                user_time_management()
            else:
                print("\nNeed some more info? Let's do a rewind.")
                introduction_timeshare()

        elif user_confirmation == "N" or user_confirmation == "n":
            print("\nThat's odd. It looks like the time stamp that"
                  " the computer""is generating is incorrect. Lets try again!")
            introduction_timeshare()
        else:
            print("\nOops! Looks like we don't know the entry:"
                  + user_confirmation + ". Lets try that again.")
            introduction_timeshare()
    else:
        print("\nOops! Lets try that again!")
        introduction_timeshare()


def welcome_time_share():
    """
    This function provides information and selections for the user to select
    and perform actions based on the menu options provided.
    """
    print("\n==========================="
          " Welcome to TimeShare ================================")
    print("Lets start with the basics... "
          "\n 1. I want to know how to use TimeShare!"
          " \n 2. I Already know how to use TimeShare.")
    user_selection = input(
        "What's your selection? (Type number of menu item): ")

    # Using the == operator to compare the input and ensure
    # that the user's entry matches the defined menu option.

    if user_selection == "1":
        # Made the function intro_TimeShare separately so that the welcome
        # function's code can be much cleaner and legible.

        introduction_timeshare()

    elif user_selection == "2":
        user_time_management()

    else:
        # Taking into account bad input, and prompting the user to try again.
        print("\nOops! That doesn't look like a valid option."
              "Let's try that again...")
        welcome_time_share()


def user_time_management():
    """
    This function is used merely to compile some preference in times to meet
    and have their meetings. Calls the function calculate_final_time_report
    and passes the user data for it to be handled.
    """
    print("\n==========================="
          "Lets start getting your time shared! ===========================")

    # Gathering information from the user for the final
    # 'Shareable time' report.

    user_name = input("What's your first name?: ")
    # Making sure there's at least some data.
    if user_name:
        after_before_midday = input("\nThanks " + user_name
                                    + ". Now, would you like your"
                                      " meetings in the Morning,"
                                      " or in the afternoon?"
                                      " Please use (M/A):")

        if after_before_midday == "M" or after_before_midday == "m":
            after_before_midday = "Morning"
        else:
            after_before_midday = "Afternoon"

        meeting_hours = float(input(
            "\nAnd how many hours a day can you dedicate for meetings?: "))
        print("Looks like you have " + str(
            meeting_hours) + " hours available for meetings.")

        meeting_minutes = float(input(
            "\nAnd how many minutes do you usually spend in meetings?: "))
        print("Looks like you spend " + str(
            meeting_minutes) + " minutes in your meetings.")

        amount_of_meetings = int(
            input("\nHow many times a week do you have meetings?: "))

        if amount_of_meetings is not 0:
            calculate_final_time_report(after_before_midday, meeting_hours,
                                        meeting_minutes, amount_of_meetings,
                                        user_name)

    else:
        print("Oops! Looks like you did not put a name. Lets try that again.")
        user_time_management()


def calculate_final_time_report(after_before_midday, hours, minutes,
                                amount_of_meetings, user_name):
    """
    Handles the last report given the hours before Mid Day, hours, minutes
    amount of meetings and takes in a name to identify the user. Presents some
    data that was entered, and then offers users the option to modify the data
    entered if so requested.
    """
    print("\n==========================="
          " Your Available Time - Without TimeShare"
          " ===========================")
    print("It looks like your preference on meetings is in the",
          after_before_midday)

    print("Total hours available:", hours)
    print("Total minutes available:", minutes)

    # Giving the user the chance of changing the hour.
    user_response = input(
        "Would you like to modify your available hours?(Y/N): ")
    if user_response == "y" or user_response == "Y":

        print("Would you like to: \n1. Remove hours \n2. Add hours")
        user_response = input(
            "What's your selection? (Type number of menu item): ")

        if user_response == "1":
            user_hour_change = int(
                input("\nWhat would be the amount of hours to remove?: "))
            # Allowing the user to remove hours.
            hours -= user_hour_change
            display_final_time_report(after_before_midday, hours, minutes,
                                      amount_of_meetings, user_name)

        elif user_response == "2":
            user_hour_change = int(
                input("\nWhat would be the amount of hours to add?: "))
            # Allowing the user to add hours.
            hours += user_hour_change
            display_final_time_report(after_before_midday, hours, minutes,
                                      amount_of_meetings, user_name)
        else:
            # Taking into account bad input,
            # and prompting the user to try again.
            print("\nOops! That doesn't look like a valid option."
                  " Let's try that again...")

    else:
        display_final_time_report(after_before_midday, hours, minutes,
                                  amount_of_meetings, user_name)


def display_final_time_report(after_before_midday, hours, minutes,
                              amount_of_meetings, user_name):
    """
    Based on random and purposeful super complex algorithms, the machine is
    able to provide back some data that can result being useful to the user.
    """
    print("\n==========================="
          " TimeShare's suggestion ===========================")
    print("Based on our calculations and your responses.....")
    print("\nMost of your meetings should be in the"
          " " + after_before_midday + ".")

    # TimeShare's way of sharing time currently is dividing by two.
    # Only doing a division here would do the trick
    # since a meeting can be 2.5 hours or more.

    time_shared_hours = int(hours / 2)
    print("\nYou should spend " + str(
        time_shared_hours) + " hour in your " + str(
        after_before_midday) + " meetings.")

    # TimeShare's way of sharing time currently is dividing by two.
    # In this case a float division to ensure it returns a rounded number.

    time_shared_hours = int(hours * amount_of_meetings // 2)
    print("\nOn a weekly basis, you should spend " + str(
        time_shared_hours) + " hours in meetings.")

    # In this equation, I'm calculating the minute range
    # based on the amount of meetings.
    time_shared_minutes = int(hours % minutes ** amount_of_meetings)
    print("\nIn terms of the meeting length in minutes, they should be " + str(
        time_shared_minutes) + " minutes long.")

    # Adding an ending string that repeats itself 2 times at the end
    # of the output of this function so that it looks better.
    for lines in range(2):
        print("======================================="
              "=======================================")

    print("The file export contains more"
          " details as what our suggestions are.")

    user_response = input(
        " Would you like to receive an export of data? (Y/N): ")

    if user_response == "Y":
        create_final_file_export(time_shared_hours, time_shared_minutes,
                                 user_name)
    elif user_response == "N":
        print("Thank you for using Time Share.")
    else:
        print("Oops... Lets try that again.")


def create_final_file_export(time_shared_hours, time_shared_minutes,
                             user_name):
    """
    Based on the data passed, it creates a TXT file record with all the data
    masterfully calculated. The arguments data based on lines and spaces,
    provides sufficient data to inform the user.
    """
    file_export = open("time_share.txt", "w")
    file_export.write("Suggested Report for " + str(user_name))
    file_export.write("\nSuggest Amount Of Hours To Spend in meetings: " + str(
        time_shared_hours))
    file_export.write(
        "\nSuggest Amount Of Minutes To Spend in meetings: " + str(
            time_shared_minutes))

    file_export.write(
        "\n================================"
        "The minute approach"
        "=======================================")
    if time_shared_minutes >= 60:
        file_export.write(
            "\nIt looks like you are still spending"
            " more than 60 minutes on meetings."
            " We would suggest on making this meeting a 30 minute meeting.")
    elif time_shared_minutes <= 60:
        file_export.write(
            "\nIt looks like your time spent on meetings"
            " is below 60 minutes. That's great!")
    file_export.write(
        "\n================================"
        "The Hour approach"
        "=======================================")
    if time_shared_hours > 3:
        file_export.write(
            "\n3 hours a day in meetings sounds like it could be too much."
            " Lets try and hour and 30 minutes.")
    elif time_shared_hours < 3:
        file_export.write(
            "\nSpending less than 3 sounds beneficial for both your"
            " workload and efficiency. Great job!")
    file_export.close()

    return print("\nFile has been successfully generated")


welcome_time_share()
