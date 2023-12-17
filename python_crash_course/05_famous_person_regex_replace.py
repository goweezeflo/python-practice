import re

raw_input = input("Enter famous person name: ")
famous_person = re.sub("\\s+", " ", raw_input.strip())
print(f"Famous person: {famous_person.title()}")
