import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")
my_orders_queue.put("tequila")


# Remove an element from the queue
print(my_orders_queue.get())
print(my_orders_queue.get())