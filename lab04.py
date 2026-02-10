def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function should take two lists and return a new list containing only the elements that are present in both lists. The final list can be in any order.

    Parameters:
    ----------
    list1 : list
        The first list to compare.
    list2 : list
        The second list to compare.

    Returns:
    -------
    list
        A list of elements common to both list1 and list2.
    """
    return list(set(list1) & set(list2))
    