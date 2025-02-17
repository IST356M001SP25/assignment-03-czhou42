'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import json
import re

def parse_package_data(package_data):
    """Parses a single package data string into structured information."""
    match = re.findall(r'(\d+)\s*(\w+)', package_data)
    package_info = {unit: int(quantity) for quantity, unit in match}
    return package_info

def calculate_total_size(package_info):
    """Calculates the total package size based on the parsed package information."""
    values = list(package_info.values())
    return values[0] * values[1] if len(values) > 1 else values[0]

st.title("Process File of Packages")

uploaded_file = st.file_uploader("Upload package file:", type=["txt"])

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8").strip().split("\n")
    parsed_packages = []
    
    for line in file_contents:
        package_info = parse_package_data(line)
        total_size = calculate_total_size(package_info)
        parsed_packages.append({"package": package_info, "total_size": total_size})
        
        st.info(f"{line} ➡ Total 📦 Size: {total_size} {list(package_info.keys())[0]}")
    
    # Save as JSON
    output_filename = uploaded_file.name.replace(".txt", ".json")
    with open(output_filename, "w") as json_file:
        json.dump(parsed_packages, json_file, indent=4)
    
    st.success(f"{len(parsed_packages)} packages written to {output_filename}")
