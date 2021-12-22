"""The bell-shaped Gaussian function, is one of the most widely
used functions in science and technol-ogy. The parameters m and s are real numbers, where s must be
greater than zero. Make a program for evaluating this function when
m = 0, s = 2, and x = 1. Verify the program’s result by compar-
ing with hand calculations on a calculator."""

from math import pi, exp, sqrt

m = 0
s = 2
x = 1

f = 1 / (sqrt(2*pi) * s) * exp(-1/2 * ((x - m) / s)**2)
print(f)
