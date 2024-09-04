n = int(input("Enter the number of terms: "))

t1, t2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:", t1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(t1)
        next = t1 + t2
        t1 = t2
        t2 = next
        count += 1
