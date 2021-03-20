# Abdiel Diaz
# TimeShare - Version 1
# The purpose of this program is to calculate what would be efficient times to meet in an array of users.
# Sources
# {https://www.programiz.com/python-programming/datetime/current-datetime}


from datetime import date


def introduction_TimeShare():
    #var
    today = date.today()
    #var

    print("\nTimeShare is a program that will assist you on discovering what time slots work best for your team.")
    user_name = input("Before we go into further detail, how can we call you?: ")

    if user_name:
        #Using the end= parameter pass in the user's name in the prompt
        print("\nThank you ", end=user_name)
        print("\nOne of the first things that we do in this program is to calculate the current date, and from there, let you decide what would work best for your team.")

        print("\nLooks like the current date is (month/day/year): ")
        #Separating the time accordingly with character / and the sep= parameter
        print(today.month, today.day, today.year, sep="/")

        user_confirmation = input("Is that correct? Y/N: ")

        if user_confirmation == "Y" or user_confirmation == "y":
            # using the character % in the function strftime to get the actual date and time.
            # The function strftime was found in programiz.com
            print("Great. Now we know that the current date is", today.strftime("%B %d, %Y"))
            print("We can do quite a lot of things with our time.", end="\n")
            print("\nThroughout this program, you'll get the chance to put in some data, it will mostly be numbers.")

            user_confirmation = input("Ready to start? Y/N: ")
            if user_confirmation == "Y" or user_confirmation == "y":
                user_time_management()
            else:
                print("\nNeed some more info? Let's do a rewind.")
                introduction_TimeShare()

        elif user_confirmation == "N" or user_confirmation == "n":
            print("\nThat's odd. It looks like the time stamp that the computer is generating is incorrect. Lets try again!")
            introduction_TimeShare()

        else:
            print("\nOpps! Looks like we don't know the entry:" + user_confirmation +". Lets try that again." )
            introduction_TimeShare()
    else:
        print("\nOops! Lets try that again!")
        introduction_TimeShare()


def welcome_TimeShare():

    print("\n=========================== Welcome to TimeShare ================================")
    print("Lets start with the basics... \n 1. I want to know how to use TimeShare! \n 2. I Already know how to use TimeShare.")
    user_selection = input("What's your selection? (Type number of menu item): ")

    #Using the == operator to compare the input and ensure that the user's entry matches the defined menu option.
    if user_selection == "1":
        #Made the function intro_TimeShare separately so that the welcome function's code can be much cleaner and legible.
        introduction_TimeShare()

    elif user_selection == "2":
        user_time_management()

    else:
        #Taking into account bad input, and prompting the user to try again.
        print("\nOoops! That doesn't look like a valid option. Let's try that again...")
        welcome_TimeShare()


def user_time_management():
    print("\n=========================== Lets start getting your time shared! ===========================")
    #Gathering information from the user for the final 'Shareable time' report.

    user_name = input("What's your first name?: ")

    #Making sure there's at least some data.
    if user_name:
        after_before_midday = input("\nThanks " + user_name + ". Now, would you like your meetings in the Morning, or in the afternoon? Please use (M/A):")

        if after_before_midday == "M" or after_before_midday == "m":
            after_before_midday = "morning"
        else:
            after_before_midday = "afternoon"

        # For this particular request, I will wait to implement it further on the project. It will essentially call another function to allow input for days.
        #meeting_days = input("and what days  can you meet?: "))

        meeting_hours = float(input("\nAnd how many hours a day can you dedicate for meetings?: "))
        print("Looks like you have " + str(meeting_hours) + " hours available for meetings." )


        meeting_minutes = float(input("\nAnd how many minutes do you usually spend in meetings?: "))
        print("Looks like you spend " + str(meeting_minutes) + " minutes in your meetings." )

        amount_of_meetings = int(input("\nHow many times a week do you have meetings?: "))


        # Function that will calculate the final report for the user.
        calculate_final_time_report(after_before_midday, meeting_hours, meeting_minutes, amount_of_meetings)

    else:
        print("Oops! Looks like you did not put a name. Lets try that again.")
        user_time_management()


def calculate_final_time_report(after_before_midday, hours, minutes, amount_of_meetings):
    print("\n=========================== Your Available Time - Without TimeShare ===========================")
    print("It looks like your preference on meetings is in the", after_before_midday)
    print("Total hours available:", hours)
    print("Total minutes available:", minutes)

    #Giving the user the chance of changing the hour.
    user_response = input("Would you like to modify your available hours?(Y/N): ")
    if user_response == "y" or user_response == "Y":

       print("Would you like to: \n1. Remove hours \n2. Add hours")
       user_response = input("What's your selection? (Type number of menu item): ")

       if user_response == "1":
            user_hour_change = int(input("\nWhat would be the amount of hours to remove?: "))
            #Allowing the user to remove hours.
            hours = hours - user_hour_change
            display_final_time_report(after_before_midday, hours, minutes, amount_of_meetings)

       elif user_response == "2":
            user_hour_change = int(input("\nWhat would be the amount of hours to add?: "))
            # Allowing the user to add hours.
            hours = hours + user_hour_change
            display_final_time_report(after_before_midday, hours, minutes, amount_of_meetings)
       else:
           # Taking into account bad input, and prompting the user to try again.
           print("\nOoops! That doesn't look like a valid option. Let's try that again...")

    else:
        display_final_time_report(after_before_midday, hours, minutes, amount_of_meetings)


def display_final_time_report(after_before_midday, hours, minutes, amount_of_meetings):
    print("\n=========================== TimeShare's suggestion ===========================")
    print("Based on our calculations and your responses.....")
    print("\nMost of your meetings should be in the " + after_before_midday + ".")

    #TimeShare's way of sharing time currently is dividing by two. Only doing a division here would do the trick since a meeting can be 2.5 hours or more.
    time_shared_hours = int(hours / 2)
    print("\nYou should spend " + str(time_shared_hours) + " hour in your " + str(after_before_midday) + " meetings.")

    #TimeShare's way of sharing time currently is dividing by two. In this case a float division to ensure it returns a rounded number.
    time_shared_hours = int(hours * amount_of_meetings // 2)
    print("\nOn a weekly basis, you should spend " + str(time_shared_hours) + " hours in meetings.")

    #In this equation, I'm calculating the minute range based on the amount of meetings.
    time_shared_minutes = int(hours % minutes ** amount_of_meetings)
    print("\nIn terms of the meeting length in minutes, they should be " + str(time_shared_minutes) + " minutes long.")

    # Adding an ending string that repeats itself 3 times at the end of the output of this function so that it looks better.
    print("\n==============================================================================" * 2)

welcome_TimeShare()


