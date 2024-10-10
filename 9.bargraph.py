#write a python profram to create bar graph for the given dataset
import matplotlib.pyplot as plt
import pandas as pd

#Let's Load the dataset (replace 'your_file.csv' with your dataset file)
data = pd.read_csv(r"C:\Users\hpsin\Downloads\Book1.csv")#now extracting data for the plot
car_brands = data['car_brand']
num_car_sold = data['num_cars_sold']

#creating a bar graph
plt.figure(figsize = (10, 6)) #adjust the size of the figure
plt.bar(car_brands, num_car_sold, color='skyblue')
plt.xlabel('Car brands')
plt.ylabel('Number of cars sold')
plt.title('Car sale by brands')
plt.xticks(rotation=90) #rotate the x-axis labels for better readability

#displaying the plot
plt.tight_layout()
plt.show()