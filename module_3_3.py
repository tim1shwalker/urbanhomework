def print_params(a=1, b='строка', c=True):
    print(a, b, c)


list_ = [1,2]
print_params(list_, 'новая строка', False)
print_params(5, 'еще одна строка')
print_params()
print_params(b=25)
print_params(c=[1,2,3]) ;
#1

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1,2, True]
values_dict = {'a': 1, 'b': 2, 'c': 3}
values_list_2 = [1,True]
print_params(*values_list_2,11)
print_params(*values_list)
print_params(**values_dict)
