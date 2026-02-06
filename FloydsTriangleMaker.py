rows=int(input("Enter number of rows (do a small number): "))
number=1
print("Floyd's Triangle:")
for i in range(1, rows + 1):
    for h in range (1, i + 1):
        print(number, end=' ')
        number=number + 1
    print()