class FunctionalHelper:

    @staticmethod
    def forEach(arr: list, func: callable):
        for i in arr:
            func(i)

    @staticmethod
    def map(arr: list, func: callable):
        return [func(i) for i in arr]

    @staticmethod
    def filter(arr: list, func: callable):
        return [i for i in arr if func(i)]

    @staticmethod
    def reduce(arr: list, func: callable, initial_value: any):
        result = initial_value
        for i in arr:
            result = func(result, i)
        return result


FunctionalHelper.forEach([1, 2, 3, 4, 5], lambda x: print(x))
double = FunctionalHelper.map([1, 2, 3, 4, 5], lambda x: x * 2)
print(double)
even = FunctionalHelper.filter([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
print(even)
total = FunctionalHelper.reduce([1, 2, 3, 4, 5], lambda acc, val: acc + val, 0)
print(total)