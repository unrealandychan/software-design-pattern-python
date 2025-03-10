# Naming is a part of clean code. It is very important to name your variables, functions, classes, etc. in a way
# that is easy to understand. In this chapter, we will discuss some naming conventions that you should follow to
# write clean code.

# 1. Use meaningful names
name = "John"  # Bad
username = "John"  # Good

d = 5  # Bad
days = 5  #Good

# Try to make your names as descriptive as possible. This will make your code easier to understand.
# And in different scope, use different names for variables.
# For example, if you have a variable named "i" in a loop, don't use the same variable name in another loop.
# This will make your code more readable and less error-prone.

# 2. Use camelCase for variable names
# CamelCase is a naming convention in which the first letter of each word is capitalized except for the first word.
# For example:
firstName = "John"  # CamelCase <- I prefer this one
first_name = "John"  # Snake case

# 3. Use the name that can be pronounced
# This will make it easier for you to discuss your code with others.
# For example:
genymdhms = 5  # Bad
generation_year_month_day_hour_minute_second = 5  # Good

# 4. Use the name that can be searched
# For example:
x = 5  # Bad
num_of_students = 5  # Good


# 5. Use the name that can be explained
# For example:
def calculate(x, y):  # Bad
    return x + y


def calculate_sum(x, y):  # Good
    return x + y


# Naming for Classes
# 1. Use PascalCase for class names
# PascalCase is a naming convention in which the first letter of each word is capitalized.
# For example:
class user:  # Bad
    pass


class User:  # Good
    pass


# Naming for Functions or methods
# 1. Use snake_case for function names
# Snake case is a naming convention in which the words are separated by underscores.
# For example:
def calculateSum():  # Bad
    pass


def calculate_sum():  # Good
    pass


# Adding context to the name (with meaning)
# For example:
# Bad
class PrinterGuessStatistic:
    number: str = ""
    verb: str = ""
    pluralModifier: str = ""

    def __init(self, candidate: str, count: int):
        self.candidate = candidate
        self.count = count

    def printGuessStatistics(self):
        if self.count == 0:
            self.number = "no"
            self.verb = "are"
            self.pluralModifier = "s"
        elif self.count == 1:
            self.number = "1"
            self.verb = "is"
            self.pluralModifier = ""
        else:
            self.number = str(self.count)
            self.verb = "are"
            self.pluralModifier = "s"
        print(f"There {self.verb} {self.number} {self.candidate}{self.pluralModifier}")


# Good
class GuessStatisticsMessageNew:
    number: str = ""
    verb: str = ""
    pluralModifier: str = ""

    def __init(self, candidate: str, count: int):
        self.candidate = candidate
        self.count = count

    def thereAreNoLetters(self):
        self.number = "no"
        self.verb = "are"
        self.pluralModifier = "s"

    def thereIsOneLetter(self):
        self.number = "1"
        self.verb = "is"
        self.pluralModifier = ""

    def thereAreManyLetters(self):
        self.number = str(self.count)
        self.verb = "are"
        self.pluralModifier = "s"

    def createPluralDependentMessageParts(self):
        if self.count == 0:
            self.thereAreNoLetters()
        elif self.count == 1:
            self.thereIsOneLetter()
        else:
            self.thereAreManyLetters()

    def make(self):
        self.createPluralDependentMessageParts()
        return f"There {self.verb} {self.number} {self.candidate}{self.pluralModifier}"


# Keep in mind that the names should be meaningful and easy to understand.
# Avoid unnecessary abbreviations and try to make your names as descriptive as possible.
# This will make your code easier to read and maintain.
# Example:
# Bad
APP_canvas_date = "2021-01-01"
# Good
app_launch_date = "2021-01-01"


# Bad
def calc(x, y):
    return x + y


# Good
def calculate_sum(x, y):
    return x + y

# In the next chapter, we will discuss function naming and restructuring.
