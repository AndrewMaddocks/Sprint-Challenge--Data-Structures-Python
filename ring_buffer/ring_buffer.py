class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # need to fill array to reference index
        self.storage = ['' for x in range(capacity)]
        self.pointer = 0

    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer += 1

        # if pointer exceeds capacity set to 0
        if self.pointer == self.capacity:
            self.pointer = 0

    def get(self):
        return [x for x in self.storage if x != '']
