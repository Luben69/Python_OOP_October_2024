from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex5 import *
print('Setup complete.')
def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = u(ratings) / len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

# Do not change: Check your answer
q4.check()