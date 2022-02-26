from __future__ import annotations


def numeric_char_to_index(ch: str) -> int:
    """
    e.g. '1' -> 1, '0'-> 0
    """
    return ord(ch) - ord('0')


def u32_to_32b_str(num: int) -> str:
    """
    Convert to 32 bits binary string
    e.g. 16 -> 00000000000000000000000000010000
    """
    return f'{num:032b}'


def common_bin_prefix(num1: int, num2: int) -> str:
    """
    Convert to 32bit binary and return common binary prefix
    """
    s1 = u32_to_32b_str(num1)
    s2 = u32_to_32b_str(num2)
    if s1[0] != s2[0]:
        return ''
    for ind in range(min(len(s1), len(s2))):
        if s1[ind] != s2[ind]:
            return s1[0:ind]
    return s1 if len(s1) <= len(s2) else s1


class _BinTrieNode:
    def __init__(self, is_terminal: bool = False, value=None):
        self.children: list[None | _BinTrieNode] = [None, None]
        self.is_terminal = is_terminal
        self.value = value


class BinTrie:
    def __init__(self):
        self.root_node = _BinTrieNode()

    def find(self, key_bin32: str):
        curr_node = self.root_node
        for ind in range(len(key_bin32)):
            child_ind = numeric_char_to_index(key_bin32[ind])
            next_node = curr_node.children[child_ind]
            if next_node is None:
                return False
            else:
                curr_node = next_node
        return curr_node.value

    def find_prefix(self, key_bin32: str):
        curr_node = self.root_node
        res_value = None
        for ind in range(len(key_bin32)):
            child_ind = numeric_char_to_index(key_bin32[ind])
            next_node = curr_node.children[child_ind]
            if next_node is None:
                break
            curr_node = next_node
            if curr_node.is_terminal:
                res_value = curr_node.value
        return res_value

    # def find_prefix(self, key):
    #     curr_node = self.root_node
    #     for ind in range(len(key)):
    #         child_ind = numeric_char_to_index(key[ind])
    #         next_node = curr_node.children[child_ind]
    #         if next_node is None:
    #             return False
    #         elif next_node.is_terminal:
    #             return next_node.value
    #         else:
    #             curr_node = next_node
    #     return curr_node.value

    def insert(self, key_bin32: str, value):
        curr_node = self.root_node
        for ind in range(len(key_bin32)):
            child_ind = numeric_char_to_index(key_bin32[ind])
            if curr_node.children[child_ind] is None:
                next_node = curr_node.children[child_ind] = _BinTrieNode()
            else:
                next_node = curr_node.children[child_ind]
            curr_node = next_node
        curr_node.value = value
        curr_node.is_terminal = True
