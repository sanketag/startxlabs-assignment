'''
Write a function which takes two arguments: a list of customers and the number of open cash registers. Each customer is represented by an i
nteger which indicates the amount of time needed to checkout. Assuming that customers are served in their original order, your function should 
output the minimum time required to serve all customers.

Examples:

get_checkout_time([5, 1, 3], 1) should return 9

get_checkout_time([10, 3, 4, 2], 2) should return 10 because while the first register is busy serving customer[0] the second register can serve 
all remaining customers.

'''




def get_checkout_time(li, num):
    x = num

    def fun(uplist, flag):
        nonlocal x

        if flag==0:
            return max(uplist)
        else:
            temp1 = min(uplist)
            zero = uplist.count(temp1)
            dlist = [i-temp1 for i in uplist if i-temp1 != 0]
            if len(li)>x+zero:
                dlist+=li[x:x+zero]
                x+=zero
                # print(temp1,".")
                return temp1+fun(dlist,1)
            else:
                dlist+=li[x:]
                # print(temp1)
                return temp1+fun(dlist,0)

    if len(li)>num:
        return fun(li[:num],1)
    elif num==0:
        return 0
    else:
        return fun(li[:],0)

print(get_checkout_time([5, 1, 3], 1))
print(get_checkout_time([10, 3, 4, 2], 2))
print(get_checkout_time([12,3,4,57,72,135,435],3))

12,3,3
9,




def fun(st):
    count = 0 
    for i in st:
        if i=='[':
            count+=1
        else:
            count-=1
            if count<0:return 'NOT OK'
    if count==0:
        return 'OK'
    else:
        return 'NOT OK'

print(fun('[[][]]]['))




def fun(li):
    temp = []
    c = 0
    mul = 1
    uplist = [i for i in li if i != 0]
    for i in uplist:
        if i<0:
            c+=1
            temp.append(i)
    if c%2!=0:
        uplist.remove(max(temp))
    for i in uplist:
        mul*=i
    return mul
    
print(fun([23, 25, 343, -3, -43, 23, -434, 0]))























