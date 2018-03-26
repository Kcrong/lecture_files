def main():  # this is function
    # types
    a_int = 1

    print(type(a_int))

    b_str = "this is string"
    print(type(b_str))

    c_list = ['this', 'is', 'list']
    print(type(c_list))

    d_tuple = ('this', 'is', 'tuple')
    print(type(d_tuple))

    e_dict = {'name': 'value',
              'this is': 'dict'}
    print(type(e_dict))

    f_set = {'a', 'b', 'c', 'c'}
    print(type(f_set))
    print(f_set)  # No duplicate!

    g_bool = False
    print(type(g_bool))

    # if condition
    if a_int == 1:  # this is if condition
        print('a is %d' % 1)

    # for loop
    for c_item in c_list:  # this is for condition
        print(c_item)

    # Iterable types
    iter(a_int)  # Error!
    iter(b_str)
    iter(c_list)
    iter(d_tuple)
    iter(e_dict)

    # While loop
    def some_func():
        hit = 0
        while hit < 10:
            print('I hit the tree %d' % hit)
            hit = hit + 1
        print('The tree fell down!!')
        
    # for - loop
    def with_for_loop():
        for i in range(10):
            print('Hit %d times' % (i+1))
        print('The tree fell down!!')


if __name__ == '__main__':  # trick for execute like main
    main()
