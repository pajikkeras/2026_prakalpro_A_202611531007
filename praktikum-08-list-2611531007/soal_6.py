LAST_DIGIT = 7  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for day in range (1,8):
    data = int(input(f'Day {day} : '))
    expenses.append(data) 
total = 0
highest = 1
highest_expense = expenses[0]
days_above_limit = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest_expense:
        highest_expense = expenses[i]
        highest = i + 1
    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

print(f"Daily Limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest} ({highest_expense})")
print(f"Days above limit: {days_above_limit}")