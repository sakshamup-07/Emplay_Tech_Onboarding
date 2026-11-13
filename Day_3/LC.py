# #1chk palin
# back = ""
# name = input("enter a string")
# for i in range(len(name)-1 , -1 , -1):
#     back+=name[i]
# if back == name:
#      print(True)
# else: print(False)

    # #2>lrgest numb
    # numbers = [1 , 2 ,3 ,4]
    # largest = numbers[0]
    # for i in numbers:
    #     if i > largest:
    #         largest = i
    # print(largest)

    # #3>find Slargest
    # largest = numbers[0]
    # slargest = numbers[0]
    # for num in numbers:
    #     if num>largest:
    #         slargest=largest
    #         largest=num
    #     elif num > slargest and num < largest:
    #         slargest = num
    # print(slargest)

    
    
    #4reverse string
# name = "saksham"
# rev=""
# for i in  range(len(name)-1 , 0 , -1):
#     rev+=name[i]
# print(rev)



#6 frequency 

# name = "programming"

# frequency = {}

# for char in name:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for char, count in frequency.items():
#     print(char, ":", count)

    #7remove duplicates

# arr = [1 ,2 ,3 ,3 ,3 ,4]
# ans=[]
# for i in arr:
#     for j in ans:
#         if i == j:
#             break
#     else:
#             ans.append(i)
# print(ans)

#8find missing number

# no = [1,2,3,5]
# total=0
# for i in no:
#     total+=i
# n = len(no) + 1
# sum = (n * (n + 1)) // 2
# print(sum-total)




#9 find non repeating char
# name ="aabbccd"
# freq={}
# for i in name:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i,v  in freq.items():
#     if(v==1):
#         print(i)

#10 two sum
# ls =[1,2,3,4,5,6]
# target = 5
# n = len(ls)
# for i in range(n):
#     for j in range(i+1 , n):
#         if ls[i]+ls[j]==target:
#             print(i , j)

#         if len(s) != len(t):
#             return False
        
#         count = [0] * 26
        
#         for i in range(len(s)):
#             count[ord(s[i]) - ord('a')] += 1  #anagram
#             count[ord(t[i]) - ord('a')] -= 1
            
#         for val in count:
#             if val != 0:
#                 return False
                
#         return True
