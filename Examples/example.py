import commonpasswords
# Importing the commonpasswords mldule
def question():
    # Defining the Function
    print(commonpasswords.detect(input("Password\n"), True))
    #                             ^^^^^^^^^^^^^^^^^^  ^^^^
    #           Requests the user for an password     Enables the module to return the reasons
    question()
    # Calls the function again until ^+c is pressed
question()
# Runs the function for the first time
