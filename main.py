import sys
import argparse
from colorama import Fore, init

init(autoreset=True)

def banner():
    print(f"""
{Fore.CYAN}
    🐯 TIGER SCAN - ENTERPRISE EDITION
    [+] Framework: Offensive Recon & Vulnerability Scanner
    [+] Status: Active & Ready
    """)

def main():
    banner()
    parser = argparse.ArgumentParser(description="TigerScan Enterprise Framework")
    parser.add_argument("-t", "--target", help="Target domain for scanning", required=True)
    args = parser.parse_args()

    print(f"{Fore.GREEN}[*] Initializing TigerScan Modules for: {args.target}")
    print(f"{Fore.YELLOW}[!] System Ready. Please run hunt.py for specific tasks.")

if __name__ == "__main__":
    main()
