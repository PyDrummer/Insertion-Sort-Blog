# Insertion Sort

## Challenge Description
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

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

## Approach & Efficiency
First google is my best friend. Utilized this post from geeks for geeks (sited source) https://www.geeksforgeeks.org/python-program-for-insertion-sort/
Next I didn't fully understand what was going on so I used this python visualizer to help me understand: http://pythontutor.com/visualize.html#mode=edit


## Solution
[Link to blog](blog.md)

To-do:
[x] Write the blog
[x] Add the code
[x] Create unit tests

