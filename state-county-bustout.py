#!/usr/bin/python3
# Author: Joe Cascio, Jr.
# email: joe.cascio.jr@gmail.com
# Licensed under GNU GPL v3 (no closed source distributions)
# May need some tweaking for Windows file path delimiters.
# Execute in the same directory that holds the covid-19-data-master directory.
# System requirements: MacOS with Python3 installed and on the command line path
# If you want, put the source file on the Python3 path. But, whatevs.
# Run it like this:
# Command-prompt-$ ./state-county-bustout.py
# working directory->./
#   state-county-bustout.py
#   covid-data-master/
#       # nytimes-generated files
#       us-states.csv
#       us-counties.csv
# tool creates this directory in the working directory
# states/
#     Alabama/
#       Alabama-state.csv  # split out state-level data from us-states.csv
#       Autauga.csv  # split out state-county level data from us-counties.csv
#       Baldwin.csv
#       etc.
#     Alaska/ 
#     etc./
import csv
import os

print("Parsing us-counties.csv...")
csvfile = open('./covid-19-data-master/us-counties.csv', 'r')
# csvfile = open('./covid-19-data-master/counties-test.csv', 'r')
fieldnames = ("date","county", "state","fips", "cases", "deaths")
reader = csv.DictReader(csvfile, fieldnames, delimiter=',')

states = {}

# Bust out counties first
first_row = True
for county_row in reader:
    if first_row:
        first_row = False
        county_file_row_zero = "date,county,state,fips,cases,deaths\n"
    else:
        state_name = county_row["state"]
        county_name = county_row["county"]
        county_row_array = None
        state_dict_of_counties = None
        if state_name not in states:
            # if the state hasn't been seen yet, create it, and an empty county_dict 
            states[state_name] = {}
            state_dict_of_counties = {}
            states[state_name] = state_dict_of_counties
            county_row_array = []
            state_dict_of_counties[county_name] = county_row_array
        else:
            # the state entry exists, and has at least an empty dict of counties
            state_dict_of_counties = states[state_name]
        # Now you have a state_dict_of_counties, one way or other
        if county_name not in state_dict_of_counties:
            # it hasn't been, so create it
            county_row_array = []
            state_dict_of_counties[county_name] = county_row_array
        else:
            # it does already exist so get it
            county_row_array = state_dict_of_counties[county_name]

        # when you get here you have a county_row_array one way or another
        # so just append the row we got from the csv file
        county_row_array.append(county_row)
        
csvfile.close()

# Now the us-states file
print("Parsing us-states.csv...")

csvfile = open('./covid-19-data-master/us-states.csv', 'r')
fieldnames = ("date", "state","fips", "cases", "deaths")
state_reader = csv.DictReader(csvfile, fieldnames, delimiter=',')

first_row = True
states_dict = {}
for state_row in state_reader:
    if first_row:
        first_row = False
        state_file_row_zero = "date,state,fips,cases,deaths\n"
    else:
        state_array = None
        state_name = state_row["state"]
#         print "found %s in states file" % (state_name)
        if state_name not in states_dict:
            state_array = []
            states_dict[state_name] = state_array
        else:
            state_array = states_dict[state_name]
        # now you have a state row array
        state_array.append(state_row)
        
csvfile.close()
        
# Now all the rows have been accounted for. 
# Create the state directories, and under them, the county csv files
# that contain the county row arrays
for state_name in states_dict:
    state_dir_path = "./states/%s" % (state_name)
    if not os.path.exists(state_dir_path):
        os.makedirs(state_dir_path)
    print ("Writing %s" % (state_name))
    
    # first write out the state's combined csv file
    state_csv_file_path = "./states/%s/%s-state.csv" % (state_name, state_name)
    state_csv_file = open(state_csv_file_path, "w")
    state_csv_file.write(state_file_row_zero)
    state_array = states_dict[state_name]
    for srow in state_array:
        state_csv_file.write("%s,%s,%s,%s,%s\n" % (srow["date"],srow["state"], srow["fips"], srow["cases"], srow["deaths"]))
    state_csv_file.close()

    # now the county csv files
    for county_name in states[state_name]:
        county_file_path = "./states/%s/%s.csv" % (state_name, county_name)
#         print "writing %s/%s" % (state_name, county_name)
        # open the county csv file for write
        county_file = open(county_file_path, 'w')
        county_file.write(county_file_row_zero)
        for row in states[state_name][county_name]:
            county_file.write("%s,%s,%s,%s,%s,%s\n" % (row["date"], row["county"], row["state"], row["fips"], row["cases"], row["deaths"]))
        county_file.close()
