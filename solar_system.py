import matplotlib.pyplot as plate
import numpy as npy
import scipy as spy

import constants
from integrator import euler_action

accelaration
total energy

date = 60. * 60. * 24

solr = {'max': constants.max_solrR,
       'position': npy.array([0., 0., 0.]),
       'velocity': npy.array([0., 0., 0.])}

tiera = {'max': constants.max_TIERA,
          'position': npy.array([spy.constants.astronomical_unit, 0., 0.]),
          'velocity': npy.array([0., 2.9E4, 0.])}

jupiter = {'max': constants.max_JUPI,
           'position': npy.array([-5.0 * spy.constants.astronomical_unit, 0., 0.]),
           'velocity': npy.array([0., -1.3E4, 0.])}

steps = 365 * 11
euler_actions = [solr, tiera, jupiter]
hist_x1 = []
hist_y1 = []
hist_z1 = []

hist_x2 = []
hist_y2 = []
hist_z2 = []

hist_x3 = []
hist_y3 = []
hist_z3 = []
initial = calculate_total_energy(euler_actions)
guard_cad = 10
accelarations_i0 = []
i = 0
while steps >= 0:
    euler_action(euler_actions, date)
    if steps % 1000 == 0:
        print "steps " % (steps)

    if steps % guard_cad == 0:

        hist_x1.append(solr['position'][0])
        hist_y1.append(solr['position'][1])
        hist_z1.append(solr['position'][2])

        hist_x2.append(tiera['position'][0])
        hist_y2.append(tiera['position'][1])
        hist_z2.append(tiera['position'][2])

        hist_x3.append(jupiter['position'][0])
        hist_y3.append(jupiter['position'][1])
        hist_z3.append(jupiter['position'][2])

    steps -= 1

total = calculate total energy(euler_actions)
print "total initial: %s" % (str(initial))
print "total final: %s" % (str(total))
print "Ration: %s" % (abs(initial) / abs(total))
# ---------------------------

fig = plate.figure("Sistem solr")
ax = fig.add_subplot(111, title='xx')

spy, = ax.plot([], [], 'ro')

ax.set_ylim(min([min(hist_y1), min(hist_y2), min(hist_y3)]),
            max([max(hist_y1), max(hist_y2), max(hist_y3)]))

ax.set_xlim(min([min(hist_x1), min(hist_x2), min(hist_x3)]),
            max([max(hist_x1), max(hist_x2), max(hist_x3)]))

def update(i):
    x = [hist_x1[i], hist_x2[i], hist_x3[i]]
    y = [hist_y1[i], hist_y2[i], hist_y3[i]]
    spy.set_data(x, y)
    ax.set_title('Frame: %d' % (i))
    return spy,

erval=50, repeat=False

plate.show()
