# Function
# Principles of Good function is SHORT, CLEAN, and DO ONE THING.
# Functions should be small. Functions should be smaller than that, and smaller than that.
# In Python , we have indentation to help us with this.
# Quote: Function should do one thing. They should do it well. They should do it only.
from abc import ABC


# Example
# Bad Code
class Employee:

    def __init__(self, payType):
        self.payType = payType


def calculatePay(employee: Employee):
    if employee.payType == "hourly":
        return "calculating hourly pay"
    elif employee.payType == "salaried":
        return "calculating salaried pay"
    elif employee.payType == "commission":
        return "calculating commission pay"
    else:
        raise ValueError("Invalid pay type")


# You can see that the calculatePay function is doing more than one thing. It is calculating pay based on the payType
# of the employee. This violates the Single Responsibility Principle. The function should do one thing and do it
# well. The function should not be responsible for checking the payType of the employee. This should be done before
# calling the function. The function should only calculate the pay based on the payType. This will make the function
# easier to read and maintain.

# Good Code
class Employee:

    def __init__(self, payType):
        self.payType = payType

    def calculatePay(self):
        return "calculating pay"


class HourlyEmployee(Employee):

    def calculatePay(self):
        return "calculating hourly pay"


class SalariedEmployee(Employee):

    def calculatePay(self):
        return "calculating salaried pay"


class CommissionEmployee(Employee):

    def calculatePay(self):
        return "calculating commission pay"


class EmployeeFactory(ABC):

    def createEmployee(self, payType):
        pass


class EmployeeFactoryImpl(EmployeeFactory):

    def createEmployee(self, payType):
        if payType == "hourly":
            return HourlyEmployee()
        elif payType == "salaried":
            return SalariedEmployee()
        elif payType == "commission":
            return CommissionEmployee()
        else:
            raise ValueError("Invalid pay type")


# It is better to use a factory pattern to create objects. This will make the code more flexible and easier to maintain.
# Although the factory pattern is not necessary in this example, it is a good practice to use it when creating objects.
# It is a good practice to use design patterns when necessary. Design patterns are proven solutions to common problems
# that software developers face. They help us write better code that is easier to read and maintain.

# Arguments of a function
# Ideally, a function should have zero arguments. This is not always possible, but it is a good practice to keep the
# number of arguments as low as possible. The more arguments a function has, the harder it is to read and maintain.
# If a function has more than three arguments, it is a sign that the function is doing too much. You should consider
# refactoring the function into smaller functions that take fewer arguments. This will make the code easier to read and
# maintain.

# Example
# Bad Code
class Config:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


def createConfig(host, port, username, password):
    return ConfigNew(host, port, username, password)


# Good Code
class ConfigNew:
    def __init__(self, data):
        self.host = data["host"]
        self.port = data["port"]
        self.username = data["username"]
        self.password = data["password"]


def createConfigNew(data):
    return ConfigNew(data)


# Flag arguments are a code smell. It is a sign that the function is doing more than one thing. You should consider
# refactoring the function into smaller functions that take fewer arguments. This will make the code easier to read and
# maintain.

# Example
# Bad Code
def render(isPreview):
    if isPreview:
        return "rendering preview"
    else:
        return "rendering production"


# Good Code
# This is a better way to write the function. It is easier to read and maintain.
def renderPreview():
    return "rendering preview"


def renderProduction():
    return "rendering production"

# Side Effects
# A function should not have side effects. A side effect is any change in the state of the program that is not
# explicitly returned by the function. Side effects make the code harder to read and maintain. They make the code
# harder to test and debug. You should avoid side effects as much as possible. You should try to write functions that
# are pure. A pure function is a function that has no side effects. It takes some input and returns some output.
# Although it is not always possible to write pure functions, you should strive to write functions that have as few
# side effects as possible. This will make the code easier to read and maintain.

