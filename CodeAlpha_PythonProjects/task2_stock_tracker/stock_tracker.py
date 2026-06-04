stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 320
}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:")
for stock, price in stock_prices.items():
    print(stock, "->", price, "USD")

portfolio = {}

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ")
    stock = stock.upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Sorry! That stock is not available. Choose from the list above.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity
    print(stock, "added to your portfolio!")

print("\n--- Your Portfolio Summary ---")
total = 0

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total += investment
    print(stock, "x", quantity, "=", investment, "USD")

print("Total Investment:", total, "USD")

save = input("\nDo you want to save your portfolio? (yes/no): ")

if save.lower() == "yes":
    file = open("portfolio.txt", "w")
    file.write("--- Your Portfolio Summary ---\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(stock + " x " + str(quantity) + " = " + str(investment) + " USD\n")
    file.write("Total Investment: " + str(total) + " USD\n")
    file.close()
    print("Portfolio saved to portfolio.txt!")