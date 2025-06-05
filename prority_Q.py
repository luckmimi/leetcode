def parent(node):
    return (node - 1) // 2
def left(node):
    return node * 2 + 1
def right(node):
    return node * 2 + 2
def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]
def min_heap_swim(heap, node):
    # 
    while node > 0 and heap[parent(node)] > heap[node]:
        heap[parent(node)] , heap[node] =  heap[node],heap[parent(node)]
        node = parent(node)
def min_heap_sink(heap, node, size):
    while left(node) < size and right(node) < size:
        min_index = node 
        if left(node) < size and heap[left(node)] < heap[min_index]:
            min_index = left(node)
        if right(node) < size and heap[right(node)] < heap[min_index]:
            min_index = right(node)
        if min_index == node:
            break
        swap(heap, min_index, node)
        node = min_index 
def max_heap_swim(heap, node):
    while node > 0 and heap[parent(node)] < heap[node]:
        heap[parent(node)] , heap[node] =  heap[node],heap[parent(node)]
        node = parent(node)
def max_heap_sink(heap, node, size):
       while left(node) < size and right(node) < size:
        max_index = node 
        if left(node) < size and heap[left(node)] > heap[max_index]:
            max_index = left(node)
        if right(node) < size and heap[right(node)] > heap[max_index]:
            max_index = right(node)
        if max_index == node:
            break
        swap(heap, max_index, node)
        node = max_index 
