Creating Files and Directories
------------------------------

---

#### Objectives
*   Create a directory hierarchy that matches a given diagram.
*   Create files in that hierarchy using an editor or by copying and renaming existing files.
*   Display the contents of a directory using the command line.
*   Delete specified files and/or directories.

---

We now know how to explore files and directories, but how do we create them in the first place?
Let's go to your SWC lessons folder, and use `ls -F` to see what it contains:

```
$ ls -F
```

Let's create a new directory called `my_scripts` using the command `mkdir my_scripts`
(which has no output):

```
$ mkdir my_scripts
```

As you might (or might not) guess from its name, `mkdir` means "make directory".
Since `my_scripts` is a relative path (i.e., doesn't have a leading slash),
the new directory is made below the current working directory:

```
$ ls -F
```

However, there's nothing in it yet:

```
$ ls -F my_scripts
```

Let's change our working directory to `my_scripts` using `cd`,
then run a text editor called Nano to create a file called `draft.txt`:

```
$ cd my_scripts
$ touch draft.txt
```


> #### Which Editor?
> 
> When we say, "`nano` is a text editor," we really do mean "text": it can
> only work with plain character data, not tables, images, or any other
> human-friendly media. We use it in examples because almost anyone can
> drive it anywhere without training, but please use something more
> powerful for real work. On Unix systems (such as Linux and Mac OS X),
> many programmers use [Emacs](http://www.gnu.org/software/emacs/) or
> [Vim](http://www.vim.org/) (both of which are completely unintuitive,
> even by Unix standards), or a graphical editor such as
> [Gedit](http://projects.gnome.org/gedit/). On Windows, you may wish to
> use [Notepad++](http://notepad-plus-plus.org/).
> 
> No matter what editor you use, you will need to know where it searches
> for and saves files. If you start it from the shell, it will (probably)
> use your current working directory as its default location. If you use
> your computer's start menu, it may want to save files in your desktop or
> documents directory instead. You can change this by navigating to
> another directory the first time you "Save As..."

Let's type in a few lines of text, then use Control-O to write our data to disk:

Once our file is saved,
we can use Control-X to quit the editor and return to the shell.
(Unix documentation often uses the shorthand `^A` to mean "control-A".)
`nano` doesn't leave any output on the screen after it exits,
but `ls` now shows that we have created a file called `draft.txt`:

Let's tidy up by running `rm draft.txt`:

```
$ rm draft.txt
```

This command removes files ("rm" is short for "remove"). If we run `ls` again,
its output is empty once more, which tells us that our file is gone:

```
$ ls
```


> #### Deleting Is Forever
> 
> Unix doesn't have a trash bin: when we delete files, they are unhooked
> from the file system so that their storage space on disk can be
> recycled. Tools for finding and recovering deleted files do exist, but
> there's no guarantee they'll work in any particular situation, since the
> computer may recycle the file's disk space right away.

Let's re-create that file and then move up one directory to your SWC folder using `cd ..`:

```
$ pwd
$ touch draft.txt
$ ls
$ cd ..
```

If we try to remove the entire `my_scripts` directory using `rm my_scripts`,
we get an error message:

```
$ rm my_scripts
rm: cannot remove `my_scripts': Is a directory
```

This happens because `rm` only works on files, not directories. The right command is `rmdir`,
which is short for "remove directory". It doesn't work yet either, though,
because the directory we're trying to remove isn't empty:

```
$ rmdir my_scripts
rmdir: failed to remove `my_scripts': Directory not empty
```

This little safety feature can save you a lot of grief, particularly if you are a bad typist.
To really get rid of `my_scripts` we must first delete the file `draft.txt`:

```
$ rm my_scripts/draft.txt
```

The directory is now empty, so `rmdir` can delete it:

```
$ rmdir my_scripts
```

> #### With Great Power Comes Great Responsibility
> 
> Removing the files in a directory just so that we can remove the
> directory quickly becomes tedious. Instead, we can use `rm` with the
> `-r` flag (which stands for "recursive"):
> 
> ```
> $ rm -r my_scripts
> ```
> 
> This removes everything in the directory, then the directory itself. If
> the directory contains sub-directories, `rm -r` does the same thing to
> them, and so on. It's very handy, but can do a lot of damage if used
> without care.

Let's create that directory and file one more time.
(Note that this time we're running `nano` with the path `my_scripts/draft.txt`,
rather than going into the `my_scripts` directory and running `nano` or 'vim' on `draft.txt` there.)

`draft.txt` isn't a particularly informative name, so let's change the file's name using `mv`,
which is short for "move":

```
$ mv my_scripts/draft.txt my_scripts/quotes.txt
```

The first parameter tells `mv` what we're "moving", while the second is where it's to go.
In this case, we're moving `my_scripts/draft.txt` to `my_scripts/quotes.txt`,
which has the same effect as renaming the file. Sure enough,
`ls` shows us that `my_scripts` now contains one file called `quotes.txt`:

```
$ ls my_scripts
```

Just for the sake of inconsistency, `mv` also works on directories - there is no separate `mvdir` command.

Let's move `quotes.txt` into the current working directory. We use `mv` once again,
but this time we'll just use the name of a directory as the second parameter
to tell `mv` that we want to keep the filename, but put the file somewhere new.
(This is why the command is called "move".) In this case,
the directory name we use is the special directory name `.` that we mentioned earlier.

```
$ mv my_scripts/quotes.txt .
```

The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `my_scripts` is empty:

```
$ ls my_scripts
```

Further, `ls` with a filename or directory name as a parameter only lists that file or directory.
We can use this to see that `quotes.txt` is still in our current directory:

```
$ ls quotes.txt
```

The `cp` command works very much like `mv`, except it copies a file instead of moving it.
We can check that it did the right thing using `ls` with two paths as parameters&mdash;like most Unix commands,
`ls` can be given thousands of paths at once:

```
$ cp quotes.txt my_scripts/quotations.txt
$ ls quotes.txt my_scripts/quotations.txt
```

To prove that we made a copy, let's delete the `quotes.txt` file in the current directory
and then run that same `ls` again. This time it tells us that it can't find `quotes.txt` 
in the current directory, but it does find the copy in `my_scripts` that we didn't delete:

```
$ ls quotes.txt my_scripts/quotations.txt
ls: cannot access quotes.txt: No such file or directory
my_scripts/quotations.txt
```

> #### Another Useful Abbreviation
> 
> The shell interprets the character `~` (tilde) at the start of a path to
> mean "the current user's home directory". For example, if my home
> directory is `/home/april`, then `~/data` is equivalent to
> `/home/april/data`. This only works if it is the first character in the
> path: `here/there/~/elsewhere` is *not* `/home/april/elsewhere`.


#### Key Points
*   Unix documentation uses '^A' to mean "control-A".
*   The shell does not have a trash bin: once something is deleted, it's really gone.

[Home](../README.md) \|
[Next Section](03-pipefilter.md)
