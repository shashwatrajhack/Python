dict = {
    "name":"John",
    "cgpa": 9.5,
    "marks": {
        "chem": 85,
        "Maths": 95,

        "Physics": 99
    }
}

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