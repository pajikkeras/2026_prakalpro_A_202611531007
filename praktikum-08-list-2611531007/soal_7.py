menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(number_of_days):
    daily_sales = []
    for menu in menus:
        portion = int(input(f"Day {day + 1}, {menu}:"))
        daily_sales.append(portion)
    sales.append(daily_sales)
print("Total per day:")

for row in range(len(sales)):
    day_total = 0
    for col in range(len(sales[row])):
        day_total += sales[row][col]
    print(f"Day {row + 1}: {day_total}")

menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for row in range(len(sales)):
        menu_total += sales[row][col]
    menu_totals.append((menus[col], menu_total))

print("Total per menu:", menu_totals) 

best_name, best_total = menu_totals[0]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name
print(f"Best seller: {best_name} ({best_total})")
