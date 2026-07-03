import json

data = 'expense.txt'

def print_table(table):
    print(table)

def load_data():
    try:
        with open(data, 'r') as file:
            res = json.load(file)
            # print(type(res))
            return res
    except FileNotFoundError:
        return []
    
def save_data(table):
    with open(data, 'w') as file:
        json.dump(table,file)
    
def add_expense(table):
    cat = input("Category: ")
    amount = input("Amount: ")
    date = input("Date in DD/MM/YYYY: ")
    table.append({'category': cat, 'amount': amount, 'date': date})
    save_data(table)

def list_all_expense(table):
    print("| S.NO | Category | Amount | Date |")
    for idx, item in enumerate(table, start= 1):
        print(f" | {idx} | {item['category']} | {item['amount']} | {item['date']} | ")

def delete_expense(table):
    list_all_expense(table)
    idx = int(input("Enter index number: "))
    if 1 <= idx <= len(table):
        del table[idx-1]
        save_data(table)
        print("Delete Success" )
    else:
        print("Invaild Number")

def monthly_report(table):
   pass
    

def total_spending(table):
    sum = 0
    for idx in table:
        sum+=int(idx['amount'])
    print(f"Total Spent on Expenses : {sum}")

def highest_expense(table):
    mx = 0
    mx_idx = 0;
    for idx, item in enumerate(table):
        if mx < int(item['amount']):
            mx = int(item['amount'])
            mx_idx = idx

    print(f"The highest expense was in the '{table[mx_idx]['category']}' category, with an amount of {table[mx_idx]['amount']} on {table[mx_idx]['date']}.")

def main():
    table = load_data()
    print_table(table)
    
    while True:
        print("\nEXPENSE TRACKER")
        print("Choose an Option: ")
        print("1. Add New Expense")
        print("2. Delete an Expense")
        print("3. Monthly Report")
        print("4. Total Spending")
        print("5. Highest expense")
        print("6. List of all expenses ")

        choice = input("Enter An Option: ")
        # print_table(table)

        match choice:
            case '1':
                add_expense(table)
            case '2':
                delete_expense(table)
            case '3':
                monthly_report(table)
            case '4':
                total_spending(table)
            case '5':
                highest_expense(table)
            case '6':
                list_all_expense(table)
            case _:
                print("invailed response")


if __name__ == "__main__":
    main()










    
