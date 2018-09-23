% Program to plot both a function, F, and data, derdata, as well the first
% and second order derivatives of each using central difference (Der
% function)

clear;

%U = input('Enter upper bound of domain: ');     % choose the function bounds
%L = input('Enter lower bound of domain: ');     
%res = input('Enter spacing between points: ');  % choose resolution

%n = (U - L)/res + 1;    % number of points 
%x = zeros(1,n);         % allocate space for array

%for i = 1:n
%    x(i) = L + (i - 1)*res;
%end

x = linspace(-1,3,100);
F = (sin(1./(x.*(2 - x)))).^2;    % function to differentiate
[der1,xc1] = Der(F,x);          % first order derivative using central diff.
[der2,xc2] = Der(der1,xc1);     % second order derivative using central diff.

load('derdata','X','Y');        % data to differentiate
[der1_2,xc1_2] = Der(Y,X);      % first order derivative using central diff.
[der2_2,xc2_2] = Der(der1_2,xc1_2); % second order derivative using central diff.

figure(1)
plot(x,F,'-');

figure(2)
plot(xc1,der1,'-');

figure(3)
plot(xc2,der2,'-');
  
figure(4)
plot(X,Y,'-');

figure(5);
plot(xc1_2,der1_2,'-');

figure(6);
plot(xc2_2,der2_2,'-');
