import datetime

def add_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Write your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(f"{date}\n{entry}\n\n")
    print("Entry added.")

def read_entries():
    try:
        with open("diary.txt", "r") as file:
            entries = file.read()
            print(entries)
    except FileNotFoundError:
        print("No entries found.")

def delete_entries():
    open("diary.txt", "w").close()
    print("All entries deleted.")

while True:
    print("\n1. Add Entry\n2. Read Entries\n3. Delete Entries\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_entry()
    elif choice == '2':
        read_entries()
    elif choice == '3':
        delete_entries()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
