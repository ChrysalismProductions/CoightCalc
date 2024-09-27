import streamlit as st

st.set_page_config(
    page_title="CoightCalc",
    page_icon="🤠"
)

#31333F

##st.markdown(
##    """
##    <style>
##    .stApp {
##        background-image: url('https://awol.com.au/wp-content/uploads/2020/03/russell-coight-all-aussie-adventures-1024x640.jpg');
##        background-position: left;
##        background-repeat: repeat;
##    }
##    </style>
##    """,
##    unsafe_allow_html=True
##)

st.markdown("<h1 style='text-align: center;'>Russell Coight's Water Calculator</h1>", unsafe_allow_html=True)

st.image('background2.jpg', use_column_width="always")

st.markdown("""
> “I never go into the outback without a decent supply of water, and the general rule for how much you'll need is three litres per day, per person, per man, per degree over 25 degrees celcius, per kilometre if walking on foot, in the winter months dividing it by two, plus... another litre... at the end.”
> 
> — Russell Coight
""")

#How many days?
days = st.number_input("Days :calendar:", min_value=1, max_value=100, value=1, step=1)

#How many people?
people = st.number_input("People 🧑", min_value=1, max_value=100, value=1, step=1)

#How many men?
men_factor = 0

if people > 0:
    men = st.number_input("Men :man:", min_value=0, max_value=people, value=0, step=1)
    men_factor = men
    

#Temperature?
temp_factor = 0

temp = st.number_input("Temperature :thermometer:", min_value=-10, max_value=60, value=25, step=1)

if temp > 25:
    temp_factor = temp - 25

#On foot? How many KM

on_foot_factor = 0

on_foot = st.checkbox("Walking? 🚶")

if on_foot:
    kilometres = st.number_input("Kilometres on foot 👣", min_value=0.0, max_value=50.0, value=0.0, step=0.5, format="%0.1f")
    on_foot_factor = kilometres
    

#Winter?

season = st.radio("Season", ["Summer 🌞", "Autumn 🍂", "Winter ⛄", "Spring 🌱"])

if season == "Winter ⛄":
    val = 1.5
else:
    val = 3

water = (val * days) + (val * people) + (val * men_factor) + (val * temp_factor) + (val * on_foot_factor) + 1

st.subheader(f"You'll need {int(water)}L for your next All Aussie Adventure* 🤠")
st.write("*Please don't take this seriously :^)")
