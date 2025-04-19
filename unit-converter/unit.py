import streamlit as st
from forex_python.converter import CurrencyRates

# Unit conversion dictionary
conversion_factors = {
    "Length": {
        "Metre": 1, "Kilometre": 0.001, "Centimetre": 100, "Millimetre": 1000,
        "Micrometre": 1e6, "Nanometre": 1e9, "Mile": 0.000621371, "Yard": 1.09361,
        "Foot": 3.28084, "Inch": 39.3701, "Nautical Mile": 0.000539957,
        "Furlong": 0.00497097, "Chain": 0.0497097, "Rod": 0.198839
    },
    "Temperature": {
        "Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15, "Rankine": 493.47
    },
    "Mass": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462,
        "Ounce": 35.274, "Ton (Metric)": 0.001, "Ton (US)": 0.000984207,
        "Stone": 0.157473, "Carat": 5000, "Grain": 15432.4
    },
    "Speed": {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694,
        "Knots": 1.94384, "Feet per second": 3.28084, "Mach (at sea level)": 0.00293858,
        "Speed of Light (in vacuum)": 3.33564e-9
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 0.000001, "Square Centimeter": 10000,
        "Square Millimeter": 1e6, "Square Mile": 3.861e-7, "Square Yard": 1.19599,
        "Square Foot": 10.7639, "Acre": 0.000247105, "Hectare": 0.0001
    },
    "Volume": {
        "Cubic Meter": 1, "Cubic Centimeter": 1e6, "Cubic Millimeter": 1e9,
        "Liter": 1000, "Milliliter": 1e6, "Gallon (US)": 264.172, "Gallon (UK)": 219.969,
        "Quart (US)": 1056.69, "Pint (US)": 2113.38, "Cup (US)": 4226.75,
        "Fluid Ounce (US)": 33814, "Tablespoon (US)": 67628, "Teaspoon (US)": 202884
    },
    "Energy": {
        "Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilocalorie": 0.000239006,
        "Watt Hour": 0.000277778, "Kilowatt Hour": 2.7778e-7, "Electronvolt": 6.242e+18,
        "British Thermal Unit (BTU)": 0.000947817, "Therm": 9.4804e-9
    },
    "Time": {
        "Second": 1, "Millisecond": 1000, "Microsecond": 1e6, "Nanosecond": 1e9,
        "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800,
        "Month (30 days)": 1/2.628e+6, "Year": 1/3.154e+7, "Decade": 1/3.154e+8,
        "Century": 1/3.154e+9
    },
    "Data Storage": {
        "Bit": 1, "Nibble": 0.25, "Byte": 1/8, "Kilobyte": 1/8192,
        "Megabyte": 1/8.389e+6, "Gigabyte": 1/8.59e+9, "Terabyte": 1/8.796e+12,
        "Petabyte": 1/9.007e+15, "Exabyte": 1/9.223e+18
    },
    "Currency": {
        "USD": 1, "EUR": 0.92, "GBP": 0.78, "INR": 83.23, "PKR": 278.12,
        "JPY": 151.25, "AUD": 1.55, "CAD": 1.35, "CHF": 0.91, "CNY": 7.14,
        "SAR": 3.75, "AED": 3.67, "TRY": 19.14
    }
}


# Streamlit UI
st.title("Unit Converter")

# Dropdown for category selection
category = st.selectbox("Select a category", list(conversion_factors.keys()))

# Dropdowns for unit selection
units = list(conversion_factors[category].keys())
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input field for value
value = st.number_input("Enter value", min_value=0.0, format="%f")

# Conversion logic
if st.button("Convert"):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        else:
            result = value
    else:
        result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    
    st.success(f"Converted value: {result} {to_unit}")
