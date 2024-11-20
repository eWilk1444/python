"""
some stuff i guess
"""


# class PrimeIterator:
#     def __init__(self, max):
#         self.max = max
#         self.number = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.number += 1
#         while not self.is_prime(self.number):
#             self.number += 1
#         if self.number >= self.max:
#             raise StopIteration
#         return self.number

#     def is_prime(self, num):
#         if num < 2:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True


# # Example usage
# for prime in PrimeIterator(25):
#     print(prime)


# def multiples_of_five(n):
#     for i in range(n):
#         yield i * 5


# # Example usage
# result = list(multiples_of_five(10))
# print(result)

# print([x*2 for x in range(10)])

# # lambda
# def double(x): return x * 2


# def sorted_list(my_list): return sorted(my_list)


# print(double(10))


def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func


closure = outer_func(10)
print(closure(5))  # Output: 1
