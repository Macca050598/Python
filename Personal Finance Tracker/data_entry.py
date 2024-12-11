from datetime import datetime


date_format = "%d-%m-%Y"
CATEGORIES = {
    "I": "Income",
    "E": "Expenses"         
              }


def get_date(prompt, allow_default = False):
    date_str = input(prompt) 
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        # Get the date, and convert it into this date format
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)
        
             
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        #Make sure amount isn't zer or less than zeo
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value")
        return amount
    # If it's less return value error
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input ("Enter the category ('I' for income and or 'E' for Expense): ").upper()
    #Uses the category variable we made and make sure a user chooses correct category
    if category in CATEGORIES:
        return CATEGORIES[category]
    #Error if they don't enter correct letter
    print("Invalid category. Please enter 'I' for income or 'E' for expense")
    return get_category()

def get_desciption():
    return input("Enter a description (optional): ")

    