# nested-tools
The nested_tools library in Python


## Setup

#### From PIP

```
$ pip install nestedtools
```

## Usage

#### Import library

```python
import nested_tools as nt
```

#### Find a nested index from the item

```python
l = [['foo', 'bar'], 'baz']
print(nt.index(l, 'bar'))
```

Output: `(0, 1)`

#### Get the item from a nested index

```python
print(nt.get(l, (0, 1)))
```

Output: `bar`

#### Flatten a nested list

```python
print(list(nt.flatten(l)))
```

Output: `['foo', 'bar', 'baz']`

#### Transpose a flat list into a nested shape

```python
old_list = ['A', 'B', 'C', 'D', 'E', 'F']
new_shape = [[0], [1, 2], [3, [4, 5]]]
print(list(nt.transpose(old_list, new_shape)))
```

Output: `[['A'], ['B', 'C'], ['D', ['E', 'F']]]`

#### Get the shape list from a nested list

```python
l = [['A'], ['B', 'C'], ['D', ['E', 'F']]]
print(list(nt.to_shape(l)))
```

Output: `[[0], [1, 2], [3, [4, 5]]]`

#### Convert all iterables to list

```python
l = [{1, 2, (3,)}, [4, {5}, (6,)]]
print(list(nt.convert_all(l)))
```

Output: `[[1, 2, [3]], [4, [5], [6]]]`

**`convert_all` takes two more optional parameters**

* `to` - a type to convert to (default = `list`):

```python
print(tuple(nt.convert_all(l, tuple)))
```

Output: `((1, 2, (3,)), (4, (5,), (6,)))`

* `exclude` - a tuple of any iterable types to not convert (default = `(str,)`):

```python
print(list(nt.convert_all(l, exclude=(set,))))
```

Output: `[{1, 2, (3,)}, [4, {5}, [6]]]`
