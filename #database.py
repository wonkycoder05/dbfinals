# database.py

import mysql.connector

# Database connection configuration
db_config = {
    'host': '127.0.0.1',        
    'user': 'admin',     
    'password': 'FinalTest0000!', 
    'database': 'dbfinal'
}

# Establish connection to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

def add_custdata():
    CustID = input("Enter New Customer ID: ")
    CustName = input("Enter Full Name: ")
    EmailAdd = input("Enter Email: ")
    PhoneNum = input("Enter Phone Number: ")
    HomeAdd = input("Enter Address: ")
    SocialSecNum = input("Enter your social security number: ")

    query = "INSERT INTO customer (CustName, PhoneNum, EmailAdd, HomeAdd, SocialSecNum) VALUES (%s, %s, %s, %s, %s)"
    values = (CustName, PhoneNum, EmailAdd, HomeAdd, SocialSecNum)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Customer record added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_cardata():
    PlateNum = input("Car Plate Number: ")
    CarType = input("Enter Car Type: ")
    CarModel = input("Enter Car Model and Name: ")
    CarColor = input("Enter Car Color: ")
    FuelType = input("Enter Gas, Hybrid, or Electric for Fuel: ")
    PriceList = input("Enter Car Rental Price Per Day: ")

    query = "INSERT INTO car (PlateNum, CarType, CarModel, CarColor, FuelType, Pricelist) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (PlateNum, CarType, CarModel, CarColor, FuelType, PriceList)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Car record added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_dmg():
    DmgID = input("New Damage ID: ")
    CustID = input("Enter Customer ID: ")
    PlateNum = input("Enter Plate Number: ")
    MaintStatus = input("Maintenance Status: ")
    DmgDone = input("Enter Damage Description: ")
    DmgPrice = input("Enter Repair Cost: ")

    query = "INSERT INTO damage (DmgID, CustID, PlateNum, MaintStatus, DmgDone, DmgPrice) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (DmgID, CustID, PlateNum, MaintStatus, DmgDone, DmgPrice)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Damage record added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def maintenancelog():
    LogID = input("Enter Maintenance Log ID: ")
    PlateNum = input("Enter Plate Number: ")
    MaintenanceType = input("Maintenance Type: ")
    MaintStatus = input("Maintenance Status: ")
    WorkshopLocation = input("Input Place of Workshop: ")
    MaintCost = input("Maintenance Cost(In Rp): ")

    query = "INSERT INTO maintenance (LogID, PlateNum, MaintenanceType, MaintStatus, WorkshopLocation, MaintCost) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (LogID, PlateNum, MaintenanceType, MaintStatus, WorkshopLocation, MaintCost)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Maintenance log added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_paymentrentals():
    PaymentID = input("Enter Payment ID: ")
    RentalID = input("Enter Rental ID: ")
    AmountPaid = int(input("Enter Amount Paid (In Rp): "))
    PaymentDate = input("Enter Payment Date (YYYY-MM-DD): ")
    PaymentMethod = input("Enter Payment Method: ")

    query = "INSERT INTO payment (PaymentID, RentalID, AmountPaid, PaymentDate, PaymentMethod) VALUES (%s, %s, %s, %s, %s)"
    values = (PaymentID, RentalID, AmountPaid, PaymentDate, PaymentMethod)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Payment record added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_reservation():
    ReservationID = input("Enter Reservation ID: ")
    CustID = input("Enter Customer ID: ")
    VehicleID = input("Enter Vehicle ID: ")
    ReservationDate = input("Enter Reservation Date (YYYY-MM-DD): ")
    StartDate = input("Enter Start Date (YYYY-MM-DD): ")
    EndDate = input("Enter End Date (YYYY-MM-DD): ")
    Status = input("Enter Reservation Status (or press Enter to leave it blank): ")

    query = """
    INSERT INTO reservation (ReservationID, CustID, VehicleID, ReservationDate, StartDate, EndDate, Status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (ReservationID, CustID, VehicleID, ReservationDate, StartDate, EndDate, Status.strip() or None)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Reservation record added!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_maintstatus():
    PlateNum = input("Enter Plate Number: ")
    new_MaintStatus = input("Enter New Status: ")

    query = "UPDATE maintenance SET MaintStatus = %s WHERE PlateNum = %s"
    values = (new_MaintStatus, PlateNum)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Maintenance status updated!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

while True:
    print("\n1. Add Vehicle")
    print("2. Add Maintenance Log")
    print("3. Add Rental Payments")
    print("4. Add Reservation")
    print("5. Update Maintenance Status")
    print("6. Add Customer Data")
    print("7. Add Damage Done")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_cardata()
    elif choice == '2':
        maintenancelog()
    elif choice == '3':
        add_paymentrentals()
    elif choice == '4':
        add_reservation()
    elif choice == '5':
        update_maintstatus()
    elif choice == '6':
        add_custdata()
    elif choice == '7':
        add_dmg()
    elif choice == '8':   
        break
    else:
        print("Invalid choice. Please choose again.")

# Close cursor and connection
cursor.close()
connection.close()
