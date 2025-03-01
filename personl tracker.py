from exp_trackr_func import *

print('Personal Expense Tracker'.center(50,'-'))
print()
2
def main():
    initialize_file()
    while True:
        print('1. Add Expense')
        print('2. View Expense')
        print('3. Filter Expense')
        print('4. Delete Expense')
        print('5. Monthly Summary')
        print('6. Exit')
        print()
        choice=input('Select any one:')

        if choice=='1':
            date=input('Enter date(yyyy-mm-dd):')
            amount=input('Enter amount:')
            category=input('Enter category:')
            description=input('Enter description:')
            add_expense(date,amount,category,description)
            print()

        elif choice=='2':
            view_expenses()
            print()

        elif choice=='3':
            filter_by=input('Filter by(date/category):')
            filter_value=input(f'enter {filter_by}:')
            filter_expenses(filter_by,filter_value)
            print()

        elif choice=='4':
            date = input('Enter date(yyyy-mm-dd):')
            amount = input('Enter amount:')
            category = input('Enter category:')
            description = input('Enter description:')
            delete_expense(date,amount,category,description)
            print()

        elif choice=='5':
            monthly_summary()

        elif choice=='6':
            print('Exit from program')
            break

        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
