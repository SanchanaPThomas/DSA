import random

class RandomizedSet:

    def __init__(self):
        self.arr = []            # List to store the values
        self.pos = {}            # Map: value -> index in arr

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]        # index of element to remove
        last_val = self.arr[-1]    # last element in the list

        # Swap with last element
        self.arr[idx] = last_val
        self.pos[last_val] = idx   # update hash index

        # Remove last element
        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
