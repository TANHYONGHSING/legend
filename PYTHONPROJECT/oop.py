#define a class called CookieCutter

class CookieCutter:
    #define the _init_method, which is called when a new object is creasted

    def __init__(self, shape):
        self.shape = shape

#define a method called cut_cookie, which prints a message indicating that a cookie has been cut 
    def cut_cookie(self):
        print(f"A {self.shape}-shaped cookie has been cut !")

#create a new object of the CookieCutter class with shape "circle"

circle_cutter = CookieCutter("circle")

#call the cut_cookie method on the circle_cutter obj

circle_cutter.cut_cookie()

#Output : "A circle has been cut"

# a new object = rectangle 
rectangle_cutter = CookieCutter("rectangle")

rectangle_cutter.cut_cookie()

# a new object = pyramid
rectangle_cutter = CookieCutter("pyramid")

rectangle_cutter.cut_cookie()