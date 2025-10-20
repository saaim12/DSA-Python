string = "abd"

def subsequences(unprocessed, processed, result):
    if unprocessed == "":
        result.append(list(processed))
        return
    char = unprocessed[0]
    subsequences(unprocessed[1:], processed, result)          # exclude char
    subsequences(unprocessed[1:], processed + char, result)   # include char

result = []
subsequences(string, "", result)
print(result)


def subStrings():
    return