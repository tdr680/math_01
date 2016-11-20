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

