'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
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

st.title("Process Package Files")

uploaded_files = st.file_uploader("Upload package files:", type=["txt"], accept_multiple_files=True)

total_files = 0
total_lines = 0

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_contents = uploaded_file.read().decode("utf-8").strip().split("\n")
        parsed_packages = []
        
        for line in file_contents:
            package_info = parse_package_data(line)
            total_size = calculate_total_size(package_info)
            parsed_packages.append({"package": package_info, "total_size": total_size})
        
        output_filename = uploaded_file.name.replace(".txt", ".json")
        with open(output_filename, "w") as json_file:
            json.dump(parsed_packages, json_file, indent=4)
        
        st.info(f"{len(parsed_packages)} packages written to {output_filename}")
        total_files += 1
        total_lines += len(file_contents)
    
    st.success(f"{total_files} files processed, {total_lines} total lines processed")
