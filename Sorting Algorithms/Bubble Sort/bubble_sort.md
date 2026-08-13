# Bubble Sort.

- Bubble sort is a very basic sorting algorithm named for the way elements "bubble up" to the top of the list.
- Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:
- Set swapping to True
- Set end to the length of the input list
- While swapping is True:
- Set swapping to False
- For i from the 2nd element to end:
- If the (i-1)th element of the input list is greater than the ith element:
- Swap the (i-1)th element and the ith element
- Set swapping to True
- Decrement end by one
- Return the sorted list