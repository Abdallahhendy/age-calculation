from datetime import *

def age_calc(date):
    curr_date_time = datetime.now()

    ''' Split the date into [year, month, and day] to ease process it'''
    # The basic way if you want to practice more
    # year = int(date.split("-")[0])
    # month = int(date.split("-")[1])
    # day = int(date.split("-")[2])

    years = curr_date_time.year - date.year
    months = curr_date_time.month - date.month
    days = curr_date_time.day - date.day

    if days < 0:
        ''' 
        Handling the negative days value by borrow days from the previous month and add it to the current neg value
        '''
        previous_month = (curr_date_time.month - 1) or 12
        previous_month_year = curr_date_time.year if previous_month != 12 else curr_date_time.year - 1
        last_day_prev_month = (datetime(previous_month_year, previous_month + 1, 1) - timedelta(days=1)).day
        days += last_day_prev_month
        months -= 1
    if months < 0:
        '''
        We can do it simple here, as the num of months is fixed and equal to 12
        '''
        months += 12
        years -= 1
    else:
        pass
    
    return years, months, days

def main():
    try:
        usr_inp = input("Enter your birth date (e.g. yyyy-mm-dd [2001-02-05]): ")
        birth_date = datetime.strptime(usr_inp, "%Y-%m-%d")
        years, months, days = age_calc(birth_date)


        print()
        print("The Results...")
        print(f"You have {years} years, {months} months, and {days} days")

    except ValueError:
        print("Unexpected input format, please use yyyy-mm-dd")

if __name__ == "__main__":
    main()
