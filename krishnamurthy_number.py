#factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
#check_no_func.
def is_krishnamurthy(num):
    original_num = num
    sum_of_factorials = 0
    
    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10

    return sum_of_factorials == original_num

num = int(input("Enter a number: "))
if is_krishnamurthy(num):
    print(f"{num} is a Krishnamurthy number.")
else:
    print(f"{num} is not a Krishnamurthy number.")
