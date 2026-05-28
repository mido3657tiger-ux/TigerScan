import os, requests

def scan(target):
    print(f"[*] Starting scan on {target}")
    os.system(f"subfinder -d {target} -silent | tee subs.txt")
    
    found = 0
    try:
        with open("subs.txt", "r") as f:
            lines = f.readlines()
    except:
        print("[!] No subdomains found")
        return
    
    print(f"[*] Found {len(lines)} subdomains")
    
    for line in lines:
        sub = line.strip()
        if not sub:
            continue
        url = "https://" + sub + "//google.com"
        try:
            r = requests.get(url, timeout=3, allow_redirects=False)
            location = r.headers.get('Location', '')
            if r.status_code in [301, 302] and "google.com" in location and sub not in location:
                print(f"[!] FOUND Open Redirect: {url}")
                with open("report.txt", "a") as rep:
                    rep.write(f"[VULN] {url}\nStatus: {r.status_code}\nLocation: {location}\n\n")
                found += 1
        except:
            pass
    
    print(f"[*] Done! Found {found} vulnerabilities")
    print(f"[*] Results saved in report.txt")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    scan(target)
