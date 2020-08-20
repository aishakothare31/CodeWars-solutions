def validate_pin(pin):
    #return true or false
    return True if pin.isnumeric() and (len(pin)==4 or len(pin)==6) else False