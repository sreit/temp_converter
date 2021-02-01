# temp_converter
### Converts Fahrenheit, Celsius and Kelvin temperatures 

This program's main purpose is to convert temperatures among Fahrenheit, Celsius and Kelvin.


It prompts the user for a starting degree and unit, as well as to which unit the user would like to convert.
Then it will make the calculations for the conversion and display the new temperature. The program runs in the command line.


This program contain several security measures:
- Repromt the user for a starting temperature until it is an integer or float
- Repromt both the start and end unit until receives the correct format of "F", "C" or "K"
  - Covert text to uppercase
- Display error message if unable to complete conversion
