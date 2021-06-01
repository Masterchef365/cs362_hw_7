def fizzbuzz(num):
    fizz = num % 3 == 0
    buzz = num % 5 == 0
    if fizz and not buzz:
        return "Fizz"
    if buzz and not fizz:
        return "Buzz"
    if fizz and buzz:
        return "FizzBuzz"
    else:
        return str(num)

if __name__ == "__main__":
    [print(fizzbuzz(num)) for num in range(1, 100)]
