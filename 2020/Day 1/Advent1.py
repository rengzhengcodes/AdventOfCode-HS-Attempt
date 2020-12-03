expense_list = []

with open("expenses.txt") as expenses:
    for expense in expenses:
        expense_list.append(int(expense.rstrip("\n")))

##for expense in expense_list:
##    for expense1 in expense_list:
##        if expense1 + expense == 2020:
##            print(expense1 * expense)

for expense in expense_list:
    for expense1 in expense_list:
        for expense2 in expense_list:
            if expense + expense1 + expense2 == 2020:
                print(expense * expense1 * expense2)
