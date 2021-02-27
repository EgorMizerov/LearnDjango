class A:
    name = "Class A"

    def hello(self):
        print("Hello form A")

    __hello = hello


class B(A):
    def hello(self):
        print("Hello from B")


b = B()
a = A()

for i in [a, b]:
    i.hello()

b._A__hello()
print(b.name)