marks = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'Eve': 90,
    0 : 21
}
print(marks[0], type(marks))  # Dictionary used here
print(marks.keys())
marks.update({'John': 95 , 'Renu': 98})  # update method used here
print(marks.get('harish'))  # get method used here

st = {1, 2, 3, 4, 5} 
st1 = {4, 5, 6, 7, 8}
print(st, type(st))  
print(st.difference(st1))  # difference method used here
print(st.difference_update(st1))  # difference_update method used here
print(st , st1)
st1.discard(6)
st1.discard(7)
print(st1)  # discard method used here