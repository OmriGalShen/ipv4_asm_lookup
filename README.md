# ipv4_asm_lookup  

## Background  

IPv4 addresses on the internet are 32 bits.   
These addresses are allocated by the Internet Assigned Numbers Authority (IANA) to organizations that are called “Autonomous Systems”.  
Each such organization has a unique Autonomous System Number - ASN.  
We are going to write a program which when given input an IP address returns the ASN it is allocated to.  

## What the script does?  
Given tsv file with updated IPv4 addresses to ASN allocation such that can be found at [iptoasn](https://iptoasn.com/)  
Store information in binary Trie (prefix) data structure [wiki](https://en.wikipedia.org/wiki/Trie)  
For quick lookup of ASM given ipv4  

## How to use:
Run lookup.py using python3  
if the file was run without arguments it will read 'ip2asn-v4-u32.tsv' by default   
(needs to be the same path as the lookup.py)   
a command line argument can be given with path to other tsv file with the same format (exmaple.tsv file can be used)  
the spcript will run basic cli for ipv4 ASM lookout
