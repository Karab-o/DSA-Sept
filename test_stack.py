import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """Comprehensive unit tests for Stack implementation."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.stack = Stack()
    
    def test_initialization(self):
        """Test that a new stack is properly initialized."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)
    
    def test_push_single_item(self):
        """Test pushing a single item to the stack."""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.peek(), 1)
    
    def test_push_multiple_items(self):
        """Test pushing multiple items to the stack."""
        items = [1, 2, 3, 'a', 'b']
        for item in items:
            self.stack.push(item)
        
        self.assertEqual(self.stack.size(), len(items))
        self.assertEqual(self.stack.peek(), 'b')  # Last item pushed
    
    def test_pop_single_item(self):
        """Test popping a single item from the stack."""
        self.stack.push(42)
        popped_item = self.stack.pop()
        
        self.assertEqual(popped_item, 42)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
    
    def test_pop_multiple_items_lifo_order(self):
        """Test that items are popped in LIFO (Last In, First Out) order."""
        items = [1, 2, 3, 4, 5]
        
        # Push items
        for item in items:
            self.stack.push(item)
        
        # Pop items and verify LIFO order
        popped_items = []
        while not self.stack.is_empty():
            popped_items.append(self.stack.pop())
        
        expected_order = [5, 4, 3, 2, 1]  # Reverse order
        self.assertEqual(popped_items, expected_order)
    
    def test_peek_without_modification(self):
        """Test that peek returns top item without modifying the stack."""
        self.stack.push('test')
        initial_size = self.stack.size()
        
        peeked_item = self.stack.peek()
        
        self.assertEqual(peeked_item, 'test')
        self.assertEqual(self.stack.size(), initial_size)  # Size unchanged
        self.assertFalse(self.stack.is_empty())
    
    def test_peek_multiple_times(self):
        """Test multiple peek operations."""
        self.stack.push(100)
        
        for _ in range(5):
            self.assertEqual(self.stack.peek(), 100)
        
        self.assertEqual(self.stack.size(), 1)  # Should still have one item
    
    def test_pop_from_empty_stack_raises_error(self):
        """Test that popping from empty stack raises IndexError."""
        with self.assertRaises(IndexError) as context:
            self.stack.pop()
        
        self.assertIn("pop from empty stack", str(context.exception))
    
    def test_peek_empty_stack_raises_error(self):
        """Test that peeking empty stack raises IndexError."""
        with self.assertRaises(IndexError) as context:
            self.stack.peek()
        
        self.assertIn("peek from empty stack", str(context.exception))
    
    def test_is_empty_functionality(self):
        """Test is_empty method under various conditions."""
        # Initially empty
        self.assertTrue(self.stack.is_empty())
        
        # After push
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        
        # After pop (back to empty)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
    
    def test_size_tracking(self):
        """Test that size is correctly tracked through operations."""
        expected_sizes = [0, 1, 2, 3, 2, 1, 0]
        actual_sizes = [self.stack.size()]
        
        # Push operations
        for i in range(1, 4):
            self.stack.push(i)
            actual_sizes.append(self.stack.size())
        
        # Pop operations (3 pops to get back to 0)
        for i in range(3):
            self.stack.pop()
            actual_sizes.append(self.stack.size())
        
        self.assertEqual(actual_sizes, expected_sizes)
    
    def test_clear_functionality(self):
        """Test that clear removes all items from the stack."""
        # Add items
        for i in range(5):
            self.stack.push(i)
        
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 5)
        
        # Clear stack
        self.stack.clear()
        
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
    
    def test_mixed_operations(self):
        """Test a sequence of mixed push, pop, and peek operations."""
        # Push some items
        self.stack.push('a')
        self.stack.push('b')
        self.assertEqual(self.stack.peek(), 'b')
        
        # Pop one item
        popped = self.stack.pop()
        self.assertEqual(popped, 'b')
        self.assertEqual(self.stack.peek(), 'a')
        
        # Push more items
        self.stack.push('c')
        self.stack.push('d')
        self.assertEqual(self.stack.size(), 3)
        
        # Pop all remaining items
        self.assertEqual(self.stack.pop(), 'd')
        self.assertEqual(self.stack.pop(), 'c')
        self.assertEqual(self.stack.pop(), 'a')
        
        self.assertTrue(self.stack.is_empty())
    
    def test_string_representation(self):
        """Test string representation methods."""
        # Empty stack
        self.assertEqual(str(self.stack), "Stack: []")
        
        # Non-empty stack
        self.stack.push(1)
        self.stack.push(2)
        expected_str = "Stack: [1, 2] (top -> bottom)"
        self.assertEqual(str(self.stack), expected_str)
    
    def test_repr_method(self):
        """Test __repr__ method for debugging."""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(repr(self.stack), "Stack([1, 2])")
    
    def test_len_method(self):
        """Test __len__ method (enables len() function)."""
        self.assertEqual(len(self.stack), 0)
        
        self.stack.push('item')
        self.assertEqual(len(self.stack), 1)
        
        self.stack.push('another')
        self.assertEqual(len(self.stack), 2)
        
        self.stack.pop()
        self.assertEqual(len(self.stack), 1)
    
    def test_different_data_types(self):
        """Test stack with different data types."""
        items = [1, 'string', [1, 2, 3], {'key': 'value'}, None, True]
        
        for item in items:
            self.stack.push(item)
        
        # Pop items in reverse order
        for expected_item in reversed(items):
            self.assertEqual(self.stack.pop(), expected_item)
    
    def test_large_operations(self):
        """Test stack with a large number of operations."""
        n = 1000
        
        # Push n items
        for i in range(n):
            self.stack.push(i)
        
        self.assertEqual(self.stack.size(), n)
        self.assertEqual(self.stack.peek(), n - 1)
        
        # Pop all items
        for i in range(n - 1, -1, -1):
            self.assertEqual(self.stack.pop(), i)
        
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)