###
# Functions to read any data type from the keyboard
#
def input_string(message):
    st = input(message)
    return st

def input_integer(message):
    inte = input(message)
    return int(inte)

def input_real(message):
    data = input(message)
    return float(data)

def input_boolean(message):
    boo = input(message)
    return boo.lower() == 'n'