import datetime
def timeslots():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%d-%m-%Y %I:%M:%S %p")
    print("Current Date and Time:", formatted_time) 
    firstslot = input("Enter the timeslot 1 (24 hour clock ):") 
    try:
        firstslot = datetime.datetime.strptime(firstslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_first = input("enter the work  of first slot ")
    secondslot = input("Enter the timeslot 2 (24 hour clock ):")
    try:
        secondslot = datetime.datetime.strptime(secondslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_second = input("enter the work  of second slot ")
    thirdslot = input("Enter the timeslot 3 (24 hour clock ):")
    try:
        thirdslot = datetime.datetime.strptime(thirdslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_third = input("enter the work  of third slot ")
    fourthslot = input("Enter the timeslot 4 (24 hour clock ):")
    try:
        fourthslot = datetime.datetime.strptime(fourthslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_fourth = input("enter the work  of fourth slot ")
    fifthslot = input("Enter the timeslot 5 (24 hour clock ):")
    try:
        fifthslot = datetime.datetime.strptime(fifthslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_fifth = input("enter the work  of fifth slot ")
    sixthslot = input("Enter the timeslot 6 (24 hour clock ):")
    try:
        sixthslot = datetime.datetime.strptime(sixthslot, "%H:%M").time()
    except ValueError:
        print("Invalid input. Please enter the timeslot in 24-hour format (HH:MM).")
        return
    work_sixth = input("enter the work  of sixth slot ")
    
    print("Timeslot 1:", firstslot, "Work:", work_first)
    print("Timeslot 2:", secondslot, "Work:", work_second)
    print("Timeslot 3:", thirdslot, "Work:", work_third)

    
timeslots()