#Question 2

list_1=[10, 20, 30]
list_2=[10, 30, 30]


def compute_matching_indices(lst1, lst2):
    where=[]
    for i in range(len(lst1)):
        if lst1[i]==lst2[i]:
          where.append(i)
    return(where)
    
compute_matching_indices(list_1, list_2)



