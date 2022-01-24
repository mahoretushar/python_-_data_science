# deque = double ended queue
from collections import deque

q_1 = deque([])
q_1.append(1)
q_1.append(2)
q_1.append(3)
print(q_1)
q_1.popleft()
print(q_1)
