# def my_gen():
#     a = 3
#     yield a

#     a = 2
#     yield a

#     a = 1
#     yield a

# my_fist_gen = my_gen()

# print(next(my_fist_gen))
# print(next(my_fist_gen))
# print(next(my_fist_gen))

def par_gen():
    for i in range(100):
        if i % 2 == 0:
            yield i

my_fist_yield = par_gen()

for i in range(100):
    print(next(my_fist_yield))

