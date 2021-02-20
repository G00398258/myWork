# put 10 random numbers in a queue, remove them one by one and print remaining numbers in queue
# Author: Gillian Kane-McLoughlin

import random
queue = []
numberofNumbers = 10
rangeTo = 100

for n in range(0, numberofNumbers):
    queue.append(random.randint(0,rangeTo))

print ("The queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0) # this stores the first element in queue as currentNumber and removes from queue
    print ("Current Number is {} and the queue is {}".format(currentNumber,queue))

print ("The queue is now empty")