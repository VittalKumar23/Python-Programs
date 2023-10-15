def checkPrime(number):
    '''This function checks for a prime number'''
    isPrime = True  # Assume the number is prime by default

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

    if isPrime:
        print(number, 'is a Prime Number')
    else:
        print(number, 'is not a Prime Number')

if __name__ == '__main__':
    userInput = int(input('Enter a number to check: '))
    checkPrime(userInput)
