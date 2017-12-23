"""

    1. Write a function that returns the multiplication of all input arguments. The function should ignore non-numeric arguments.
    2. Write a function that takes a list of strings AND a minimum length (number) and returns only the strings that are longer than
    3. Write a function groupby that takes a key-function and a list. The function should call key-function on all items in the
       list and return a dictionary whose keys are the results of key-function and values are all values from the list that
       productd that key

"""


def mymul(*args):
    """
    Multiply all integers passed as parameter(s) to the function
    """
    product = 1
    for x in args:
        if x.__class__.__name__ == 'int':
            product = product * x
    return product


def longer_than_n(min_length, *args):
    """
    Find all words having length greater than the given number
    """
    return [word for word in args if len(word) > min_length]


def groupby(key_func, *args):
    """
    Group the given list of strings based on the given key function
    """
    output_dict = dict()
    for text in args:
        key = key_func(text)
        if not output_dict.get(key, None):
            output_dict[key] = list()
        output_dict[key].append(text)
    return output_dict

print mymul("efd")
print longer_than_n(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
print groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')