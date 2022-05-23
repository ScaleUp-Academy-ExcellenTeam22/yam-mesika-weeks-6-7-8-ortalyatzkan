from collections import defaultdict


def group_by(func, iterable):
    """
    A function that gets a function and iterable,
    the function returns a dictionary,
    where the keys are the values returned from the function passed as the first parameter.
    The value corresponding to a particular key is a list of all the words for which the function returned the key.
    :param func:The function that is run on the iterable.
    :param iterable:The iterable whose values are sent to the function.
    :return:A dictionary whose keys are the values returned from the function,
            And its values are the temp values corresponding to the key values.
    """
    def_dict = defaultdict(list)
    [def_dict[func(item)].append(item) for item in iterable]
    return def_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
