import mysql.connector as mycon

# Connect to the database
db = mycon.connect(
    host="localhost",
    user="BHAVYA",
    password="30072004BB@@@",
    database="hotel_management"
)

cursor = db.cursor()

# Function to add a room
def add_room():
    room_number = input("Enter Room Number: ")
    room_type = input("Enter Room Type: ")
    room_rent = float(input("Enter Room Rent: "))

    sql = "INSERT INTO rooms (room_number, room_type, room_rent, status) VALUES (%s, %s, %s, 'free')"
    values = (room_number, room_type, room_rent)
    cursor.execute(sql, values)
    db.commit()
    print("Room added successfully.")

# Function to add a customer
def add_customer():
    customer_id=int(input("enter the customer id"))
    customer_name = input("Enter Customer Name: ")
    customer_address = input("Enter Customer Address: ")
    customer_phone = input("Enter Customer Phone: ")
    customer_email= input("Enter Customer email: ")


    sql = "INSERT INTO customers (customer_id,customer_name, customer_address, customer_phone, customer_email ) VALUES (%s, %s, %s, %s,%s)"
    values = (customer_id,customer_name, customer_address, customer_phone,customer_email  )
    cursor.execute(sql, values)
    db.commit()
    print("Customer added successfully.")





    # Function to generate a bill
def generate_bill():
    room_number = input("Enter Room Number: ")
    customer_id = input("Enter Customer ID: ")

    # Check if the room is occupied
    cursor.execute("SELECT status FROM rooms WHERE room_number = %s", (room_number,))
    room_status = cursor.fetchone()

    if room_status is not None and room_status[0] == 'occupied':
        print(f"Room {room_number} is already occupied.")
        return

    cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()

    if customer is None:
        print(f"Customer with ID {customer_id} does not exist.")
        return

    cursor.execute("SELECT room_rent FROM rooms WHERE room_number = %s", (room_number,))
    room_rent = cursor.fetchone()[0]

    # Calculate total payable amount
    advance = float(input("Enter Advance Amount: "))
    days_stayed = int(input("Enter the number of days stayed: "))
    total_amount = (room_rent * days_stayed) - advance

    # Insert bill into the database
    cursor.execute("INSERT INTO bills (room_number, customer_id, total_amount) VALUES (%s, %s, %s)",
                   (room_number, customer_id, total_amount))

    # Update the room status to 'occupied'
    cursor.execute("UPDATE rooms SET status = 'occupied' WHERE room_number = %s", (room_number,))

    db.commit()
    print(f"Bill generated successfully. Total Amount: {total_amount}")

def display_staying_customers():
   
    sql = "SELECT c.customer_id, c.customer_name, r.room_number, r.room_type, b.total_amount " \
          "FROM customers c " \
          "JOIN bills b ON c.customer_id = b.customer_id " \
          "JOIN rooms r ON b.room_number = r.room_number " \
          "WHERE r.status = 'occupied';"

    cursor.execute(sql)
    records = cursor.fetchall()

    if not records:
        print("No customers are currently staying at the hotel.")
    else:
        print("Details of customers staying at the hotel:")
        print("{:<5} {:<20} {:<10} {:<15} {:<15}".format("ID", "Name", "Room No", "Room Type", "Total Amount"))
        print("-" * 65)
        for record in records:
            customer_id, customer_name, room_number, room_type, total_amount = record
            print("{:<5} {:<20} {:<10} {:<15} {:<15}".format(customer_id, customer_name, room_number, room_type, total_amount))

    db.close()



# Example usage
while True:
    print("1. Add Room")
    print("2. Add Customer")
    print("3. Display Staying Customers")
    print("4.  Generate Bill")
    print("5.  Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_room()
    elif choice == '2':
        add_customer()
    elif choice == '3':
        display_staying_customers()
    elif choice == '4':
        generate_bill()
    elif choice == '5':
        break
# Close the database connection
db.close()
