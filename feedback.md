# Feedback
9.24
You have a good start. I'd like to steer you toward using contour plots and the quiver function (it is in numpy in python and built-in in MATLAB). You should also take another look at the challenge problem in matlab - you're not actually graphing what you think you're graphing. And the 1D charged line - your calculation is only finding the electric potential on one axis. The charge distribution may be 1D, but the field is still produced in the 3D world.
9.26
Looks better I would still try to get the quiver function working in concert with the contour plots because that gives the best visualization, I think. The nit picks: in your python code line 87, you are calling nquad to integrate - I believe that is causing your program to run really slowly. nquad is generally going to take more time then dblquad or some other double integration technique. And in both platforms, learn the syntax for the gradient function - it will be more general.
