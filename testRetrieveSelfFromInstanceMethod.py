# coding: utf-8

def test_function(my_class_method):
    print(my_class_method())
    test_self = my_class_method.im_self
    print(test_self.troll())


class Test():
    def lol(self):
        return "Can you look that Simon?"

    def troll(self):
        return "Who's the BOSS now?"


test = Test()
test_function(my_class_method=test.lol)
