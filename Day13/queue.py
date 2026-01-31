class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        print(self.__queue)
        if self.__queue:
            val = self.__queue[-1] #Last one in the list was come first to the queue. So he should be removed from queue at the first
            del self.__queue[-1]
            return val
        return QueueError

    def get_queue(self):
        return self.__queue


class LengthQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def get_len(self):
        return len(Queue.get_queue(self)) 


try:
    restaurant_queue = Queue()

    restaurant_queue.put("Amal")
    restaurant_queue.put("Kamal")
    restaurant_queue.put("Bimal")
    restaurant_queue.put("Nimal")
    restaurant_queue.put("Sunimal")

    print(restaurant_queue.get())
    print(restaurant_queue.get())

    child_queue = LengthQueue()
    child_queue.put("Amal")
    child_queue.put("Kamal")
    print(child_queue.get_len())




except QueueError:
    print("Queue is empty")







