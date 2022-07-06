"""
Memory process and types of memory:

A program may run in three stages in memory(RAM) like:

1. Code loader => Application when clicked entier code will load.

2. Stack => stack takes place when compiler load the code and provide a space for two things:
            * variables (object)(any type)  -> name,address of it

3. Heap  => Heap contain actual values of the object. stack will refer to heap for values using address of objects in stack. 


"""
 
# About stack
# -----------

a = 10

b = 10 # Both a and b value is same so only one value stored in heap

print(id(a))
print(id(b))# is same because the address is stored in stack, the value is stored in heap,value only one copy because python won't create another same value instead it map reference to it.


a,b = 11,12
#now a and b assigned to new values now new address created in stack and heap got new values and the old value 10 is not pointed to any reference address, reference_count is 0. 

#now python trigger garbage collector

#GARBAGE COLLECTOR:

#garbage collector will automatically collect the values which has 0 reference count so allocating and deallocating is done by PVM programmer no need to worry about stack memory free up.

#call stack 

# it is a small space in stack where every functions takes place. inside the values of function will stored in stack and heap memory when the func calls, when func return all will be removed. 
def stack(): 
    x = 10
    print(x)

stack()

#life of function and its values in memory only when function calls and when it return it will be poped from memory same for classes and methods(fucntions).

#stack fill memory error = stack overflow


#Heap

#heap is just can't be access directly using code we can using pointer not recommended.

#heap memory  == RAM memory in computer

#As said heap stores the values of the program and pass values when the stack needed by reference


#heap fills full error = out of memory

"""
Parameter                               STACK                           HEAP

Basic                      Memory is allocated in a         Memory is allocated in any random order.
                           contiguous block.	


for more difference refer geeks for geeks

"""