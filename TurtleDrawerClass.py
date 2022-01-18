class TurtleDrawer:
    def __init__(self, points, turtle):
        self.points = points
        self.turtle = turtle

    def draw(self):
        screen = self.turtle.Screen()
        t = self.turtle.Turtle()

        t.speed(0)

        for ptGroup in self.points:
            x, y = ptGroup[0]

            t.penup()
            t.setpos(x, y)
            t.pendown()

            for x, y in ptGroup:
                t.setpos(x, y)

        screen.mainloop()
