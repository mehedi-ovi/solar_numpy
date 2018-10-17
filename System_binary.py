import matplotlib.pyplot as plate
import numpy as npy
import scipy as spy

import constants
from integrator import euler_action

date = 60. * 60.


trella1 = {'max': constants.max_solrR/2,
             'position': npy.array([-3 * spy.constants.astronomical_unit, 0, 0]),
             'velocity': npy.array([0, 5E3, 0])}

trella2 = {'max': constants.max_solrR/2.,
             'position': npy.array([3 * spy.constants.astronomical_unit, 0, 0]),
             'velocity': npy.array([0, -5E3, 0])}

steps = 366 * 10 * 24

hist_x1 = []
hist_y1 = []
hist_z1 = []

hist_x2 = []
hist_y2 = []
hist_z2 = []

save_every = 10

initial = calculate total energy(euler_actions)

while steps >= 0:
    euler_action(euler_actions, date)

    if steps % 1000 == 0:
        print " %d steps: " % (steps)

    if steps % save_every == 0:
        hist_x1.append(trella1['position'][0])
        hist_y1.append(trella1['position'][1])
        hist_z1.append(trella1['position'][2])
        hist_x2.append(trella2['position'][0])
        hist_y2.append(trella2['position'][1])
        hist_z2.append(trella2['position'][2])

    steps -= 1
total = calculate total energy(euler_actions)
print "total initial: %s" % (str(initial))
print "total final: %s" % (str(total))

plate.plot(hist_x1, hist_y1, 'r.')
plate.plot(hist_x2, hist_y2, 'g.')

plate.show()
