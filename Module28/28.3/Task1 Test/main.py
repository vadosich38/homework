class X:
    pass
#####


class A(X):
    pass


class B(X):
    pass


class C(X):
    pass


class D(X):
    pass
#######


class E(A, B):
    pass


class F(B, C):
    pass


class G(B, C, D):
    pass


class H(C, D):
    pass
#####


class J(E, G):
    pass


class K(F, G, H):
    pass
####


class Z(J, K):
    pass


help(Z)
print(Z.__mro__)
