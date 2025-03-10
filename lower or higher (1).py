import random

def get_bound():
    while True:
        try:
            lower_bound = int(input("enter the lower bound: "))
            upper_bound = int(input("enter the upper bound: "))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print("error: lower bound must be less than upper bound. please try again.")
        except ValueError:
            print("error: please enter valid integers.")

def main():
    while True:
        lower_bound, upper_bound = get_bound()
        random_number = random.randint(lower_bound, upper_bound)
        print(f"generated random number: {random_number}")
        
        while True:
            choice = input("do you want to generate another number? (yes/no): ").strip().lower()
            if choice in ['yes', 'no']:
                break
            else:
                print("error: please enter 'yes' or 'no'.")
        
        if choice == 'no':
            print("exiting the program.")
            break

if __name__ == "__main__":
    main()