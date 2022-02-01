#Project Name: Rocket Simulation
#Author: Conner Fransoo
#Date: January 30th, 2022

import math

idealDesign = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

oxidizerToFuelRatio = 2.5

#kg
engineMass = 15.0
payload = 10.0
dryMass = 0.0
wetMass = 0.0

#s
specificImpulse = 250.0
burnTime = 0.0
#N
thrust = 10000.0
#Pa
tankPressure = 2500000.0
#m
bodyTubeThickness = 0.002
fairingHeight = 1.0
tankThickness = 0.01
rocketRadius = 0.175
rocketHeight = 0.7
#m/s
deltaV = 0.0
#kg/m^30
keroseneDensity = 800.0
loxDensity = 1141.0
aluminumDensity = 2700.0
    
def finalMass(rocketRadius, rocketHeight):
    #Assumes the body tube and fairing are made out of aluminum (density: 2700kg/m^3)
    #LOX tank and fuel tank height proportions based on 2.5 Oxidizer to Fuel Mass Ratio and the differences in density
    bodyTubeMass = math.pi*((rocketRadius**2.0)-((rocketRadius-bodyTubeThickness)**2))*rocketHeight*aluminumDensity
    fairingMass = bodyTubeThickness * aluminumDensity * math.pi * rocketRadius * math.sqrt((rocketRadius**2)+(fairingHeight**2))
    loxTankMass = (math.pi * ((rocketRadius-bodyTubeThickness) ** 2) * bodyTubeThickness * aluminumDensity * 2) + (math.pi * (((rocketRadius-bodyTubeThickness) ** 2)-((rocketRadius-bodyTubeThickness-tankThickness) ** 2)) * (0.6368*(rocketHeight-0.04)) * aluminumDensity)
    fuelTankMass = (math.pi * ((rocketRadius-bodyTubeThickness) ** 2) * bodyTubeThickness * aluminumDensity * 2) + (math.pi * (((rocketRadius-bodyTubeThickness) ** 2)-((rocketRadius-bodyTubeThickness-tankThickness) ** 2)) * ((rocketHeight-0.04)/2.753) * aluminumDensity)
    global dryMass
    dryMass = bodyTubeMass + fairingMass + loxTankMass + fuelTankMass + engineMass + payload
    return dryMass
     
def initialMass(dryMass, rocketRadius, rocketHeight):
    loxMass = loxDensity * math.pi * ((rocketRadius-bodyTubeThickness-tankThickness)**2) * (0.6368*(rocketHeight-0.04))
    fuelMass = keroseneDensity * math.pi * ((rocketRadius-bodyTubeThickness-tankThickness)**2) * ((rocketHeight-0.04)/2.753)
    global wetMass 
    wetMass = dryMass + loxMass + fuelMass
    return wetMass
    
def calculateBurnTime(wetMass, dryMass):
    global burnTime
    burnTime = (wetMass-dryMass)/(thrust/(9.81*specificImpulse))
    return burnTime
    
def calculatedeltaV(initialMass, finalMass, burnTime):
    global deltaV
    deltaV = (specificImpulse * 9.81 * math.log(wetMass / dryMass))-(9.81*burnTime)
    return deltaV

while rocketRadius < 0.31:    
    while wetMass < 340:
        initialMass(dryMass, rocketRadius, rocketHeight)
        finalMass(rocketRadius, rocketHeight)
        calculateBurnTime(wetMass, dryMass)
        calculatedeltaV(wetMass, dryMass, burnTime)
        if deltaV > idealDesign[2]:
            idealDesign[0] = rocketRadius
            idealDesign[1] = rocketHeight
            idealDesign[2] = deltaV
            idealDesign[3] = burnTime
            idealDesign[4] = wetMass
            idealDesign[5] = dryMass
        rocketHeight += 0.00001
    rocketRadius += 0.00001
    rocketHeight = rocketRadius * 4.001
    
print(idealDesign[0])
print(idealDesign[1])
print(idealDesign[2])
print(idealDesign[3])
print(idealDesign[4])
print(idealDesign[5])
    
    
print(" Hello ")

finalMass(idealDesign[0], idealDesign[1])
print(dryMass)
initialMass(dryMass, idealDesign[0], idealDesign[1])
print(wetMass)
calculateBurnTime(wetMass, dryMass)
print(burnTime)
print(calculatedeltaV(wetMass, dryMass, burnTime))

maxHeight = (-9.81*idealDesign[3]/2)+(((9.81*specificImpulse*idealDesign[3]*dryMass)/(wetMass-dryMass))*math.log(dryMass/wetMass))+(9.81*specificImpulse*idealDesign[3])+((deltaV ** 2)/(9.81*2))
print(maxHeight)
flightTime = idealDesign[3]+(idealDesign[2]/9.81)
print(flightTime)


