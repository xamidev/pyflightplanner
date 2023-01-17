from clint.textui import colored
import requests
from bs4 import BeautifulSoup

class Weather:
    
    def __init__(self, departureAirport, arrivalAirport):
        self.departureAirport = departureAirport
        self.arrivalAirport = arrivalAirport
    
    def getMetarInfo(self):
        departurePage = requests.get(f"https://metar-taf.com/{self.departureAirport}")
        departureSoup = BeautifulSoup(departurePage.content, 'html.parser')
        departureMetar = departureSoup.select('code')[0].text
        if self.departureAirport != self.arrivalAirport:
            arrivalPage = requests.get(f"https://metar-taf.com/{self.arrivalAirport}")
            arrivalSoup = BeautifulSoup(arrivalPage.content, 'html.parser')
            arrivalMetar = arrivalSoup.select('code')[0].text
            return departureMetar, arrivalMetar
        else: return departureMetar, departureMetar