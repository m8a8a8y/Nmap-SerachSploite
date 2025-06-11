Here is your complete `README.md` file ready for GitHub:

---

````markdown
# Nmap SearchSploit Automation Tool

Automates vulnerability scanning by combining **Nmap** service detection with **SearchSploit** vulnerability lookup. Generates organized text and PDF reports summarizing discovered exploits.

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

- Interactive CLI to select Nmap timing templates (T1–T5)
- Option to scan all ports (`-p-`) or default/common ports
- Performs aggressive scans with service version detection (`-A -sV`)
- Parses Nmap XML output to extract services and versions
- Uses **SearchSploit** to find exploits for detected services (based on product + major version)
- Generates detailed **text and PDF reports**
- Automatically runs with `sudo` for privileged scan capabilities

---

## ✅ Requirements

- **Python 3.6+**
- **Nmap** – [Download](https://nmap.org/download.html)
- **SearchSploit** – from [Exploit-DB](https://www.exploit-db.com/searchsploit)
- **fpdf** Python package for PDF report generation

---

## ⚙️ Installation

### 1. Install Nmap

```bash
sudo apt update
sudo apt install nmap
````

### 2. Install SearchSploit

```bash
sudo apt install exploitdb
```

### 3. Install Python dependencies

```bash
pip3 install fpdf
```

### 4. Clone the repository

```bash
git clone https://github.com/yourusername/nmap-searchsploit-tool.git
cd nmap-searchsploit-tool
```

---

## 💻 Usage

Run the tool with `sudo` for full privileges:

```bash
sudo python3 nmap_searchsploit.py <target-ip-or-domain>
```

### Example:

```bash
sudo python3 nmap_searchsploit.py 192.168.1.53
```

### You will be prompted to:

1. Select a **timing template**:

   ```
   T1: Paranoid
   T2: Sneaky
   T3: Normal (default)
   T4: Aggressive
   T5: Insane
   ```

2. Choose **port scan option**:

   ```
   1. All ports (-p-)
   2. Common ports (default)
   ```

---

## 📄 Output

The tool generates two output files:

* `exploit_summary_<target>_<timestamp>.txt` — Full SearchSploit results
* `exploit_summary_<target>_<timestamp>.pdf` — Clean summary report for easy sharing

### Example:

```
exploit_summary_192_168_1_53_20250611_123456.txt
exploit_summary_192_168_1_53_20250611_123456.pdf
```

---

## 🧰 Troubleshooting

* **`ModuleNotFoundError: No module named 'fpdf'`**
  Install the missing dependency:

  ```bash
  pip3 install fpdf
  ```

* **`Nmap scan failed`**
  Ensure you run the script with `sudo`:

  ```bash
  sudo python3 nmap_searchsploit.py <target>
  ```

* **`searchsploit: command not found`**
  Install Exploit-DB tools:

  ```bash
  sudo apt install exploitdb
  ```

* **`-p-` port scan option not working**
  Ensure you select option `1` when prompted and note that scanning all ports can be slow.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to:

* Open [issues](https://github.com/yourusername/nmap-searchsploit-tool/issues)
* Submit [pull requests](https://github.com/yourusername/nmap-searchsploit-tool/pulls)

### Future Improvements:

* CVE severity scoring via [NVD API](https://nvd.nist.gov)
* HTML report generation
* Integration with Metasploit for automated exploitation
* Asynchronous/multi-threaded search for faster lookups

---


## 👤 Author

**(m8a8a8y)**
Cybersecurity Engineer | Penetration Tester
[GitHub Profile](https://github.com/m8a8a8y)

```


