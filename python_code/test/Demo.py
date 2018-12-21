d = {"1": {"1": {"1": 0}}, "9": 0, "3": {"2": 0}, "2": 0}
key_list = list(d.keys())
# print(key_list)

def func(d):
    for key in key_list:
        if d[key] == 0:
            d.pop(key)
        elif type(d[key]) == dict:
            print(d[key])
            func(d[key])
