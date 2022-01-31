'''
Project Name: Rocket Simulation
Author: Conner Fransoo
Date: January 30th, 2022

'''
import math

oxidizerToFuelRatio = 2.5

#kg
engineMass = 15
payload = 10
initialMass = 20
finalMass = 19.99
#s
specificImpulse = 250
#N
thrust = 10000
#Pa
tankPressure = 2500000
#m
bodyTubeThickness = 0.002
#m/s


def calculatedeltaV(impulse, initialMass, finalMass):
    deltaV = impulse * 9.81 * math.log(initialMass / finalMass)
    return deltaV
    
print(calculatedeltaV(specificImpulse, initialMass, finalMass))
