# import json

# employee = {
#     "name": "Saksham",
#     "age": 22,
#     "skills": ["Python", "SQL"]
# }

# json_data = json.dumps(employee)

# print(json_data)
# print(type(json_data))

import json

employee = {
    "name": "Saksham",
    "age": 22,
    "department": "Engineering"
}

with open("Day_2/employee.json", "w") as file:
    json.dump(employee, file, indent=4)