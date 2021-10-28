import numpy as np 
def getarray(x,y):
    num1 = [str(a) for a in str(x)]
    num2 = [str(a) for a in str(y)]
    m = len(num1)
    n = len(num2)
    num1 = np.array(num1)
    num2 = np.array(num2)
    return(num1,num2)
    

value1 = 3141592653589793238462643383279502884197169399375105820974944592
value2 = 2718281828459045235360287471352662497757247093699959574966967627

# This is the implementation of Karatsuba Multiplication rule for very large values
# This is the part of exercise for the course https://www.coursera.org/learn/algorithms-divide-conquer/home/welcome

def multi(num1,num2):
    x = str(num1)
    y = str(num2)
    len1 = len(x)
    len2 = len(y)
    if(len1 > len2):
        y = (len1-len2)*'0' + y
    if(len2 > len1):
        x = (len2-len1)*'0' + x
    print(num1,num2)

    if(len1 ==1):
        return int(num1)*int(num2)
    len1=len(x)
    len2=len(y)
        


    numAarray = x[0:int((len1 +1)/2)]
    numBarray = x[int((len1 +1)/2):]
    numCarray = y[0:int((len2 +1)/2)]
    numDarray = y[int((len2 +1)/2):]


    ac = multi(numAarray,numCarray)
    bd = multi(numBarray,numDarray)
    a_b = int(numAarray) + int(numBarray)
    c_d = int(numCarray) + int(numDarray)
    adbc = int(multi(a_b,c_d) - ac -bd)
    print(ac,bd,adbc)

    if(len1%2 ==0):
        ans = int((10**len1)*ac + (10**int(len1/2))*adbc + bd)
    else:
        ans = int(((10**(len1-1))*ac + (10**int((len1-1)/2))*adbc +bd))

    
    print(ans)
    return ans

    

value = multi(value1,value2)
print(value)
