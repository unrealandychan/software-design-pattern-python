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
