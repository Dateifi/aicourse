# Update "from oving_uke03 import ..." below with the name of the python file containing your classes
# Run tests from command line: python -m pytest LinkedListUnitTests.py

from Uke3_Øvingsoppgaver import MyLinkedList, MyStack, MyFIFO
import pytest


class TestLinkedList:
    def test_list_creation(self):
        # Create list with single (non-iterable) data item
        list1 = MyLinkedList(42)
        # Create list based on (iterable) list of mixed data types
        list2 = MyLinkedList([1,2,[3,4],{'a':5,'b':6},'ka-ching'])
        # Create empty list
        list3 = MyLinkedList(None)

    def test_append(self):
        list1 = MyLinkedList('a')
        list1.append('b')

    def test_len(self):
        list1 = MyLinkedList([1,2,3,4])
        assert len(list1) == 4, "incorrect length for non-empty list"
        list2 = MyLinkedList(None)
        assert len(list2) == 0, "incorrect length for empty list"

    def test_getitem(self):
        list1 = MyLinkedList(['a','b','c'])
        assert list1[2] == 'c', "incorrect item retrieved using __getitem__"
        
    def test_getitem_outofrange(self):
        list1 = MyLinkedList(['a','b','c'])
        with pytest.raises(IndexError):
            list1[9]
        list2 = MyLinkedList(None)
        with pytest.raises(IndexError):
            list2[0]   

    def test_setitem(self):
        list1 = MyLinkedList(['a','b','c'])
        list1[2] = 'd'
        assert list1[2] == 'd', "not able to correctly set value"

    def test_insert(self):
        list1 = MyLinkedList(['a','b','c'])
        list1.insert(0,'x')
        list1.insert(3,'y')
        assert list1[0] == 'x', "value not correctly inserted"
        assert list1[3] == 'y', "value not correctly inserted"

    def test_delitem(self):
        list1 = MyLinkedList(['a','b','c','d'])
        del(list1[2])
        del(list1[2])
        del(list1[0])
        assert list1[0] == 'b', "incorrect element remaining after deletions"
        
    def test_add(self):
        list1 = MyLinkedList(['a','b']) + MyLinkedList(['c','d','e','f'])
        assert len(list1) == 6, "incorrect length after concatenation of lists"
        assert list1[4] == 'e'

    def test_iteration(self):
        list1 = MyLinkedList([4,5,6,7])
        count = 0
        for item in list1:
            count += 1
        assert count == 4, "incorrect number of iterations"
        assert item == 7, "incorrect item returned in last iteration"
        
    def test_equality(self):
        list1 = MyLinkedList(['a','b','c'])
        list2 = MyLinkedList([1,2])
        list3 = MyLinkedList([1,2])
        assert list1 != list2, "different lists considered equal"
        assert list1 == list1, "two references to same object not considered equal"
        assert list2 == list3, "two lists with identical content not considered equal"
        
    def test_contains(self):
        list1 = MyLinkedList(['a','b','c','d'])
        assert 'c' in list1, "did not detect existing element in list"
        assert 'x' not in list1 , "erroneously detected element not in list"


class TestStack:
    def test_create_stack(self):
        stack = MyStack()
        
    def test_push_to_stack(self):
        stack = MyStack()
        stack.push('a')
        stack.push('b')
        
    def test_pop_from_stack(self):
        stack = MyStack()
        stack.push('a')
        stack.push('b')
        stack.push('c')
        assert stack.pop() == 'c', "last item pushed is not first item returned"
        assert stack.pop() == 'b'
        assert stack.pop() == 'a'
        
        with pytest.raises(IndexError):
            stack.pop()

        
class TestFIFO:
    def test_create_queue(self):
        queue = MyFIFO()
        
    def test_enqueue(self):
        queue = MyFIFO()
        queue.enqueue('a')
        queue.enqueue('b')
        
    def test_dequeue(self):
        queue = MyFIFO()
        queue.enqueue('a')
        queue.enqueue('b')
        queue.enqueue('c')
        assert queue.dequeue() == 'a', "first item enqueued is not first item dequeued"
        assert queue.dequeue() == 'b'
        assert queue.dequeue() == 'c'

        with pytest.raises(IndexError):
            queue.dequeue()
        