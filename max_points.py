class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

# Need to do that for some unknown precompiled problem
# Index is used to track the points for further usage,
# uni means how many overlapping points on same position
class my_Point:
    def __init__(self, p):
        self.x = p.x
        self.y = p.y
        self.index = 0
        self.uni =1
        
def to_my_Point(points):
    new_points = []
    for point in points:
        new_points.append(my_Point(point))
    return new_points

# Each line is defined by two points, and later all the points on that line will be added during 
# Iterations.
class Line:
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.point_list = [p1,p2]
        self.max_ps = p1.uni + p2.uni
        self.p_index = [p1.index, p2.index]
        
    def onLine(self,p3):
        x = p3.x
        y = p3.y
        if(points_equal(self.p1,self.p2)):
            self.p2 = p3
            return True
        if(self.p1.x == self.p2.x):
            return self.p1.x == p3.x
        elif(self.p1.y == self.p2.y):
            return self.p1.y == p3.y
        elif(points_equal(self.p1,p3) or points_equal(self.p2,p3)):
            return True
        else:
            if((x-self.p2.x)*(self.p1.y - self.p2.y) == (y - self.p2.y)*(self.p1.x - self.p2.x)):
                return True
        return False
    
    def addPoint(self,p):
        self.point_list.append(p)
        self.max_ps += p.uni
        self.p_index.append(p.index)

# Draw the line expect for those one in the eliminate list
def drawLine(points,new_point,elim_index):
    new_list = []
    for point in points:
        if not (point.index in elim_index):
            new_list.append(Line(point,new_point))
    return new_list

# Test if two points are overlapping.
def points_equal(p1,p2):
    if(p1.x == p2.x and p1.y == p2.y):
        return True
    else:
        return False
# Test if a point is in a point list, also record the overlapping points.     
def in_set(points,p):
    for point in points:
        if(p.x == point.x and p.y == point.y):
            point.uni += 1
            return True
    return False

# Return the points in a list that there are no overlapping points,
# but also count the number of overlapping points, carry that information in the 
# point.uni
def unique_set(points):
    unique_set = []
    for point in points:
        if not(in_set(unique_set,point)):
            unique_set.append(point)
    return unique_set

class Solution:
    
    def maxPoints(self, ori_points: List[Point]) -> int:
        du_points = to_my_Point(ori_points) 
        points = unique_set(du_points)
        p_len = len(points)
        for i,point in enumerate(points):
            point.index = i

        if(p_len == 0):
            return 0
        elif(p_len == 1):
            return points[0].uni
        
        line_set = [Line(points[0],points[1])]
        max_p = line_set[0].max_ps
        
        for i in range(2,p_len): # DP process
            elim_ind = []
            for line in line_set:
                if(line.onLine(points[i])):
                    elim_ind +=line.p_index
                    line.addPoint(points[i])
                if(line.max_ps > max_p):
                    max_p = line.max_ps
           
            add_list = drawLine(points[0:i],points[i],elim_ind)
            line_set += add_list

        return max_p