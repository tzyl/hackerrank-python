class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue empty.")
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Queue empty.")
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2


q = int(input())
queue_using_two_stacks = QueueUsingTwoStacks()
for i in range(q):
    query = [int(s) for s in input().split()]
    if query[0] == 1:
        queue_using_two_stacks.enqueue(query[1])
    elif query[0] == 2:
        queue_using_two_stacks.dequeue()
    elif query[0] == 3:
        print(queue_using_two_stacks.peek())
