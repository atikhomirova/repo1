# Task 01
# Find most frequent element in the list

"""
Anton:
Please take a look at PEP8.
Also I highly recommend you use the following tools to check code style:
- flake8;
- pydocstyle.
"""

if __name__ == "__main__":
    lst = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5]
    print(max(set(lst), key=lst.count))

"""
Anton:
Good practice is to use the following construction:
if __name__ == '__main__':
    run your code
"""
