# -*- coding: utf8 -*-


class PartLoloTestBad(object):
    """ Part of the class LoloTestBad """
    def __init__(self, var_test=None):
        self.var_test = var_test

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class LoloTestBad(object):
    """ Tests pour Lolo """
    def __init__(self, lolo_var=PartLoloTestBad(), list_test=[]):
        self.lolo_var = lolo_var
        self.list_test = list_test

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class PartLoloTestGood(object):
    """ Part of the class LoloTestBad """
    def __init__(self, var_test=None):
        self.var_test = var_test

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class LoloTestGood(object):
    """ Tests pour Lolo """
    def __init__(self, lolo_var=None, list_test=[]):
        self.lolo_var = lolo_var
        self.list_test = list(list_test)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    badTest1 = LoloTestBad()
    badTest1.lolo_var.var_test = "Test"
    badTest1.list_test.append("test1")
    badTest2 = LoloTestBad()
    print badTest1
    print badTest2
    print

    goodTest1 = LoloTestGood()
    goodTest1.lolo_var = PartLoloTestGood(var_test="Test")
    goodTest1.list_test.append("test1")
    goodTest2 = LoloTestGood()
    print goodTest1
    print goodTest2
    print

    goodTest1 = LoloTestGood(list_test=["test0"])
    goodTest1.lolo_var = PartLoloTestGood(var_test="Test")
    goodTest1.list_test.append("test1")
    goodTest2 = LoloTestGood()
    print goodTest1
    print goodTest2
    print
