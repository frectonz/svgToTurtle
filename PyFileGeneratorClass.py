from util import verbosePrint


class PyFileGenerator:
    def __init__(self, points, pyFilename, verbose, noTrace=False):
        self.points = points
        self.pyFilename = pyFilename
        self.verbose = verbose
        self.noTrace = noTrace

    def generatePythonFile(self):
        fileContent = "import turtle\n\n"
        fileContent += "WIDTH = 800\n"
        fileContent += "HEIGHT = 600\n\n"
        fileContent += "screen = turtle.Screen()\n"
        fileContent += "t = turtle.Turtle()\n\n"
        fileContent += "turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)\n"
        fileContent += "t.speed(0)\n\n"

        if self.noTrace:
            fileContent += "screen.tracer(0)"

        for ptGroup in self.points:
            x, y = ptGroup[0]

            fileContent += "t.penup()\n"
            fileContent += "t.setpos({x}, {y})\n".format(x=x, y=y)
            fileContent += "t.pendown()\n\n"

            for x, y in ptGroup:
                fileContent += "t.setpos({x}, {y})\n".format(x=x, y=y)

        fileContent += "\nscreen.mainloop()\n"

        return fileContent

    def writePythonFile(self):
        fileContent = self.generatePythonFile()

        verbosePrint(self.verbose, "Started generating file...")
        with open("{filename}.py".format(filename=self.pyFilename), "w") as pyFile:
            pyFile.write(fileContent)
        verbosePrint(self.verbose, "Ended generating file.")

    def generate(self):
        self.writePythonFile()
