def list_del_nth(lst, index):
    try:
        del lst[index]
        print('Successfully')
    except IndexError:
        print('Index Not Found')
    except Exception:
        print('Unexpected Error')

test_list = [10, 20, 30, 40, 50]

list_del_nth(test_list, 2)
print(test_list)

list_del_nth(test_list, 10)

list_del_nth(test_list, 'string')
