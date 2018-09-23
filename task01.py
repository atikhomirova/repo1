# Task 01
# Find most frequent element in the list

"""
Anton:
Please take a look at PEP8.
Also I highly recommend you use the following tools to check code style:
- flake8;
- pydocstyle.
"""

l = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5]

print(max(set(l),key=l.count))

"""
Anton:
Good practice is to use the following construction:
if __name__ == '__main__':
    run your code
"""
