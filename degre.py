# Programme qui convertit des °C en °F

# Demande à l'utilisateur d'entrer une température en degrés Celsius
degre_celcius = float(input ("Entrez des degrés Celsius : "))

# Convertit la température de Celsius en Fahrenheit en utilisant la formule de conversion
degre_fahrenheit = degre_celcius * 9/5 + 32 

# Affiche le résultat de la conversion
print(degre_celcius,"°C correspond à", degre_fahrenheit,"°F")
