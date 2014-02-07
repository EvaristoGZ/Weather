# -*- coding: utf-8 -*-
import json
print "Aplicación base || OpenWeatherMap"
print ""

prov = ['1. Almería', '2. Cádiz', '3. Córdoba', '4. Granada', '5. Huelva', '6. Jaén', '7. Málaga', '8. Sevilla']
for elemento in prov:
	print elemento

valor = (int(raw_input("\n¿De qué ciudad quieres saber la temperatura actual?\n"))-1)
provlimp = (prov[valor][3:])

print "\nLa temperatura actual de %s es la siguiente:\n" % (provlimp)