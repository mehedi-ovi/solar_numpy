import numpy as npy

from calculas import accelaration_gravity


def euler_action(euler_actions, date):
    for corpa in euler_actions:
        corpa['position'] += corpa['velocity'] * date
        accelaration = celullar_accelaration(corpa, euler_actions)
        corpa['velocity'] += accelaration * date


def leapf_step(euler_actions, accelarations, date):
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


def celullar_accelaration(corpa, euler_actions):
    accelaration = 0.0
    for c in euler_actions:
        if npy.any(corpa['position'] != c['position']):
            accelaration += accelaration_gravity(corpa['position'], c['position'], c['max'])
    return accelaration

