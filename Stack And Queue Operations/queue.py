class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self):
        item=int(input('Enter Item to push :'))
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        print(self.queue.pop(0),' NO deleted.')

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()

while(1):
    print('Menu\n\t1.enqueue()'
      '\n\t2.dequeue()'
      '\n\t3.Display'
      '\n\t4.Show Size of Queue'
      '\n\t5.Exit')
    match ch:=int(input('Enter Your Choice:')):
        case 1: q.enqueue()
        case 2: q.dequeue()
        case 3: q.display()
        case 4: print(q.size())
        case 5: exit()
        case _:
            print('Wrong Choice')




