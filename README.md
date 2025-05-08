# Mothitor Light - CSC 230 Final Project

## The purpose of our project

This project was designed for Professor Abarca, and the Insect Ecology Lab at Smith College. One of the lab's current projects, the Mothitor, is a non-lethal moth monitoring device that attracts insects to a lit-up wooden panel and takes pictures of them using a RaspberryPi. The Mothitor collects data at night, from 9pm to 12am, from roughly April to September. Because the Mothitor function by using a light trap, the data collected is impacted by the overall amount of light around. For example, a significantly lower amount of moth will be captured during a full moon. 

For this purpose, Skye Weaver-Worster 25J', worked to implement a data transfer system to collect SQM (Sky Quality Meter) measurements in the MacLeish Field station (where the Mothitor instances are situated) and send the data back to Smith using a Raspberry Pi.

Our project enables a more accessible usage of that data, and adds additional information. Indeed, including moon phase data was a requirement for our stakeholder, Professor Abarca. Because accessibility was our main focus, we focused on using a restricted amount of tools to harmonize the data. We also made it into a .cvs format, prefered by ou stakeholder. Furthermore, to ease future data analysis in Professor Abarca's classes and lab, we incorporated an R package, [MothitR](https://github.com/CDarling25/mothitoR), to summarize and visualize the data.

You can also find an overview of our different approaches to this project in [this presentation](https://docs.google.com/presentation/d/10UENs4Snu6hpDb2WjVCBXUIZV9QgE7sOm1h-WBfR50c/edit?slide=id.p#slide=id.p).

## Included Files

### 'Mothitor Join.qmd'

Takes in a manually input (in R) csv of Mothitor light sensor data and joins it to the moon phase data based on date.

### 'convert.py'

`python3 convert.py [file_name]`

Takes in a user-input Mothitor light sensor .dat file and converts it to a .csv.

### 'convert_and_moon.py'

`python3 convert_and_moon.py [file_name]`

Takes in a user-input Mothitor light sensor .dat file, converts it to a .csv, and joins the moon phase data to it.

### 'moon_light_join.sql'

Sample code that creates databases for the Mothitor light data and moon phase data, and joins them together in a SQL environment.

### 'moon_phases.csv'

A .csv file of moon phase data.

## Our MothitoR R package

This R package contains data summary functions for light and moon data: https://github.com/CDarling25/mothitoR

## How to set up and run the project

Instructions for the MothitR R package can be found in the MothitR's README.

To set up this project, clone this repository and run 'convert.py' or 'convert_and_moon.py' depending on desired output. In the command line, input the filename for the file to be processed.

Presentation Link: https://docs.google.com/presentation/d/10UENs4Snu6hpDb2WjVCBXUIZV9QgE7sOm1h-WBfR50c/edit?usp=sharing
