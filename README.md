# Max_Points_On_Line
## Dynamic Programming Solution
The key of this question is about how the new line is considerated.
Let' s begin with only two points, obviously in this case, the maximum points is 2, and there is at most 1 line.
If we start by adding the third point to the set, we can see that:
there are two cases, the first case is that this point is on the previous line(one of),
in this case, the number of points on that previous line is increased by adding this 
new point on it.
In case 2, however, the result is creating two more lines, since it's not on any of the previous lines.
Now we have 3 lines in total, we can use the similar strategy when we are adding the 4th point to the set, the key idea is, for any line that the new point is on, we add the new point to the line, for any line this point is not on, we create new lines by connecting the new point to those points on those lines.

There are many other details to consider, for example, it's far more easy to do when you add the overlapping points together(For instance, there are 3 points on same location(2,3), what you do now is only save one(2,3) point and give it an attribute(unit = 3) ). 
The rest of the details are in the code. 
If there is any problem or potential issue, let me know pls.
Tx
