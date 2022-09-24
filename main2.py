class Meta(type):
    def __new__(mcs, *args):
        args[2]["class_number"] = Meta.children_number
        Meta.children_number += 1
        return type.__new__(mcs, *args)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    class_number = None

    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    class_number = None

    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
