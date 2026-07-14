import numpy as np
import matplotlib.pyplot as plt
plt.close('all')



def n(x, n_type):
    x = x/1000
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






"""(16)_<<<<<<<<<<<<<<<<<<<<<<<<<<<_PRISM_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>_(16)"""
#Visual demo: 8_OWP_PIC1_Prism.pdf
#Let's calculate and plot the the delta (angle of deviation) of a gamma=60° 
#prism as a function of the angle of incidence! The prism is made out of fused
#silica!
gamma = 60
gamma = np.deg2rad(gamma)
alpha1 = np.arange(0, 89+1, 1)
alpha1 = np.deg2rad(alpha1)
wl = 600#nm



#delta = alpha1 + alpha2 - gamma. We need alpha2!
beta1 = np.arcsin(   np.sin(alpha1) / n(wl, 'n_FS')   )
beta2 = gamma - beta1
alpha2 = np.arcsin(   n(wl, 'n_FS') * np.sin(beta2)   )
delta = alpha1 + alpha2 - gamma



plot(   (np.rad2deg(alpha1), np.rad2deg(delta), 'r-', ''),
     title='',     xlabel='Angle of incidence [°]',
     ylabel='Angle of deviation [°]'   )
#Notice how there is a minimum angle of deviation! Furthermore, in the variable
#explorer we can see that that the delta ndarray has nan values for low values
#of alpha1! This is because below a certain alpha1 value, we are below the 
#critical angle of incidence of the prism!
#Critical angle of incidence is where alpha2 = 90°:
alpha2_crit = 90
alpha2_crit = np.deg2rad(alpha2_crit)
beta2_crit = np.arcsin(   np.sin(alpha2_crit) / n(wl, 'n_FS')   )
beta1_crit = - beta2_crit + gamma
alpha1_crit = np.arcsin(   n(wl, 'n_FS') * np.sin(beta1_crit)   )
print(np.rad2deg(alpha1_crit))



#Now let's have a look at the minimum of delta!
#delta(alpha1) = alpha1 + alpha2(alpha1) - gamma
#d(delta) / d(alpha1) = 0 at the minimum!
#d(delta) / d(alpha1) = 1 + d(alpha2) / d(alpha1)
#From these: d(alpha2) / d(alpha1) = -1, therefore (-1)*alpha2=alpha1 at the 
#minimum, which means one is a clockwise, another is an anti-clockwise turn,
#but |alpha1|=|alpha2|, and therefore |beta1|=|beta2|=|gamma/2|!
#Notice how delta is the smallest when the light path is symmetrical!







"""(17)_<<<<<<<<<<<<<<<<<<<<<_DISPERSIVE PRISM_>>>>>>>>>>>>>>>>>>>>>>>>_(17)"""
#In the case of dispersion, n=n(wl), and wl=c/om (om -> omega, angular 
#frequency)
#delta(om) = alpha1 + alpha2(om) - gamma

#Let's use a prism made of fused silica, where gamma = 60°, and use it at an angle
#where there is minimal angular deviation at wl = 800nm! Plot the angle of 
#deviation as a function of angular frequency and wavelength!
gamma = 60
gamma = np.deg2rad(gamma)
wl_r = 800#nm -> delta: minimal -> beta1 = gamma/2
alpha1_r = np.arcsin(   n(wl_r, 'n_FS') * np.sin(gamma/2)   )



om = np.arange(1.8, 3.3, 0.1)#PHz!
c = 299.792458#nm*PHz
wl = c / om * 2 * np.pi



beta1 = np.arcsin(   np.sin(alpha1_r) / n(wl, 'n_FS')   )
beta2 = gamma - beta1
alpha2 = np.arcsin(   np.sin(beta2) * n(wl,'n_FS')   )



delta = alpha1_r + alpha2 - gamma
plot(     (wl, np.rad2deg(delta), 'r-', ''), ylabel='Angle of deviation [°]',
     xlabel='Wavelength [nm]'     )
plot(     (om, np.rad2deg(delta), 'r-', ''), ylabel='Angle of deviation [°]',
     xlabel='Angular frequency [PHz]'     )








