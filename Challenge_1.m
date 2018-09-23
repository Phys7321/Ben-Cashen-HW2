clear;

m = 1;
a = 2;
x = linspace(0,a - 0.0001,10000);
n = length(x);
f = @(x) sqrt((8*m)./(a.^4 - x.^4));
y = f(x);
t1 = integral(f,x(1),x(n));
t2 = trapz(x,y);
fprintf('MATLAB Integral Function: t = %f \nTrapezoid Method: t = %f',t1,t2);

f = @(x,y) sqrt((8*m)./(y.^4 - x.^4));
y = linspace(0.01,4,10000);
n = length(y);

t = [];

for i = y(1:n)
t = [t,trapz(x,f(x,i))];
end

plot(y,t,'-');

