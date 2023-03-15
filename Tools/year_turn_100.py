def main():
    # Ask the user for their name and age
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    # Calculate the year the user will turn 100
    current_year = 2022
    years_to_100 = 100 - age
    year_turn_100 = current_year + years_to_100

    # Print the result
    print(f"Hi {name}! You will turn 100 years old in the year {year_turn_100}.")

if __name__ == "__main__":
    main()