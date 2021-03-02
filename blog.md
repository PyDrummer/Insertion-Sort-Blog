# Insertion Sort

## What is it?

A sorting algorithm that evaluates an array and sorts as it goes. If a value is greater than another in the array then you continue to push that value farther into the array until it's sorted lowest int to greatest int.

The Pseudo code:
```
InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

What we need to do is first declare our function insertionsort that passes in an array of ints.

Next we begin a for loop "for i in the range of 1, and the length of the array".

Now we set a mover variable which will equal the array of ints at i. This will be the variable that will move through the array first checking if it's greater than other values.

Set a follower variable which will equal i subtracted by 1.

We can now begin a while loop with this condition: while follower is greater than or equal to 0 and our mover is less than our array at position follower then:

Our array at the position of follower + 1 equals our array at follower. Our follower now is subtracted by 1 and finally our array at the follower + 1 is now equal to the mover.

## The break down (in steps)

This algorithm will iterate through each int and compare the mover to the array at the follower.

<img src="https://i.imgur.com/4ZRRe0H.png">

In the screenshot i is currently equal to 1, the mover (at array[1]) is 4, the follower is at 0. We go into the while loop.

<img src="https://i.imgur.com/dhOw3BZ.png">

Now in the while loop, at the array where follower+1 is equal to the follower (in this case 8), follower then gets subtracted by one making it -1 breaking the while loop and making the array at that follower = to the mover (4)

<img src="https://i.imgur.com/ATrlfPy.png">

Since the while loop is broken we go to the next iteration of the for loop. So i becomes 2 and mover becomes 23, and follower becomes 1 (8).

<img src="https://i.imgur.com/GXdQ6m6.png">

Since 23 is greater than 8 it the "while mover < an_array[follower]" breaks the loop. Bringing us to the next iteration of the loop.

Now i becomes 3, mover is 42 and follower is 2 (23) the same condition as above makes the while loop break and go to the next iteration.

This time i is 4, mover is 16 and follower is 3 (42). Since 42 is greater than 16 we can go into the while loop.

<img src="https://i.imgur.com/MxmnU6P.png">

42 now takes the place of 4 but the while loop still continues because 16 is less than 23.

<img src="https://i.imgur.com/3rjdvzH.png">

Since 23 has now moved into the place of 3 and 16 is in the place of 2, 16 is less than 23 but greater than 8 so we move to the next iteration in the loop.

Now i is 5, mover becomes 15 and follower is 4 (42).

Because of the same while condition, 42 now takes the place of 5, mover gets compared to then next iteration below (3) which is 23. It is less than so it is compared to the next iteration (2) which is 16, and it is still less than.

Only after comparing to (1) which is 8 does the while loop break and store 15 at the place of 2.

<img src="https://i.imgur.com/TWLmf0B.png">

In conclusion the last iteration has a return of none so the loop has completed and now your array/list has been sorted!

I hope this blog helps to demystify the insert sort algorithm.

This was programmed in python. 

- I got assistance for the algorithm from: https://www.geeksforgeeks.org/python-program-for-insertion-sort/ 
- The visualizer used is: http://pythontutor.com/visualize.html#mode=edit
