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






"""(18)_<<<<<<<<<<<<<<<<<<<_NUMERICAL DERIVATION_>>>>>>>>>>>>>>>>>>>>>>_(18)"""
#Since delta(om) = alpha1 + alpha2(om) - gamma:
#d(delta) / d(om) = d(alpha2) / d(om)
#In this section, we will be differentiating numerically using the forward,
#backward and central difference! Let's use delta/alpha2 from the previous
#excercise!
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



alpha2 = np.rad2deg(alpha2)
dom = 0.1
disp_f = np.zeros(len(om)-1)
"""disp_b = disp_f"""
disp_b = np.zeros(len(om))
disp_c = np.zeros(len(om))



for i in range(len(om)-1):
    disp_f[i] = (   alpha2[i+1] - alpha2[i]   ) / dom



"""
for i in range(1, len(om)):
    disp_b[(len(om)-1)-i] = (   alpha2[(len(om)-1)-i] - alpha2[(len(om)-1)-i+1]   ) / dom
   """ 
    
   
    
for i in range(len(om)-1):    
    disp_b[i+1] = (   alpha2[i+1] - alpha2[i]   ) / dom
disp_b = np.delete(disp_b, 0)




for i in range(len(om)-2):
    disp_c[i+1] = (   alpha2[i+2] - alpha2[i]   ) / 2 / dom
disp_c = np.delete(disp_c, 0)
disp_c = np.delete(disp_c, len(disp_c)-1)



disp_plot=plot(   (om[:-1], disp_f, 'r+', 'Forward'),
     (om[1:], disp_b, 'b+', 'Backward'),
     (om[1:-1], disp_c, 'go', 'Central'),
     xlabel='Angular frequency [PHz]', ylabel='Angular dispersion [°/PHz]',
     legend=1, legLoc='upper center',
     title='Numerically calculated dispersion')

disp_plot.lines[0].set_markersize(10)
disp_plot.lines[1].set_markersize(10)
#The error of the forward and backward difference is of order O(dom), whereas
#the error of the central difference is O(dom**2), so the central difference
#is more precise.



#By using the 1 & 2 point forwarded and backwarded Taylor polynomial of f_i 
#(so f_i+1 and f_i+2) and some linear algebra, we can get the 3 $ 5 point
#difference formulae for our numerical calculations, which are more precise 
#than the previously calculated 2 & 3 point differences.
#See 9_OWP_LATEX_difference.pdf for better readability.
disp_f2 = np.zeros(len(om)-2)
disp_b2 = np.zeros(len(om))
disp_c5 = np.zeros(len(om))



for i in range(len(disp_f2)):
    disp_f2[i] = (   -3*alpha2[i] + 4*alpha2[i+1] - alpha2[i+2]   ) /2/dom



for i in range(len(disp_b2)-2):
    disp_b2[i+2] = (   alpha2[i] - 4*alpha2[i+1] + 3*alpha2[i+2]   ) /2/dom
disp_b2 = np.delete(disp_b2, np.s_[0:2])    #[0:2] alone gives a Syntax Error.
                                            #list[0:2] makes sense, but [0:2] 
                                            #does not.



for i in range(len(disp_c5)-4):
    disp_c5[i+2] = (   alpha2[i] - 8*alpha2[i+1] + 8*alpha2[i+3] - alpha2[i+4]
                    )/12/dom
disp_c5 = disp_c5[2:-2]     #A simpler solution than np.delete :)



disp_plot=plot(   (om[:-2], disp_f2, 'r+', 'Forward 2'),
     (om[2:], disp_b2, 'b+', 'Backward 2'),
     (om[2:-2], disp_c5, 'go', 'Central 5'),
     xlabel='Angular frequency [PHz]', ylabel='Angular dispersion [°/PHz]',
     legend=1, legLoc='upper center',
     title='2 and 5 point difference dispersion')

disp_plot.lines[0].set_markersize(10)
disp_plot.lines[1].set_markersize(10)



#Now let's compare the 3 and 5 point center difference values with the 
#np.gradient  function's results!
disp_g = np.gradient(alpha2, om)    #d(alpha2) / d(om)!

disp_plot=plot(   (om[1:-1], disp_c, 'r+', 'Central 3'),
     (om[2:-2], disp_c5, 'b+', 'Central 5'),
     (om, disp_g, 'go', 'Gradient'),
     xlabel='Angular frequency [PHz]', ylabel='Angular dispersion [°/PHz]',
     legend=1, legLoc='upper center',
     title='2 and 5 point difference dispersion')

disp_plot.lines[0].set_markersize(15)
disp_plot.lines[1].set_markersize(15)
#We can see that np.gradient's dimension is greater than the ndarrays we used
#for our central difference formulae, furthermore observe that where disp_c5
#exists, it is equal to the values given by the gradient formula!

#This is because np.gradient uses the 3 point central difference, and extends
#that with the 2 point forward and backward differences at the edges, hence the
#discrepancy in dimension!

























