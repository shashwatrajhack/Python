#if else statement in python

is_male = False
is_tall = False 

if is_male and is_tall:
    print("you are a tall male")

elif is_male and not(is_tall):
    print("you are a short man")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male and not tall")        
