# functions
#checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid: 

        error = ('Please enter a number that is more than zero')

        try:

            # asks user to enter a number
            response = float(input('Enter a number: '))

            # checks if numer is more than zero
            if response > 0:
                return response

            # outputs error if numer is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()