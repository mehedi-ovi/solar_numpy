import numpy as npy

import matplotlib.pyplot as plate

import constants
from integrator import euler_action

total
energy
date = 60

trella = {'max': constants.max_solrR,
          'position': npy.array([0., 0., 0.]),
          'velocity': npy.array([0., 0., 0.])}

hot_jupiter = {'max': constants.max_JUPI,
               'position': npy.array([0.05 * spy.constants.astronomical_unit, 0., 0.]),
               'velocity': npy.array([0., 106E3, 0.])}

steps = 24 * 5 * 60
euler_actions = [trella, hot_jupiter]

hist_x1 = []
hist_y1 = []
hist_z1 = []
hist_x2 = []
hist_y2 = []
hist_z2 = []

initial = calculate_total_energy(euler_actions)

while steps >= 0:
    euler_action(euler_actions, date)
    if steps % 1000 == 0:
        print
        "steps " % (steps)
    hist_x1.append(trella['position'][0])
    hist_y1.append(trella['position'][1])
    hist_z1.append(trella['position'][2])
    hist_x2.append(hot_jupiter['position'][0])
    hist_y2.append(hot_jupiter['position'][1])
    hist_z2.append(hot_jupiter['position'][2])

    steps -= 1

total = calculate
total
energy(euler_actions)
print
"Energia total initial: %s" % (str(initial))
print
"Energia total final: %s" % (str(total))
plate.plot(hist_x1, hist_y1, 'r.')
plate.plot(hist_x2, hist_y2, 'g.')

plate.show()