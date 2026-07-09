# with open("practice.txt", "w") as f:
#     f.write("I am Python file handling.\n from apna college.\n i am learning python for machine learning and data science.");
#     f.write("Using java and c++ is also important for programming.\njava is a good programming language.\n java is a programming language.")

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")

# with open("practice.txt","w") as f:
#     f.write(new_data)

#check for the word in line and print the line number

def check_word():
    word = "learning"
    data = True

    line_number = 1

    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_number)
                return
            line_number += 1


check_word()