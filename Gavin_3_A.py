from functools import reduce

expense_list=[]

def get_expenses():
    #Infinite Loop
    while True:
        #Prompy user
        expense = input("Enter next type of expense(or type DONE to finish): ")
        if expense.lower() == 'done':
            break
        try:
            expense_amount = float(input(f"Enter amount for {expense}: "))
            expense_list.append((expense,expense_amount))   
        except ValueError:
            print("\nPlease enter amount without any special characters\n")
    return expense_list

# Function to calculate the total expense
def calculate_total(expense_list):
    return reduce(lambda x, y: x + y[1], expense_list, 0)

# Function to find the highest expense
def find_highest_expense(expense_list):
    return reduce(lambda x, y: x if x[1] > y[1] else y, expense_list)

# Function to find the lowest expense
def find_lowest_expense(expense_list):
    return reduce(lambda x, y: x if x[1] < y[1] else y, expense_list)

expenses = get_expenses()
total_expense = calculate_total(expenses)
highest_expense = find_highest_expense(expenses)
lowest_expense = find_lowest_expense(expenses)
    
print("\nExpense Summary:")
print(f"Total expense: ${total_expense:.2f}")
print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")