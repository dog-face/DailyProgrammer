class rectangle:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    def get_intersect(self, other):
        intersect_left = max(self.left, other.left)
        intersect_right = min(self.right, other.right)
        intersect_bottom = max(self.bottom, other.bottom)
        intersect_top = min(self.top, other.top)

        print("intersect_x_min: " + str(intersect_left))
        print("intersect_x_max: " + str(intersect_right))
        print("intersect_y_min: " + str(intersect_bottom))
        print("intersect_y_max: " + str(intersect_top))

        if intersect_right < intersect_left or intersect_top < intersect_bottom:
            return 0

        intersect_rect = rectangle(intersect_left, intersect_bottom, intersect_right, intersect_top)
        return intersect_rect

    def get_area(self):

        delta_x = self.left - self.right
        delta_y = self.top - self.bottom

        area = delta_x * delta_y
        if area < 0:
            area = 0
        return area

    def is_contained(self, x, y):
        return x > self.left and x < self.right and y > self.bottom and y < self.top

    def is_point_contained(self, point):
        x = point[0]
        y = point[1]
        return self.is_contained(x, y)


rect1 = rectangle(-4,4, -0.5,2)
rect2 = rectangle(0.5,1, 3.5,3)


print("Intersection area: " + str(rect1.get_intersect(rect2)))



#0,0 2,2
#1,1 3,3
