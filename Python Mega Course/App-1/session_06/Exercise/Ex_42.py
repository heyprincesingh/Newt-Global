# Creating Multiple Text Files
# In the coding area, we have defined a list of countries. 
# Add some code that uses a for loop to generate a text file for each country (e.g., "Albania.txt", "Belgium.txt", and so on).

# Each file should have its country name as content (e.g., Albania.txt has Albania as content).

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for country in countries:
    file = open(f"{country}.txt", "w")
    file.write(country)
    file.close()