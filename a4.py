'''
1. Given an integer variable `x`, write a conditional statement that will assign
to a variable `s` the string value `"POSITIVE"`, `"NEGATIVE"`, or `"ZERO"`
(depending on whether `x` is positive, negative, or zero, respectively). Assume
`x` has the value 2 for the purposes of this prompt (but also try plugging
in the values 0 and -1 for x, to ensure that your conditional statements are
written correctly).
'''

x=2
s="foo"

if x>0:
    s="POSITIVE"
else:
    if x==0:
        s="ZERO"
    else:
        if x<0:
            s="NEGATIVE"



'''
2. Given integer variables `lb`, `ub`, `p`, and `q`, write a loop that will
count how many numbers between `lb` and `ub` (inclusive) are divisible by both
`p` and `q`. For the purposes of this prompt, assume that `p` is 2 and `q` is 3.
Also assume that `lb` is 1 and `ub` is 20. Thus, your result should be 3
(because only 6, 12, and 18 are divisible by both 2 and 3).
'''

lb=1
ub=20
p=2
q=3

count=0

while lb<ub:
    if lb%2==0 and lb%3==0:
        count+=1
    if lb%2==0 and lb%3==0:    
        print (lb, "is divisible by", p, "and", q)
    lb+=1
print(count, "numbers are divisible by", p, "and", q)








'''
3. Given a list of integers `lst`, write a loop to count the number of negative
numbers in the list. Assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt. Thus, your result should be 2 (because only -1 and -3
are negative numbers).
'''

lst=[-1, 2, -3, 4, 0]
countneg=0

for i in lst:
   if i<0:
      countneg+=1
print(countneg)




'''
4. Write a loop to compute a variable `all_pos` that has the value `True` if
all of the elements in a list of integers `lst` are positive and `False`
otherwise. Again, assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt.
'''


lst=[-1, 2, -3, 4, 0]
allpos=[]
check=[]


for i in lst:
    if i>0:
        check.append("True")
    else:
        check.append("False")
        
        
for i in check:
    if i=="False":
       allpos=[False]
    else:
       allpos=[True]
allpos




'''
5. Given a list of keys and a list of values, use a loop to construct a
dictionary that maps the ith key in the list of keys to the ith value in the
list of values. For the purposes of this prompt, assume that the list of keys
is `["x", "y", "z"]` and the list of values is `[10, 20, 30]`.
'''


kyuss=["x", "y", "z"]
valu=[10, 20, 30]


dictio={}

for i in range(len(kyuss)):
    dictio[kyuss[i]] = valu[i]
    
dictio





'''
6. Compute the most frequently occuring categorical label for the region
depicted in the satellite images provided (see description in prompt on Canvas).
'''

band_red = [[1, 10, 255],
            [200, 155, 20],
            [30, 20, 10]]
band_nir = [[1, 20, 255],
            [10, 20, 30],
            [200, 155, 20]]


redimage=[]
nirimage=[]

for pixred in range(len(band_red)):
   for pixredsingle in band_red[pixred]:
       redimage.append(pixredsingle)
                
for pixnir in range(len(band_nir)):
 for pixnirsingle in band_nir[pixnir]:
  nirimage.append(pixnirsingle)


NDVIminus=[]

for i in range(len(redimage)):
    NDVIminus.append(nirimage[i]-redimage[i])


NDVIplus=[]

for i in range(len(redimage)):
    NDVIplus.append(nirimage[i]+redimage[i])


NDVI=[]

for i in range(len(NDVIminus)):
    NDVI.append(NDVIminus[i] / NDVIplus[i])



Types={"flooded":0, "barren":0, "vegetation-rich":0,}
for i in range(len(NDVI)):
    if -1 <= NDVI[i] <= -0.25:
        Types["flooded"]+=1
    elif -0.25 < NDVI[i]<=0.25:
        Types["barren"]+= 1 
    elif 0.25 < NDVI[i] <=1.0 :
        Types["vegetation-rich"]+= 1


MostLikelyLabel="foo"

if Types["flooded"]>Types["barren"] and Types["flooded"]>Types["vegetation-rich"]:
   MostLikelyLabel="flooded" 
elif Types["barren"]>Types["flooded"] and Types["barren"]>Types["vegetation-rich"]:
        MostLikelyLabel="barren"
elif Types["vegetation-rich"]>Types["flooded"]  and Types["vegetation-rich"]>Types["barren"]:
       MostLikelyLabel=["vegetation-rich"]
      

print(MostLikelyLabel)



'''
7. Read in any files named `band_nir.csv` and `band_red.csv` as lists of lists
and print out the highest frequency label for the corresponding region.
'''

import csv
band_nir= []
with open("band_nir.csv") as f:
     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
     for pixel in reader:
         band_nir.append(pixel)
band_nir



import csv
band_red= []
with open("band_red.csv") as f:
     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
     for pixel in reader:
         band_red.append(pixel)
band_red


redimage=[]
for pixred in range(len(band_red)):
   for pixredsingle in band_red[pixred]:
       redimage.append(pixredsingle)
       
print(max(redimage))


nirimage=[]
for pixnir in range(len(band_nir)):
 for pixnirsingle in band_nir[pixnir]:
  nirimage.append(pixnirsingle)

print(max(nirimage))




