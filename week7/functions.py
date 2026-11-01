#--------Self-Assessment--------
#1.The first bug that was identified in broken_sales.py was 
#missing colon after "for sale in sales". I used ChatGPT to
#find the bug. A SyntaxError is caused every time the code
#tries to run. I need more practice checking syntax and tracing
#loops on my own.

# 2. apply_discount(price, tier) takes an original price and a membership
# tier. It returns the price after the discount. Gold gets 15% off,
# silver gets 10% off, bronze gets 5% off, and other tiers get no discount.
# Someone could use it without reading its code if they knew the proper inputs
# and what it returns.

#A3.I Disclosure: I used ChatGPT to help identify bugs and help with incorrect formatting.

#--------Exercise 1--------
def calculate_tax(price, rate):
    """Return the tax amount for a price and tax rate."""
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

#--------Exercise 2--------
def apply_discount(price, tier):
    """Return the discounted price for gold, silver, bronze, or other tiers."""
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

#--------Exercise 3--------
discounted_price = apply_discount(200, "gold")
price_with_tax = discounted_price + calculate_tax(discounted_price, 0.07)
print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${price_with_tax:.2f}")


def final_price(price, tier, tax_rate):
    """Apply the discount, then add tax to the discounted price."""
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

#--------Exercise 4--------
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#--------Exercise 5--------
# Fixed version of broken_sales.py.
# Bug 1: total = sale replaces the total with each sale instead of adding.
# Fix: Use += to keep a running total of all five sales.
# Bug 2: The second for loop is missing a colon, causing a SyntaxError.
# Fix: Add a colon at the end of the loop header.
# Bug 3: i <= len(sales) allows i to reach 5, but the last valid index is 4.
# Fix: Use < so the loop stops before trying to read sales[5].
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#--------Exercise 6--------
# Expected output: 100, 1998, 100, each on its own line.
# The x outside the function is global and stays 100. Inside double_it,
# x is a separate local variable set to 999. The function returns 999 * 2,
# which is 1998. It does not change the global x.
x = 100


def double_it():
    x = 999
    return x * 2


print(x)
print(double_it())
print(x)
