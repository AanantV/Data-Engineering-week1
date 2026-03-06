import json
from datetime import datetime 

def app_manager():

    fn = "Week 2/Day 2/settings.json"
    modified = "Week 2/Day 2/modified.json"

    def load():
        try:
            with open(fn, 'w') as file:
                settings = {
                        "app": {
                                    "version": "1.0",
                                    "auto_update": True
                                },
                        "user": {
                                    "name": "Alex",
                                    "notifications": True
                                },
                        "theme": {
                                    "mode": "dark",
                                    "color": "blue"
                                }
                    }
                json.dump(settings, file, indent =4)
        
        except Exception as e:
            print(f"JSON error : {e}")

    def update_settings(data,path,value):
        current = data
        keys = path.split('.')

        for key in keys[:-1]:
            current = current.setdefault(key,{})
        current[keys[-1]] = value
            
        with open(fn, "w") as file:
            json.dump(data,file, indent =4)

        with open(fn, "r") as file:
            json.load(file)
        
                    
    def reset_defaults():
        load()

    def time_export():

        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(now)

        with open(fn,"r") as file:
            reader = json.load(file)

        report = f"""DATA EXPORT FOR SETTINGS

Document generated on: {timestamp}

SETTINGS.JSON

USER NAME: {reader['user']['name']}
USER NOTIFICTAIONS: {reader['user']['notifications']} 
APP VERSION: {reader['app']['version']}
AUTO-UPDATE? {reader['app']['auto_update']}
THEME: {reader['theme']['mode']}
COLOR: {reader['theme']['color']}"""
        
        with open("Week 2/Day 2/report.txt", "w") as file:
            writer = file.write(report)

    while True:
        print("\n--- App Manager ---")
        print("1. Load")
        print("2. Update")
        print("3. Reset Defaults")
        print("4. Export")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            load()
        elif choice == "2":
            with open(fn, "r") as file:
                data = json.load(file)
            path = input("Enter the settings you want to update with dot notation: ")
            value = input("Enter the data to be modified")
            update_settings(data,path,value)
        elif choice == "3":
            reset_defaults()
        elif choice == "4":
            time_export()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
    

    
app_manager()