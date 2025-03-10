def display_menu():
    print("\n List Options:")
    print("1. add an item")
    print("2. view list")
    print("3. remove item")
    print("4. clear the shopping list")
    print("5. exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("choose an option 1-5: ")
        
        if choice == '1':
            item = input("enter the item to add: ")
            shopping_list.append(item)
            print(f"added: {item}")
        
        elif choice == '2':
            print("\n shopping List:")
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
        
        elif choice == '3':
            item = input("enter the name of the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"removed: {item}")
            else:
                print(f"item '{item}' not found.")
        
        elif choice == '4':
            shopping_list.clear()
            print("shopping list cleared")
        
        elif choice == '5':
            print("exiting the program")
            break
        
        else:
            print("your choice is invalid choice. select a valid option.")

if __name__ == "__main__":
    main()