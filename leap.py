
def is_leap(a):
    if(int(a / 4) * 4 == a):
        if(int(a / 100) * 100 == a):
            return False;
        else:
            return True;
    else:
        return False;
