class A:
    vara="welcome to class A"
class B:
    varb="Welcome to class B"
class C(A,B):
    varc="welcome to class C"
c1=C()
print(c1.vara)
print(c1.varb)
print(c1.varc)

