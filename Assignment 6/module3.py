
#Question 3

Raw_Temp=[["20081114", "Chicago", "50.1", "30.0", "35.7"],
 ["20081114", "Detroit", "45.2", "30.3", "33.4"]]


def lowest_temperature(data, date):
    '''
    This function takes a date as input (always [0] in the data list) 
    and returns the lowest temperature for that city (choses between[3],
    the lowest temperatures for that day)
    '''
    '''
    Parameters
    ----------
    data : list of list with day, city, highest, lowest and average temp
    date : date of the measurement

    Returns: lowest temperature

    '''
    City=["foo"]
    Temp=[2000]
    for i in range(len(Raw_Temp)):
     if Raw_Temp[i][0]==date:
        for i in range(len(Raw_Temp)):
             if float(Raw_Temp[i][3])<float(Temp[0]):
                 Temp=Raw_Temp[i][3]
                 City=[Raw_Temp[i][1]]
                 
       
    print("In ", City, "on ", date, 
          "it has been registered a minimum temperature of ", Temp)       

                 
    return(City)


        

lowest_temperature(Raw_Temp, "20081114")      


