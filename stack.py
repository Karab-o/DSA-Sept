class Stack:
    """
    A Stack (LIFO - Last In, First Out) data structure implementation.
    
    This implementation uses a Python list as the underlying storage mechanism
    and provides all standard stack operations with optimal time complexity.
    """
    
    def __init__(self):
        """
        Initialize an empty stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack
            
        Time Complexity: O(1) - Amortized
        Space Complexity: O(1)
        """
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        Returns:
            The item that was at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """
        Return the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Return the number of items in the stack.
        
        Returns:
            int: The number of items in the stack
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items)
    
    def clear(self):
        """
        Remove all items from the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items = []
    
    def __str__(self):
        """
        Return a string representation of the stack.
        
        Returns:
            str: String representation showing stack contents
            
        Time Complexity: O(n) where n is the number of items
        Space Complexity: O(n)
        """
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self._items} (top -> bottom)"
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: Detailed string representation
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return f"Stack({self._items})"
    
    def __len__(self):
        """
        Return the length of the stack (enables len() function).
        
        Returns:
            int: Number of items in the stack
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items)