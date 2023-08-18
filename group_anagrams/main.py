from typing import List
from collections import defaultdict

# TODO DOCK CONTAINERS
# TODO For loop hashmap then save chars dict with
# ints indicating the amount needed. Inside with a list of words then
# extract the lists of words connected to the chars dict return.


def group_anagrams(strs: List[str]) -> List[List[str]]:
    hash_map = defaultdict(int)
