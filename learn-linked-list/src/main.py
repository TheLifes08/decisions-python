class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        s1, s2 = "None", "None"

        if self.__prev__ != None:
            s1 = self.__prev__.get_data()
        if self.__next__ != None:
            s2 = self.__next__.get_data()

        return "data: {}, prev: {}, next: {}".format(self.__data, s1, s2)


class LinkedListIterator:
    def __init__(self, linked_list):
        self.current = linked_list.__first__

    def __next__(self):
        if self.current != None:
            node = self.current
            self.current = self.current.__next__
            return node
        else:
            raise StopIteration


class LinkedList:
    def __init__(self, first=None, last=None):
        if first == None:
            self.__length = 0
            self.__first__ = None
            self.__last__ = None

            if last != None:
                raise ValueError("invalid value for last")

        elif first != None and last == None:
            self.__length = 1
            self.__first__ = Node(first)
            self.__last__ = self.__first__

        else:
            self.__length = 2
            self.__first__ = Node(first)
            self.__last__ = Node(last, prev=self.__first__)
            self.__first__.__next__ = self.__last__

    def __len__(self):
        return self.__length

    def __iter__(self):
        return LinkedListIterator(self)

    def __str__(self):
        if self.__length > 0:
            return "LinkedList[length = {}, [{}]]".format(self.__length, "; ".join(list(map(str, self))))
        else:
            return "LinkedList[]"

    def append(self, element):
        if self.__length == 0:
            self.__first__ = Node(element)
            self.__last__ = self.__first__
        else:
            self.__last__.__next__ = Node(element, prev=self.__last__)
            self.__last__ = self.__last__.__next__

        self.__length += 1

    def clear(self):
        self.__length = 0
        self.__first__ = None
        self.__last__ = None

    def pop(self):
        if self.__length == 0:
            raise IndexError("LinkedList is empty!")
        else:
            if self.__last__.__prev__ == None:
                self.__last__ = None
                self.__first__ = None
            else:
                self.__last__ = self.__last__.__prev__
                self.__last__.__next__ = None

            self.__length -= 1

    def popitem(self, element):
        current = None
        is_exists = False

        for node in self:
            if node.get_data() == element:
                is_exists = True
                current = node

        if is_exists:
            if current is self.__last__:
                if self.__last__.__prev__ == None:
                    self.__last__ = None
                    self.__first__ = None
                else:
                    self.__last__ = self.__last__.__prev__
                    self.__last__.__next__ = None
            elif current is self.__first__:
                if self.__last__.__prev__ == None:
                    self.__last__ = None
                    self.__first__ = None
                else:
                    self.__first__ = self.__first__.__next__
                    self.__first__.__prev__ = None
            else:
                current.__next__.__prev__ = current.__prev__
                current.__prev__.__next__ = current.__next__
            self.__length -= 1
        else:
            raise KeyError("{} doesn't exist!".format(element))
