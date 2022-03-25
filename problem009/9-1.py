def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    i = len(s) - 1
    while i > 0 and s[i] == " ":
        i -= 1
    last_char_index = i

    while i >= 0 and s[i] != " ":
        i -= 1
    if last_char_index == 0:
        return 1
        
    return last_char_index - i

s = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]

for i in s:
    print(lengthOfLastWord(i))
