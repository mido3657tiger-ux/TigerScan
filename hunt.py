import requests
import sys
import threading
from colorama import Fore, Style, init

# تهيئة الألوان
init(autoreset=True)

class TigerHunter:
    def __init__(self, target):
        self.target = target
        self.vuln_file = "vulnerabilities.txt"
        
    def banner(self):
        print(f"{Fore.CYAN}[*] TigerScan - Offensive Recon Module")
        print(f"{Fore.CYAN}[*] Target: {self.target}")
        print("-" * 40)

    def check_open_redirect(self, subdomain):
        # مصفوفة تجريبية للحقن (Payloads)
        payloads = ["//google.com", "///google.com", "https://google.com"]
        for p in payloads:
            url = f"https://{subdomain}/{p}"
            try:
                response = requests.get(url, timeout=5, allow_redirects=False)
                if response.status_code in [301, 302, 303]:
                    location = response.headers.get('Location', '')
                    if "google.com" in location:
                        print(f"{Fore.RED}[!] VULNERABILITY FOUND: {url}")
                        self.save_result(url, location)
            except:
                pass

    def save_result(self, url, location):
        with open(self.vuln_file, "a") as f:
            f.write(f"URL: {url}\nRedirect: {location}\n{'-'*20}\n")

    def run_recon(self):
        self.banner()
        print(f"{Fore.YELLOW}[+] Starting Deep Scan Modules...")
        # قائمة تجريبية للنطاقات
        subdomains = [f"dev.{self.target}", f"api.{self.target}", f"test.{self.target}"]
        
        threads = []
        for sub in subdomains:
            t = threading.Thread(target=self.check_open_redirect, args=(sub,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        print(f"{Fore.GREEN}[*] Recon cycle finished. Check {self.vuln_file} for results.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hunt.py <target.com>")
    else:
        hunter = TigerHunter(sys.argv[1])
        hunter.run_recon()
