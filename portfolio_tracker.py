# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 150,
    "MSFT": 320
}

total_value = 0

# Number of stocks
n = int(input("Enter the number of different stocks: "))

# Get stock details
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_value += investment
        print(f"Value of {stock_name}: ${investment}")
    else:
        print("Stock not available!")

print("\n-----------------------------")
print("Total Investment Value: $", total_value)

# Save to a file
choice = input("\nDo you want to save the portfolio? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("------------------------\n")
        file.write(f"Total Investment Value: ${total_value}")

    print("Portfolio saved successfully in portfolio.txt")
else:
    print("Portfolio not saved.")