import numpy as np
import matplotlib.pyplot as plt
plt.close('all')



def n(x, n_type):
    if n_type=='n_BK7' and np.all(0.3<=x) and np.all(x<=2.5):
        return (1+1.03961212/(1-0.00600069867/x**2)+0.231792344/
            (1-0.0200179144/x**2)+1.01046945/(1-103.560653/x**2))**.5
    #Conditions: 
    #Temperature = 293 °K
    #Wavelength range: 0.3um - 2.5um
    
    elif n_type=='n_FS' and np.all(0.21<=x) and np.all(x<=6.7):
        return (1+0.6961663/(1-(0.0684043/x)**2)+0.4079426/
        (1-(0.1162414/x)**2)+0.8974794/(1-(9.896161/x)**2))**.5
    #Conditions: 
    #Temperature = 293 °K
    #Wavelength range: 0.21um - 6.7um
    
    else:
        return 'Invalid input'



def plot(*lines, title='', xlabel='', ylabel='', legend=0, legLoc='upper right'):
    fig, ax = plt.subplots()
    for x, y, style, label in lines:    
        ax.plot(x, y, style, label=label)
        if legend==1:
            ax.legend(loc=legLoc)
        
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    
    return ax


"""(13)_<<<<<<<<<<<<<<<<<<<<<<<_CONVEX LENS_>>>>>>>>>>>>>>>>>>>>>>>>>>>>_(13)"""
#The radius of a surface is negative/positive if viewed from the propagation 
#direction of the light ray it is concave/convex, so in the case of a double
#convex lense, R1>0 and R2<0.

#The formula with which we describe the focal length of a thin convex lense (on
#both sides of the lense, if the medium is also the same on both sides) is as
#follows: 
#                          1/f = (n-1) * (1/R1 - 1/R2)
#Here, 'f' depends on 'n', which depends on the wavelength of the incoming
#light.

#Let's calculate the focal length of a planoconvex lens, whose flat side 
#meets the light rays first!
R1 = np.inf
R2 = -100#mm
wl = 633#nm, wavelength

f = 1  /  (    (n(wl/1000, 'n_BK7')-1)*(1/R1 - 1/R2)    )
print('The calculated focal length is: {0:.3f} mm.'.format(f))



#Now let's plot the focal length's dependence on wavelength!
wl = np.arange(400,1000,1)
#f = 1  /  (    (n(wl/1000, 'n_BK7')-1)*(1/R1 - 1/R2)    )
f = -R2 / (  n(wl/1000, 'n_BK7')-1  )   #The calculations are easier this way
                                        #for the CPU, the error will be less.
plot(  (wl, f, 'r-', ''), xlabel='Wavelength [nm]', ylabel='Focal length [mm]',
     title='Chromatic aberration')

#Let's check the difference between the max and the min of the 'f' set:
print('Difference between the highest and lowest focal lengths: {0:.3f}.'
          .format(np.max(f)-np.min(f)))



#Now let's use the pathing of rays to calculate the focal length! 
#A demonstration of the ray's pathing and the notations can be seen in
#inkscapeTest.pdf!
def focalLength(R, y, wl):
    z0, y0 = 0, y
    y1 = y0
    z1 = np.sqrt(R**2-y1**2)
    phi = np.arcsin(y1/R)
    alpha = phi
    beta = np.arcsin(  n(wl/1000, 'n_BK7')*np.sin(alpha)  )
    m = np.tan(phi - beta)
    b = y1 - m*z1
    y2 = 0
    z2 = y2 - b/m
    return  z2 - R
    
    
wl = np.arange(400, 1000, 1)
R=100
y = 1
plot(  (wl, focalLength(R, y, wl), 'r-', ''),  title='Chromatic aberration',
     xlabel='Wavelength [nm]',
     ylabel='Focal length [mm]')



#Now let's check the difference between these methods:
plot(  (wl, focalLength(R, y, wl)-f, 'r-', ''),  title='Difference',
     xlabel='Wavelength [nm]',
     ylabel='Focal length difference [mm]')














































































