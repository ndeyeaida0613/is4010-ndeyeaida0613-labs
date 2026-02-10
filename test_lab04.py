import pytest
from lab04 import find_common_elements, find_user_by_name, get_list_of_even_numbers

def test_find_common_elements_with_common_items():
    """Test find common elements whn they exist."""
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]

    assert set(find_common_elements(l1, l2)) == {4, 5}

    def test_find_common_elements_with_no_common_items():
        """Test finding common elements when none exist."""
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]

        assert find_common_elements(l1, l2) == []

        def test_find_common_elements_with_duplicates():
            """Test finding common elements with duplicates in lists."""
            l1 = [1, 1, 2, 3, 3]
            l2 = [1, 2, 2, 4, 5]
            result = find_common_elements(l1, l2)

            assert set(result) == {1, 2}

@pytest.fixture
def sample_users():
    """Fixture proviting sample user data for testing."""
    return [
        {"name": "Alice", "age": 30, "email":"alice@example.com"},
        {"name": "Bob", "age": 25, "email":"bob@example.com"},
        {"name": "Charlie", "age": 35},
    ]

def test_find_user_by_name_existing(sample_users):
    """Test finding a user that exists."""
    assert find_user_by_name(sample_users, "alice") == {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

def test_find_user_by_name_non_existing(sample_users):
    """Test searching for a user that does not exist."""
    assert find_user_by_name(sample_users, "david") is None

def test_find_user_by_name_case_insensitivity(sample_users):
    """Test searching in an empty user list."""
    assert find_user_by_name([], "alice") is None
    
    def test_user_by_name_case_sensitivity(sample_users):
        """Test that user search is case-sensitive."""
        assert find_user_by_name(sample_users, "ALICE") is None
        assert find_user_by_name(sample_users, "alice") is not None
    
    def test_get_list_of_even_numbers_mixed():
        """Test filtering even numbers from a mixed list."""
        assert get_list_of_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    
def test_get_list_of_even_numbers_all_odd():
    """Test filtering even numbers from a list of all odd numbers."""
    assert get_list_of_even_numbers([1, 3, 5, 7]) == []

def test_get_list_of_even_numbers_all_even():
    """Test filtering even numbers from a list of all even numbers."""
    assert get_list_of_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_get_list_of_even_numbers_empty():
    """Test filtering even numbers from an empty list."""
    assert get_list_of_even_numbers([]) == []

def test_get_list_of_even_numbers_with_zero():
    """Test that zero is correctly identified as even."""
    assert get_list_of_even_numbers([0, 1, 2, 3]) == [0, 2]

def test_get_list_of_even_numbers_preserves_order():
    """Test that the order of even numbers is preserved."""
    assert get_list_of_even_numbers([10, 1, 8, 3, 6, 5, 4]) == [10, 8, 6]

def test_get_list_of_even_numbers_negative():
    """Test filtering even numbers including negative numbers."""
    assert get_list_of_even_numbers([-4, -3, -2, -1, 0, 1, 2]) == [-4, -2, 0, 2]


