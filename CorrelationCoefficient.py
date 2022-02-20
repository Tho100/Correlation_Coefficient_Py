import math
import pandas as pd 

X = [1,2,3,4,5,6]
Y = [2,4,7,9,12,14]

# Sum(X)
sum_x = 0
for j in range(len(X)):
    X_elements = X[j]
    print(X_elements)
    sum_x = sum_x + (X[j])
print('Sum(X): ',sum_x)

print('\n')

# Sum(Y)
sum_y = 0
for q in range(len(Y)):
    Y_element = Y[q]
    sum_y = sum_y + Y_element
    print(Y_element)
print('Sum(Y):',sum_y)

print('\n')

# X * Y
sum = 0
for n in range(len(X)):
    XY = (X[n] * Y[n])
    sum = sum + (X[n] * Y[n])
    print(XY)

print('Sum(XY):',sum)

print('\n')

# X^2 (X**2)
sum_x_squared = 0
for i in range(len(X)):
    X_square = X[i]**2
    sum_x_squared = sum_x_squared + (X[i]**2)
    print(X_square)
print('Sum(X^2):',sum_x_squared)

print('\n')

# Y^2 (Y**2)
sum_y_squared = 0
for k in range(len(Y)):
    Y_square = Y[k]**2
    sum_y_squared = sum_y_squared + (Y[k]**2)
    print(Y_square)
print('Sum(Y^2):',sum_y_squared)

print('\n')

# Find the correlation coefficient
r0 = ((len(X))*(sum)-(sum_x)*(sum_y))
r_sqrt_x = (math.sqrt((len(X))*(sum_x_squared)-((sum_x)**2)))
r_sqrt_y = (math.sqrt(len(Y)*(sum_y_squared)-((sum_y)**2)))
multiply_sqrt_y_sqrt_x = r_sqrt_x*r_sqrt_y
r = r0/(multiply_sqrt_y_sqrt_x)
print(r)

dataframe = pd.DataFrame({
'Sum(X)': [sum_x],
'Sum(Y)': [sum_y],
'Sum(X^2)': [X_square],
'Sum(Y^2)': [Y_square],
'Sum(X*Y)': [sum],
'Correlation Coefficient: ': [r],})
dataframe
