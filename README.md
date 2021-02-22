# nytimes-covid-data-tool
A Python3 command line tool to explode the NYTimes covid-19-data into separate state and county csv files.

## Purpose
Since early in the covid-19 epidemic, I've been charting the daily new cases and new deaths in certain states and counties using spreadsheets in the Mac app Numbers. This tool, **state-county-bustout.py**, was created in early February 2021 because the county level csv file had gotten so big (>1M lines), Numbers couldn't load it all. So I wrote this little Python program to bust out the state level and county level csv data into separate files. 

## Functionality
When run, it parses the us-states.csv and us-counties.csv files in the covid-19-data-master directory which can be downloaded from the [NYTimes covid-19-data git repository](https://github.com/nytimes/covid-19-data).
It creates a directory tree under the working directory that looks like this:

```
your-working-directory/
    states/
        Alabama/
            Alabama-state.csv
            Autauga.csv
            Baldwin.csv
            Barbour.csv
            etc...
        Alaska/
            Alaska-state.csv
            Aleutians East Borough.csv
            Aleutians West Census Area.csv
            Anchorage.csv
            etc...for each county in the state
        etc... for each state or territory
```

Each time the program is run, each csv file (3330 of them) is overwritten, or created anew if necessary. So therefore, it is not recommended that you modify the generated csv files unless you plan to make copies, or move them somewhere other than the current working directory. Otherwise, your changes will be lost the next time the program is run. But if you create additional files in the states directory tree, they will retained. Knowing this, you can plan your work accordingly.

## System Requirements
Python 3 must be installed and on the command line path.

The script should run on any Mac running Catalina 10.15.7 and probably a lot of earlier MacOS releases that come with Python3 installed. The code uses literal slashes "/" as the file system path delimiters. Therefore it might need to be tweaked for Windows. If someone wants to undertake that, it would be appreciated as I don't do Windows.

## Using the program
1. In your working directory, put a copy of the Python source file **state-county-bustout.py**
2. Download the covid-19-data-master.zip file from the [NYTimes covid-19-data git repository](https://github.com/nytimes/covid-19-data) into your working directory
3. Unzip the file. It will create a directory **covid-19-data-master** containing the raw data.
4. In a command line window, run ```./state-county-bustout.py```

The program takes about 10 seconds to run on a 2013 iMac 3.5 GHz Quad-Core Intel Core i7 running Catalina, and generates output like this:
```
Josephs-iMac:COVID-19 joecascio$ ./state-county-bustout.py 
Parsing us-counties.csv...
Parsing us-states.csv...
Writing Washington
Writing Illinois
Writing California
Writing Arizona
Writing Massachusetts
Writing Wisconsin
Writing Texas
Writing Nebraska
Writing Utah
Writing Oregon
Writing Florida
Writing New York
Writing Rhode Island
Writing Georgia
Writing New Hampshire
Writing North Carolina
Writing New Jersey
Writing Colorado
Writing Maryland
Writing Nevada
Writing Tennessee
Writing Hawaii
Writing Indiana
Writing Kentucky
Writing Minnesota
Writing Oklahoma
Writing Pennsylvania
Writing South Carolina
Writing District of Columbia
Writing Kansas
Writing Missouri
Writing Vermont
Writing Virginia
Writing Connecticut
Writing Iowa
Writing Louisiana
Writing Ohio
Writing Michigan
Writing South Dakota
Writing Arkansas
Writing Delaware
Writing Mississippi
Writing New Mexico
Writing North Dakota
Writing Wyoming
Writing Alaska
Writing Maine
Writing Alabama
Writing Idaho
Writing Montana
Writing Puerto Rico
Writing Virgin Islands
Writing Guam
Writing West Virginia
Writing Northern Mariana Islands
Josephs-iMac:COVID-19 joecascio$
```


