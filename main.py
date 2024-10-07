shopping_list = []

print("Welcome to Shopping List Organizer")
def show_menu():
    print("\nYour Current Shopping List:")
    for item in shopping_list:
        print(f"- {item}")
    print("\n\nWhat would you like to do?")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Sort List")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    while choice == "1":
        item = input("Enter item to add: ").capitalize()
        if item == "Q":
            break
        shopping_list.append(item)
        print(f"{item} added to the shopping list.\n")

    while choice == "2":
        print("Enter 'Q' to exit")
        # Check if the shopping list is empty
        if shopping_list:
            # Display all items with numbers
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")
            
            # Ask for the item number to remove
            inp = input("Enter the number of the item to remove: ")
            if inp == "Q":
                break
            elif inp.isdigit():
                index = int(inp) - 1

                # Check if the input is within the valid range
                if index < len(shopping_list):
                    removed_item = shopping_list.pop(index)
                    print(f"{removed_item} removed from the shopping list.")
            else:
                print("Invalid selection.")
        else:
            print("The list is empty.")

    if choice == "3":
        shopping_list.sort()
        print("The shopping list has been sorted alphabetically.")

    elif choice == "4":
        print("Thank you for using the Shopping List Organizer. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
