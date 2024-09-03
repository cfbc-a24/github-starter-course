#Question 1

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