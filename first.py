#import statement   https://pandas.pydata.org/pandas-docs/stable/dsintro.html
import pandas as pd

#loading dataset, read more at http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table 

df = pd.read_csv("iris.data")

#by default header is first row

#df = pd.read_csv("iris.data", sep=",", names=["petal_length","petal_width","sepal_length", "sepal_width", "category"])

#size of df
df.shape()
df.head()
#df.tail(3)

'''
Entire table is a data frame and 
The basics of indexing are as follows:

Operation	                        Syntax	        Result
Select column	                    df[col]	        Series
Select row by label	                df.loc[label]	Series
Select row by integer location	    df.iloc[loc]	Series
Slice rows	                        df[5:10]	    DataFrame
Select rows by boolean vector	    df[bool_vec]	DataFrame
'''
#frame[colname]
#df.frame["category"]

#Acess particular element :df.loc[row_indexer,column_indexer]
#df.loc[123,"petal_length"]
#df.loc[123,"petal_length"] = <value of appropriate dtype>


#assign always returns a copy of the data, leaving the original DataFrame untouched.
#df.assign(sepal_ratio = df['sepal_width'] / df['sepal_length']).head())
'''
Simple python programming constructs:

FOR loop:

for item in sequence:
        # commands
else:
        #commands
        
example:

word = "Hello"
for character in word:
        print(character)


While loop:

while (condition):
        # commands
else:
        # commands

example:

i = 0
while (i < 3):
        print("Knock")
        i += 1
print("Penny!")



if-else in python

example:
option = int(input(""))

if (option == 1):
        result = a + b
elif (option == 2):
        result = a - b
elif (option == 3):
        result = a * b
elif (option == 4):
        result = a / b
if option > 0 and option < 5:
        print("result: %f" % (result))
else:
        print("Invalid option")
print("Thank you for using our calculator.")



'''
 









