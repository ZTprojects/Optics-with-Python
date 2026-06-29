""" TASK: write a script that calculates and prints the distance of 
    an image created by a convex lens!
        *** f = 5 cm, t = -6 cm
            
        ==>   1/im - 1/ob = 1/f   ==>   1/im = 1/f + 1/ob   ==>
        im = (f*ob) / (ob+f)
"""
f, ob = 5, -6
im = (f*ob) / (ob+f)
print("Image distance: {0:.2f}".format(im))
#Image distance: 30.00







"""(1)_<<<<<<<<<<<<<<<<<<<<<<<_WHILE AND FOR LOOP_>>>>>>>>>>>>>>>>>>>>>>>>>>"""
t = 0
while t<5:
    t=t+1
    print(t)
""" 1
    2
    3
    4
    5"""


name = 'Python'
i = 0
while i < len(name):
    print(name[i])
    i+=1
""" P
    y
    t
    h
    o
    n"""
    
"""for loop"""
name = 'Python'
for i in name:
    print(i)
""" P
    y
    t
    h
    o
    n"""   






"""(2)_<<<<<<<<<<<<<<<<<<<<<<<<_INPUT FUNCTION_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
a = input('Wavelength: ')   #Wavelength:
print(a)                    #555 - this is a string!
print(type(a))              #<class 'str'> - I told you.


a = float(input('Wavelength: '))    #Wavelength:
print(a)                            #444.0 - this is a float!
print(type(a))                      #<class 'float'>







"""(3)_<<<<<<<<<<<<<<<<<<<<<<<<<<<_FUNCTIONS_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
def cube(x):
    #return the cube of a number
    return x**3
    #'x' exists only in the "little bubble" of this function. It does not exist
    #in the outside world. 'x' is shy.

def volume(x):
    #calculates the volume of a sphere
    return 4 * 3.1415 * cube(x) / 3
    #Here I summon a previously defined function: cube(). The 'cube' function 
    #will take the variable from the 'volume' function

r = input('Radius of sphere: ')     #Radius of sphere: 3
r = float(r)
V = volume(r)
print('The volume of the sphere: {0:.2f}.'.format(V))




































