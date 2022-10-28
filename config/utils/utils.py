
def name_formatting(value: str) -> str:
    """
    Method for format string as a Name
    @param value: String value, which needs formatting.
    @return: return a string as a name format.
    """
    return value.replace('(', '').replace(')', '')
