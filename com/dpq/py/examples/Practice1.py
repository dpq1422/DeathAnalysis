import sys
import calendar
from datetime import date


class MyPractice:

    def __init__(self, name):
        self.name = name

    def printSample(self):
        print("Hello i am " + self.name)

    @staticmethod
    def getPythonVersion():
        return {"Python version": sys.version, "Version info.": sys.version_info}

    @staticmethod
    def getCurrentDateAndTime():
        import datetime
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

    @staticmethod
    def getAreOfCircle(r):
        from math import pi
        r = float(r)
        print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

    @staticmethod
    def stringWithReverseOrder(name, delimiter):
        name = str(name)
        if name == "" or name.rstrip() == "":
            return name
        if name.__contains__(delimiter):
            return name.split(delimiter)[1] + delimiter + name.split(delimiter)[0]

        return name

    @staticmethod
    def covertIntoListAndTuple(values, delimiter):
        lst = str(values).split(delimiter)
        print("List is:", lst)
        print("Tuple is:", tuple(lst))

    @staticmethod
    def getFileExtension(fileName):
        return str(fileName).split(".")[1]

    @staticmethod
    def getFirstAndLastElement(colours):
        print("first value: "+colours[0])
        print("first value: " + colours[len(colours)-1])

    @staticmethod
    def getCurrentMonth(year, month):
        print("Current month: ", calendar.month(year, month))

    @staticmethod
    def diffBWDates(firstDate, lastDate):
        f_date = date(firstDate.__getitem__(0), firstDate.__getitem__(1), firstDate.__getitem__(2))
        l_date = date(lastDate.__getitem__(0), lastDate.__getitem__(1), lastDate.__getitem__(2))
        delta = l_date - f_date
        print(delta.days)


if __name__ == '__main__':
    MyPractice("deepak").printSample()
    # example 1
    # Write a Python program to get the Python version
    pythonVersion = MyPractice.getPythonVersion().get("Python version")
    pythonVersionDetailedInfo = MyPractice.getPythonVersion().get("Version info.")
    print("Python version", pythonVersion)
    print("Version information", pythonVersionDetailedInfo)

    # 2.Write a Python program to display the current date and time. output sample:2014-07-05 14:34:14
    MyPractice.getCurrentDateAndTime()

    # 3. Write a Python program which accepts the radius of a circle from the user and compute the area
    MyPractice.getAreOfCircle(1.1)
    # 4.Write a Python program which accepts the user's first and last name and print them in reverse
    # order with a space between them.
    print(MyPractice.stringWithReverseOrder("deepak bhardwaj", " "))

    # 5 Write a Python program which accepts a sequence of comma-separated numbers from user and
    # generate a list and a tuple with those numbers
    MyPractice.covertIntoListAndTuple("1,2,76,12,90,56,23", ",")
    # 6 Write a Python program to accept a filename from the user and print the extension of that
    print(MyPractice.getFileExtension("country.csv"))

    # 7. Write a Python program to display the first and last colors from the following list
    MyPractice.getFirstAndLastElement(["Red", "Green", "White", "Black"])

    # 8. Write a Python program to print the calendar of a given month and year.
    MyPractice.getCurrentMonth(2020 , 9)

    # 9 Write a Python program to calculate number of days between two dates.
    MyPractice.diffBWDates((2014, 7, 2), (2015, 7, 11))