class Plane:
    def __init__(self, name, fuelConsumption, baseFactor, soloPrice, doublePrice):
        self.name = name
        self.fuelConsumption = fuelConsumption # liters per hour
        self.baseFactor = baseFactor
        self.soloPrice = soloPrice # euros per hour
        self.doublePrice = doublePrice # price when FI is onboard

    def fuelCalculation(self):
        pathLength = int(input("Total route (in nautical miles): "))
        pathDuration = (self.baseFactor*pathLength)/60 # hours
        usedFuel = pathDuration*self.fuelConsumption + (100/60)*self.fuelConsumption
        print(f"Fuel needed for that flight is {round(usedFuel, 1)} liters.")

SportStarRTC = Plane("SportStar RTC", 19, 0.7, 124, 144)
SportStarRTC.fuelCalculation()