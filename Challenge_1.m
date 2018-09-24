clear;

m = 1;
amp = 2;
x = linspace(0,amp - 0.0001,10000);
n = length(x);
f = @(x) sqrt((8*m)./(amp.^4 - x.^4));
y = f(x);
t1 = integral(f,x(1),x(n));
t2 = trapz(x,y);
fprintf('MATLAB Integral Function: t = %f \nTrapezoid Method: t = %f',t1,t2);

f = @(x,a) sqrt((8*m)./(a.^4 - x.^4));
a = linspace(0.01,4,10000);
n = length(a);

t = [];

for i = a(1:n)
x = linspace(0,i - 0.0001,10000);
t = [t,trapz(x,f(x,i))];
end

plot(a,t,'-');
xlabel('Amplitude');
ylabel('Period');
