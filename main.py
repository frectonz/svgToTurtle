#!./venv/bin/python3

from PointsGeneratorClass import PointsGenerator
from PyFileGeneratorClass import PyFileGenerator
from TurtleDrawerClass import TurtleDrawer
import turtle

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="A tool to generate python turtle scripts from svg files.")
    parser.add_argument("svgFile", type=str,
                        help="the svg file to be converted")

    args = parser.parse_args()

    if args.svgFile:
        numOfPointsInput = int(input("Enter number of points: "))
        verboseInput = input("Enter verbosity (y/n): ")

        fileName = args.svgFile
        numOfPoints = numOfPointsInput
        verbose = verboseInput == "y"
        draw = False
        generateFile = True

        # Points Generation
        pointsGenerator = PointsGenerator(fileName, numOfPoints, verbose)
        points = pointsGenerator.generate()

        # Python file generator
        if generateFile:
            pyFileGenerator = PyFileGenerator(points, fileName, verbose)
            pyFileGenerator.generate()

        # Turtle Drawer
        if draw:
            turtleDrawer = TurtleDrawer(points, turtle)
            turtleDrawer.draw()
