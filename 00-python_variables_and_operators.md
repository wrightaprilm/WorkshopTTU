#Variables

Variables are names for objects that we'd like to store.

When we assign them, we use the
```python
=
```

operator. When, for example, we type:

```python
>>> observations = 5
```

we set the value of observations to five. If we type:

```python
>>> print observations
```

we should receive
```python
5
```

in response.

###A note on names

As scientists, we often want to be very explicit when recording information. This is good. But spaces in the name of a variable in Python, will cause the name to be read wrong. Observe:

```python
>>> number of observations = 5
      ^
SyntaxError: invalid syntax
```

Because of the space, Python has become confused about what you're assigning and to which variable. The error we received is a syntax error, which tells us that there is some problem with the way we've entered the command. For best results, staying away from spaces in naming is a good idea. 


#Some simple operations with variables
##Mathematical operators

|Symbol | Meaning |
|-------|------|
| +  | add |
| **  | exponent |
| -    | subtract |
| *   | multiply |
| /  | Divide |


## Comparison operators

Note that these compare the item on the left of the operator to the item on the right.

| Symbol | Meaning |
| --------|---------|
| ==  | is equal to  |
| <  | is less than |
| >  | is greater than |



We can use a combination of variable storage and mathematical operators to beginning stringing together mathematical statements right away!

```python
>>> a = 5
>>> b = 1
>>> print a + b
6
>>> c = (a + b)/b
>>> c
6
>>> d = (a + b)/a
>>> d
1
```

Record scratch! Why did we get 6/5 = 1? We've been working with what are called integers, which round off values between integers. If we want a little more precision, we can use floats:

```python
>>> a = float(a)
>>> b = float(b)
>>> d = (a+b)/a
>>> d
1.2
```

That's better.

##A not on types

Python has several native types. The most well-used are ints, floats and strings. Integers are whole numbers, floats can contain decimals, and strings are characters. To move between them, we use _casting_.

```python
>>> a = 5
>>> a = float(5)
... 5.0
```

Ints can be cast as floats, floats as ints, and numerical strings as ints or floats. But casting a word as an int doesn't work:

```python
>>> name = "April"
>>> float(name)
... ValueError: could not convert string to float: April
```

This can be helpful for error checking, as we'll see later.

###Bonus tidbit: Readable results

```python
>>> a = 5 
>>> print 'A is equal to %i' % a
A is equal to 5
```


We can insert our variables into sentences to make results more readable. In the above code, we are inserting an integer, a, into the sentence. We know we are inserting an integer because the first percentage sign is followed with an i.

If we had assigned a to a string, like so:

```python
>>> a = 'aaa'
```

We would change that %i to %s:

```python
>>> print 'A is equal to %s' % a
A is equal to aaa
```

Exercise

+ Assign two variables to different numbers
+ Print back the variables to ensure the assignment worked
+ Do a mathematical operation of your choosing
+ Compare the results of the operation to a number held in the third variable
+ Print a summary of your results to the screen in a full sentence
+ Try this again, but have your third variable be a word. Do you understand what happened here? Let's talk about it!



