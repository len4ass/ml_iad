class AnyAttr(dict):
    def __getattr__(self, item):
        if item in self.keys():
            return self[item]

        self[item] = item
        return item

    def __setattr__(self, key, value):
        str_val = [i for i in value if i in key]
        s = ""
        for c in str_val:
            s += c
        self[key] = s




ins = AnyAttr()
print(ins.hello1)
ins.hello1 = "privet"
print(ins.hello1)
print(ins.hello2)