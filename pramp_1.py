'''
Given an  array, return the first element whose value 
equals its index.

[-4, -3, 0, 1, 4, 6]
 -- > 4
 0   1   2  3  4  5
 
[-100, -99, -98]
-- > -1

[0, 1, 2, 3, 4, 5]
-- > 0 or 1 or 2 or 3 or 4 or 5 (any answer is correct)

[1, 2, 3, 4, 5, 6]
-- > -1

[-1, 0, 1, 2, 3, 4]
-- > -1
 0   1  2  3  4  5
                 l
                 f

[-1, 0, 1, 2, 3, 5]
-- > 5
[-35, -34, -23, -1, 0, 1, 4, 7, 15, 16, 20, 21]

  0    1    2   3   4  5  6  7  8   9   10  11
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

num_list.value(43) -- > 
last = len(num_list) # 99
first = 0

mid = (last - first) / 2 + first


first = mid + 1 # 50

'''

def array_index(num_list):
    # O(n)
   for idx, value in enumerate(num_list):
      if idx == value:
         return idx
   return -1

def binary_search(num_list):
   # O(log n)
   first = 0 
   last = len(num_list) - 1
   
   while first < last:
      mid = (last - first) / 2 + first
      if mid > num_list[mid]:
         first = mid + 1
      elif mid < num_list[mid]:
         last = mid - 1
      else:
         return mid
   return -1
  