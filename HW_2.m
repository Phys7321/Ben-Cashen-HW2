clear;

% First case (1D line charge)
r = linspace(1.1,5,100);    % displacement from origin along x-axis
r_p = linspace(0,1,100);    % source displacement vector
f = @(r,r_p) 2 .* r_p./(r - r_p);   % functional form of integral (1/(4*pi*epsilon_0) set to unity)
n = length(r);
V = [];
for d = r(1:n)
    V = [V,trapz(r_p,f(d,r_p))];    % trapezoidal method for taking integral

end 

figure(1)
plot(r,V)
xlabel('x')
ylabel('V(x)')

% Solving for E field
[E_neg,rc] = Der(V,r);  % derivative of potential using central diff.
E = -E_neg;             % E field is neg. of the gradient of potential

figure(2)
plot(rc,E)
xlabel('x')
ylabel('E(x)')

% Second case (2d line charge)
x = linspace(1,5,80);  % displacement from origin along x-axis
y = linspace(2,6,80);  % displacement from origin along y-axis
x_p = linspace(0,1,100);    % displacement vector of first line charge
y_p = linspace(1,2,100);    % displacement vector of second line charge

f1 = @(x,y,x_p) x_p.^2 ./sqrt((x-x_p).^2 + y.^2);   % functional form of integral for potential of first line charge

f2 = @(x,y,y_p) y_p ./sqrt(x.^2 + (y-y_p).^2);      % functional form of integral for potential of second line charge

V = zeros(length(x),length(y));
for i = 1:length(x)
    for j = 1:length(y)
        
        V1 = trapz(x_p,f1(x(i),y(j),x_p)) ;         % potential V is sum of potentials from each line charge
        V2 = trapz(y_p,f2(x(i),y(j),y_p)) ; 
        V(i,j) = V1 + V2;
    end    
    
end    


figure(3)
mesh(x,y,V)
xlabel('x')
ylabel('y')
zlabel('V(x,y)')
az = 45;
el = 45;
view(az,el);


% Solving for E field

Ex = -diff(V)./0.05 ;   % 0.05 is difference between adjacent x and y values 
Ey = -diff(V,1,2)./0.05;
xc = 0.5*conv2(x,[1,1],'valid');    % since the above equations solved for the average E field between adjacent
yc = 0.5*conv2(y,[1,1],'valid');    % points, we need to take the avg. x and y positions between points 

figure(4)
mesh(y,xc,Ex)
xlabel('x')
ylabel('y')
zlabel('Ex(x,y)')
az = 45;
el = 45;
view(az,el);

figure(5)
mesh(yc,x,Ey)
xlabel('x')
ylabel('y')
zlabel('Ey(x,y)')
az = 45;
el  =45;
view(az,el);

% Third case (2d disk of charge)
x = linspace(-4,4,160);
y = linspace(-4,4,160);
z = 1;


V = zeros(length(x),length(y));

%Using MATLAB double integral function to solve potential
for i = 1:length(x)
    for j = 1:length(y)
        f = @ (r,theta) cos(theta).* r.^2./sqrt((x(i)-r.*cos(theta)).^2 + (y(j)-r.*sin(theta)).^2 + z.^2);
        V(i,j) = integral2(f,0,2,0,2*pi) ; 
    end    

end    

figure(6)
mesh(x,y,V)
xlabel('x')
ylabel('y')
zlabel('V(x,y)')


% Solving for E field

Ex = -diff(V)./0.05 ;   %taking difference in V down columns
Ey  = -diff(V,1,2)./0.05;   %taking diff in V across rows 
xc = 0.5*conv2(x,[1,1],'valid');
yc = 0.5*conv2(y,[1,1],'valid');

figure(7)
mesh(y,xc,Ex)
xlabel('x')
ylabel('y')
zlabel('Ex(x,y)')

figure(8)
mesh(yc,x,Ey)
xlabel('x')
ylabel('y')
zlabel('Ey(x,y)')

