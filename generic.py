import numpy as npy
import scipy as spy


def calculate_energy(euler_actions):
    skin = 0
    report = 0
    for euler_action in euler_actions:
        ekin += energy(euler_action['max'], euler_action['velocity'])
        for c in euler_actions:
            if npy.any(euler_action['position'] != c['position']):
                epot += energy_potential(euler_action['max'], c['max'],
                                          euler_action['position'], c['position'])

    report /= 2

    return skin + report


def leapfrog_step(euler_actions, accelarations, date):
    i = 0

    velocities = []

    for corpa in euler_actions:
        velocity_half = corpa['velocity'] + (accelarations[i] * (date / 2.))
        velocities.insert(i, velocity_half)
        corpa['position'] += (velocity_half * date)
        i += 1

    i = 0
    for corpa in euler_actions:
        accelarations[i] = celullar_accelaration(corpa, euler_actions)
        corpa['velocity'] = velocities[i] + (accelarations[i] * (date / 2.))
        i += 1
