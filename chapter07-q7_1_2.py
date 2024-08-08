def list_average(lst):
    try:
        average = sum(lst) / len(lst)
        return average
    except ZeroDivisionError:
        return 'Error: Division by zero - The list is empty.'
    except TypeError:
        return 'Error: List contains non-numeric elements.'
    except Exception as e:
        return f'An unexepected error occured: {e}'

print(list_average([1.5, 2.5, 3.5]))
print(list_average([]))
print(list_average(['a', 2.5]))
