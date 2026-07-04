import numpy as np
import matplotlib.pyplot as plt
plt.close('all')






"""(10)_<<<<<<<<<<<<<<<<<<<<<<<<<_CONVEX MIRROR_>>>>>>>>>>>>>>>>>>>>>>>_(10)"""
#We will be using geometric optics here. The light rays coming parallel to the
#optical axis and are far away from it will be focused to between the paraxial
#focus point and the vertex of the mirror. 

#Below there will be a calculation of the light ray's path. For the explanation
#of the used notations, take a look at '4_OWP_convexLens_ea4_PICTURE_1.png'. 
#Note to self: find a better alternative to MS Paint...


""" FP2 line: longitudinal spherical aberration (LSA)
    FP3 line: transversal spherical aberration (TSA)


1.) P0:  z0=0,  y0=y,  R=2f

2.) P1:  y1=y0=y,  z1=sqrt(R**2-y1**2)

3.) alpha=asin(y1/R),  m=tg(2*alpha),  b=y1-m*z1

4.) P2:  y2=0,  z2=(y2-b)/m

5.) P3:  z3=f,  y3=m*z3+b

6.) LSA=z2-f,  TSA=0-y3


Now it is time work with these formulas. Let's define the parameters of a con-
vex lens and draw it first!"""
f = 25 #mm, focal length of the mirror
D = 50 #mm, height of the optical element
#y of circle in [0, D/2] using N=31 points
N=31
#z axis in [20mm,51mm], y axis in [-5mm, 26mm]
z_min, z_max = 20, 51
y_min, y_max = -10, 26
#draw the optical axis at y=0!



R = 2*f
phi_max = np.arcsin(D/2/R)
phi = np.linspace(0,  phi_max,  N) 
circle_y = R * np.sin(phi)
circle_z = R * np.cos(phi)
#optical_Axis = np.zeros(len())



fig, ax1 = plt.subplots()
ax1.plot(circle_z, circle_y, 'b-')

ax1.set_xlabel('z [mm]')
ax1.set_xlim(z_min, z_max)
ax1.set_ylabel('y [mm]')
ax1.set_ylim(y_min, y_max)

ax1.set_title('Convex Mirror')
ax1.grid(which='major', axis='both')
ax1.axhline(y=0, color='black', linewidth='1')



"""Now let's draw a set of light rays travelling in our optical system!"""
y0 = np.linspace(0, y_max-1, 26)
alpha = np.arcsin(y0/R)
m = np.tan(2*alpha)
b = y0 - m*np.sqrt(R**2 - y0**2)    #m*np.cos(alpha) is also fine
z3 = f
y3 = m*z3+b

lineEnd_y=y0
lineEnd_z=np.sqrt(R**2-lineEnd_y**2)



fig, ax2 = plt.subplots()
ax2.plot(circle_z, circle_y, 'b-', linewidth='3')

for i in range(len(y0)):    #range(len(y0)) --> 0,1,2,...25 (integers!)
    ax2.plot([0, R * np.cos( alpha[i]  )],  [y0[i], y0[i]],  'r-',
             linewidth='1')
    ax2.plot(   [z3, lineEnd_z[i]],   [y3[i], lineEnd_y[i]], 'r-',
             linewidth='1')

ax2.set_xlabel('z [mm]')
ax2.set_xlim(z_min, z_max)
ax2.set_ylabel('y [mm]')
ax2.set_ylim(y_min, y_max)

ax2.set_title('Convex Mirror - Spherical Aberration')
ax2.grid(which='major', axis='both')
ax2.axhline(y=0, color='black', linewidth='2')



"""Let's also make a graph of TSA and LSA on the same figure!"""
z2 = -b/m
LSA = z2 - f
TSA = 0-y3



fig, (ax3,ax4) = plt.subplots(1,2)
fig.suptitle('TSA and LSA')

ax3.plot(y0, LSA, 'r')
ax3.set_xlabel('y0 [mm]')
ax3.set_ylabel('LSA [mm]')
ax3.grid()
ax3.set_title('LSA graph')
ax3.set_ylim(top=  max(  max(TSA), max(LSA))  +1)

ax4.plot(y0, TSA, 'r')
ax4.set_xlabel('y0 [mm]')
ax4.set_ylabel('TSA [mm]')
ax4.grid()
ax4.set_title('TSA graph')
ax4.set_ylim(top=  max(  max(TSA), max(LSA))  +1)



#fig, (  (ax1,ax2),  (ax3,ax4)  ) = plt.subplots(2,2) --> This DOES NOT work,
#because here ax plots get overwritten by the plt.subplots() command, which
#overwrites the old axes with new empty ones.

#Check out 4_OWP_convexMirror_ea4_PICTURE_2.png for the f = 500 mm case, 
#where you can't notice the spherical aberration!






































































