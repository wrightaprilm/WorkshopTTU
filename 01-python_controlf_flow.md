#Lists and Beginning Control Flow

But really, how often are we just trying to do an operation on one variable? Or two numbers that we're entering into the computer by hand?

Approximately never.

##Lists

A list is an ordered collection of elements. These elements can be of different types. For now, let's keep it simple.


```python
>>> last_name = ['w', 'r, 'i', 'g', 'h', 't','5','1,'2']
```

The equals sign creates an item called last_name. When the Python interpreter reaches the open square bracket, it knows to expect items to be stored in a list. Each item in the list is enclosed in single quotes, separated from all other list elements by a comma.

Go ahead and make your own list. Call one of us over if you get an error message, so we can share with the class.

Lists are really useful because they can store data and you can then access that data in a variety of ways.

For example, if I knew that the first character of my last name, I could type:

```python
>>> print last_name[0]
'w'
```

Oho, zero. Python, as a language initializes from zero. This is like C and unlike R. So, the first element in a list is the zeroth element. This can be a little tricky at first.

If I wanted a few letters of my last name, I could do something like this:

```python
>>> last_name[0:3]
'w', 'r', 'i'
```

Try taking a few different "slices" of your list. Can you convince yourself of what is happening, particularly about how Python knows where to start and stop?

##Control Flow

The for loop is one of the most common ways to iterate over multiple data points in Python. These loops do some action a finite amount of times.

For example:

```python
>>> for letter in last_name:
...     print letter

'w'
'r'
'i'
'g'
'h'
't'
'5'
'1'
'2'
```

In this case, action is print, and that action is done for each letter in my list. "letter" is a loop variable, a unit of our list. If we use the syntax "for ... in list", python will automatically interpret the name between _for_ and _in_ as a variable.

Also, see those three dots before "print letter?" The python interpretted automatically includes those dots to help visualize the structure of your for loop. Don't type these three dots yourself, or python will get confused.



Just printing things to the screen isn't very helpful. We may want to look for a specific letter in my name - that is, we may want to filter our lists by some criterion.

```python
>>> search_letter = 'a'
>>> if search_letter in last_name:
...     print 'yay'
... else:
...     print 'boo'

'boo'
```


What we've created here is an if-else statement. In these statements, if one condition (in list) is fulfilled, one action will be executed. In this case, we print 'yay'. If the other condition is fulfilled, we print 'boo'. If and else statements can be expanded to have many conditions (though this can be a pain), or left simply as 'if' with no action taken for variables that do not meet the condition.

If and else statements can be used to filter data. In the next example, we'll put the letters in one of two places, depending on what those letters are:

```python
>>> 
>>> positives = []
>>> negatives = []
>>> for letter in last_name:
...     if letter == 'g':
...         positives.append(letter)
...     else:
...         negatives.append(letter)

>>> print positives
>>> print negatives
```


There's some complex stuff going there! So, we're looping over the letter in last_name and sorting by whether or not those letters are the letter g (Hint: why would we use '==' instead of is? When would we expect 'is' not to work?). Then, we're appending those to the end of a list.

##Exercise time!

+ Filter your last_name list by if the value is numeric or alpha
    + But first, think of a test for the input. What must be true of your input for your code to work?
    + And write a test that your output will eventually pass. What must be true of your output if you know you've done this right?

 

