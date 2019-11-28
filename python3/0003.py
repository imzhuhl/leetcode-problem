import collections

def lengthOfLongestSubstring(s: str) -> int:
    record = collections.deque()
    hs = set()
    rst = 0
    for i, c in enumerate(s):
        if hs and c in hs:
            rst = max(rst, len(hs))
            for i in range(len(hs)):
                x = record.popleft()
                hs.remove(x)
                if x == c:
                    break
        hs.add(c)
        record.append(c)
    rst = max(rst, len(hs))
    return rst 


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abba"))
