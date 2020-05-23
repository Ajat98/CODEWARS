
#S1
def narcissistic( value ):
    digits = len(str(value))
    total = 0
    #if not value: return False
    for i in str(value):
        total += int(i) ** digits
    if total == value:
        return True
    else:
        return False
        
#S2 List comp
def narcissistic( value ):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
