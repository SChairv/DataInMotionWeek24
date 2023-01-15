# Given a person variable:
# person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]
#
# Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value. This is the end goal:
#
# {'name': 'Bruce', 'job': 'Batman', 'city': 'Gotham'}

person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]
answer = dict(person)
print (answer)
answer["name"] = input("Please enter a first name ")
answer["job"] = input("Please enter the job ")
answer["city"] = input("Please enter your city ")
print (answer)






