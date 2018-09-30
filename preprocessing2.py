import pandas as pd


#Processing Initial CSV File
df = pd.read_csv("TrafficData2.csv")
# Remove Initial Column : Redundant
df = df.drop(columns=['Unnamed: 0'])


# Create list of times of 15 min increments
timecolumn=pd.date_range("00:00", "23:45", freq="15min").time

#rename the columns V00 - V95 to the 15 min increments
df.rename(columns=dict(zip(df.columns[5:], timecolumn)),inplace=True)

# Only Get a Single Intersection
trafficnode = df[(df.ds_location == "LATROBE  ST SW OF VICTORIA ST") & (df.lane_mvt =="LEFT AND THRU")]
# reset the index increments
trafficnode=trafficnode.reset_index(drop=True)



trafficnode.to_csv('processed2.csv', index=False)



print(timecolumn)


