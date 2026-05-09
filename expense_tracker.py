import mysql.connector
from datetime import date

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chanchal@SQL2026",
    database="expense_tracker"
)

cursor=db.cursor()

print("Sucessfully Connected")


def add_expense():
    title=input("Enter expense title : ")
    amount=float(input("Enter Amount : "))
    category=input("Enter the Category :")
    current_date = date.today()


    query=""" 
    INSERT INTO expenses(title,amount,category,expense_date) VALUES (%s,%s,%s,%s)"""


    values=(title,amount,category,current_date)

    cursor.execute(query,values)
    db.commit()

    print("Expense added successfully")


def delete_expense():
    expense_id=int(input("Enter expense ID to delete :"))
    
    query="DELETE FROM expenses where id = %s"

    cursor.execute(query,(expense_id,))
    db.commit()

    print("Expenese deleted Successfully")

def view_expenses():
    query = "SELECT * FROM expenses"

    cursor.execute(query)

    records = cursor.fetchall()

    print("\n----------Expenses ----------\n")

    print(f"{'Sr' :<5} {'ID':<5} {'Title':<15}{'Amount':<10} {'Category':<15} {'Date'}")

    print("-" *70)

    serial = 1

    for row in records:
        print(f"{serial:<5} {row[0]:<5} {row[1]:<15} {row[2] :<10} {row[3]:15} {row[4]}")
        serial +=1

while True:
    print("\n -----------Expense Tracker----------")
    print("1. ADD EXPENSE")
    print("2.VIEW EXPENSES")
    print("3.DELETE EXPENSE")
    print("4.EXIT")


    choice=int(input("Enter Your Choice :"))

    if choice ==1:
        add_expense()

    elif choice ==2:
        view_expenses()
    
    elif choice==3:
        delete_expense()

    elif choice==4:
        print("Exiting...")
        break

    else :
        print("Invalid Choice")
