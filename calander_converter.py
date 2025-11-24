#Ethiopian and Gregorian Calendar Converter

calander = input("Enter:\nA.Convert GC to EC\nB.Convert EC to GC: \nchoice: ")

flag = False


#GC to EC conversion
if calander == "A":
    gc_input = input("Enter the Gregorian date in this format dd/mm/yyyy: ")

    # Split the date into day, month, year
    gc_day, gc_month, gc_year = gc_input.split("/")

    # Convert them to integers
    gc_day = int(gc_day)
    gc_month = int(gc_month)
    gc_year = int(gc_year)

    #year conversion
    if gc_year < 1:
        flag = True
        print("Invalid year for Gregorian calendar.")
    elif (gc_month < 9 or (gc_month == 9 and gc_day < 11)) or gc_day == 11 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_year = gc_year - 8
    else:
        ec_year = gc_year - 7

    #month conversion

    if gc_month < 1 or gc_month > 12:
        flag = True
        print("Invalid month for Gregorian calendar.")
    elif gc_month in [4, 6, 9, 11] and gc_day > 30:
        flag = True
        print("Invalid day for Gregorian calendar.")
    elif (gc_month == 9 and gc_day == 11) and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_month = 13
    elif (gc_month == 9 and gc_day >= 11) or (gc_month == 10 and gc_day <= 10):
        ec_month = 1
    elif (gc_month == 10 and gc_day >= 11) or (gc_month == 11 and gc_day <= 9):
        ec_month = 2
    elif (gc_month == 11 and gc_day >= 10) or (gc_month == 12 and gc_day <= 9):
        ec_month = 3
    elif (gc_month == 12 and gc_day >= 10) or (gc_month == 1 and gc_day <= 8):
        ec_month = 4
    elif (gc_month == 1 and gc_day >= 9) or (gc_month == 2 and gc_day <= 7):
        ec_month = 5
    elif (gc_month == 2 and gc_day >= 8) or (gc_month == 3 and gc_day <= 9):
        ec_month = 6
    elif (gc_month == 3 and gc_day >= 10) or (gc_month == 4 and gc_day <= 8):
        ec_month = 7
    elif (gc_month == 4 and gc_day >= 9) or (gc_month == 5 and gc_day <= 8):
        ec_month = 8
    elif (gc_month == 5 and gc_day >= 9) or (gc_month == 6 and gc_day <= 7):
        ec_month = 9
    elif (gc_month == 6 and gc_day >= 8) or (gc_month == 7 and gc_day <= 7):
        ec_month = 10
    elif (gc_month == 7 and gc_day >= 8) or (gc_month == 8 and gc_day <= 6):
        ec_month = 11
    elif (gc_month == 8 and gc_day >= 7) or (gc_month == 9 and gc_day <= 5):
        ec_month = 12
    else:
        ec_month = 13

    #day conversion
    
    if gc_day < 1 or gc_day > 31:
        flag = True
        print("Invalid day for Gregorian calendar.")
    elif gc_month == 1:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 2 and (gc_year % 4 == 0 and (gc_year % 100 != 0 or gc_year % 400 == 0)):
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 2 and gc_day >= 29:
        flag = True
        print("Invalid day for February in Gregorian calendar.")
    elif gc_month == 2:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 3:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 4:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 5:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 6:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 7:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 8:
        ec_day = gc_day - 6
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 9 and gc_day > 11 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_day = gc_day - 11 
    elif gc_month == 9 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_day = gc_day - 5
    elif gc_month == 9 and gc_day >= 11:
        ec_day = gc_day - 10
    elif gc_month == 9 and gc_day < 11:
        ec_day = gc_day - 5
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 10:
        ec_day = gc_day - 10
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 11:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
    elif gc_month == 12:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
    if flag == False:
        print(f"The Ethiopian calander is: {ec_day}/{ec_month}/{ec_year}")

#EC to GC conversion

elif calander == "B":
    ec_input = input("Enter the Ethiopian date in this format dd/mm/yyyy: ")

    # Split the date
    ec_day, ec_month, ec_year = ec_input.split("/")

    # Convert to integers
    ec_day = int(ec_day)
    ec_month = int(ec_month)
    ec_year = int(ec_year)
    #year conversion

    if ec_year < 1:
        flag = True
        print("Invalid year for Ethiopian calender.")

    elif ec_month < 4 or (ec_month == 4 and ec_day < 23):
        gc_year = ec_year + 7
    else:
        gc_year = ec_year + 8

    #month conversion

    if ec_month < 1 or ec_month > 13:
        flag = True
        print("Invalid month for Ethiopian calendar.")
    elif (ec_month == 6 and ec_day == 21) and ((ec_year + 1) % 4 == 0 and ((ec_year + 1) % 100 != 0 or (ec_year + 1) % 400 == 0)):
            gc_month = 2
    elif (ec_month == 4 and ec_day >= 23) or (ec_month == 5 and ec_day <= 23):
        gc_month = 1
    elif (ec_month == 5 and ec_day >= 24) or (ec_month == 6 and ec_day <= 21):
        gc_month = 2
    elif (ec_month == 6 and ec_day >= 22) or (ec_month == 7 and ec_day <= 22):
        gc_month = 3
    elif (ec_month == 7 and ec_day >= 23) or (ec_month == 8 and ec_day <= 22):
        gc_month = 4
    elif (ec_month == 8 and ec_day >= 23) or (ec_month == 9 and ec_day <= 23):
        gc_month = 5
    elif (ec_month == 9 and ec_day >= 24) or (ec_month == 10 and ec_day <= 23):
        gc_month = 6
    elif (ec_month == 10 and ec_day >= 24) or (ec_month == 11 and ec_day <= 24):
        gc_month = 7
    elif (ec_month == 11 and ec_day >= 25) or (ec_month == 12 and ec_day <= 25):
        gc_month = 8
    elif (ec_month == 12 and ec_day >= 26) or (ec_month == 1 and ec_day <= 20) or (ec_month == 13 and ec_day <= 5):
        gc_month = 9
    elif (ec_month == 13 and ec_day == 6) and ((ec_year + 1) % 4 == 0 and ((ec_year + 1) % 100 != 0 or (ec_year + 1) % 400 == 0)):
        gc_month = 9
    elif (ec_month == 1 and ec_day >= 21) or (ec_month == 2 and ec_day <= 21):
        gc_month = 10
    elif (ec_month == 2 and ec_day >= 22) or (ec_month == 3 and ec_day <= 21):
        gc_month = 11
    elif (ec_month == 3 and ec_day >= 22) or (ec_month == 4 and ec_day <= 22):
        gc_month = 12

    #day conversion

    if ec_day < 1 or ec_day > 30:
        flag = True
        print("Invalid day for Ethiopian calendar.")
    elif ec_month == 1 and (gc_year % 100 != 0 or gc_year % 400 == 0):
        gc_day = ec_day + 11
        if gc_day > 30:
            gc_day -= 30
    elif ec_month == 1 :
        gc_day = ec_day + 10
        if gc_day > 30:
            gc_day -= 30
    elif ec_month == 2:
        gc_day = ec_day + 10
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 3:
        gc_day = ec_day + 9
        if gc_day > 30:
            gc_day -= 30
    elif ec_month == 4:
        gc_day = ec_day + 9
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 5:
        gc_day = ec_day + 8
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 6 and (gc_year % 100 != 0 or gc_year % 400 == 0):
         gc_day = ec_day + 8
         if gc_day > 28:
            gc_day -= 29
    elif ec_month == 6:
        gc_day = ec_day + 7
        if gc_day > 28:
            gc_day -= 28
    elif ec_month == 7:
        gc_day = ec_day + 9
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 8:
        gc_day = ec_day + 8
        if gc_day > 30:
            gc_day -= 30
    elif ec_month == 9:
        gc_day = ec_day + 8
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 10:
        gc_day = ec_day + 7
        if gc_day > 30:
            gc_day -= 30
    elif ec_month == 11:
        gc_day = ec_day + 7
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 12:
        gc_day = ec_day + 6
        if gc_day > 31:
            gc_day -= 30
    elif ec_month == 13 and ((ec_year + 1) % 4 == 0 and ((ec_year + 1) % 100 != 0 or (ec_year + 1) % 400 == 0)):
        gc_day = ec_day + 5
    elif ec_month == 13 and ec_day > 5:
        flag = True
        print("Invalid day for Ethiopian 13th month.")
    elif ec_month == 13:
        gc_day = ec_day + 5
    if flag == False:
        print(f"The Gregorian calander is: {ec_day}/{ec_month}/{ec_year}")
else:
    print(f"{calander} is Invalid choice. Please select A or B.")
        