def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Type-annotated function element_length that takes a iterable
        argument.
        Args:
            lstr: iterable object.
        Return:
            element length.
    """
    return [(i, len(i)) for i in lst]
