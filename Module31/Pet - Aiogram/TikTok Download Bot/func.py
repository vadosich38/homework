def find_substring(string: str, sub_string: str) -> str:
    index = string.find(sub_string)
    return string[index + len(sub_string): index + len(sub_string) + 19]
