"""
Creating a Priority Queue
The lowest priority value is the element that has the highest priority
"""

class Node:
    """
    This class create new node
    """
    def __init__(self, value, priority):
        """
        This is the constructor, it is used to construct nodes
        """
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    """
    This class create new PriorityQueue
    """
    # This is the constructer
    def __init__(self):
        """
        This is the constructor, it is used to construct priority queue
        """
        self.head = None
        self.max_job_id = 0

    # This method add nodes to the Priority Queue
    def enqueue(self, value, priority):
        """
        This method add nodes to the queue
        """
        if self.max_job_id < int(value[0][3:]):
            self.max_job_id = int(value[0][3:])

        """"""""""""""""""""""""
        # https://www.geeksforgeeks.org/priority-queue-using-linked-list/
        if self.head:
            if self.head.priority < priority:
                new_node = Node(value,priority)
                new_node.next = self.head
                self.head = new_node
                return 1  
            else:
                current = self.head
                while current.next:
                    if priority >= current.next.priority:
                        break
                    current = current.next
                 
                new_node = Node(value,priority)
                new_node.next = current.next
                current.next = new_node
                return 1
        else:
            self.head = Node(value,priority)
            return 1
        """"""""""""""""""""""""

    def dequeue(self, to_delete): # O(1)
        """
        This method remove nodes to the queue based on the priority
        """
        current = self.head
        while current:
            if current.priority == to_delete:
                self.head = current.next
                break
            else:
                if current.next.next == None:
                    current.next = None
                    break
                elif current.next.priority == to_delete:
                    current.next = current.next.next
                    break
            current = current.next      
        # if(self.head):
        #     # self.to_delete = self.head.value[0]
        #     self.head = self.head.next
        # else:
        #     return None

    def remove(self, data):
        """
        This function remove specific node from the priority queue based on the job id
        """
        current = self.head
        while current:
            if current.value == data:
                self.head = current.next
                break
            else:
                if current.next.next == None:
                    current.next = None
                    break
                elif current.next.value == data:
                    current.next = current.next.next
                    break       
            current = current.next

    def print_q(self):
        """
        This method print the priority queue elements
        it is used for testing
        """
        current=self.head
        while current:
            print(current.value,current.priority)
            current=current.next
