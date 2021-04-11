# Python List Comprehensions

Before beginning make sure you have a basic understanding of Lists, which are just containers to hold data. Besides basic lists, Python supports a data structure called a "list comprehension", used to construct lists in a natural, easy way. In many cases, a complex task can be constructed using just a single line.

## Part 1: Intro

Let’s start with looking at simple list comprehension. It's common to construct a new list based on values from an existing list after they, say, are filtered by an expression. 

Try this in your shell:

```
>>> numbers = [3, 27, 34, 12, 5]
>>> [num * 3 for num in numbers]
[9, 81, 102, 36, 15]
```

Read this from right to left. We're looping through `numbers`, assigning each individual numbers to the temporary variable, `num`. We're then applying the expression `num * 3`, then appending each result to a new list.

How would you do this using a regular list construct?

```
>>> numbers = [3, 27, 34, 12, 5]
>>> new_numbers = list()
>>> for num in numbers:
...     new_numbers.append(num * 3)
...
>>> new_numbers
[9, 81, 102, 36, 15]
```

Let's try something a little more advanced.


```python
# intro - ex1a


def create_list(alpha_list):
    beta_list = []
    for letter in alpha_list:
        if filter(letter):
            beta_list.append(letter)
    return beta_list


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)
```

In this example, we're creating a new list, `beta_list`, of letters greater than or equal to 'B' by iterating through the `alpha_list` and applying the appropriate filter on the list. *This filter is called a predicate.*

When you run this code you should see:

```
['B', 'C', 'D', 'E', 'F', 'G', 'H']
```

How do we do this with a list comprehension: 

```python
# intro - ex1b


def create_list(alpha_list):
    return [letter for letter in alpha_list if filter(letter)]


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)
```

Run the code. You should see the same output. Now read it out loud, right to left, starting with the original list, then applying the `if` statement: "Return each letter in `alpha_list` if it's greater than or equal to 'B'". 

Simple. Concise. Efficient.

## Part 2: Chained vs. Nested Lists

Now that we have a a basic understanding of list comprehensions, let's take it a step further and look at how to chain or combine list comprehensions, which are akin to nested lists - both of which are used for iterating on more than one loop.

```python
# chained and nested loops - ex2


num_list = [2, 4, 6]
alpha_list = ['A', 'B', 'C']

print "\n# 1) ------------ #\n"

# chain
print ['{}-{}'.format(letter, number) for letter in alpha_list for number in num_list]

# nest
beta_list = []
for letter in alpha_list:
    for number in num_list:
        beta_list.append('{}-{}'.format(letter, number))

print beta_list

print "\n# 2) ------------ #\n"

# chain
print [['{}-{}'.format(letter, number) for letter in alpha_list] for number in num_list]

# nest
beta_list = []
for number in num_list:
    beta_list_inner = []
    for letter in alpha_list:
        beta_list_inner.append('{}-{}'.format(letter, number))
    beta_list.append(beta_list_inner)
print beta_list

print "\n# 3) ------------ #\n"

# chain
print ['{}-{}'.format(letter, number) for letter in alpha_list if letter < 'C' for number in num_list if number < 5]
print ['{}-{}'.format(letter, number) for letter in alpha_list for number in num_list if number < 5 and letter < 'C']


# nest
beta_list = []
for letter in alpha_list:
    if letter < 'C':
        for number in num_list:
            if number < 5:
                beta_list.append('{}-{}'.format(letter, number))
print beta_list

beta_list = []
for letter in alpha_list:
    for number in num_list:
        if number < 5 and letter < 'C':
            beta_list.append('{}-{}'.format(letter, number))
print beta_list
```

Test this out:

```
# 1) ------------ #

['A-2', 'A-4', 'A-6', 'B-2', 'B-4', 'B-6', 'C-2', 'C-4', 'C-6']
['A-2', 'A-4', 'A-6', 'B-2', 'B-4', 'B-6', 'C-2', 'C-4', 'C-6']

# 2) ------------ #

[['A-2', 'B-2', 'C-2'], ['A-4', 'B-4', 'C-4'], ['A-6', 'B-6', 'C-6']]
[['A-2', 'B-2', 'C-2'], ['A-4', 'B-4', 'C-4'], ['A-6', 'B-6', 'C-6']]

# 3) ------------ #

['A-2', 'A-4', 'B-2', 'B-4']
['A-2', 'A-4', 'B-2', 'B-4']
['A-2', 'A-4', 'B-2', 'B-4']
['A-2', 'A-4', 'B-2', 'B-4']
```

So, you can nest a number of list comprehensions inside of one another; however, by doing so, you often sacrifice readability. Notice in the last example set of list comprehensions that there are multiple `if` statements in comprehension. This is fairly common: In fact, you can add any number of loop in a list comprehension, and each may have an optional `if` statement associated with it:

`print ['{}-{}'.format(letter, number) for letter in alpha_list if letter < 'C' for number in num_list if number < 5]`

This example is fairly complex. Can you tell what's happening? Beak it down into pieces, if necessary:

1. First, return the letter from `alpha` list, if it's less than 'C'.
2. Then, return the number from `num_list` if it's less than 5.

Make sense?

## Part 3: Iterators

```python
# reversed / iterators - ex3


alpha_list = ['A', 'B', 'C']

# reversed 
rev_list = list(reversed(alpha_list))
print [i + a for i in alpha_list for a in rev_list]
print [i + a for i in alpha_list for a in reversed(alpha_list)]
rev_old = reversed(alpha_list)
print [i + a for i in alpha_list for a in alpha_list[::-1]]
rev_old = alpha_list[::-1]
print [i + a for i in alpha_list for a in rev_old]
```

Output:

``` 
['AC', 'AB', 'AA', 'BC', 'BB', 'BA', 'CC', 'CB', 'CA']
['AC', 'AB', 'AA', 'BC', 'BB', 'BA', 'CC', 'CB', 'CA']
['AC', 'AB', 'AA', 'BC', 'BB', 'BA', 'CC', 'CB', 'CA']
['AC', 'AB', 'AA', 'BC', 'BB', 'BA', 'CC', 'CB', 'CA']
```

1. In the first example the `reversed()` method creates a generator which we then cast to to a list.
2. In the remaining examples, we're all doing something very similar except we're using list comprehensions to iterate through the generators to create the new lists.

## Part 4 - Dictionary Comprehensions

A dictionary comprehension is like a list comprehension only it models a dictionary instead of a list.

```python
# dict comps - ex4


num_list = [2, 4, 6]
keys = [1, 3, 5]

print dict((x, y) for x in keys for y in num_list)
print dict(zip(keys, num_list))


class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{} ({})".format(self.name, self.id)

people = [
    Person(1, 'Josh'),
    Person(2, 'Megan'),
    Person(3, 'Ken')
]

print dict([(p.id, p) for p in people])
```

Output:

```
{1: 6, 3: 6, 5: 6}
{1: 2, 3: 4, 5: 6}
{1: Josh (1), 2: Megan (2), 3: Ken (3)}
```

Try this out in your shell:

```
>>> abc = {'a': 1, 'b': 2, 'c': 3}
>>> {value:key for key, value in abc.items()}
{1: 'a', 2: 'b', 3: 'c'}
```

This just flipped the keys and values of the `abc` dict. Based on this example, can you tell what's happening in the examples from above?

## Part 5: Set Comprehensions

As you probably guessed, a set comprehensions allows sets to be constructed in the same manner as a list comprehension.

Test it out:

```
>>> basic_set = set(range(19))
>>> {num for num in basic_set if num % 2 == 0}
set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
```

That's it.


## Conclusion

List comprehensions provide a clear, concise means for creating lists plus they provide a substantial performance boost because they run at C language speed within the Python interpreter:

```python
import time


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time

# ---- run code ---- #

test_list = xrange(1, 90000000)

comp_timer = ExecutionTime()
[num for num in test_list  if num % 2 == 0]
print 'List Comprehension finished in {} seconds.'.format(comp_timer.duration())

regular_list = list()
regular_timer = ExecutionTime()
for num in test_list:
    if num % 2 == 0:
        regular_list.append(num)
print 'Regular List finished in {} seconds.'.format(regular_timer.duration())
```

Results:

```
List Comprehension finished in 14.3765029907 seconds.
Regular List finished in 18.2762210369 seconds.
```

Just be aware that, often, more complex lists, especially nested or chained lists, can be much more difficult to read using list comprehensions - so you may need to use regular list constructs instead.