#Tan Hyong Hsing 20DDT21F1002
#Mohd Nur Haziq Bin Dahia 20DDT21F1048

#First we import pyodbc so we can access the Microsoft SQL Server
import pyodbc

# Then we connect to the database by provide the driver , server , database , trusted connection value
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};""Server=MSI;""Database=Mansoura;""Trusted_Connection=yes")

# Then create a cursor object to execute SQL queries
cursor = connection.cursor()

# Select tblltem table from database
table_query = ("SELECT * FROM sys.tables WHERE name='tblltem'")
cursor.execute(table_query)

# This function is to allow user to insert new record inside the database
def insert_record():
    name = input("Enter item's name: ")
    price = float(input("Enter item's price: "))
    quantity = int(input("Enter item's quantity: "))

    insert_query = '''
    INSERT INTO tblltem (name, price, quantity) VALUES (?, ?, ?)
    '''
    cursor.execute(insert_query, (name, price, quantity))
    connection.commit()
    print("Record inserted successfully.")

# This function will display the name & price of a item price that higher than 10
def display_items():
    display_query = '''
    SELECT name, price FROM tblltem WHERE price > 10
    '''
    cursor.execute(display_query)
    items = cursor.fetchall()
    if items:
        print("Items with price greater than RM10:")
        for item in items:
            print(f"Name: {item[0]}, Price: {item[1]}")
    else:
        print("No items with price greater than RM10 found.")

# This item will let user update the exist record in database
def update_quantity():
    item_name = input("Enter the name of the item to update quantity: ")
    new_quantity = int(input("Enter the new quantity: "))

    update_query = '''
    UPDATE tblltem SET quantity = ? WHERE name = ?
    '''
    cursor.execute(update_query, (new_quantity, item_name))
    connection.commit()
    print("Quantity updated successfully.")

# This function let user to delete item in the database that have 0 quantity
def delete_items():
    delete_query = '''
    DELETE FROM tblltem WHERE quantity = 0
    '''
    cursor.execute(delete_query)
    connection.commit()
    print("Items deleted successfully.")

# This is the loop that need user's input , it will keep loop unless user exit the system
insertion_completed = False
while True:
    print("******************************************")
    print("Mansoura Exclusive".center(40))
    print("PRODUCT's RECORD SYSTEM".center(40))
    print("******************************************")
    print("1. Add New item")
    print("2. Display Details of Item")
    print("3. Update Quantity of Item")
    print("4. Delete Unavailable Item")
    print("5. Exit System")
    print("******************************************")
    choice = input("Please enter your choice: ")

    if choice == '1':
        insert_record()
        insertion_completed = True
    elif choice == '2':
        display_items()
    elif choice == '3':
        if not insertion_completed:
            print("Please insert records first before updating the quantity.")
            continue
        update_quantity()
    elif choice == '4':
        delete_items()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

    if insertion_completed and choice != '1':
        continue

    if choice != '1':
        insertion_completed = False

# Closing the cursor and connection
cursor.close()
connection.close()
