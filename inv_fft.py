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
# Gets coefficients from sample coordinates representation
# param A list containing sample coordinates 
# returns list of coefficients
def inv_fast_fourier_transform(A):
    N = len(A)                                  # length of coefficients list

    # base case
    if N == 1:
        return A
        
    w = cmath.exp((-2*math.pi*complex(0,1))/N)  # calculate the roots of unity
    A_e = []                                    # even coefficients
    A_o = []                                    # even coefficients

    # split coordinates into even and odd
    for i in range(0,N):
        if is_even(i):
            A_e.append(A[i])
        else:
            A_o.append(A[i])

    # get coefficients for even and odd coordinates
    y_e = inv_fast_fourier_transform(A_e)
    y_o = inv_fast_fourier_transform(A_o)

    # deducing last half of coordinates
    y = [0] * N
    for j in range(0,int(N/2)):
        y[j] = y_e[j] + pow(w,j)*y_o[j]
        y[j + int(N/2)] = y_e[j] - pow(w,j)*y_o[j]

    return y

# Get user input
print('Input coordinates as complex numbers split by commas:')
user_input = input()
user_input = user_input.split(',')

coeffs = []
for x in user_input:
    coeffs.append(complex(x))


print('Calculating fast fourier transform for: ', coeffs)
result = inv_fast_fourier_transform(coeffs) #Samples #Input Coeff Representation


# get real part of complex number and divide that by length
final = []
for x in result:
    final.append((x.real)/len(result))
print(final) 
