import math as m

def function(x): 
    # return 5*x**2 - 3*x - 2
    return x**3 - 2*x - 5

def bisection(a, b, error):
    if function(a) * function(b) > 0:
        return "No zero found"
    else:
        while (b - a) / 2.0 > error:
            midpoint = (a + b) / 2.0
            if function(midpoint) == 0:
                return midpoint
            elif function(a) * function(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint
    
    
print(bisection(0, 10, 0.0000001))