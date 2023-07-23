# first try
originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []

for element in originalList:
    if element % 2 == 0:
        newList.append(element)
    else:
        continue
#     The else: continue part of your code is not needed because if the condition in the if statement is not met,
#     the loop will automatically continue to the next iteration.

print(newList)

# list comprehension
originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = [element for element in originalList if element % 2 == 0]
print(newList)

