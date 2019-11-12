"""
function annotation
clip(text: str, max_len: 'int > 0'=5) -> str
"""


def clip(text: str, max_len: 'int > 0' = 5) -> str:
    """
    cut text from the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before > -1:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after > -1:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print('12 3 4567 89: ->', clip('12 3 4567 89'))
    print('1234567 89: ->', clip('1234567 89'))
    print('123456789: ->', clip('123456789'))
    print(clip.__annotations__)
