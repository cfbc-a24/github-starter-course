'''
1. Complete the function `compute_matching`, which takes two lists of equal
length and returns a list of the same length where the `i`th element is True if
the `i`th elements of the two lists are equal.
'''

list_1=[10, 20, 30]
list_2=[10, 30, 30]

def compute_matching(lst1, lst2):
    match=[0]*len(lst1)
    for i in range(len(lst1)):
        if lst1[i]==lst2[i]:
            match[i]=True
        else:
                match[i]=False
    return match

compute_matching(list_1, list_2)







'''
2. Complete the function `compute_matching_indices`, which takes two lists of
equal length and returns a list of the indices where the elements of the two
lists are equal.
'''
list_1=[10, 20, 30]
list_2=[10, 30, 30]


def compute_matching_indices(lst1, lst2):
    where=[]
    for i in range(len(lst1)):
        if lst1[i]==lst2[i]:
          where.append(i)
    return(where)
    
compute_matching_indices(list_1, list_2)




'''
3. Write a python function `lowest_temperature(data, date)` that takes as an
argument a list of lists (of weather data -- as in the prompt on Canvas) and
returns the name of the city with the lowest temperature for the specified date.
'''

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




'''
4. Generalize the coin flip prompt covered in class
'''


def Inputs_Redundant():
    '''
    

    Returns the inputs that we need for the coin toss function
    -------
    consecutive_heads : the nummber of consecutive heads that you want
    before the counting stops (integer)
    n_trials : number of trials to arrive at the target of consecutive 
    heads (integer)
    seed : sets random seed for reproducibility (integer)

    '''
    consecutive_heads = int(input("How many Consecutive Heads? "))
    n_trials = int(input("How Many Trials? "))
    seed = int(input("What is the seed? "))
    return consecutive_heads, n_trials, seed




def Coin_Toss(weight):
    '''


    Parameters
    ----------
    weight : (float) a number from 0 to 1.000001 to give weight to the 
    coin. Since we have a random generator number from 0 to 1, if it
    is fair the head is simulated by the number being below 0.5
    If we want to increase the times that head appears we increase the
    number so that it is more likely that the random number will be below
    it. In the extreme case 1.000001 the random number is always below
    this number so it is always head and we would need just the
    consecutive_heads number of toss to get that number of consecutive_he

    Returns: the average number of flips that you need in order to get
    the desired consecutive heads. Average over the number of trials
    that you specified
    -------
    None.

    '''
    import random

    sim_results = []
    consecutive_heads, n_trials, seed = Inputs_Redundant()
    
    random.seed(seed)
    
    for i in range(n_trials):
        total_flips = 0
        current_heads = 0  
        target = consecutive_heads 
        
        while current_heads < target:
            # 1. Flip a coin
            flip = random.random()

            # 2a. If it's heads: increment consecutive_heads
            if flip < weight:  # Assuming weight is the probability of getting heads
                current_heads += 1
            # 2b. If it's tails: reset consecutive_heads to 0
            else:
                current_heads = 0

            # 3. Increment the total_flips after coin is flipped
            total_flips += 1

        sim_results.append(total_flips)

    avg = sum(sim_results) / len(sim_results)

    print(avg, "average total number of coin flips in order to get", target, "heads in a row.")


'''
Example with Fair coin, if it was an extreme unfair coin which returns
only head it would be 1.0000001 so it would always be below and so it would
always be head and we would need just 5 toss for Coin_Toss(1.00001)
'''

Coin_Toss(0.5)




