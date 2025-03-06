import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    @staticmethod
    def add_employee():
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        
        print("Employee added successfully!")
    
    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        print("Employee Records:")
        for record in records:
            print(record.strip())
    
    @staticmethod
    def search_employee():
        employee_id = input("Enter Employee ID to search: ")
        found = False
        
        if os.path.exists(EmployeeManager.FILE_NAME):
            with open(EmployeeManager.FILE_NAME, "r") as file:
                records = file.readlines()
                
            for record in records:
                if record.startswith(employee_id + ","):
                    print("Employee Found:")
                    print(record.strip())
                    found = True
                    break
        
        if not found:
            print("Employee not found.")
    
    @staticmethod
    def update_employee():
        employee_id = input("Enter Employee ID to update: ")
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        updated_records = []
        found = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        for record in records:
            if record.startswith(employee_id + ","):
                print("Current record:", record.strip())
                name = input("Enter new name (leave blank to keep current): ") or record.split(',')[1]
                position = input("Enter new position (leave blank to keep current): ") or record.split(',')[2]
                salary = input("Enter new salary (leave blank to keep current): ") or record.split(',')[3].strip()
                updated_records.append(f"{employee_id},{name},{position},{salary}\n")
                found = True
            else:
                updated_records.append(record)
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully!")
        else:
            print("Employee not found.")
    
    @staticmethod
    def delete_employee():
        employee_id = input("Enter Employee ID to delete: ")
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        
        updated_records = []
        found = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        
        for record in records:
            if record.startswith(employee_id + ","):
                print("Employee record deleted:", record.strip())
                found = True
            else:
                updated_records.append(record)
        
        if found:
            with open(EmployeeManager.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")
    
    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                EmployeeManager.add_employee()
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                EmployeeManager.search_employee()
            elif choice == "4":
                EmployeeManager.update_employee()
            elif choice == "5":
                EmployeeManager.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    EmployeeManager.menu()
