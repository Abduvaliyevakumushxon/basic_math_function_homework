def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    from math import floor
    x=a%b
    return x
print(main(23,5))