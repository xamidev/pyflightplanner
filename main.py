from clint.textui import colored
from plane import Plane
from weather import Weather

def planeRelatedPrep():
    print("\n*******************\n* PyFlightPlanner *\n*******************")
    print("\n\tAvailable Planes\n\t[1] SportStar RTC\n\t[2] Robin DR400/120\n")
    plane = int(input("Enter plane number: "))
    crewWeight = float(input("Crew weight: "))
    luggageWeight = float(input("Luggage weight: "))
    global departureAirport, arrivalAirport
    departureAirport = input("Enter departure airport: ")
    arrivalAirport = input("Enter arrival airport (leave blank for local flight): ")
    # Plane definitions
    if plane==1: aircraft = Plane("SportStar RTC", 19, 0.7, 124, 144, 353, 0.249, crewWeight, 0.545, luggageWeight, 1.083, 0, 0.680, 600, 1.25, 19.95)
    elif plane==2: aircraft = Plane("Robin DR400/120", 25, 0.6, 158, 178, 575, 0.385, crewWeight, 0.41, luggageWeight, 1.9, 0, 1.12, 900, 0.385, 19.95)
    aircraft.weightAndBalance(aircraft.fuelCalculation())

def weatherRelatedPrep():
    if arrivalAirport == "": weather = Weather(departureAirport, departureAirport)
    elif arrivalAirport != "": weather = Weather(departureAirport, arrivalAirport)
    depMetar, arrMetar = weather.getMetarInfo()
    metars = []
    metars.append(depMetar)
    metars.append(arrMetar)
    if metars[0] == metars[1]: metars.pop(1)
    for metar in metars:
        # local flight
        forecastHour = metar[metar.find("Z")-4:metar.find("Z")-2]
        forecastMinute = metar[metar.find("Z")-2:metar.find("Z")]
        actualAirport = metar[metar.find("METAR")+6:metar.find("METAR")+10]
        print(f"\nCurrent weather forecast for {colored.green(actualAirport)} | Done today at {forecastHour}:{forecastMinute} UTC")
        windForce = metar[metar.find("KT")-2:metar.find("KT")]
        windDirection = metar[metar.find("KT")-5:metar.find("KT")-2]
        qnh = metar[metar.find("Q")+1:metar.find("Q")+5]
        if qnh[0] == "0": qnh = qnh[1:]
        temperature = metar[metar.find("/")-2:metar.find("/")]
        dewPoint = metar[metar.find("/")+1:metar.find("/")+3]
        if temperature[0] == "0": temperature = temperature[1:]
        if dewPoint[0] == "0": dewPoint = dewPoint[1:]
        if abs(int(temperature)-int(dewPoint))>5:
            air = colored.yellow("Dry")
        else: air = colored.magenta("Wet")
        print(f"Wind is {windDirection}° {windForce} knots | QNH: {qnh} hPa | Temperature: {temperature}°C | Dew point: {dewPoint}°C | Air is {air}")
        print(f"Raw data: {metar}")

# tbd: price calculation

planeRelatedPrep()
weatherRelatedPrep()