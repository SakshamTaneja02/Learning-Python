class Base:
    pass

class Der1(Base):
    pass

class Der2(Base):
    pass

class Der2(Base):
    pass

class Der3(Der1, Der2):
    pass
# this is hybrid inheritance

class B:
    pass
class A(B):
    pass
class C(B):
    pass
# this is hierarchical inheritance