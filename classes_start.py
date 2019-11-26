#
# Example file for working with classes
#

class my():
  def meth1(self):
    print("move meth1")

  def meth2(self, some):
    print("move meth2"+ some)

class my1(my):
  def meth1(self):
    my.meth1(self)
    print("move meth11")

  def meth2(self, some):
    print("move11 meth2" + some)


def main():
  c = my()
  c2 = my1()
  c2.meth1()
  c2.meth2("this is not something")
  c.meth1()
  c.meth2("this is something")
  
if __name__ == "__main__":
  main()

