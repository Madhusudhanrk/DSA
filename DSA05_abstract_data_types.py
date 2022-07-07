# Abstract DataType: **********************************************************************
# ------------------

# data type:
# ------------

# it conatains two things

#  1.Domain means int or float type

#  2.Operations, int can perform addition, string can't

#eg: s = "madhu" => s.len()

# user defined data type:
# -------------------------

# like class inside class we can perform multiple things using methods and primitive data types.

#eg: b = book(), b.count_books()  here we defined class and count_books in class user implemented

#based on how user implemented it will work.

# Abstract data type(ADT): built-in
# ------------------------------------------------------------------------------------------------

#simpley we cannot define ADT types

# We only allowed to use it not allowed to implement any operations in their definitions

# List = [] we can use list like list = [1,2,3,4]

# list.count() or list.index(value) like hear we are not allowed to define what list.methods do we are only allowed to use them this is abstract data type.
 
# user is only allowed to use them by using their function name and providing operating values not allowed to implement any thing with their definition because they are abstracted(hidden) 

# Why ADT:
# --------

# because every bit program writing takes too much time

# user writing program called client program, this program just take ADT datatyes for its work and no need to worry about its implementation(definition) in future if it is changed no problem to client program becuase by changing funtions we get implementations use in abstract form.

# --------------------------------------------------------------------------------------------------

# Abstract data type(ADT) we define:
# -----------------------------------
# own data structure means own definition for functions in this DS.

# Think of ADT as a black box which hides the inner structure and design of the data type

#List ADT we created and we can use pop(),insert() methods with our custom definition for list data structure.

# Features of ADT:
# -----------------

"""
Abstraction:              The user does not need to know the implementation of the data structure.
Better Conceptualization: ADT gives us a better conceptualization of the real world.
Robust:                   The program is robust and has the ability to catch errors

"""
 
"""
conclusion:

    we need to define abstract datatypes like list, graphs, trees, array N of DS
    we need to create our functions(methods) for this DS or data types.
    we need to use them in our client program like custom ADT.FUNC() this definition written by us but
    is abstracted from client program.
"""