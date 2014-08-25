#Scripts as modules

Writing scripts is all fine and good. But we want our scripts to save us time. We want to reuse them, so we're not doubling up on work constantly. 

Let's take the code we just made and saved to a script. If that is a useful function, we might want to use it in multiple scripts (tomorrow, I will show you an example of a function I use almost daily). We could do this by copying and pasting the script into every script in which we would like to use it. But that's a lot of work, and makes our files bigger. We could move the script between directories every time we want to use it, but again, this is work, and leaves us prone to forgetting where our scripts are located. Ideally, we'd like to have one copy of each script, in a version-controlled repository with unit tests.

We're going to add a small piece to the bottom of our script:

```python
if __name__ == '__main__':
	filter_name(last_name, search_key)
```

This looks weird, right? The syntax of if __name__ == '__main__': tells Python that the code in tis script can be called from other scripts, and that if it is, it should do the action of filtering the name list.

This gets a little complicated, though. We need to tell Python where it can find our code, which involves editing the PYTHONPATH, the places where Python natively searches for scripts. Since not all of you may be interested in doing this (for example, if you plan on writing a lot of one-off scripts to solve problems that aren't repeated, you might not want to do this), please see us after the workshop or before the start tomorrow, and we can assist you.

If you choose to do this, the script can then be called inside of other scripts:

```python
import example_script
my_two_lists = example_script.filter_name
#note that when invoking the new script, you will have to provide the arguments 
#for filter_name
```

or at the interpreter in the same way.

#Key Points

+ Code reuse is good and saves time
+ But can involve initial investment (setting up paths)
+ Importing scripts as modules enables code reuse
