# -*- coding: utf-8 -*-


###############################################################################
# Aufgabe 3 (Mengenoperationen / Aussagen)
###############################################################################

from sets import Set

A = Set([ 2, 4, 6, 8])
B = Set([-3, -2, 2, 8])
C = Set([6, -3, 2])
D = Set([-2, 3])

print "(a)   A - B          = {0} ".format(A - B)
print "(b)   A ∩ D ∩ B      = {0} ".format(A & D & B)
print "(c)   (C ∩ D) ∪ B    = {0} ".format((C & D) | B)

print "(g)   A ⊂ B          ➤ {0} ".format(A < B)
print "      2 ∈ A          ➤ {0} ".format(2 in A)


###############################################################################
# Aufgabe 5 (Mengen zeichnen)
###############################################################################

import numpy as np
import matplotlib.pyplot as plt

x_min = -10.0
x_max = 10.0
x_step = 0.1
y_min = -10.0
y_max = 10.0

x = np.arange(x_min, x_max+1, x_step)
plt.axis([x_min, x_max, y_min, y_max])

# (a) M1
def f_a(x):
    return (x**2 + 7 - 8*x) / 2

# (b) M2
def f_b(x):
    return (6 - abs(x - 4)) / 2

plt.plot(x, f_a(x), x, f_b(x))
plt.show()


###############################################################################
# Aufgabe 6 (Lösen von Gleichungen/Ungleichungen)
###############################################################################

# (a)
plt.axis([x_min, x_max, y_min, y_max])
plt.grid(True)

def f_left(x):
    return abs(x + 4)

def f_right(x):
    return 3 * abs(x - 2) + x

plt.plot(x, f_left(x), x, f_right(x))
plt.show()

# (b)
x_min = -10.0
x_max = 20.0
x_step = 0.1
y_min = -10.0
y_max = 10.0

x = np.arange(x_min, x_max+1, x_step)
plt.axis([x_min, x_max, y_min, y_max])
plt.grid(True)

def f_left(x):
    return (x**2 - 40*x -73)/(-3*x**2 - 4)

def f_right(x):
    return x/x # small hack to return always 1.0

plt.plot(x, f_left(x), x, f_right(x))
plt.show()
