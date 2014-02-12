# -*- coding: utf-8 -*-
import json
import requests
print "Aplicación base || OpenWeatherMap"
print ""

prov = ['1. Almería', '2. Cádiz', '3. Córdoba', '4. Granada', '5. Huelva', '6. Jaén', '7. Málaga', '8. Sevilla']
for elemento in prov:
	print elemento

valor = (int(raw_input("\n¿De qué ciudad quieres saber la temperatura actual?\n"))-1)
provlimp = (prov[valor][3:]) # Elimina la numeración de la provincia #

datos = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % provlimp})

valores = json.loads(datos.text) # Carga los datos en un diccionario json #
temperatura = valores['main']['temp']
temperatura = round(temperatura - 273,1)

print "\nLa temperatura actual de %s %sºC\n" % (provlimp,temperatura)