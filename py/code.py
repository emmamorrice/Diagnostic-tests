##importing libraries needed
import pandas as pd

##all sources from https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data

##identifying sources
##schema= pd.read_csv("https://github.com/emmamorrice/Diagnostic-tests/raw/main/stats19_schema%20(1).csv")
##schema_pivoted= pd.read_csv("https://github.com/emmamorrice/Diagnostic-tests/raw/main/Schema%20with%20codes%20csv.csv")
##accidents
dfcollisions = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-collision-1979-latest-published-year.csv", low_memory=False, error_bad_lines=False)
##vehicles
dfvehicles = pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-vehicle-1979-latest-published-year.csv", low_memory=False, error_bad_lines=False)
##casualties
dfcasualties= pd.read_csv("https://data.dft.gov.uk/road-accidents-safety-data/dft-road-casualty-statistics-casualty-1979-latest-published-year.csv", low_memory=False, error_bad_lines=False)

##dropping columns that aren't going to be needed
dfcollisionsedited= dfcollisions.drop(columns=['accident_index', 'police_force', 'local_authority_ons_district', 'local_authority_highway', 'junction_control', 'second_road_class', 'second_road_number', 'pedestrian_crossing_human_control', 'pedestrian_crossing_physical_facilities', 'urban_or_rural_area', 'trunk_road_flag', 'lsoa_of_accident_location'])
dfvehiclesedited= dfvehicles.drop(columns=['accident_index', 'vehicle_reference', 'vehicle_direction_from', 'vehicle_direction_to', 'vehicle_location_restricted_lane', 'journey_purpose_of_driver', 'propulsion_code', 'driver_imd_decile', 'driver_home_area_type', 'lsoa_of_driver'])
dfcasualtiesedited= dfcasualties.drop(columns=['accident_index', 'vehicle_reference', 'casualty_reference', 'casualty_home_area_type', 'casualty_imd_decile', 'lsoa_of_casualty'])


##mergecolumns
merge1= pd.merge(dfcollisionsedited, dfvehiclesedited, how='outer')
merge2= pd.merge(merge1, dfcasualtiesedited, how='outer')

##Schema for columns to change them from codes to more detailed descriptions
##police force
police_force= pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vR33WpF01r3XMwvfutHsFI5UTbJF41XthCioWIWcDtAJE_TckGKnOUkn1P1Eip4HPrTL2CqyleEXv7T/pub?gid=0&single=true&output=csv")

#merging all of the schema
merge_police_force= pd.merge(merge2, police_force, how='outer')

##filtering the first road class column to show A only - code taken from schema document
##accidents= merge2[merge2['first_road_class']=='3']
##accidents2=accidents[accidents['first_road_number']=='9']
##A92022= accidents2[accidents2['accident_year']== '2022']

##save csv
merge2.to_csv(r'data/A9fullspreadsheet.csv')
