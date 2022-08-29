from bs4 import BeautifulSoup
import time
import csv
import re


soup = BeautifulSoup(
    'https://www.hotelscombined.com/Hotel/Stay_Afrique_Hotel.htm', 'html.parser')

print(soup.prettify())
