
# Minimum time required python file

Write a function which takes two arguments: a list of customers and the number of open cash registers. Each customer is represented by an integer which indicates the amount of time needed to checkout. Assuming that customers are served in their original order, your function should output the minimum time required to serve all customers.

Examples:

get_checkout_time([5, 1, 3], 1) should return 9

get_checkout_time([10, 3, 4, 2], 2) should return 10 because while the first register is busy serving customer[0] the second register can serve all remaining customers.

### [Solution]():

* Recursive function which require list of customers for every open cash register with a flag for availability of more customers.
* Stepping each customer with least time requirement in the line.
* Adding next customers in the list.





# Subset python file

Write a function that satisfies the following rules:
Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.

Examples:

["hello", "Hello"]
should return true because all of the letters in the second string are present in the first, ignoring case.

["hello", "hey"]
should return false because the string "hello" does not contain a "y".

["Alien", "line"]
should return true because all of the letters in "line" are present in "Alien".

### [Solution]():

1. Function contains logic of set difference method generally used in mathematics set.
2. Function contains all method that iterate the condiition for all elements.
3. Function contains while loop to iterate each element one by one.
4. Function contains issubset predefined function with subset finding concept.


