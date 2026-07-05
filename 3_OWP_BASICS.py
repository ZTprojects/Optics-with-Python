"""(8)_<<<<<<<<<<<<<<<<<_IMPORTING MODULES ctd.:NUMPY_>>>>>>>>>>>>>>>>>>_(8)"""
import numpy as np

#np.zeros(shape, dtype=float, order='C'): creates an ndarray with zeroes.
#shape: int or tuple made out of ints. Size of the new object.
#dtype: data type of the zeroes, floats and integers, for example.
print(np.zeros(5))              #[0. 0. 0. 0. 0.]
print(np.zeros(5, dtype=int))   #[0 0 0 0 0]
print(np.zeros((3,5)))          #this will be a 3x5 type matrix:
                                #[[0. 0. 0. 0. 0.]          
                                # [0. 0. 0. 0. 0.]
                                # [0. 0. 0. 0. 0.]] 
#np.ones is a similar function.


a = np.linspace(0, 10, 11)
print(a)            #[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
print(2*a)          #[ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18. 20.]
print(a**2)         #[  0.   1.   4.   9.  16.  25.  36.  49.  64.  81. 100.]
print((a+5)*2)      #[10. 12. 14. 16. 18. 20. 22. 24. 26. 28. 30.]
print(np.sin(a))    #'a' is used as if its elements were radians:
#[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
#-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]


#Operations with ndarray: if a mathematical function is undefined or infinite
#at a certain point, python will still calculate the other values.
a = np.linspace(-4,4,9)
print(a)                #[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
print(np.log(a))        #nan: not a number, inf: infinite
#[       nan        nan        nan        nan       -inf 0.
#0.69314718 1.09861229 1.38629436]


#Operations between ndarrays.
a = [0,1,2]
b = [3,4,5]
#print(b-a) TypeError: unsupported operand type(s) for -: 'list' and 'list'
a = np.array(a)
b = np.array(b)
print(b-a)      #[3 3 3]


#The elements of an ndarray are accessed similarly to that of a list or string:
print(a[1])     #1
print(a[1:3])   #[1 2]


#Addition of elements:
data = np.arange(5)
sum = 0
for i in data:
    sum = sum + i
print(sum)          #10


#Writing data onto a file: 
#numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n',
#header='', footer='', comments='# ', encoding=None)
#fname: filename, X: object to be written, fmt: format (eg.: string)
#delimiter: character dividing the data columns, newline: string that separates
#data lines, header: string on top of the file, footer: string at the bottom of
#the file

#numpy.stack(arrays, axis=0, out=None)
#Concatenates objects in the direction of a given axis.
#arrays: the objects to concatenate. axis=0 --> horizontal, =1 --> vertical

t = np.linspace(-10,10,21)
om0 = 3.0
b = 0.2
phi = om0 * t + b*t**2
print(t)
#[-10.  -9.  -8.  -7.  -6.  -5.  -4.  -3.  -2.  -1.   0.   1.   2.   3.
#   4.   5.   6.   7.   8.   9.  10.]
print(phi)
#[-10.  -10.8 -11.2 -11.2 -10.8 -10.   -8.8  -7.2  -5.2  -2.8   0.    3.2
#  6.8  10.8  15.2  20.   25.2  30.8  36.8  43.2  50. ]
c = np.stack(   (t, phi), axis = 1   )
print(c)
""" [[-10.  -10. ]
     [ -9.  -10.8]
     [ -8.  -11.2]
     [ -7.  -11.2]
     [ -6.  -10.8]
     [ -5.  -10. ]
     [ -4.   -8.8]
     [ -3.   -7.2]
     [ -2.   -5.2]
     [ -1.   -2.8]
     [  0.    0. ]
     [  1.    3.2]
     [  2.    6.8]
     [  3.   10.8]
     [  4.   15.2]
     [  5.   20. ]
     [  6.   25.2]
     [  7.   30.8]
     [  8.   36.8]
     [  9.   43.2]
     [ 10.   50. ]]"""
info = 'Time'
info += '\nDate: 2023.06.21'
info += '\n\n Time (fs),\t Phase (rad)'

np.savetxt(   'test2.txt', c, fmt='%2.1f', delimiter=',', newline='\n',
           header=info   )
"""THE RESULT:
# Time
# Date: 2023.06.21
# 
#  Time (fs),	 Phase (rad)
-10.0		 -10.0
-9.0	     -10.8
-8.0		 -11.2
-7.0		 -11.2
-6.0		 -10.8
-5.0		 -10.0
-4.0		 -8.8
-3.0		 -7.2
-2.0		 -5.2
-1.0		 -2.8
0.0		     0.0
1.0		     3.2
2.0		     6.8
3.0		     10.8
4.0		     15.2
5.0		     20.0
6.0		     25.2
7.0		     30.8
8.0		     36.8
9.0		     43.2
10.0		 50.0"""


#Reading saved files:
#numpy.loadtxt(fname, dtype=<class 'float'>, comments='#',
#delimiter=None, converters=None, skiprows=0, usecols=None,
#unpack=False, ndmin=0, encoding='bytes')

#fname: file to read, skiprows: amount of rows to skip (eg. to skip header)
#usecols: columns to read, unpack: separates columns into separate objects
#comments: rows to skip

t, phi = np.loadtxt('test2.txt', delimiter =',', unpack=True, skiprows=0)
#skiprows = 0, because comments='#' by default, so the header is skipped.
print('Time (fs): \n', t)
#[-10.  -9.  -8.  -7.  -6.  -5.  -4.  -3.  -2.  -1.   0.   1.   2.   3.
#4.   5.   6.   7.   8.   9.  10.]
print('Phase (rad): \n', phi)
#[-10.  -10.8 -11.2 -11.2 -10.8 -10.   -8.8  -7.2  -5.2  -2.8   0.    3.2
#6.8  10.8  15.2  20.   25.2  30.8  36.8  43.2  50. ]






"""(9)_<<<<<<<<<<<<<<<<<<<<<<<<<<<<_MATPLOTLIB_>>>>>>>>>>>>>>>>>>>>>>>>>_(9)"""
#An external module of python made mostly for the 2D visualization of data.
#Contains multiple submodules. The submodule needed for the 2D visualization
#is called Pyplot:
import matplotlib.pyplot as plt
plt.close('all')    #Closes all previously opened plots (for clarity).
#This submodule requires numpy arrays, so that module must be imported, too.



#Let's have a look at some simple plots:
plt.plot([1,2,3,3,2,5,6,5,6,7])   #The 'x' axis starts with 0 and step = 1.      



#New datasets below. Important: len(x) = len(y)!
x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)



plt.figure()    #without plt.figure(), the 2 plots appear on the same 
                #figure surface. The 'figure' is what the plot will appear on.
plt.plot(x,y)
plt.show()



#Let's apply "decorations"!
x1 = np.linspace(-2*np.pi, 2*np.pi, 200)
y1 = np.sin(x1)
x2 = np.linspace(-2*np.pi, 2*np.pi, 20)
y2 = np.sin(x2)



plt.figure(3, figsize = (7,5))
plt.plot(  x1, y1, 'g-', label='Theory'  )          #'g-': green line
plt.plot(  x2, y2, 'ro', label='Measurement'  )     #'ro': red dots
plt.xlabel('Phase (rad)')                           #axis title
plt.ylabel('Voltage (V)')
plt.legend(loc='upper right')                       #location of plot labels
plt.show()



#Applying a grid:
#matplotlib.pyplot.grid(b=None, which='major', axis='both', **kwargs)
#which: grid line type ('major, 'minor', 'both')
#axis: grid line direction ('x', 'y', 'both')



"""Here is an explanation of **kwargs using an example:"""
#Code:
def human(**kwargs):
    print(kwargs)
human(name="Tomi", age=9001)       
#Result:
"""{'name': 'Tomi', 'age': 9001}
Basically, **kwargs takes a custom amount of key-value pairs. In the above 
example, we created a dictionary!"""
    


"""Here is an explanation of **kwargs using examples:"""    
def listing(*args):
    print(args)
listing(1, 2, 3, 4)
#Result:
"""(1, 2, 3, 4)
This is actually a tuple (not a list). *args takes a custom amount of
positional arguments and works with them."""



def summation(*args):
    return np.sum(args)

print(summation(1,2,3))
#Result: 6
    
    
    
#matlotlib.pyplot.subplot(*args,**kwargs)
#Adds a new graph to a figure. Creates an object from class 'axes'. Example:
fig, ax1 = plt.subplots()   #Similar to 'a, b = 2, 1'. 'fig' will be the figure
#(go figure...), and ax1 will be the plot. 'fig' is like a piece of paper onto
#which we can draw the ax1 plot!

#Here are a few methods for the 'axes' class:
#axes.plot([x], y, [fmt], data=None, **kwargs) 
#axes.set_xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)
#Axes.set_ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)




























