import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style, init
import random
import time
import sys
from datetime import datetime

init(autoreset=True)

class TigerScan:
    def __init__(self):
        self.version = "v2.1 - DEVIL RECON"
        self.banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
{Fore.RED}║                  TIGERSCAN {self.version}                     ║
{Fore.RED}║          Advanced Unconventional Reconnaissance           ║
{Fore.RED}║                 Anarchist • Dark • Profitable             ║
{Fore.RED}╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        self.user_agents = [
            "TigerScan-Devil-v2.1",
            "Mozilla/5.0 (Anarchist Recon)",
            "BlackHat-Tiger-X",
            "ShadowRecon-Operator",
            "FuckTheFirewall-v9"
        ]

    def print_banner(self):
        print(self.banner)
        print(f"{Fore.CYAN}[+] TigerScan Professional Mode Activated - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    def scan_target(self, target):
        print(f"{Fore.MAGENTA}[★] بدء الهجوم الاحترافي غير المألوف على: {Fore.WHITE}{target}\n")
        time.sleep(0.7)

        headers = {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "text/html,application/xhtml+xml",
            "Connection": "keep-alive"
        }

        try:
            start_time = time.time()
            response = requests.get(f"http://{target}", 
                                  headers=headers, 
                                  timeout=12, 
                                  allow_redirects=True)
            
            elapsed = round(time.time() - start_time, 2)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = soup.find_all('a')
            title = soup.title.string.strip() if soup.title else "No Title"

            print(f"{Fore.GREEN}[✓] Connection Successful ({elapsed}s)")
            print(f"{Fore.GREEN}[✓] Status Code: {response.status_code}")
            print(f"{Fore.YELLOW}[★] Page Title: {title}")
            print(f"{Fore.CYAN}[★] Extracted Links: {len(links)}")
            print(f"{Fore.MAGENTA}[★] Server: {response.headers.get('Server', 'Hidden')}\n")

            # Unusual Intelligence
            print(f"{Fore.RED}[+] Unusual Recon Insights:")
            if any(word in response.text.lower() for word in ['wordpress', 'wp-content']):
                print(f"   → {Fore.YELLOW}WordPress Detected (High Exploit Potential)")
            if 'cloudflare' in response.headers.get('Server', '').lower():
                print(f"   → {Fore.YELLOW}Cloudflare Protected (Bypass Techniques Available)")

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[✘] فشل الاتصال: {str(e)[:80]}")
        except Exception as e:
            print(f"{Fore.RED}[✘] خطأ غير متوقع: {e}")

    def run(self):
        self.print_banner()
        target = input(f"{Fore.WHITE}[+] أدخل الهدف (example.com): {Fore.YELLOW}").strip()
        
        if not target:
            print(f"{Fore.RED}[!] لم يتم إدخال هدف.")
            sys.exit(1)
            
        if not target.startswith(('http://', 'https://')):
            target = target.replace('https://', '').replace('http://', '')
        
        self.scan_target(target)
        
        print(f"\n{Fore.CYAN}[+] TigerScan انتهى. جاهز للنسخة التجارية والفلوس.")

if __name__ == "__main__":
    scanner = TigerScan()
    scanner.run()
