collection = set()
collection.add(25)
collection.add(20)
collection.add(32)
collection.add(80)
collection.add("hello")
collection.add((1,2,3,"hello"))
print(collection)
collection.remove(25)
print(collection.pop())
print(collection.pop())
print(collection)
collection.clear()
print(collection)

subjects = {"Python","java","c++","Python","java","c","c++","javaScript","c++","java","Python"};

print(subjects);
print(len(subjects));
