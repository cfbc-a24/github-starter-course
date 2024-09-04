ledger = [("Huff", 10),
          ("Griff", 50),
          ("RC", 40),
          ("Huff", 90),
          ("Sly", -10),
          ("Griff", 100),
          ("Griff", -60),
          ("RC", 80),
          ("Griff", 50)]


def champions(ledger, threshold, num_champs):
    '''
    Computes the first num_champs houses to reach a score
    of at least threshold.

    Inputs:
        ledger: a list of scoring events, where each scoring
            event is a (string, integer) pair consisting of
            the name of the house and the number of points
            that is added to that house's score (which may
            be negative).
        threshold: (positive integer) a house has completed
            the house cup when they meet or exceed this score.
        num_champs: (positive integer) The maximum number
            of houses to include in the list of champions
    
    Returns: (list of strings) A list of the first num_champs
        houses to complete the house cup, in order.
    '''
    winners=[]
    howmany=[0]
    houses={}

    for i in range(len(ledger)):
     houses[ledger[i][0]]=houses.get(ledger[i][0],0)+ledger[i][1]
     if ledger[i][0] in houses and houses[ledger[i][0]]>=threshold:
                winners.append(ledger[i][0])
                howmany[0]=howmany[0]+1
                del houses[ledger[i][0]]
     if howmany[0]>=num_champs:
                break
    
    
    return winners        
        
        
champions(ledger, 100, 6)  

  
champions(ledger, 100, 2)       
   
