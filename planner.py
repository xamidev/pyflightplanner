from clint.textui import colored

class Plane:
    def __init__(self, name, fuelConsumption, baseFactor, soloPrice, doublePrice, emptyPlaneWeight, emptyPlaneArm, pilotsWeight, pilotsArm, luggageWeight, luggageArm, usableFuelWeight, usableFuelArm, maxTakeoffWeight, meanAerodynamicChord, gravityCentrePosition):
        self.name = name
        #Fuel Calculations
        self.fuelConsumption = fuelConsumption # liters per hour
        self.baseFactor = baseFactor
        #Price Calculations
        self.soloPrice = soloPrice # euros per hour
        self.doublePrice = doublePrice # price when FI is onboard
        #Weight and Balance
        self.emptyPlaneMoment = emptyPlaneWeight*emptyPlaneArm
        self.pilotsMoment = pilotsWeight*pilotsArm
        self.luggageMoment = luggageWeight*luggageArm
        self.usableFuelMoment = usableFuelWeight*usableFuelArm
        self.maxTakeoffWeight = maxTakeoffWeight
        self.takeoffWeight = emptyPlaneWeight+pilotsWeight+luggageWeight+usableFuelWeight
        self.meanAerodynamicChord = meanAerodynamicChord # meters
        self.gravityCentrePosition = gravityCentrePosition # %MAC

    def fuelCalculation(self):
        pathLength = int(input("Total route (in nautical miles): "))
        pathDuration = (self.baseFactor*pathLength)/60 # hours
        usedFuel = pathDuration*self.fuelConsumption + (100/60)*self.fuelConsumption
        print(f"Fuel needed for that flight is {round(usedFuel, 1)} liters.")

    def weightAndBalance(self):
        totalMoment = self.emptyPlaneMoment+self.pilotsMoment+self.luggageMoment+self.usableFuelMoment
        if self.takeoffWeight > self.maxTakeoffWeight:
            print(f"{colored.red('Warning')}: Current takeoff weight is over the limit.")
        totalArm = totalMoment/self.takeoffWeight
        macProportion = (totalArm/self.meanAerodynamicChord)*100
        if macProportion > self.gravityCentrePosition:
            print(f"Aircraft is balanced {colored.blue('rear')}")
        elif macProportion < self.gravityCentrePosition:
            print(f"Aircraft is balanced {colored.blue('front')}")
        print(f"Total Moment: {colored.cyan(round(totalMoment, 1))} kg.m | Total Arm: {colored.cyan(round(totalArm, 3))} m | Total Mass: {self.takeoffWeight} kg")


# Plane definitions
# Add a plane by adding a new line with all the needed plane characteristics

SportStarRTC = Plane("SportStar RTC", 19, 0.7, 124, 144, 353, 0.249, 125, 0.545, 7.5, 1.083, 60, 0.680, 600, 1.25, 19.95)


#tbd: ask for pilot weight, luggage weight, etc. and get fuel weight from fuelCalculation
SportStarRTC.fuelCalculation()
SportStarRTC.weightAndBalance()