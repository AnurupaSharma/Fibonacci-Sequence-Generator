#!/usr/bin/env python
# coding: utf-8

# In[1]:


def generate_fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence

    sequence.append(0)
    if n == 1:
        return sequence

    sequence.append(1)
    if n == 2:
        return sequence

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence


n = int(input("Enter the number of Fibonacci sequence elements to generate: "))


fibonacci_sequence = generate_fibonacci_sequence(n)
print("Fibonacci Sequence:")
print(fibonacci_sequence)


# In[ ]:




