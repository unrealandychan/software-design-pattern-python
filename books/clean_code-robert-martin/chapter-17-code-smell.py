# Code Smell
# There are some common code smells that you should be aware of.


# I. Comments
# 1 - Inappropriate Information: Comments should not contain information that is already present in the
# code. Comments should be used to explain why the code is doing something, not what the code is doing.

# 2 - Obsolete Comments: Comments that are no longer relevant should be removed. Obsolete comments can be misleading and
# confusing.

# 3 - Redundant Comments: Comments that are redundant should be removed. Redundant comments can clutter the code and
# make it harder to read.

# 4 - Poorly Written Comments: Comments should be well-written and easy to understand. Poorly written comments can be
# confusing and misleading.

# 5 - Commented-Out Code: Commented-out code should be removed. Commented-out code can
# clutter the code and make it harder to read.

# II. Environment
# 1 - Build Requires More Than One Step: The build process should be simple and straightforward. If the build process
# requires more than one step, it can be a sign that the code is too complex.

# 2 - Tests Require More Than One Step: The test process should be simple and straightforward. If the test process
# requires more than one step, it can be a sign that the code is too complex.

# III. Functions
# 1 - Too Many Arguments: Functions should have as few arguments as possible. If a function has more than three
# arguments, it can be a sign that the function is doing too much.

# 2 - Output Arguments: Functions should not have output arguments. Output arguments make the code harder to read and
# maintain.

# 3 - Flag Arguments: Functions should not have flag arguments. Flag arguments make the code harder to read and
# maintain. Since the function does more than one thing.

# 4 - Dead Function: Dead code should be removed. Dead code can clutter the code and make it harder to read.

# IV. General
# 1 - Many Language in One Source File: Source files should be written in a single language. Mixing multiple languages
# in a single source file can be confusing and make the code harder to read.

# 2 - Obvious Behavior is Unimplemented: Obvious behavior should be implemented. If the code does not behave as
# expected, it can be a sign that the code is incorrect.

# 3 - Incorrect Behavior at the Boundaries: The code should behave correctly at the boundaries. If the code behaves
# incorrectly at the boundaries, it can be a sign that the code is incorrect.

# 4 - Overridden Safeties: Safeties should not be overridden. Overriding safeties can make the code less safe and
# introduce bugs.

# 5 - Duplication: Duplication should be removed. Duplication can make the code harder to read and maintain.
# In most of the cases, there are unnecessary code blocks that can be removed like the following:
# if discount_type == "Christmas":
#     return total * 0.5
# elif discount_type == "Easter":
#     return total * 0.2
# elif discount_type == "New Year":
#     return total * 0.3
# else:
#     return total

# 6 - Code at Wrong Level of Abstraction: Code should be written at the right level of abstraction. If the code is
# written at the wrong level of abstraction, it can be a sign that the code is incorrect.

# 7 - Base Classes Depending on Their Derivatives: Base classes should not depend on their derivatives. If a base class
# depends on its derivatives, it can be a sign that the code is incorrect.

# 8 - Too Much Information: Classes should have as few responsibilities as possible. If a class has too much
# information, it can be a sign that the class is doing too much.

# 9 - Dead Code: Dead code should be removed. Dead code can clutter the code and make it harder to read.

# 10 - Vertical Separation: Related code should be vertically separated. If related code is not vertically separated,
# it can be a sign that the code is incorrect.

# 11 - Inconsistency: Code should be consistent. For example, if you are using camelCase for variable names, you should
# use camelCase for all variable names. Inconsistency can make the code harder to read and maintain. And in different
# scope, use different names for variables.

# 12 - Clutter: Clutter should be removed. Clutter can make the code harder to read and maintain.

# 13 - Artificial Coupling: Classes should not be artificially coupled. If classes are artificially coupled, it can be a
# sign that the code is incorrect.

# 14 - Feature Envy: Methods should not be envious of other classes. If a method is envious of another class,
# it can be a sign that the code is incorrect.

# 15 - Selector Arguments: Functions should not have selector arguments. Selector arguments make the code harder to read
# and maintain. Since the function does more than one thing. This is a lazy way to write code and it is a code smell.

# 16 - Obscured Intent: Code should be easy to understand. If the code is hard to understand, it can be a sign that the
# code is incorrect.

# 17 - Misplaced Responsibility: Classes should have a single responsibility. If a class has more than one
# responsibility, it can be a sign that the class is doing too much.

# 18 - Inappropriate Static: Static methods should be used appropriately. If a method is static, it should be used
# appropriately. In Python, static methods are used to define methods that do not operate on instances of a class and
# that's not meant to be overridden.

# 19 - Use of Magic Numbers: Magic numbers should be avoided.

# 20 Function Names Should Say What They Do: Function names should say what they do. If a function name does not say
# what the function does, it can be a sign that the function is incorrect.

# 21 - Understand the Algorithm: You should understand the algorithm before you start coding. If you do not understand
# the algorithm, it can be a sign that the code is incorrect.

# 22- Make Logical Dependencies Physical: Logical dependencies should be made physical. If logical dependencies are not
# made physical, it can be a sign that the code is incorrect.

# 23 - Avoid Negative Conditionals: Negative conditionals should be avoided. If a conditional is negative, it can be a
# sign that the code is incorrect.

# 24 - Prefer Polymporphism to If/Else or Switch/Case: Polymorphism should be preferred to if/else or switch/case.
# If/else or switch/case should be avoided. Polymorphism is a powerful technique that allows you to write cleaner and
# more maintainable code.

# 25 - Follow Standard Conventions: Standard conventions should be followed. If standard conventions are not followed,
# it can be a sign that the code is incorrect.

# 26 - Replace Magic Numbers with Named Constants: Magic numbers should be replaced with named constants. If a magic
# number is used, it can be a sign that the code is incorrect.

# 27 - Be Precise: Code should be precise. If the code is imprecise, it can be a sign that the code is incorrect.

