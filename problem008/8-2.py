def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.strip().split()[-1])

s = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]

for i in s:
    print(lengthOfLastWord(i))