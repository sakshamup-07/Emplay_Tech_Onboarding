nums = list(map(int, input('enter numbers: ').split()))
sf_list = sorted(set(nums), key=nums.count)[-1]
print(sf_list)  #map is for type conversion, set is for unique values, sorted is for sorting the values based on their count in the original list, and [-1] is for getting the last element of the sorted list which is the most frequent number.and list is for converting the map object to a list.