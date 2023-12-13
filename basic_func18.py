def main(a):
    '''Assign the value pi to the parametr "a". Round the result to 2 decimal places and return it.
    
    Args:
        a (float): a number
        
    Returns:
        float: the result.
    '''
    import math
    a=math.pi
    x1=round(a,2)
    return x1
print(main("a"))