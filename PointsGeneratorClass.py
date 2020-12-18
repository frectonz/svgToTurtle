from svg.path import parse_path
from bs4 import BeautifulSoup
from util import verbosePrint


class PointsGenerator:
    def __init__(self, filename, numOfPoints, verbose):
        self.filename = filename
        self.numOfPoints = numOfPoints
        self.verbose = verbose

    def readSVGFile(self):
        with open(self.filename, "r") as svgFile:
            content = svgFile.read()
        return content

    def extractPathsFromSVG(self):
        svg = self.readSVGFile()
        soup = BeautifulSoup(svg, "lxml")

        verbosePrint(self.verbose, "Finding all paths...")
        paths = soup.findAll("path")
        verbosePrint(self.verbose, "Ended finding all paths.")

        return paths

    def extractDAttrsFromPaths(self):
        paths = self.extractPathsFromSVG()
        dAttrs = []

        verbosePrint(self.verbose, "Started collecting d attrs...")
        for path in paths:
            dAttrs.append(path.get("d"))
        verbosePrint(self.verbose, "Ended collecting d attrs.")

        return dAttrs

    def parseDAttrsToComplexNumbers(self):
        dAttrs = self.extractDAttrsFromPaths()
        parsedPaths = []

        verbosePrint(self.verbose, "Started parsing d attrs...")
        for dAttr in dAttrs:
            parsedPaths.append(parse_path(dAttr))
        verbosePrint(self.verbose, "Ended parsing d attrs.")

        return parsedPaths

    def extractXAndYValuesFromParsedPaths(self):
        parsedPaths = self.parseDAttrsToComplexNumbers()
        points = []
        numOfPts = self.numOfPoints

        verbosePrint(
            self.verbose, "Started extracting x and y values from paths...")
        for parsedPath in parsedPaths:
            pts = [(p.real, p.imag) for p in (parsedPath.point(i / numOfPts)
                                              for i in range(0, numOfPts + 1))]
            points.append(pts)
        verbosePrint(
            self.verbose, "Ended extracting x and y values from paths.")

        return points

    def generate(self):
        return self.extractXAndYValuesFromParsedPaths()
