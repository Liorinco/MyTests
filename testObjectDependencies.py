# -*- coding: utf8 -*-


class Person(object):
    """ Person """
    def __init__(self, name=None, yeux=None):
        super(Person, self).__init__()
        self.name = name
        self.yeux = yeux

    def __repr__(self):
        return str(self.__dict__)

    def cloner(self, clone_person=None):
        print "# cloner(self=" + str(self) + ", clone_person=" +  \
            str(clone_person) + ")"

        if not isinstance(clone_person, Person):
            clone_person = Person()

        clone_person.name = self.name

        if self.yeux is None:
            clone_person.yeux = None

        else:
            clone_person.yeux = self.yeux.cloner(clone_person.yeux)

        return clone_person


class Yeux(object):
    """ Yeux """
    def __init__(self, couleur="marron"):
        super(Yeux, self).__init__()
        self.couleur = couleur

    def __repr__(self):
        return str(self.__dict__)

    def cloner(self, clone_yeux=None):
        print "# cloner(self=" + str(self) + ", clone_yeux=" +  \
            str(clone_yeux) + ")"

        if not isinstance(clone_yeux, Yeux):
            clone_yeux = Yeux()

        clone_yeux.couleur = self.couleur

        return clone_yeux

    def changer_couleur(self, nouvelle_couleur):
        print "# changer_couleur(self=" + str(self) + \
            ", nouvelle_couleur=" + str(nouvelle_couleur) + ")"
        self.couleur = nouvelle_couleur


if __name__ == '__main__':
    # Tests to make a true copy
    yeux = Yeux(couleur="bleu")
    toto = Person(name="Toto", yeux=yeux)
    faux_clone_toto = toto
    print toto
    print faux_clone_toto
    print

    faux_clone_toto.yeux.changer_couleur(nouvelle_couleur="vert")
    print toto
    print faux_clone_toto
    print

    vrai_clone_toto = Person()
    print toto
    print faux_clone_toto
    print vrai_clone_toto
    print

    toto.cloner(clone_person=vrai_clone_toto)
    print toto
    print faux_clone_toto
    print vrai_clone_toto
    print

    vrai_clone_toto.yeux.changer_couleur(nouvelle_couleur="rouge")
    print toto
    print faux_clone_toto
    print vrai_clone_toto
    print

    # Tests to verify no unused class were instanciated
    yeux_titi = Yeux()
    titi = Person(name="Titi", yeux=yeux_titi)
    print titi
    print

    clone_titi = Person(yeux=yeux_titi)
    clone_titi = titi.cloner(clone_person=clone_titi)
    print titi
    print clone_titi
    print

    clone_titi.yeux.changer_couleur(nouvelle_couleur="gris")
    print titi
    print clone_titi
    print
