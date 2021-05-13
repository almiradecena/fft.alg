import math
import cmath

## 
# returns True if x is even, False otherwise
def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

##
# Gets sample coordinates from coeffecient representation
# param A list containing coefficient representation
# returns list of sample coordinates
def fast_fourier_transform(A):
    n = len(A)                                      # length of coefficient list

    # base case
    if n == 1:
        return A
        
    w = cmath.exp((2*math.pi*complex(0,1))/n)       # calculate the roots of unity
    A_e = []                                        # even coefficients
    A_o = []                                        # odd coefficients

    # split coefficients into even and odd
    for i in range(0,n):
        if is_even(i):
            A_e.append(A[i])
        else:
            A_o.append(A[i])
    
    # get sample coordinates for even and odd coefficients
    y_e = fast_fourier_transform(A_e)
    y_o = fast_fourier_transform(A_o)

    # deducing last half of coefficients
    y = [0] * n
    for j in range(0, int(n/2)):
        y[j] = y_e[j] + pow(w, j)*y_o[j]
        y[j + int(n/2)] = y_e[j] - pow(w, j)*y_o[j]

    return y

print('Input coefficients as integers split by commas:')
user_input = input()
user_input = user_input.split(',')

coeffs = []
for x in user_input:
    coeffs.append(int(x))

print('Calculating fast fourier transform for: ', coeffs)
result = fast_fourier_transform(coeffs) #Samples #Input Coeff Representation
print(result) 
