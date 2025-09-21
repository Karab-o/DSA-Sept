# Stack Implementation - Time Complexity Analysis

## Operations Overview

| Operation | Time Complexity | Space Complexity | Description |
|-----------|----------------|------------------|-------------|
| `__init__()` | O(1) | O(1) | Initialize empty stack |
| `push(item)` | O(1) amortized | O(1) | Add item to top |
| `pop()` | O(1) | O(1) | Remove and return top item |
| `peek()` | O(1) | O(1) | Return top item without removing |
| `is_empty()` | O(1) | O(1) | Check if stack is empty |
| `size()` | O(1) | O(1) | Return number of items |
| `clear()` | O(1) | O(1) | Remove all items |
| `__len__()` | O(1) | O(1) | Return length (enables len()) |
| `__str__()` | O(n) | O(n) | String representation |
| `__repr__()` | O(n) | O(n) | Debug string representation |

## Detailed Analysis

### Push Operation - O(1) Amortized
- **Best/Average Case**: O(1) - Direct append to Python list
- **Worst Case**: O(n) - When list needs to resize (rare)
- **Amortized**: O(1) - Resizing happens infrequently
- **Why Efficient**: Python lists are dynamic arrays that double in size when full

### Pop Operation - O(1)
- **All Cases**: O(1) - Removes last element from Python list
- **No resizing needed** when removing elements
- **Memory deallocation** is handled by Python's garbage collector

### Peek Operation - O(1)
- **All Cases**: O(1) - Direct access to last element via indexing
- **No modification** of underlying structure

### Space Complexity
- **Overall Space**: O(n) where n is the number of elements
- **Each Operation**: O(1) additional space (except string methods)

## Real-World Performance Considerations

### Memory Usage
```python
# Memory-efficient for typical use cases
# Python list overhead: ~56 bytes + 8 bytes per pointer
# For 1000 integers: ~8KB total memory
```

### Cache Performance
- **Sequential memory access** for iteration
- **Good cache locality** due to contiguous storage
- **Minimal memory fragmentation**

### Scalability
- **Excellent for moderate sizes** (< 10^6 elements)
- **Memory efficient** compared to linked implementations
- **No pointer overhead** unlike linked structures

## Comparison with Alternative Implementations

### Array-based (Our Implementation)
- ✅ O(1) random access
- ✅ Memory efficient
- ✅ Good cache performance
- ❌ Fixed capacity (mitigated by dynamic resizing)

### Linked List Implementation
- ✅ Dynamic size without resizing
- ❌ O(1) memory overhead per element
- ❌ Poor cache performance
- ❌ No random access

### Deque-based Implementation
```python
from collections import deque
# Alternative: deque for guaranteed O(1) operations
# Trade-off: Slightly more memory overhead
```

## Performance Benchmarks (Theoretical)

| Operation | 1K elements | 10K elements | 100K elements |
|-----------|-------------|--------------|---------------|
| Push | ~0.1 μs | ~0.1 μs | ~0.1 μs |
| Pop | ~0.05 μs | ~0.05 μs | ~0.05 μs |
| Peek | ~0.02 μs | ~0.02 μs | ~0.02 μs |

*Note: Actual performance depends on hardware and Python implementation*