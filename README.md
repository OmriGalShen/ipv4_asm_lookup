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
1. Extract 'ip2asn-v4-u32.tsv.gz', such that 'ip2asn-v4-u32.tsv' should be in project folder  
2. Run 'python .\lookup.py' to run with default 'ip2asn-v4-u32.tsv' file  
3. Run 'python .\lookup.py path_to_tsv' to run other tsv file (such as 'exmaple.tsv' in project file)  
4. Follow basic cli instructions
