class Queue:
    def __init__(self):
        self.entries = []
        self.lenght = 0
        self.front = 0

    def __repr__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self,item):
        self.entries.append(item)
        self.lenght += 1

    def get(self):
        dequeue = self.entries[self.front]
        self.entries = self.entries[1:]
        self.lenght -= 1
        return dequeue

    def fron(self):
        return self.entries[0]

    def size(self):
        return self.lenght


if __name__ == '__main__':
    ll = Queue()
    for i in range(10):
        ll.put(i)
    print(ll)
    ll.get()
    print(ll)
    print(ll.fron())
    print(ll.size())