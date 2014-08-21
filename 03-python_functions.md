#Functions

So far in this bootcamp, we've written code in the interpreter without much thought to the structure of how software can be organized. Functions provide structure for our code, and provide small, simple blocks of code that can be tested (more on this tomorrow with John) The basic idea of a function is like that of an organ in the body: a unit that does a particular task and returns a defined output.

Let's recall our code from earlier:

```python

last_name = ['w','r','i','g','h',t']

positives = []
negatives = []
for letter in last_name:
    if letter == 'g':
         positives.append(letter)
     else:
         negatives.append(letter)

```

Odds are, we will not want to sit at the command line and type this in every time we need to filter a list. What we're going to do in this module is learn how to take this bit of code, functionize it, save it to a script and make it more generalizeable to different lists and search keys. First, open your graphical text editor and paste in the code.

A function is defined in the following way:

```unix
def name_of_function():
	code goes here
```

The def() statement tells you the name of the function. In the parenthesis, we can put arguments, or information the function needs. We'll come back to this in a second. Our functionized code, in a clunky way in which you shouldn't write functions, could look like so:

```python

last_name = ['w','r','i','g','h','t']
key = 'g'

def filter_name(last_name, key):
	positives = []
	negatives = []
	for letter in last_name:
		if letter == key:
			positives.append(letter)
		else: 
			negatives.append(letter)
	return([positives, negatives])

```

That last line is called a return statement. It tells Python what we'd like to receive back. This is different than a print statement, as we are creating an object that can be used by other functions, not simply displaying information. The return statement ends a function.

We can call our function like so:

```python
filter_name()

[['g'], ['w', 'r', 'i', 'h', 't']]

```

##Can anyone see a problem?

What we've done is called hardcoding. Hardcoding is the practice of including important information in the code itself. Generally, this is bad practice, as every time we want to change our data, we must go into the code and change it. This increases possiblility of making a mistake and wrecking some of our code. We can avoid this by changing our code around a bit.

```python 
last_name = ['w','r','i','g','h','t']
key = 'g'

def filter_name(last_name, key):
        positives = []
        negatives = []
        for letter in last_name:
                if letter == key:
                        positives.append(letter)
                else: 
                        negatives.append(letter)
        return([positives, negatives])


```

And we change our call to the function a touch, to reflect this difference.

```python
filter_name(name, key)
[['g'], ['w', 'r', 'i', 'h', 't']]
```

This is better: we don't need to edit the function to change the data. But we do still need to open the file and tinker in there. What if we could avoid this?

Well, we can. Python comes with a number of modules that can be imported for use by the user. One such module is the [sys module](https://docs.python.org/2/library/sys.html), and it's most well-known function is called argv. This command allows users to feed a script some input, without ever opening the script.

We're going to change our function a little bit, and create our first real Python script. Close iPython (control + d). In the text editor, add a Python shebang line to the top of your script. This tells the computer that this file is executeable as python code.

```python
#!/usr/bin/env python
```

Under this, import the sys module:

```python

import sys
```
It's standard practice to include all modules at the top of the script.

We can now modify our script to look like this:

```python
last_name = sys.argv[1]
key = sys.argv[2]

def filter_name(last_name, key):
        positives = []
        negatives = []
        for letter in last_name:
                if letter == key:
                        positives.append(letter)
                else: 
                        negatives.append(letter)
        return([positives, negatives])
```

What this means is for the variable last_name, accept an argument presented at the command line. The first argument provided, will become last_name. The second will be the search key. Save this file as a .py file.

> It's generally considered super rude to not accurately reflect the scripting language in the file extension.
> .py files are python executeables. 

So if we type the following at the command line:

```python

python example_script.py  wright g
```

We get 

##...nothing!

Who knows why? 

Go ahead and stick a print statement in your function. If you still don't see output, make sure you've included a function call.

Lastly, we want to include comments in this so we don't forget what we did and why:

```python
last_name = sys.argv[1]
key = sys.argv[2]

def filter_name(last_name, key):
	"""functions have a special kind of comment called a docstring. It is denoted
	with three quotes. These can be multi-line without including the quotes on 
	each line. These are just helpful comments at the novice level, but if you 
	plan to distribute code, are very important. See here for more: 
	http://www.pythonforbeginners.com/basics/python-docstrings """
	positives = []
	negatives = []
#Regular comments can be embedded in the text after a pound sign.
	for letter in last_name:
		if letter == key:
			positives.append(letter)
		else: 
            negatives.append(letter)
        return([positives, negatives])
```


##Challenges:

+ What happens if you put your print statement outside of your function?
+ How could you pipe unix and python together so you could save your input?
