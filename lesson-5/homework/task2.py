def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

# Get user input
initial_amount = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
years = int(input("Enter the number of years: "))

# Call the function
invest(initial_amount, annual_rate, years)
