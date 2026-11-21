categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# finds the highest expense
max_expense = max(expenses)

# finds the index of the highest expense
max_index = expenses.index(max_expense)

# prints the most expensive category
print("Most expensive category:", categories[max_index])
print("Expense:", max_expense)