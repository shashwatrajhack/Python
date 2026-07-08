

#Loops in python



i = 0;
while(i<=10):
    print(i)
    i+=1

print("loop end");

collections = ["Apple","Grapes","Banana"]

for el in collections:
    print(el)


for  el in collections:
    if(el == "Mango"):
        print("Mango found")
        break
    print(el)

#range(start,stop,step) using for loop
for el in range(2,21,3):
    print(el)

#sum of n numbers by for loop

i = 0;
sum = 0;

while(i<=10):
    sum +=i;
    i+=1
    
print("sum:",sum);

#factorial by for loop
i = 6;

fact = 1;

for el in range(1,i+1):
    fact = fact*el
    el += 1

print(fact);


#factorial by while loop
i = 6

fact = 1

while(i>0):
    fact *= i
    i -=1

print(fact)
