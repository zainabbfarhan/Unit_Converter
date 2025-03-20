import streamlit as st #f0f2f6
st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    color: white;
}
    .stApp {
        background:linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
    }
            
    h1{
        text-align: center;
        font-size: 36px;
        color: #ffffff;
        }
            
    .stButton>button{
        background:liner-gradient(45deg,rgb(148, 11,132), #351c75);
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border:none;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px  5px 15px rgba(0, 201, 255, 0.4);
        }
            
        .stButton>button:hover{
        transform: scale(1.05);
        background:linear-gradient(45deg, #92fe9d, #00c9ff);
        color: #000000;
        }
        
        .result-box{
        font-size: 20px;
        font-weight:bold;
        text-align: center;
        background:linear-gradient(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
        }

    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #000000; 
        }    
</style>
""", unsafe_allow_html=True)

st.title("Unit Converter")

# Title and description
st.markdown("<h1> Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("This is a simple unit converter application. It allows you to convert various units of measurement.")

#sidebar menu

conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature",])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1 , col2 = st.columns(2)

#length conversion
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Milimeters" ,"Miles", "Yards", "Feet"])

    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Milimeters" ,"Miles", "Yards", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])

    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


#Converted Function
def convert_length(value, from_unit, to_unit):
    length_units={
        'Meters': 1,
        'Kilometers': 0.001,
        'Centimeters': 100,
        'Milimeters': 1000,
        'Miles': 0.000621371,
        'Yards': 1.09361 ,
        'Feet': 3.28
    }

    return(value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units={
        'Kilograms': 1,
        'Grams': 1000,
        'Milligrams': 1000000,
        'Pounds': 2.2046,
        'Ounces': 35.27
    }
    return(value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
       return(value*9/5+32)if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value 

    elif from_unit == "Fahrenheit":
        return(value-32)*5/9 if to_unit == "Celsius" else (value-32)*5/9+273.15 if to_unit == "Kelvin" else value

    elif from_unit =="Kelvin":
        return(value-273.15) if to_unit == "Celsius" else (value -273.15)*9/5+32 if to_unit == "Fahrenheit" else value
    return value 

#Button for conversion

if st.button("Convert"):
  if conversion_type == "Length":
    result = convert_length(value, from_unit, to_unit)

  elif conversion_type == "Weight":
    result = weight_converter(value, from_unit, to_unit)

  elif conversion_type == "Temperature":
    result = temperature_converter(value, from_unit, to_unit)

  st.markdown(f"<div class='result-box'>{value}{from_unit} = {result:.4f}{to_unit}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='footer'>Developed by ZAINAB FARHAN</div>", unsafe_allow_html=True)
