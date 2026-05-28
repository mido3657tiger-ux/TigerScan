# 🐯 TigerScan: Advanced Bug Bounty Recon Framework

<div align="center">

![Version](https://img.shields.io/badge/TigerScan-v1.0-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20|%20Android-red?style=for-the-badge)

**Built by hunters, for hunters. The ultimate reconnaissance powerhouse.** 🎯

</div>

---

## 📖 Overview
**TigerScan** is a professional-grade reconnaissance framework designed to automate the discovery of vulnerabilities and assets in bug bounty programs. It leverages multi-threading and advanced scanning techniques to provide fast, reliable, and actionable intelligence.

## 🚀 Key Capabilities
* **Rapid Recon:** Automate subdomain discovery (2000+ per run).
* **Vulnerability Detection:** Built-in scanner for Open Redirects and common misconfigurations.
* **High-Speed Scanning:** Multi-threaded HTTP status code verification.
* **Data Persistence:** Intelligent SQLite integration for logging and historical analysis.
* **Reporting:** Automated generation of professional reports for findings.

## 🛠️ Requirements
* Python 3.x
* Git
* Termux (for Android users) or Linux OS

## 📥 Installation
Copy and run these commands in your terminal:
```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install git python -y

# Clone the repository
git clone [https://github.com/mido3657tiger-ux/TigerScan](https://github.com/mido3657tiger-ux/TigerScan)
cd TigerScan

# Setup environment
pip install requests
# If you have a requirements file, use: pip install -r requirements.txt
⚡ Usage
​1. Run Subdomain & Open Redirect Scanner:python3 hunt.py example.com
2. Run Multi-threaded HTTP Scanner:python3 tiger_core.py
📂 Project Structure
​hunt.py: Primary module for recon and redirect scanning.
​tiger_core.py: Engine for multi-threaded HTTP analysis.
​modules/: Extended scripts for specialized scanning.
​data/: Database storage for scan results.
​👤 Author
​Tiger-X-Cyber | Professional Bug Bounty Hunter
Follow on HackerOne
​⚠️ Legal Disclaimer
​This tool is for educational purposes and authorized security testing ONLY. The user is responsible for obeying all applicable local and international laws. Developers assume no liability for misuse.
​Stay hungry, hunt smart. 🎯
