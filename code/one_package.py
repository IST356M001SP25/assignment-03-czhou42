'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import re

def parse_package_data(package_data):
    """Parses the package data string into structured information."""
    match = re.findall(r'(\d+)\s*(\w+)', package_data)
    package_info = {unit: int(quantity) for quantity, unit in match}
    return package_info

def calculate_total_size(package_info):
    """Calculates the total number of eggs based on the parsed package information."""
    if 'eggs' in package_info and 'cartons' in package_info:
        return package_info['eggs'] * package_info['cartons']
    return 0

st.title("Process One Package")
package_data = st.text_input("Enter package data:")

if package_data:
    package_info = parse_package_data(package_data)
    total_eggs = calculate_total_size(package_info)
    st.json(package_info)
    
    for key, value in package_info.items():
        st.info(f"{key} ➡ {value}")
    
    st.success(f"Total 📦 Size: {total_eggs} eggs")