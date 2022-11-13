import priority_queue as prio

"""
This function read data from file and add them to the Priority Queue.
"""
pq=prio.PriorityQueue()

# reading the data from the txt document
file = open("database.txt", "r")

# Looping through every line in the text document
for line in file: # O(n) n being the number of lines
    striped_line = line.strip()
    temp_list = striped_line.split(", ")
    pq.enqueue([temp_list[0], temp_list[1]] , [int(temp_list[2]), int(temp_list[3])])

file.close()