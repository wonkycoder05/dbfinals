import mysql.connector

# Database connection configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'admin',
    'password': 'FinalTest0000!',
    'database': 'vehicle_rental'
}

try:
    # Establish connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    def add_customer():
        CustName = input("Enter Full Name: ")
        EmailAdd = input("Enter Email: ")
        PhoneNum = input("Enter Phone Number: ")
        HomeAdd = input("Enter Address: ")
        SocialSecNum = input("Enter your Social Security Number: ")

        query = """
        INSERT INTO customer (CustName, PhoneNum, EmailAdd, HomeAdd, SocialSecNum)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (CustName, PhoneNum, EmailAdd, HomeAdd, SocialSecNum)

        try:
            cursor.execute(query, values)
            connection.commit()
            print("Customer record added!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_vehicle():
        VehicleID = input("Enter Vehicle ID: ")
        PlateNum = input("Enter Car Plate Number: ")
        VehicleType = input("Enter Car Type: ")
        VehicleModel = input("Enter Car Model and Name: ")
        VehicleColor = input("Enter Car Color: ")
        FuelType = input("Enter Fuel Type (Gas, Hybrid, Electric): ")
        PricePerDay = float(input("Enter Car Rental Price Per Day: "))

        query = """
        INSERT INTO vehicle (VehicleID, PlateNum, VehicleType, VehicleModel, VehicleColor, FuelType, PricePerDay)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (VehicleID, PlateNum, VehicleType, VehicleModel, VehicleColor, FuelType, PricePerDay)

        try:
            cursor.execute(query, values)
            connection.commit()
            print("Vehicle record added!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_maintenance_log():
        vehicle_VehicleID = input("Enter Vehicle ID: ")
        PlateNum = input("Enter Plate Number: ")
        MaintenanceType = input("Enter Maintenance Type: ")
        MaintStatus = input("Enter Maintenance Status: ")
        WorkshopLocation = input("Enter Workshop Location: ")
        MaintCost = float(input("Enter Maintenance Cost: "))

        query = """
        INSERT INTO maintenancelog (vehicle_VehicleID, PlateNum, MaintenanceType, MaintStatus, WorkshopLocation, MaintCost)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (vehicle_VehicleID, PlateNum, MaintenanceType, MaintStatus, WorkshopLocation, MaintCost)


        try:
            cursor.execute(query, values)
            connection.commit()
            print("Maintenance log added!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_payment():
        # Get input from the user
        PaymentID = input("Enter Payment ID: ").strip()
        RentalID = input("Enter Rental ID: ").strip()
        CustID = input("Enter Customer ID: ").strip()
        EmployeeID = input("Enter Employee ID: ").strip()
        AmountPaid = input("Enter Amount Paid: ").strip()
        PaymentDate = input("Enter Payment Date (YYYY-MM-DD): ").strip()
        PaymentMethod = input("Enter Payment Method (e.g., Credit Card, Debit Card): ").strip()

        # Validate AmountPaid (ensure it contains only digits)
        if not AmountPaid.isdigit():
            print("Error: Amount Paid must contain only numeric values.")
            return
        
        # Insert query
        query = """
        INSERT INTO payment (PaymentID, AmountPaid, PaymentDate, PaymentMethod, rental_RentalID, rental_customer_CustID, rental_employee_EmployeeID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (PaymentID, AmountPaid, PaymentDate, PaymentMethod, rental_RentalID, rental_customer_CustID, rental_employee_EmployeeID)

        try:
            # Execute the query
            cursor.execute(query, values)
            connection.commit()
            print("Payment record added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def update_maintenance_status():
        vehicle_VehicleID = input("Enter Vehicle ID: ")
        new_status = input("Enter New Maintenance Status: ")

        query = """
        UPDATE maintenancelog
        SET MaintStatus = %s
        WHERE vehicle_VehicleID = %s
        """
        values = (new_status, vehicle_VehicleID)

        try:
            cursor.execute(query, values)
            connection.commit()
            print("Maintenance status updated!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    while True:
        print("\n1. Add Customer")
        print("2. Add Vehicle")
        print("3. Add Maintenance Log")
        print("4. Add Payment")
        print("5. Update Maintenance Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            add_vehicle()
        elif choice == '3':
            add_maintenance_log()
        elif choice == '4':
            add_payment()
        elif choice == '5':
            update_maintenance_status()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
