"""
Class: CS230--Section HB3
Name: Eric Li
Data: earthquakes_us_20201123.csv
Description: This program will contains two queries. The first one will dedicate to show the relationship between the
            possible factors that may affect the magnitude: depth, type of earthquake, and magnitude type. The second
            one will present a overall map of the locations of the earthquake in the past two months.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
            URL: Will be updated later
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


filename = "earthquakes_us_20201123.csv"

colume_name = {
    "TYPE" : 'type',
    'MAG' : 'mag',
    "MAGTYPE" : 'magType',
    'DEPTH' : 'depth',
}

# Query 1 - part 1: frequency chart of each type of earthquake

def load_data():
    data = pd.read_csv(filename)
    return data

def frequency_chartT(data):
    mag = data.loc[:,[colume_name['TYPE'], colume_name['MAG']]]
    return px.scatter(mag, x =colume_name['TYPE'], y = colume_name['MAG'], color = colume_name['TYPE'])

def frequency_chartMT(data):
    magT = data.loc[:,[colume_name['MAGTYPE'], colume_name['MAG']]]
    return px.scatter(magT, x =colume_name['MAGTYPE'], y = colume_name['MAG'], color = colume_name['MAGTYPE'])


# Query 1 - part 2: relationship between depth and magnitude

def line_chart(data):
    depth = data.loc[:,[colume_name['DEPTH'], colume_name['MAG']]]
    return px.line(depth, x = colume_name['DEPTH'], y = colume_name['MAG'])


def main():
    st.title("Final Project")
    st.subheader("Frequency of each type pf earthquake")
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text("Finished loading data!")
    st.plotly_chart(frequency_chartT(data))

    st.subheader('Frequency of each type of magtype')
    st.plotly_chart(frequency_chartMT(data))

    st.subheader("Relationship between depth and magnitude")
    st.plotly_chart(line_chart(data))

main()

# Query 2 : map of location of earthquake
data = pd.read_csv(filename)
st.subheader("Map of earthquakes' location")
location = pd.DataFrame(data, columns = ["latitude","longitude"])
if st.checkbox("Show the latitude and longitude of earthquakes"):
    st.subheader("Location data")
    st.write(location)
st.write("Overview of location of earthquake in past two months")
st.map(location)
