Raw_Temp = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
            ["20081114", "Detroit", "45.2", "30.3", "33.4"]]

def lowest_temperature(data, date):
    '''
    This function takes a date as input (always [0] in the data list) 
    and returns the lowest temperature for that city (chooses between[3],
    the lowest temperatures for that day)
    '''
    '''
    Parameters
    ----------
    data : list of list with day, city, highest, lowest and average temp
    date : date of the measurement

    Returns: lowest temperature
    '''
    filtered_data = [(record[1], float(record[3])) for record in data if record[0] == date]
    if not filtered_data:
        return None
    City, Temp = min(filtered_data, key=lambda x: x[1])
                 
    print("In ", City, "on ", date, 
          "it has been registered a minimum temperature of ", Temp)       

    return City

lowest_temperature(Raw_Temp, "20081114")


#they fail only because they return a string instead of a list with a string inside but the city is right