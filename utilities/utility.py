import numpy as np
import pandas as pd
	
region_lat_long_mean_df = pd.read_csv('data/region_lat_long_mean.csv',index_col=0)
region_median_df = pd.read_csv('data/region_median.csv',index_col=0)
state_median_df = pd.read_csv('data/state_median.csv',index_col=0)


def region_lat_long(region):
	latitude = region_lat_long_mean_df.loc[region]['lat']
	longitude = region_lat_long_mean_df.loc[region]['long']

	return latitude,longitude

def region_median_fun(region):
	region_median = region_median_df.loc[region]['region_median']
	return region_median

def state_median_fun(state):
	state_median = state_median_df.loc[state]['state_median']
	return state_median

def house(data):
	house_type = {
		'apartment' :0,
		'condo' : 0,
		'cottage/cabin' : 0,
		'duplex' :0,
		'flat' : 0,
		'house' : 0,
		'in-law' : 0,
		'land' : 0,
		'loft' : 0,
		'manufactured' : 0,
		'townhouse' : 0
		}
	

	if data in house_type.keys():
	  house_type[data]=1 

	return list(house_type.values())


def laundry_option(data):
	laundry_option = {
		'laundry in bldg' :0,
		'laundry on site' :0,
		'no laundry on site' : 0,
		'w/d hookups' : 0,
		'w/d in unit' :0	
		}


	if data in laundry_option.keys():
	  laundry_option[data]=1 

	return list(laundry_option.values())


def parking_option(data):
	parking_option = {
		'attached garage' :0,
		'carport' :0,
		'detached garage' : 0,
		'no parking' : 0,
		'off-street parking' :0,	
		'street parking' : 0,
		'valet parking' :0,
		}


	if data in parking_option.keys():
	  parking_option[data]=1 

	return list(parking_option.values())