"""
IP WHOIS Lookup Tool

Created on : 18-02-2018
Created by : Saurabh Modi

Reads a list of IP addresses from input.txt (one per line), runs a WHOIS
lookup on each one and appends the result to WhoIs_Look_Up.csv.
A reverse DNS (PTR) helper is also included for extra IP context.
"""

import dns.resolver
import dns.reversename
from ipwhois import IPWhois

INPUT_FILE = "input.txt"
OUTPUT_FILE = "WhoIs_Look_Up.csv"
NOT_FOUND = "Not Found"


class IPLookup:
    
    def whois_lookup(self, ip_address):
        #Return the WHOIS record (dict) for an IP, or 'Not Found' on failure.
        try:
            return IPWhois(ip_address).lookup_whois()
        except Exception:
            return NOT_FOUND

    def reverse_dns(self, ip_address):
        #Return the first PTR (reverse DNS) record for an IP, or 'Not Found' on failure.
        try:
            reverse_name = dns.reversename.from_address(ip_address)
            resolver_call = getattr(dns.resolver, "resolve", None) or dns.resolver.query
            answers = resolver_call(reverse_name, "PTR")

            for record in answers:
                return str(record)
            return NOT_FOUND
        except Exception:
            return NOT_FOUND


def format_record(record):
    
    #Quotes and brackets are stripped to keep the output easy to read.
    
    text = str(record)
    for char in ("'", "{", "}", "[", "]"):
        text = text.replace(char, "")
    return text


def main():
    lookup = IPLookup()

    
    with open(INPUT_FILE, "r") as input_file, open(OUTPUT_FILE, "a") as output_file:
        for line in input_file:
            ip_address = line.strip()

            if not ip_address:
                continue

            result = lookup.whois_lookup(ip_address)
            output_file.write(ip_address + "=>," + format_record(result) + "\n")
            print(ip_address + " successfully written to " + OUTPUT_FILE)


if __name__ == "__main__":
    main()
