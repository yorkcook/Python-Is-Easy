for num in range(1, 101, 1):
    # print(num)
    
    if num % 3 == 0 and num % 5 ==0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0 and num % 5 ==0:
        print('FizzBuzz')
    elif  num % 2 != 0:
        print('Prime Number')
    else:
        print(num)