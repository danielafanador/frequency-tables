# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

frequency_table = {}

def freq_table (any_list):
    
    for element in any_list:
        
        if element in frequency_table:    
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1
    
    return frequency_table
    
#frequency_table = freq_table (genres)

#print (genres)

genres_ft = freq_table (genres)

print (genres_ft)