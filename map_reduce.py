#!/usr/bin/env python


#map -- run for all elements in array


my_array = range(12) # [1,2...12]

squares = map(lambda x: x*x , my_array)

print  "Obtained using map %s" % squares


#-- List comphrension

squares_list_comp = [x * x for x in my_array]

print  "Obtained usning List comphrension %s"% squares_list_comp


# Generators

def sq_gen () :
    for item in range(8,10) :
        yield item * item


# Generators
foobar = sq_gen ()
print foobar.next()
print foobar.next()
print foobar.next()
print foobar.next()
print foobar.next()
print foobar.next()
