from Binary_Search_Tree import Binary_Search_Tree
class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    if self.__sub__(other).__n * self.__sub__(other).__d  < 0 :#by multiplying numerator and denonimator of (self-other), see if (self-other) is negative or positive.
        return True
    else:
        return False
    #TODO replace pass with your implementation,
    #returning True if self is less than other and
    #False otherwise.

  def __gt__(self, other):
    if self.__sub__(other).__n * self.__sub__(other).__d  > 0 :#by multiplying numerator and denonimator of (self-other), see if (self-other) is negative or positive.
        return True
    else:
        return False
    #TODO replace pass with your implementation,
    #returning True if self is greater than other and
    #False otherwise.


  def __eq__(self, other):
    if self.__n == other.__n and self.__d == other.__d:#since gcd(n,d)=1, fractions of different values have unique n and d.
        return True
    else:
        return False
    #TODO replace pass with your implementation,
    #returning True if self equal to other and
    #False otherwise. Note that fractions are
    #stored in reduced form.


  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
    x = Fraction(10,20)#test __eq__() when reduced form is the same
    y = Fraction(1,2)
    if x == y:
        print(" __eq__() test case 1 works")
    else:
        print(" __eq__() test case 1 doesn't work")

    x1 = Fraction(2,-3)#test __eq__() when negative sign is at denominator or numerator
    y1 = Fraction(-2,3)
    if x1 == y1:
        print(" __eq__() test case 2 works")
    else:
        print(" __eq__() test case 2 doesn't work")

    x2 = Fraction(2,-4)#different denominator same numerator
    y2 = Fraction(2,-3)
    if x2 > y2:
        print(" __gt__() test case 1 works")
    else:
        print(" __gt__() test case 1 doesn't work")

    x3 = Fraction(1,-3)#different numerator same denonimator
    y3 = Fraction(2,-3)
    if x3 > y3:
        print(" __gt__() test case 2 works")
    else:
        print(" __gt__() test case 2 doesn't work")

    x4 = Fraction(2,4)#different denominator same numerator
    y4 = Fraction(2,3)
    if y4 > x4:
        print(" __gt__() test case 3 works")
    else:
        print(" __gt__() test case 3 doesn't work")

    x5 = Fraction(1,3)#different numerator same denonimator
    y5 = Fraction(2,3)
    if y5 > x5:
        print(" __gt__() test case 4 works")
    else:
        print(" __gt__() test case 4 doesn't work")

    x5 = Fraction(2,3)#two equal fractions
    y5 = Fraction(2,3)
    if y5 > x5:
        print("__gt__() test case 5 doesn't work")
    else:
        print(" __gt__() test case 5 works")

    x6 = Fraction(2,3)#different numerator and different denonimator
    y6 = Fraction(4,5)
    if y6 > x6:
        print("__gt__() test case 6 works")
    else:
        print(" __gt__() test case 6 doesn't work")

    x7 = Fraction(-1,3)#when fractions have different signs
    y7 = Fraction(2,3)
    if y7 > x7:
        print(" __gt__() test case 7 works")
    else:
        print(" __gt__() test case 7 doesn't work")

    a1 = Fraction(2,-4)#different denominator same numerator
    b1 = Fraction(2,-3)
    if b1 < a1:
        print(" __lt__() test case 1 works")
    else:
        print(" __lt__() test case 1 doesn't work")

    a2 = Fraction(1,-3)#different numerator same denonimator
    b2 = Fraction(2,-3)
    if b2 < a2:
        print(" __lt__() test case 2 works")
    else:
        print(" __lt__() test case 2 doesn't work")

    a3 = Fraction(2,4)#different denominator same numerator
    b3 = Fraction(2,3)
    if a3 < b3:
        print(" __lt__() test case 3 works")
    else:
        print(" __lt__() test case 3 doesn't work")


    a4 = Fraction(1,3)#different numerator same denonimator
    b4 = Fraction(2,3)
    if a4 < b4:
        print(" __lt__() test case 4 works")
    else:
        print(" __lt__() test case 4 doesn't work")

    a5 = Fraction(2,3)#tests if __lt__ treats two equal fraction correctly
    b5 = Fraction(2,3)
    if b5 < a5:
        print("__lt__() test case 5 doesn't work")
    else:
        print(" __lt__() test case 5 works")

    x6 = Fraction(2,3)#different numerator and different denonimator
    y6 = Fraction(4,5)
    if x6 < y6:
        print("__lt__() test case 6 works")
    else:
        print(" __lt__() test case 6 doesn't work")

    a7 = Fraction(-1,3)#when fractions have different signs
    b7 = Fraction(2,3)
    if a7 < b7:
        print(" __lt__() test case 7 works")
    else:
        print(" __lt__() test case 7 doesn't work")

    a = Fraction(2,3)#create some fraction objects to sort
    b = Fraction(23,233)
    c = Fraction(22,7)
    d = Fraction(355,113)
    e = Fraction(4,8)
    f = Fraction(8,4)
    g = Fraction(241,2020)
    arr1 = [a,b,c,d,e,f,g]#store fraction objects in an array
    print(arr1)
    tree1 = Binary_Search_Tree()#AVL tree to insert fraction objects
    for a in arr1:
        tree1.insert_element(a)#insert_element() should balance these fraction objects
    sorted_arr1 = tree1.to_list()#return list representation of in order traversal, fraction objects should be in increasing order
    print(sorted_arr1)

    A = Fraction(20,1)
    B = Fraction(241,141)
    C = Fraction(4,3)
    D = Fraction(1,1)
    E = Fraction(301,312)
    F = Fraction(6,66)
    arr2 = [A,B,C,D,E,F]
    print(arr2)
    tree2 = Binary_Search_Tree()#another sorting. The fractions are in decreasing order, so it is worst case.
    for a in arr2:
        tree2.insert_element(a)
    sorted_arr2 = tree2.to_list()
    print(sorted_arr2)
  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
