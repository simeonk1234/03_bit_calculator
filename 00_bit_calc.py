# functions go here

# Puts series of symbols at the start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer")
    print()
    print("This program assumes that images are being respresented in 24 bit colour (ie: 24 bits per pixel). For text we asume that ascii encoding is being used (8 bits per character) ")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    return ""

# checks user's choice is an integer, text or an image
def user_choice():
    
    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"] 
    image_ok = ["image", "img", "I", "pix", "picture", "pic", "p"]
   
    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in text_ok:
            return "text"
            
        elif response in integer_ok:
            return "integer"
            
        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "Integer"
            else:
                return "image"
            
        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()

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

# calculates the # of bits for text (# of character x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculates the # of bits (length of sting x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...". format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# finds # of bits for 24 bit colour
def image_bits():

    image_height = num_check("Enter Image Height: ", 1)
    print()
    image_width = num_check("Enter Image Width: ", 1)
    
    num_pixels = image_width * image_height
    num_bits = num_pixels * 24

    print()
    print("The # of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("The # of bits = {} x 24 = {}".format(num_pixels, num_bits))

    return ""

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


# Heading
statement_generator("look - stars", "*")

# Display instructions if user has not used program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()
    
# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For interges, ask for integer
    if data_type =="integer":
        int_bits()
    # For images, ask for width and height
    # (must be and inetger more than or equal to 0)
    elif data_type =="image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()