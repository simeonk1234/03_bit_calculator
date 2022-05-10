# checks input is a number more than a given value
def num_check(question, low):
    
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero "
        "(or equal to) {}".format(low)
        print()

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# converts decimal to binary and states how
# many beets are needed
def int_bits():

    # get integer (must be >=0)
    var_integer = num_check("Please enter an integer: ", 0)

    # source for code below is
    # https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of stirng above)

    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# Main routine 

int_bits()