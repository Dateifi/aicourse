# Update "from oving-uke04 import ..." below with the name of the python file containing your classes
# Run tests from command line: python -m pytest SortingUnitTests.py

from Uke4_Øvingsoppgaver import random_string_list, insertion_sort, merge_sort, merge
import pytest

def test_random_string():
    list_length = 7
    str_list = random_string_list(list_length)
    assert len(str_list) == list_length, "Incorrect list length"
    assert isinstance(str_list[0],str), "Element in list not instance of string"
    assert len(str_list[0]) == 10, "String not 10 characters long"
    
def test_insertion_sort_num():
    unsorted_list = [5,3,8,4,1,0,7]
    sorted_list = [0,1,3,4,5,7,8]
    assert insertion_sort(unsorted_list) == sorted_list, "Incorrect sorting"

def test_insertion_sort_strings():
    unsorted_list = random_string_list(1000)
    assert insertion_sort(unsorted_list) == sorted(unsorted_list), "Incorrect sorting"
    
def test_merge():
    list1 = [5,7,42,69]
    list2 = [0,21,32]
    merged_list = [0,5,7,21,32,42,69]
    assert merge(list1,list2) == merged_list, "Incorrect merging of lists"
    
def test_merge_sort_num():
    unsorted_list = [5,3,8,4,1,0,7]
    sorted_list = [0,1,3,4,5,7,8]
    assert merge_sort(unsorted_list) == sorted_list, "Incorrect sorting"    
    
def test_merge_sort_strings():
    unsorted_list = random_string_list(1000)
    assert merge_sort(unsorted_list) == sorted(unsorted_list), "Incorrect sorting"

