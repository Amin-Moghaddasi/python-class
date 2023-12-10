class functions:
    def even_number(number):
        if number % 2 == 0:
            print('{number} is even'.format(number=number))
            return 0
        else:
            print('{number} is odd'.format(number=number))
            return 0
    def power_two(number):
        return number * number
