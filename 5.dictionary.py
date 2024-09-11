# Q)Create a dictionary and apply the following methods
# 1.Print dictionary items
# 2.Access items
# 3.Use get() 
# 4.Change Value
# 5.use len()


#Create a dictionary
mydict ={
    "name": "john",
    "age": 30,
    "City":"New York"
}

#print dictionary items
print("Dictionary Items: ",mydict)

#Access items
name =mydict["name"]
age =mydict["age"]

print("Accessed items: ",name,age)

#use get() - the get() method returns the value of the item with the specified key

city=mydict.get("City:","Unknown")
country=mydict.get("Country","Not Specified")

print("City: ",city,"Country: ",country)

#Change Value
mydict["age"]=35
mydict["City"]="San Francisco"
print("Updated Dictionary: ",mydict)


#len() - the len() method returns the number of items in the dictionary
print("Length of Dictionary: ",len(mydict))