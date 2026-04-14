def print_table(n):
    print("TABLE OF", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter number: "))
print_table(num)
