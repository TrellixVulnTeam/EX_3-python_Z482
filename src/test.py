from queue import PriorityQueue
from Node_data import Node_data,geo_location

dict={"n1":{'n2':2},'n2':{}}
for k,v in dict.items():
    print (v)
q = PriorityQueue()
for n in range(4):
    node = Node_data (key=n, pos=(n + 1, n - 1, 0))
    q.put(node)
q.put(Node_data(key=4,weight=1))
q.put(Node_data(key=5,weight=0))

for n in range(6):
    print(q.get())
