"""Time required by all the customers to checkout."""

def get_checkout_time(cust,c_r):
    rem = c_r-1
    
    """Recursive function to process next customers."""
    def fun(e,f):
        nonlocal rem
        
        """Checking if suitable amount of cash registers are available"""
        if f==0:
            return max(e)
        else:
            temp = min(e)
            zero = e.count(temp)
            
            """Reducing time spent by the customer with minimum time requirement from every cash register"""
            temp1 = [i-temp for i in e if (i-temp)!=0]
            rem+=1

            """Adding next customers in the line"""
            if rem<len(cust)-zero:
                return temp+fun(temp1+cust[rem:rem+zero],1)
            else:
                return temp+fun(temp1+cust[rem:],0)
    
    """Checking if suitable amount of cash registers are available"""
    
    """Assigning a customer to every cash register along with the flag of remaining customers"""
    if c_r>=len(cust):
        return fun(cust,0)
    else:
        return fun(cust[:c_r],1)

print(get_checkout_time([5, 1, 3], 1))
print(get_checkout_time([10, 3, 4, 2], 2))