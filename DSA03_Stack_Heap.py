"""
A program may run in three stages in memory like:

1.A program itself loading like compiler of the language and vital things to run code.

2.Stack  = This is a temproray memory usually keep in memory like variables, expressions and values in local scope based on which part of code running. if entire module running it memory all varibales and expressions.

3.Heap  = stack uses the Heap to store values of variable, variable types, address of the variables in memory is heap work


"""

"""
Key Differences Between Stack and Heap Allocations 
 

In a stack, the allocation and de-allocation are automatically done by the compiler whereas in heap, it needs to be done by the programmer manually.

Handling of Heap frame is costlier than the handling of the stack frame.

Memory shortage problem is more likely to happen in stack whereas the main issue in heap memory is fragmentation.

Stack frame access is easier than the heap frame as the stack have a small region of memory and is cache-friendly, but in case of heap frames which are dispersed throughout the memory so it causes more cache misses.

A stack is not flexible, the memory size allotted cannot be changed whereas a heap is flexible, and the allotted memory can be altered.

Accessing time of heap takes is more than a stack.

"""