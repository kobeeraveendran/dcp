class Iterator2D(object):

    def __init__(self, array2d):
        self.array = array2d
        self.curr_array = 0
        self.curr_elem = 0

    def next(self):
        try:
            if self.curr_elem >= len(self.array[self.curr_array]):
                
                # go to the next available non-empty array
                self.curr_array += 1
                while not self.array[self.curr_array]:
                    self.curr_array += 1

                output = self.array[self.curr_array][self.curr_elem]
                self.curr_elem += 1
                return output

            # general case
            output = self.array[self.curr_array][self.curr_elem]
            self.curr_elem += 1
            return output

        except:
            raise IndexError("Exhausted all elements from the input array.")

    def has_next(self):

        if self.curr_elem < len(self.curr_array):
            return True

        try:
            i = self.curr_array
            while not self.array[i]:
                i += 1

            return True

        except:
            return False

if __name__ == "__main__":

    iterator = Iterator2D([
        [1, 2], 
        [3], 
        [], 
        [4, 5, 6]
    ])

    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())