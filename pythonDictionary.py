dict = {
    "name":"John",
    "cgpa": 9.5,
    "marks": {
        "chem": 85,
        "Maths": 95,

        "Physics": 99
    }
}

wordMeaning = {
    "table":("A peice of furniture","list of facts and figures"),
    "cat": "A small animal"
}

marks = {};

physics = int(input("Enter your physics marks:"))
chemistry = int(input("Enter your chem marks: "))
maths = int(input("Enter your maths marks: "))

marks.update({"Physics":physics, "Chemistry":chemistry, "Maths":maths})

print(marks);



print(wordMeaning);
print(wordMeaning.get("table")[0]);

print(dict["name"]);
print(dict["cgpa"]);

print(dict["marks"]["Maths"]);

print(len(list(dict.keys())))

print(dict.items())

print(dict.get("marks").get("Maths"))

print(dict.update({"city":"Bangalore"}))

print(dict.items());

print(dict.keys())

print(dict);