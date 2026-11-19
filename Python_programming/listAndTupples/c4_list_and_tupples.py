# friends = ['Saksham', 'Rohit', 'Rishabh', 'Aman', 'Ankit']
# print(friends[0:3])  # Slicing used here
# for i in range(len(friends)):
#     print(friends[i]+'\n')  # Indexing used here

mtpple = ('Saksham', 'Rohit', 'Rishabh', 'Aman', 'Ankit')
print(mtpple.count('Saksham'))  # count method used here
repeated = mtpple * 2  # Repetition used here
print(repeated)
concatenated = mtpple + ('John', 'Doe')  # Concatenation used here
print(concatenated)
print('Saksham' in mtpple)  # Membership operator used here
print(len(mtpple))  # Length function used here
print(mtpple.index('Rohit'))  # index method used here
print(mtpple[1:4])  # Slicing used here
print(mtpple[::-1])  # Reversing a tuple using slicing
a , b , c , d ,e = mtpple[::-1] # Reverse Unpacking used here
print(a)