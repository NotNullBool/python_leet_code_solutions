
def is_anagram(s: str, t: str) -> bool:
    slist = list(s)
    tlist = list(t)
    slist.sort()
    tlist.sort()
    return slist == tlist

if __name__ == "__main__":
    print(is_anagram("hello","olleh"))
