def main():
    # Ask the user for their name and age
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    year = int(input("Enter the age you want to figure out the year for: "))

    # Calculate the year the user will turn 100
    current_year = 2022
    years_to_year = year - age
    year_turn_year = current_year + years_to_year

    # Print the result
    print(f"Hi {name}! You will turn {year} years old in the year {year_turn_year}.")

if __name__ == "__main__":
    main()