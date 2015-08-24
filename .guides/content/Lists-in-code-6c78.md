Let's see how we actually work with lists in our code.

## The `print` function
This function lets you write things to the screen.

## List Example 1
The first example shows one way of creating an list. We first create an empty list using 

```python
list1 = []
```

Then we manually add values on the following lines. Finally, we print them all out in a loop.

## List Example 2
The second example shows how we can create and populate a list using a single line of code. We then print out the results in the same way.

```python
list2 = ['Mary', 'had' , 'a', 'little', 'lamb']
```

## for element in list

Python makes it really easy to loop over every element in a list using, see the line below. The loop walks through the list, starting at index 0, and assigns it to `element` (you can call the variable whatever you want). 

```python
for element in list:
  # do something with the list element
```