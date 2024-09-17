import pandas as pd

#replace 'your_file.csv' with the actual path to your csv file
file_path = 'C:\Program Files\Spyder\pkgs\pandas\Book2.csv'

#Read the csv file into a pandas dataframe
df = pd.read_csv(file_path)

#print the first 5 lines (+header) of the csv file
print("first 5 lines of the csv file")
print(df.head(5))

#print the last 5 lines (+header) of the csv file
print("last 5 lines of the csv file")
print(df.tail(5))
