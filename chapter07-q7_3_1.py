class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
        super().__init__("辞書にはキーが登録されていません")

def get_dict_value(dict_tbl, key):
    if key in dict_tbl:
        return dict_tbl[key]
    else:
        raise MyDictKeyError(key)

if __name__ == "__main__":
    dict_tbl = {'a': 1, 'b': 2, 'c': 3}

    try:
        print(get_dict_value(dict_tbl, 'b'))
        print(get_dict_value(dict_tbl, 'x'))
    except MyDictKeyError as e:
        print(e)
