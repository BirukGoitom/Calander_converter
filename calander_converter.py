calander = int(input("Enter:\n1.Convert GC to EC\n2.Convert EC to GC: \nchoice: "))
#first commit
if calander == 1:
    gc_year = int(input("Enter the Gregorian year: "))
    gc_month = int(input("Enter the Gregorian month (1-12): "))
    gc_day = int(input("Enter the Gregorian day: "))
    if gc_year < 1:
        print("Invalid year for Gregorian calendar.")
    elif gc_day == 11 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_year = gc_year - 8
        print(f"The Ethiopian year is: {ec_year}")
    elif gc_month < 9 or (gc_month == 9 and gc_day < 11):
        ec_year = gc_year - 8
        print(f"The Ethiopian year is: {ec_year}")
    else:
        ec_year = gc_year - 7
        print(f"The Ethiopian year is: {ec_year}")

    if gc_month < 1 or gc_month > 12:
        print("Invalid month for Gregorian calendar.")

    elif (gc_month == 9 and gc_day == 11) and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_month = 13
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 9 and gc_day >= 11) or (gc_month == 10 and gc_day <= 10):
        ec_month = 1
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 10 and gc_day >= 11) or (gc_month == 11 and gc_day <= 9):
        ec_month = 2
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 11 and gc_day >= 10) or (gc_month == 12 and gc_day <= 9):
        ec_month = 3
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 12 and gc_day >= 10) or (gc_month == 1 and gc_day <= 8):
        ec_month = 4
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 1 and gc_day >= 9) or (gc_month == 2 and gc_day <= 7):
        ec_month = 5
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 2 and gc_day >= 8) or (gc_month == 3 and gc_day <= 9):
        ec_month = 6
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 3 and gc_day >= 10) or (gc_month == 4 and gc_day <= 8):
        ec_month = 7
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 4 and gc_day >= 9) or (gc_month == 5 and gc_day <= 8):
        ec_month = 8
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 5 and gc_day >= 9) or (gc_month == 6 and gc_day <= 7):
        ec_month = 9
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 6 and gc_day >= 8) or (gc_month == 7 and gc_day <= 7):
        ec_month = 10
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 7 and gc_day >= 8) or (gc_month == 8 and gc_day <= 6):
        ec_month = 11
        print(f"The Ethiopian month is: {ec_month}")

    elif (gc_month == 8 and gc_day >= 7) or (gc_month == 9 and gc_day <= 5):
        ec_month = 12
        print(f"The Ethiopian month is: {ec_month}")

    else:
        ec_month = 13
        print(f"The Ethiopian month is: {ec_month}")

    if gc_day < 1 or gc_day > 31:
        print("Invalid day for Gregorian calendar.")

    elif gc_month == 1:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 2 and gc_day > 29:
        print("Invalid day for February in Gregorian calendar.")

    elif gc_month == 2 and (gc_year % 4 == 0 and (gc_year % 100 != 0 or gc_year % 400 == 0)):
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 2:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 3:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 4:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 5:
        ec_day = gc_day - 8
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 6:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 7:
        ec_day = gc_day - 7
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 8:
        ec_day = gc_day - 6
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 9 and gc_day > 11 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_day = gc_day - 11 
        print(f"The Ethiopan day is: {ec_day}")

    elif gc_month == 9 and ((gc_year + 1) % 4 == 0 and ((gc_year + 1) % 100 != 0 or (gc_year + 1) % 400 == 0)):
        ec_day = gc_day - 5
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 9 and gc_day >= 11:
        ec_day = gc_day - 10
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 9 and gc_day < 11:
        ec_day = gc_day - 5
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 10:
        ec_day = gc_day - 10
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 11:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")

    elif gc_month == 12:
        ec_day = gc_day - 9
        if ec_day < 1:
            ec_day += 30
        print(f"The Ethiopian day is: {ec_day}")
    
elif calander == 2:
    ec_year = int(input("Enter the Ethiopian year: "))
    ec_month = int(input("Enter the Ethiopian month (1-13): "))
    ec_day = int(input("Enter the Ethiopian day: "))
    
    if ec_year < 1:
        print("Invalid Ethiopian year.")

    elif ec_month < 4 or (ec_month == 4 and ec_day < 23):
        gc_year = ec_year + 7
        print(f"The Gregorian year is: {gc_year}")
    else:
        gc_year = ec_year + 8
        print(f"The Gregorian year is: {gc_year}")

    if ec_month < 1 or ec_month > 13:
        print("Invalid Ethiopian month.")
    else:
        gc_month = ec_month + 8
        if gc_month > 12:
            gc_month -= 12
        print(f"The Gregorian month is: {gc_month}")
    
    if ec_day < 1 or ec_day > 30:
        print("Invalid day for Ethiopian calendar.")
    else:
        gc_day = ec_day + 9
        if gc_day > 31:
            gc_day -= 30
        print(f"The Gregorian day is: {gc_day}")

            
else:
    print("Invalid input. Please enter 1 or 2.")
