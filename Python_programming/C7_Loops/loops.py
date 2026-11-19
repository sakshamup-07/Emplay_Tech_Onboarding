for i in range(1,6):
    if i == 3:
        continue  # continue statement used here
    print(i)
else:            
 print("done")  # else block used here with for loop

n = int(input("Enter a number: "))
for i in range(1,n+1):
     print(" "*i , end="")  # end parameter used here to avoid new line after each print 
     print("*"*(n-i+1) , end="")  # end parameter used here to avoid new line after each print