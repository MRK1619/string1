# Longest Common Prefix
def get_longest(words):
    if not words:
        return ''
    common = words[0]
    for word in words:
        while not word.startswith(common):
            common = common[:-1]
    return common

if __name__ == '__main__':
    print(f"Longest prefix: \n{get_longest(['flower', 'flow', 'fly'])}")