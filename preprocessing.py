import pandas as pd



df = pd.read_csv("Hawthorn.csv")




remove_zero =df[(df.row_rank != 2) | (df.QT_VO != 0)]



groupedtime=remove_zero.groupby('QT_INTERVAL_COUNT')

validated_array = []
print(groupedtime)
# IF VALUE IN RANK = 2 , REMOVE ALL ROWS WITH 0 IN RANK 1
for QT_INTERVAL_COUNT, time_df in groupedtime:

    #for index, row in df.iterrows():

    for index,checkrank2 in time_df.iterrows():
        if(checkrank2.row_rank == 2):
            time_df = time_df[(time_df.row_rank == 1) & (time_df.QT_VO != checkrank2.QT_VO) | (time_df.row_rank == 2) ]


    #If value in rank 2 exists
    if ((time_df.row_rank == 2).any() & (time_df.QT_VO != 0).any()):
        # AND if its rank 1 and doesnt a value of 0
        time_df = time_df[(time_df.row_rank == 1) &  (time_df.QT_VO != 0) | (time_df.row_rank == 2)]
        validated_array.append(time_df)

        #print(time_df)
    else:
        validated_array.append(time_df)

    print(time_df)




groupedtime= pd.concat(validated_array)

groupedtime.to_csv('processed.csv', index=False)

print (time_df)

