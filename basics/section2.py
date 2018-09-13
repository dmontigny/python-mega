def c2f(c = 0):
    """ Section 2-31: Create a function that converts Celsius degrees to Fahrenheit. The formula to convert Celsius to
    Fahrenheit is F = C × 9/5 + 32."""
    print(c * 9/5 + 32.)

# c2f(100)

def string_length(mystring):
    """ Section 2-33:35: Your duty is to modify the function so that if an integer is passed as an input, the function
    should output a message like "Sorry integers don't have length"."""
    if type(mystring) == int or type(mystring) == float:
        print("Sorry {}s don't have length".format(type(mystring)))
        exit()
    else:
        return len(mystring)

print(string_length('16354165sf1536165g2s13g1'))
