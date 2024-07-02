import json
import time
import os

def main():
    def clear_console():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')

    with open("data.json", "r") as f:
        data = json.load(f)
    clear_console()
    print("                                 Welcome to fitty!")
    time.sleep(2)
    clear_console()
    if data['save'] == "false":

        # Get user input
        name = input("Enter your name: ")
        w = int(input("Enter your weight in KG: "))
        h = int(input("Enter your height in CM: "))
        a = int(input("Enter your age: "))
        sex = input("Enter your sex ")
        
        while sex.lower() not in ["male", "female"]:
            print("Invalid input. Please enter your biological sex.")
            sex = input("Enter your sex: ")
        
        # Update the data dictionary with user input
        data["name"] = name
        data["weight"] = w
        data["height"] = h
        data["age"] = a
        data["sex"] = sex.lower()
        data["save"] = "true"
        if data["sex"] == "male":
            data["BMR"] = 10 * data['weight'] + 6.25 * data['height'] - 5 * data['age'] + 5
            data["calories"] = data["BMR"] * 1.2
    
        if data["sex"] == "female":
            data["BMR"] = 10 * data['weight'] + 6.25 * data['height'] - 5 * data['age'] - 161
            data["calories"] = data["BMR"] * 1.2


        # Write the updated data back to data.json
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    while True:

        print(f"""
              your current stats are: weight: {data['weight']}kg, height: {data['height']}cm, age: {data['age']}, BMR = {data['BMR']}, calories left for the day: {data['calories']}
              """)
        
        action = input("""What would you like to do?
                        1. update 
                        2. add meal
                        3. quit
                        4. reset
                        """)
        while action not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a valid option.")
            action = input("""What would you like to do?
                            1. update 
                            2. add meal
                            3. quit
                            4. reset
                            """)

        if action == "1":
            data['weight'] = int(input("Enter your weight in KG: "))
            data['height'] = int(input("Enter your height in CM: "))
            data['age'] = int(input("Enter your age: "))
            sex = input("Enter your sex: ")
            data["sex"] = sex.lower()
        
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        
        if action == "2":
            meal = int(input("Enter the calories of the meal: "))
            data['calories'] -= meal
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        
        if action == "3":
            break

        if action == "4":
            sure = input("Are you sure you want to reset? y/n ")
            if sure.lower() == "n":
                continue
            if sure.lower() == "y":
                data["weight"] = 0
                data["height"] = 0
                data["age"] = 0
                data["BMR"] = 0
                data["calories"] = 0
                data["sex"] = 0
                data["name"] = 0
                data["save"] = "false"
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                break

if __name__ == "__main__":
    main()