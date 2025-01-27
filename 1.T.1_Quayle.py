# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:51:38 2025

@author: 19105
"""

# Queue implementation with basic operations
class Queue:
    def __init__(self):
        self.items = []  # Using a list to hold queue elements
    
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """Remove an item from the front of the queue."""
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty!")
            return None
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def display(self):
        """Display the current state of the queue."""
        print("Queue:", " -> ".join(map(str, self.items)) if self.items else "Empty")
        

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()  # Try dequeuing from an empty queue
