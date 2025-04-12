from Node import Node
from LinkedList import LinkedList


num_list = LinkedList()
print('INPUT NODES : : : GO')
node_a = Node(input('N1 : '))
node_b = Node(input('N2 : '))
node_c = Node(input('N3 : '))
node_d = Node(input('N4 : '))
node_e = Node(input('N5 : '))
node_f = Node(input('N6 : '))

# using functions
num_list.append(node_b)   
num_list.append(node_c)   
num_list.append(node_e)   

num_list.prepend(node_a)  

num_list.insert_after(node_c, node_d)  
num_list.insert_after(node_e, node_f)  

# output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.remove_after(node_e)   # Remove the tail (17)
num_list.remove_after(None)     # Remove the head (66)


# Output final list
print('List after removing nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()
