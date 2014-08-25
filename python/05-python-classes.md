#Classes

We've discussed grouping code by it's function. We can also group objects by their properties. We've talked so far about different kinds of objects. Objects, in Python, have properties. A list, for example, if ordered. This is something that is true about a list, no matter how we call it. 

Classes allow us to make custom objects with our own needed properties. Classes have what are called **methods**. Methods are functions that allow us to define the properties of our class. These properties are often called **attributes**.

```python
class Coordinates(object):
    def __init__(self, name):
        self.name = name
    def set_lat(self, lat):
        self.lat = lat
    def set_long(self, long):
        self.long = long
    def set_date(self, date):
        self.date = date
```

What we have defined above are four methods: one which initializes the class (*init*), one which sets the longitudes of the class (*set_lat*), one which defines longitudes (*set_long*) and one which defines when the data were collected (*set_date*). This translates to the class having a name, a latitude, a longitude and a date attribute. We can now define these at the command line.

```python

swc_coords = Coordinates('swc_coords')

```

In the above, we've defined the name of our variable to swc_coords, with the value swc_coords. Defining the name looks a little different than other class definitions, because it is initializing and defining the class. If we call this object, we see the below:

```python
swc_coords
 <__main__.Coordinates at 0xb49eb1ac>

```

Telling us that this is an object of class 'Coordinates' that has an address in memory. To define our lat and long, let's bring back our friends from yesterday:

```python
import numpy as np

lat, lon = np.loadtxt('swc_bc_coords.csv', delimiter=',', unpack=True)

swc_coords.set_lat(lat)

swc_coords.set_long(lon)

swc_coords.set_date('2014.08.24')

```

This dot notation works because we already have a memory address for this Class. Once initialized, we can just add attributes (that we defined when we set up the class) with this notation. We can look at what we defined like so:

```python 
swc_coords.date
'2014.08.24'
```
Our class attributes can be acted upon in standard ways:

```python
swc_coords.lat.mean()
38.661083392857144
```

OK, so why? We've organized attributes of our code. But so what, would it be worse if our objects were separate? Maybe, maybe not. For complex data structures, this code is readble. We know what, to what, exactly 'lat' and 'long' belong. If we have multiple years of data, we might make each year an instance of the coordinate class. This would spare us having to define lat_2010, lat_2011, lat_2012, lat_2013, lat_2014, long_2010, long_2011, long_2012, long_2013, long_2014, date_2010, date_2011, date_2012, date_2013, date_2014, and keep all htat straight. Instead, we have simpler notation of coords_2010.date and so on. 

Also, consider the following situation: You collected your data one year, but subsequently decided that to collect some additional bit of data next year.

```python
class NewCoords(Coordinates):
    number_ran = '113'
```

And now I can define attributes:

```python
coords.set_lat(lat)

coords.set_long(lon)

coords.set_date('2014.08.24')
```

You'll notice I didn't tell NewCoords what it's attributes ought to be. This is because it **inherited** them from the class coordinates. And this is a strength of object-oriented programming: it can enable easier reuse of pre-defined objects. Many popular softwares are moving to be object-oriented because of this quality.

For example:

```python
class Model(object):
    def __init__(self, name, collector):
        self.name = name
		self.colector = c_name
    def set_math(self, math):
        self.math = math 
    def set_lat(self, lat):
        self.lat =lat
    def set_long(self, long):
        self.long=long

coords = Model('coords')
coords.set_lat(lat)
coords.set_long(long)
coords.set_math(coords.lat*coords.long)

```

Here, we've programmed a really simple model that returns a result (not that it should be believed the result should mean anything). We also added a 'collector' aspect to the __init__ statement, in case we wanted to compare SWC locations to another software school (like the Hacker School). We can imagine that if we wanted to model the data in a more complex way than this nonsense, we could build a new class that inherits aspects from this model. Many software packages in biology are moving towards this framework. Classes give people power to define small classes to do organize the important aspects of their data, or of models, and they allow easy attribution of that work back to specific individuals.








