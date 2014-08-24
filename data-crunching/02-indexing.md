
# Indexing and Selecting

*explain purpose of indexing and slicing here...explain what a value is and what
an index is...maybe use a series with an index as an example*

## Basics

we have the most basic indexing using []

can select a column by name


    surveys['species']

you can also set a variable to your subset


    surveys_species=surveys['species']

You can pass a list of columns to [] to select columns in that order. If a
column is not contained in the dataframe, an exception will be raised. This is
useful for applying a function (like transform) to a subset of your columns.


    surveys[['species', 'plot']]

You can also access columns on DataFrames as an attribute:


    surveys.wgt

## Slicing Ranges

Slicing using the [] operator slices rows in dataframes. When slicing in pandas
the start bound and the stop bound are included. data[start:stop]


    surveys[0:3]


    surveys[:5]


    surveys[-1:]

can set values using slices


    surveys_copy=surveys.copy()
    surveys_copy[0:3]=0

## Selection with .ix method

Return the column in question and its data type. Format is [row, column] *add in
what inputs are, etc*


    surveys.ix[:,'species']

you can also set variables to your subset of data. this will be a series


    surveys_species=surveys.ix[:,'species']

more slicing


    surveys.ix[100,['species', 'wgt']]

## Selection by Label

all labels must be in index or a KeyError will be raised. remember that the
start bound and the stop bound are included. Integers can be used, but they
refer to the index label and not the position.


    surveys.loc[[0,10],:]


    surveys.loc[0,['species', 'plot','wgt']]

## Selection by Position

0-based indexing, start bounds included and upper bound excluded. trying to use
a non-integer will raise an IndexError


    surveys.iloc[:3]

integer slicing


    surveys.iloc[0:10, 4:6]

slicing rows


    surveys.iloc[0:3,:]

slicing columns


    surveys.iloc[:, 0:5]

integer lists


    surveys.iloc[[2,4,6],[1,3,5]]

can pull out a specific data point


    surveys.iloc[7,156]
