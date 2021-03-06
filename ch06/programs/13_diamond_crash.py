# Input and input validation
while True:
    n_str = input("Enter n: ")
    if not n_str.isdigit():
        print("Data validation failed!")
        print("n should be a positive integer")
        continue
    n = int(n_str)
    if n < 1 or n > 19 or n % 2 == 0:
        print("Data validation failed!")
        print("n should be odd and between 1 and 19 inclusive")
        continue
    break

# Process and output
stars = []
index = 1
while index < n:
    stars += [" " * ((n - index) // 2) + "*" * index]
    index += 2

for index in range(n // 2):
    print(stars[index])
for index in range(n // 2 + 1):
    print(stars[-index - 1])
