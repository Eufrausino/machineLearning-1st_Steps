List = [value + 10 for value in range(5)]
print(List)

ListII = [value for value in range(1,30) if value % 4 == 0]
print(ListII)

ListIII = ['A' if grade >= 8 else 'B' for grade in range(1,11)]
print(ListIII)