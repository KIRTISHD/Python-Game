import collection,math,os

def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath,filename)
    return fullname

def line(a,b,x,y):
    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)

class vector(collection.Sequence):
    PRECISION = 6
    __slots__ = ('_x','_y','_hash')

    def __init__(self,x,y):
        self._hash = None
        self._x = round(x,self.PRECISION)
        self._y = round(y,self.PRECISION)

    @property
    #getter
    def x(self):
          return self._x
        
    @property
    #setter
    def x(self,value):
        if self._hash is not None:
            raise ValueError('Cannot set x after hashing')
        self._x = round(value,self.PRECISION)

    @property
    #getter
    def y(self):
          return self._y
        
    @property
    #setter
    def y(self,value):
        if self._hash is not None:
            raise ValueError('Cannot set y after hashing')
        self._y = round(value,self.PRECISION)

    def __hash__(self):
        #v.__hash__() -> hash(v)

        #v = vector(1,2)

        if self._hash is None:
            pair = (self.x,self.y)
            self._hash = hash(pair)

        return self._hash

    def __len__(self):
        return 2

    def __getitem__(self,,index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        else:
            raise IndexError

    def copy(self):

        type_self = type(self)
        return type_self(self.x,self.y)

    def __eq__(self.other):
        #v = w if v = vector(1,2) = w = vector(1,2)

        if isinstance(other,vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self,other):
        if instance(other,vector):
            return self.x != other.x and self.y != other.y
        return NotImplemented

    def __iadd__(self,other):
        #v._iadd__(w) -> v += w
        """ if add(4,5) then (5,6)"""
        if self._hash is None:
            raise ValueError('Cannout add vector after hashing')
        elif isinstance(other,vector):
            self.x = other.x
            self.y = other.y
        else:
            self.x += other
            self.y += other
        return self


    def __add__(self,other):
        #v._iadd__(w) -> v + w
        copy = self.copy()
        return copy._iadd__(other)

    def move(self,other):
        #move vector by others(n places)
        #v = vector(1,2) w = vector(3,4) v.move(w)  v-->vector(4,6)

        self.__iadd__(other)

    def.__isub__(self,other):

        if self._hash is not None:
            raise ValueError('Cannot subtract vector after hashing')
        elif isinstance(other,vector):
            self.x = other.x
            self.y = other.y

        else:
            self.x-=other
            self.y-=other
        return self

    def __sub__(self,other):
        copy = self.copy()
        return copy.__isub__(other)

    
        
