"""
Madlibs using string concatenation
"""

#ways to concatenate in python
# starwars = "jedi"
#print("May the force be with " + starwars)
#print("May the force be with {}".format(starwars))
#print(f"May the force be with {starwars}")

group1 = input("group1: ")
group2 = input("group2: ")
person1 = input("person1: ")
person2 = input("person2: ")
person3 = input("person3: ")
weapon = input("weapon: ")

madlib = f"May the force be with {group1}. {group1} will defeat {group2}, \
when {person1} and {person2} will destroy the {weapon} built by {person3}."

print(madlib)