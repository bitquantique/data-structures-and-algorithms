# O(n) - Order “n”.

- O(n) is very common - When the number of steps in an algorithm grows at the same rate as its input size, it's classified as O(n).
- For example, our find min algorithm from earlier is O(n):
- Set min to positive infinity.
- For each number in the list, compare it to min. If it is smaller, set min to that number.
- min is now set to the smallest number in the list.
- The input to the find min algorithm is a list of size n. Because we loop over each item in the input once, we add one step to our algorithm for each item in our list.