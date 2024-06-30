#Input:
#    arg 1: list of csv file names to be merged 
#    arg 2: file name of output file
# Output: outputfile with merged csv files 
#REFERENCES 
# https://saturncloud.io/blog/how-to-merge-two-csvs-using-pandas-in-python/
# https://www.freecodecamp.org/news/dataframe-to-csv-how-to-save-pandas-dataframes-by-exporting/#:~:text=to_csv()%20Method-,The%20.,format%20for%20storing%20tabular%20data.

import pandas as pd 
x=0
y=1

def mergecsv(listoffiles, outputfile):
    #merge dataframes so that keys merge
    while y <= len(listoffiles):
        #open dataframes from listoffiles
        df1=pd.read_csv(listoffiles[x])
        df2=pd.read_csv(listoffiles[y])
        merged_df = pd.merge(df1, df2, how='outer')
        x+=2
        y+=2

    #export dataframes to output file 
    merged_df.to_csv(outputfile, index=True)


mergecsv(["class1.csv","class2.csv"],"outputclass.csv")