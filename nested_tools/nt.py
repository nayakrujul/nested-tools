def index(lst, item):
    for i, x in enumerate(lst):
        if x == item:
            return (i,)
        if isinstance(x, (list, tuple)):
            ind = index(x, item)
            if ind:
                return (i,) + ind
    return False

def get(lst, index):
    if len(index) == 1:
        return lst[index[0]]
    return get(lst[index[0]], index[1:])

def flatten(lst):
    for item in lst:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

def transpose(lst, shape):
    for i in shape:
        if isinstance(i, int):
            yield lst[i]
        else:
            yield list(transpose(lst, i))
            
def to_shape(lst, i=0):
    for item in lst:
        if isinstance(item, (list, tuple)):
            yield list(to_shape(item, i))
            i += len(item)
        else:
            yield i
            i += 1

def make_same_shape(lst1, lst2):
    flat = flatten(lst1)
    shape = to_shape(lst2)
    return transpose(list(flat), list(shape))

def convert_all(lst, to=list, exclude=(str,)):
    for item in lst:
        if hasattr(item, '__iter__') and not isinstance(item, exclude):
            yield to(convert_all(item, to, exclude))
        else:
            yield item
            
