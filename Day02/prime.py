def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

print("Prime numbers are:")
for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=" ")