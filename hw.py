def is_power_of_8(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n //= 8
    return n == 1

num = int(input("Enter your number: "))

if is_power_of_8(num):
    print("Yes")
else:
    print("No")
