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
        self.usableFuelArm = usableFuelArm
        self.maxTakeoffWeight = maxTakeoffWeight
        self.emptyPlaneWeight = emptyPlaneWeight
        self.pilotsWeight = pilotsWeight
        self.luggageWeight = luggageWeight
        self.meanAerodynamicChord = meanAerodynamicChord # meters
        self.gravityCentrePosition = gravityCentrePosition # %MAC

    def fuelCalculation(self):
        pathLength = int(input("\nTotal route (in nautical miles): "))
        pathDuration = (self.baseFactor*pathLength)/60 # hours
        usedFuel = pathDuration*self.fuelConsumption + (100/60)*self.fuelConsumption
        return (usedFuel*0.72)*self.usableFuelArm

    def weightAndBalance(self, calculatedFuelMoment):
        print(colored.green(f"\nYour flight with the {self.name} is ready!"))
        fuel=(calculatedFuelMoment/self.usableFuelArm)*(1/0.72)
        print(f"\nFuel needed for that flight is {round(fuel, 1)} liters.")
        totalMoment = self.emptyPlaneMoment+self.pilotsMoment+self.luggageMoment+calculatedFuelMoment
        tow = (self.pilotsWeight+self.emptyPlaneWeight+self.luggageWeight+(calculatedFuelMoment/self.usableFuelArm))
        if tow > self.maxTakeoffWeight:
            print(f"{colored.red('Warning')}: Current takeoff weight is over the limit.")
        totalArm = totalMoment/tow
        macProportion = (totalArm/self.meanAerodynamicChord)*100
        if macProportion > self.gravityCentrePosition:
            print(f"Aircraft is balanced {colored.blue('rear')}")
        elif macProportion < self.gravityCentrePosition:
            print(f"Aircraft is balanced {colored.blue('front')}")
        print(f"Total Moment: {colored.cyan(round(totalMoment, 1))} kg.m | Total Arm: {colored.cyan(round(totalArm, 3))} m | Total Mass: {colored.cyan(round(tow,1))} kg | Autonomy: {colored.cyan(round(fuel/self.fuelConsumption, 1))} hours")

def informationGathering():
    print("\n*******************\n* PyFlightPlanner *\n*******************")
    print("\n\tAvailable Planes\n\t[1] SportStar RTC\n")
    plane = int(input("Enter plane number: "))
    crewWeight = float(input("Crew weight: "))
    luggageWeight = float(input("Luggage weight: "))
    
    # Plane definitions
    if plane==1: aircraft = Plane("SportStar RTC", 19, 0.7, 124, 144, 353, 0.249, crewWeight, 0.545, luggageWeight, 1.083, 0, 0.680, 600, 1.25, 19.95)
    aircraft.weightAndBalance(aircraft.fuelCalculation())

informationGathering()

#metar : si BKN0 ou OVC0 => bcp de nuages bas donc mort