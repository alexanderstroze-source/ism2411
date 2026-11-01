```python
# Self Assesment Questions

# 1. The most surprising thing to me is that negative indices let you access
# items starting from the end of a list. I thought that I would have to count always
# positions from the beginning to find the last item.

# 2. A list will help me to organize and compare the sales that are made on a daily basis in a business class.
#I could use #Rather than manually sorting and calculating values in the spreadsheet,
#Use Python to write a program to calculate averages and filter days by sales goal.
# --------Excercise 1--------
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --------Excercise 2--------
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# --------Excercise 3--------
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# --------Excercise 4--------
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# --------Excercise 5--------
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples cannot be changed after creation.")
    print("Tuples are useful for coordinates because they prevent accidental changes.")

print(coords)

# --------Excercise 6--------
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# --------Excercise 7--------
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)

# --------Excercise 8--------
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
```
