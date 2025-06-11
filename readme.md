Here's the **full `README.md`** file for your **Nmap SearchSploit Automation Tool**, formatted for GitHub and ready to publish:

---

````markdown
# 🔍 Nmap SearchSploit Automation Tool

A cybersecurity tool that automates vulnerability scanning by combining **Nmap** service detection with **SearchSploit** vulnerability lookups. It extracts detected services from a target, searches for known public exploits, and generates both **text and PDF reports** summarizing the results.

---

## 📚 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🚀 Features

- User-friendly CLI for Nmap timing and port options
- Performs aggressive Nmap scan (`-A`) with service detection (`-sV`)
- Option to scan **all 65535 ports** (`-p-`) or default ports
- Parses Nmap XML results to extract services and major versions
- Searches **Exploit-DB** using `searchsploit` for each detected service
- Saves results in both `.txt` and `.pdf` formats for easy analysis and sharing
- Supports Linux and is built for **Kali Linux penetration testers**

---

## ✅ Requirements

- Python 3.6 or higher
- [Nmap](https://nmap.org/download.html)
- [SearchSploit](https://github.com/offensive-security/exploitdb)
- Python package: `fpdf`

---

## ⚙️ Installation

### 1. Install Dependencies

#### 📦 Nmap

```bash
sudo apt update
sudo apt install nmap
````

#### 📦 SearchSploit

```bash
sudo apt install exploitdb
```

#### 📦 Python package

```bash
pip3 install fpdf
```

### 2. Clone This Repository

```bash
git clone https://github.com/yourusername/nmap-searchsploit-tool.git
cd nmap-searchsploit-tool
```

---

## 💻 Usage

Run the tool with superuser privileges:

```bash
sudo python3 nmap_searchsploit.py <target-ip-or-domain>
```

### 🧭 Interactive Options

1. **Timing template**

   ```
   T1: Paranoid
   T2: Sneaky
   T3: Normal (default)
   T4: Aggressive
   T5: Insane
   ```

2. **Port scanning**

   ```
   1. All ports (-p-)
   2. Common ports (default)
   ```

---

## 📄 Output

The script generates two files after scanning:

* ✅ `exploit_summary_<target>_<timestamp>.txt`
  A full log of SearchSploit results.

* ✅ `exploit_summary_<target>_<timestamp>.pdf`
  A clean summary report with key info, formatted for review or reporting.

Example:

```bash
exploit_summary_192_168_1_53_20250611_123456.txt
exploit_summary_192_168_1_53_20250611_123456.pdf
```

---

## 🧰 Troubleshooting

| Issue                                         | Solution                                                    |
| --------------------------------------------- | ----------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'fpdf'` | Install with `pip3 install fpdf`                            |
| `searchsploit: command not found`             | Run `sudo apt install exploitdb`                            |
| Nmap scan fails                               | Ensure you're running with `sudo`                           |
| Long scan time                                | All-port scan (`-p-`) is slow — use default ports if needed |

---

## 🔒 Sample Use Case

This tool is ideal for:

* Penetration testers conducting fast recon
* Cybersecurity students learning about exploit discovery
* Red teams automating passive scanning workflows

---

## 🤝 Contributing

We welcome contributions and improvements! Here's how to help:

* Report bugs via GitHub [Issues](https://github.com/yourusername/nmap-searchsploit-tool/issues)
* Submit PRs for features or fixes
* Suggest enhancements (e.g., CVE scoring, Metasploit integration)

### 🔧 Future Enhancements

* CVSS scoring from NVD API
* HTML report generation
* Exploit validation via Metasploit
* Multithreaded SearchSploit queries

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mohammad Abu Yahya** ([@m8a8a8y](https://github.com/m8a8a8y))
Cybersecurity Engineer | CTF Player | Red Team & SOC Analyst
King Faisal University Cybersecurity Club Leader
🇯🇴 Based in Jordan | Passionate about Python, Pentesting, and Automation

```

---

Let me know if you’d like a matching `LICENSE`, `.gitignore`, or `requirements.txt` file.
```
