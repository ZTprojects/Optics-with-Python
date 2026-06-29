""" (4) create a list whose name is data, with the elements 5, 10, 15, 20, 25.
    Show the type of data and its elements."""
data = [5, 10, 15, 20, 25]
print(type(data))       #<class 'list'>
for i in data:
    print(type(i))      
""" <class 'int'>
    <class 'int'>
    <class 'int'>
    <class 'int'>
    <class 'int'>"""





"""(5)_<<<<<<<<<<<<<<<<<<<<<_APPLICATION OF METHODS_>>>>>>>>>>>>>>>>>>>>>>>>"""
days = ['Monday', 'Tuesday', 'Wednesday']
print(days)                 #['Monday', 'Tuesday', 'Wednesday']

days.append('Thursday')
print(days)                 #['Monday', 'Tuesday', 'Wednesday', 'Thursday']
days.extend(['Friday', 'Saturday', 'Sunday'])
print(days)                 #['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                            #'Friday', 'Saturday', 'Sunday']
                            




"""(6)_<<<<<<<<<<<<<<<<<<<<<<_SAVING INTO A FILE_>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
fileOut = open('test.txt', 'w')     #'w' refers to writing mode,
                                    #as opposed to 'r' - reading mode
#'fileOut and 'test.txt' are not the same. 'file' is a file object in Python 
#throug hwhich we can access 'test.txt' in Python. 'test.txt' is stored on the  
#SSD. This is the first step of saving into a file - we must open a file first.
#Let's use a method to write into a file.

                                                #data = [5, 10, 15, 20, 25]
fileOut.write(''.join(str(i) for i in data))    #note that .write() expects 
                                                #strings, and NOT numbers
#for i in data --> goes through every element in data
#str(i) --> takes a given 'i', turns it into a string. 'i' is given by for loop
#''.join() --> the join method takes its argument and writes it into the file
#As can be seen above, 'join' is a method of the string class.


fileOut.close()
#Closes the file object file. Content of txt file: 510152025
#Now I will open the file to be read.


fileIn = open('test.txt', 'r')  #opens the test.txt file for reading. fileIn is
                                #what refers to the file.
forPrint = fileIn.read()        #reads the content of test.txt. If read doesn't
#receive an argument, it reads everything, from beginning to end.
print(forPrint)             #510152025
print(type(forPrint))       #<class 'str'>






"""(7)_<<<<<<<<<<<<<_IMPORTING MODULES: MATH AND NUMPY>_>>>>>>>>>>>>>>>>>>>>"""
#using external, importable modules with premade functions, classes, etc.
from math import sqrt   #here we imported a single function from math
print(sqrt(4))          #there is no need to use a "prefix" with this method


import math as m    #we will refer to the math module as 'm'
print(m.sqrt(4))    #we used the .sqrt function
         
              
#Numpy module: a complementary module of python
#Important data type: ndarray. Similar to lists, but every element
#must be the same type, so for example, only integers, floats, etc..
#Operations on ndarrays are done element by element.
import numpy as np
myList = [20.0, 800., 0.0, 3.0, 111.0]  #Note that all elements are floats!
print(type(myList))                     #<class 'list'>


myNdarray = np.array(myList)    #Converts an object (myList) into an ndarray.
print(myNdarray)                #If not all elements are the same, they will 
print(type(myNdarray))          #still be converted to the most general one.
#If one element is a string, every element will be a string.


myList_2 = ['Wavelength', 20.0, 800., 0.0, 3.0, 111.0]
myNdarray_2 = np.array(myList_2)   
print(myNdarray_2)          #['Wavelength' '20.0' '800.0' '0.0' '3.0' '111.0']                 
print(type(myNdarray_2))    #Notice how everything is a string now.
                            #<class 'numpy.ndarray'> is the type. 


#np.linspace(start, stop, num=50, endpoint=True, retstep=False,dtype=None):
#creates an ndarray with elements starting from 'start' and ending with 'stop.
#There will be a 'num' amount of elements in total with equal spacing.
wl = np.linspace(700, 900, 5)
print(wl)                       #[700. 750. 800. 850. 900.]
print(type(wl))                 #<class 'numpy.ndarray'>


#np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None):
#very similar to the linspace function, but the starting and final element will
#be base**start ands base**stop, and you can also change the default base value.
myLogSpace = np.logspace(-2, 3, 6)
print(myLogSpace)       #[1.e-02 1.e-01 1.e+00 1.e+01 1.e+02 1.e+03]
print(type(myLogSpace)) #<class 'numpy.ndarray'>


#np.arange(start, stop, step, dtype=None): creates an ndarray, whose first 
#element is 'start', and will add new elements which are bigger than the
#previous element by the 'step' value until before an element would become
#bigger than the 'stop' value.
myArange = np.arange(100, 700, 100)
print(myArange) #[100 200 300 400 500 600]

myArange = np.arange(100., 700, 100)
print(myArange) #[100. 200. 300. 400. 500. 600.] --> turned into floats.

myArange = np.arange(100, 110)
print(myArange) #[100 101 102 103 104 105 106 107 108 109] -->step default is 1

myArange = np.arange(4)
print(myArange) #[0 1 2 3] --> start default is 0. Notice how the ndarray does
                #not reach the 'stop' value!

















