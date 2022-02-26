import csv
import ipaddress
import sys

from ipv4_to_asm.bin_trie import common_bin_prefix, BinTrie, u32_to_32b_str


def load_ipv4_tsv_file(path_to_tsv: str) -> BinTrie:
    """
    Load tsv file in the following format:
    Each line is a tab-separated record with this format:
    Start of IP address range (as integer, inclusive)
    End of IP address range (as integer, inclusive)
    Autonomous System Number - ASN
    Country
    Autonomous System name
    and returns binary trie used for asm lookup based on ip
    """
    res_tree = BinTrie()
    try:
        with open(path_to_tsv, "r", encoding="utf8") as file:
            tsv_file = csv.reader(file, delimiter="\t")
            for line in tsv_file:
                start_ip = int(line[0].strip())
                end_ip = int(line[1].strip())
                asm = int(line[2].strip())
                prefix_bin = common_bin_prefix(start_ip, end_ip)
                res_tree.insert(prefix_bin, asm)
        print("Read tsv file successfully")
    except Exception as e:
        print(e)
    return res_tree


def ip_to_asm_lookup(asm_lookup_tree: BinTrie, ipv4_str: str) -> int:
    """
    Given asm_lookup_tree and ip given in string format e.g. '31.13.24.0'
    returns allocated ASN
    """
    ipv4_u32 = int(ipaddress.IPv4Address(ipv4_str))  # convert from ip string to unsigned integer
    ipv4_bin32 = u32_to_32b_str(ipv4_u32)
    return asm_lookup_tree.find_prefix(ipv4_bin32)


def is_valid_ipv4(ipv4: str) -> bool:
    try:
        ipaddress.ip_address(ipv4)
    except ValueError:
        return False
    return True


def user_input_loop(lookup_tree: BinTrie):
    """
    Basic cli, receives from user ip and displays ASM found
    """
    while True:
        print("\n* Enter nothing to exit *")
        user_input = input("Enter ip (example: 31.13.24.0): ")
        if not is_valid_ipv4(user_input):
            print("Invalid ipv4 format")
        elif user_input == '':  # exit condition
            exit(0)
        else:
            res = ip_to_asm_lookup(lookup_tree, user_input)
            if res is not None:
                print(f"ASM result: {res}")
            else:
                print("ASM not found")


if __name__ == '__main__':
    path = ''
    if len(sys.argv) == 1:
        path = 'ip2asn-v4-u32.tsv'
    elif len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Missing argument: path to tsv file")
        exit(1)

    tree = load_ipv4_tsv_file(path)
    user_input_loop(tree)
