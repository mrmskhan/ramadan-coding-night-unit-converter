import streamlit as st # streamlit is a library for building web apps

# function to convert unit based on predefined conversions factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000  # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input or output

    # logic to convert units
    if key in conversions:
        conversion_factor = conversions[key]  # variable name
        return value * conversion_factor
    else:
        return "Conversion not supported" # return a massage if the conversion is npt support

# Streamlit UI components 
st.title("Unit Converter(Created by M.Saleem Khan)") #set the title of the web app

# user input: numerical value to convert
value = st.number_input("Enter the value:")

# dropdown to select unit to convert to
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# button to trigger the convertion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"Converted value: {result}") # display the result
