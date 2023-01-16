from clint.textui import colored
from plane import Plane
from weather import Weather

def planeRelatedPrep():
    print("\n*******************\n* PyFlightPlanner *\n*******************")
    print("\n\tAvailable Planes\n\t[1] SportStar RTC\n")
    plane = int(input("Enter plane number: "))
    crewWeight = float(input("Crew weight: "))
    luggageWeight = float(input("Luggage weight: "))
    
    # Plane definitions
    if plane==1: aircraft = Plane("SportStar RTC", 19, 0.7, 124, 144, 353, 0.249, crewWeight, 0.545, luggageWeight, 1.083, 0, 0.680, 600, 1.25, 19.95)
    aircraft.weightAndBalance(aircraft.fuelCalculation())

def weatherRelatedPrep():
    departureAirport = input("Enter departure airport: ")
    arrivalAirport = input("Enter arrival airport (leave blank for local flight): ")

    if arrivalAirport == "": weather = Weather(departureAirport, departureAirport)
    elif arrivalAirport != "": weather = Weather(departureAirport, arrivalAirport)
    weather.getMetarInfo()

planeRelatedPrep()
weatherRelatedPrep()

#Scrape METAR data (tbd) and if BKN or OVC are found (or other stuff) => weather warnings in red