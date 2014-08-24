##Pandas

We've talked a whole bunch about looping and opening files and reading them. So far we've worked with plain-text files. But some files have unusual dialects. One common example of such a file is an Excel file.

You should have downloaded a file called 'Sites_simple.xls'. This is the same file as we used earlier, but written in Excel format. To use it, we need to parse that file. The library 'pandas' can do this.

We will first import pandas.

```python
>>> import pandas
```

Many users have written their own libraries for doing fun things. These users may choose to distribute these functions for general use by the community. Pandas (http://pandas.pydata.org/) is such a library.

When we use a library that we downloaded from the internet, it is not part of Python's base functionality. Therefore, we tell Python that we'd like to use this extra library with the import command.

Now we're going to take our spreadsheet and use Pandas to import it.

```python
>>> xl = pandas.ExcelFile('surveys.xlsx')
>>> xl
<pandas.io.parsers.ExcelFile object at 0x102a39610>
```
This should seem familiar - much like with our initial exercises in opening files, we are referencing the file and not the data within it. So let's liberate that data!

Excel documents are made up of sheets, which are linked documents containing different subsets of data. We're keeping it simple - all our data is in one sheet.

```python
>>> xl.sheet_names
[u'Sheet1', u'Sheet2', u'Sheet3']
>>> df = xl.parse('Sheet1')

       record_id  month  day  year  plot species  sex  wgt
0              1      7   16  1977     2     NaN    M  NaN
1              2      7   16  1977     3     NaN    M  NaN
2              3      7   16  1977     2      DM    F  NaN
3              4      7   16  1977     7      DM    M  NaN
4              5      7   16  1977     3      DM    M  NaN
5              6      7   16  1977     1      PF    M  NaN
6              7      7   16  1977     2      PE    F  NaN
7              8      7   16  1977     1      DM    M  NaN
8              9      7   16  1977     1      DM    F  NaN
[35549 rows x 8 columns]
```

If I wanted to see a specific observation in the zeroeth row, say, the third one, I could index like so:

```python
>>> df.ix[0,3]
180.0
```

What happens if we try the following:

```python
df[0,3]
```

How about:

```python
df[:3]
```

Alternatively, I could choose to view the third column for all rows:

```python

>>> df.ix[:,3]
0     1977
1     1977
2     1977
3     1977
4     1977
5     1977
6     1977
7     1977
8     1977
9     1977
10    1977
11    1977
12    1977
13    1977
14    1977
...
35534    2002
35535    2002
35536    2002
35537    2002
35538    2002
35539    2002
35540    2002
35541    2002
35542    2002
35543    2002
35544    2002
35545    2002
35546    2002
35547    2002
35548    2002
Name: year, Length: 35549, dtype: int64

```

Try slicing up your data in different ways. Does everything give you the expected output? What does the dtype keyword mean?

That's all well and good, but we have these nice row and column names! Let's use them!

```python
>>> df = xl.parse('Sheet1', index_col = 0,header=0)
>>> df.head

<bound method DataFrame.head of            month  day  year  plot species  sex  wgt
record_id                                          
1              7   16  1977     2     NaN    M  NaN
2              7   16  1977     3     NaN    M  NaN
3              7   16  1977     2      DM    F  NaN
4              7   16  1977     7      DM    M  NaN
5              7   16  1977     3      DM    M  NaN
6              7   16  1977     1      PF    M  NaN
7              7   16  1977     2      PE    F  NaN
8              7   16  1977     1      DM    M  NaN
9              7   16  1977     1      DM    F  NaN
10             7   16  1977     6      PF    F  NaN
11             7   16  1977     5      DS    F  NaN
12             7   16  1977     7      DM    M  NaN
13             7   16  1977     3      DM    M  NaN
14             7   16  1977     8      DM  NaN  NaN
15             7   16  1977     6      DM    F  NaN
16             7   16  1977     4      DM    F  NaN
17             7   16  1977     3      DS    F  NaN

df['month']
Out[26]: 
record_id
1            7
2            7
3            7
4            7
5            7
6            7
7            7
8            7
9            7
10           7
11           7
12           7
13           7
14           7
15           7
...
35535        12
35536        12
35537        12
35538        12
35539        12
35540        12
35541        12
35542        12
35543        12
35544        12
35545        12
35546        12
35547        12
35548        12
35549        12
Name: month, Length: 35549, dtype: int64
```

By specifying an index column as the zeroeth column, we are now able to access the data by the name of the column.

When we specify the header as the zeroeth row, we get to do fun things like so:

```python
>>> df.ix[0:5,'month']

record_id
1            7
2            7
3            7
4            7
5            7
Name: month, dtype: int64

```

In this way, we can break our data down for manipulation. We can use this to build more complex functions:

```python
>>> a = df.ix[:,'wgt']
>>> a
df['wgt']

record_id
1           NaN
2           NaN
3           NaN
4           NaN
5           NaN
6           NaN
7           NaN
8           NaN
9           NaN
10          NaN
11          NaN
12          NaN
13          NaN
14          NaN
15          NaN
...
35535        53
35536        42
35537        46
35538        31
35539        68
35540        23
35541        31
35542        29
35543        34
35544       NaN
35545       NaN
35546       NaN
35547        14
35548        51
35549       NaN
Name: wgt, Length: 35549, dtype: float64
```

a behaves like a list, so we can do list-based operations on it.

Because Excel is kind of terrible (and writing it out requires another library), you can output your data to a csv like so:

```python
>>> outfile = open('output.csv', 'w')
>>> df.to_csv(outfile)
>>> outfile.close()
```


##Exercise

I've attached a sample of different numpy functions in a file called 'functions.md'. Have a look at them. Try writing a two function set: one function that returns a slice of data, and another that does a function of your choice on that slice.


