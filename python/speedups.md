##Table of ways to speed up your code

| Instead of ... | Do | Why| When to use the slower code |
|----------------|----|----|-----------------------------|
| readlines()| Loop over the file| readlines reads in the whole file at once, which takes a lot of memory. When you loop, you can start processing the data *immediately*, which saves time, and allows you to save smaller subsets of the file in memory, if you wish | When you really quick want to visualize the file at the interpreter |
| declaring and making a list | list comprehension | These run in the C language, which makes them faster | For readability. If your code will be read by novices, it might be best to keep it simple |
| open | with open | this is not a speed-up per se, but prevents us from having to remember to close our loops | Again, readability. |


