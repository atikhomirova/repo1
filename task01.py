# Task 01
# Find most frequent element in the list

l = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5]

print(max(set(l),key=l.count))