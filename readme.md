# Nmap SearchSploit Automation Tool

Automates vulnerability scanning by combining **Nmap** service detection with **SearchSploit** vulnerability lookup, and generates a PDF report summarizing discovered exploits.

---

## Table of Contents

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

## Features

- Runs **Nmap** scan with user-selected timing template (`T1` to `T5`)
- Option to scan **all ports** (`-p-`) or default common ports
- Enables **aggressive scan** (`-A`) and service version detection (`-sV`)
- Parses Nmap XML output to extract detected services and versions
- Searches for known exploits using **SearchSploit** on extracted services (searches product + major version)
- Generates a clean, organized **PDF report** summarizing vulnerabilities found
- Runs Nmap with **sudo** automatically for full scan privileges

---

## Requirements

- Python 3.6 or higher
- [Nmap](https://nmap.org/download.html) installed and available in system PATH
- [SearchSploit](https://www.exploit-db.com/searchsploit) tool installed and available in system PATH
- Python package `fpdf` for PDF report generation

---

## Installation

1. **Install Nmap**

   On Debian/Ubuntu/Kali:

   ```bash
   sudo apt update
   sudo apt install nmap
````

2. **Install SearchSploit**

   On Debian/Ubuntu/Kali:

   ```bash
   sudo apt install exploitdb
   ```

3. **Install Python dependencies**

   ```bash
   pip3 install fpdf
   ```

4. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/nmap-searchsploit-tool.git
   cd nmap-searchsploit-tool
   ```

---

## Usage

Run the script with sudo (required for full scans):

```bash
sudo python3 nmap_searchsploit.py <target-ip-or-domain>
```

### Example:

```bash
sudo python3 nmap_searchsploit.py 192.168.1.53
```

### You will be prompted to:

1. Select the Nmap timing template:

   ```
   T1: Paranoid
   T2: Sneaky
   T3: Normal (default)
   T4: Aggressive
   T5: Insane
   ```

2. Choose port scan option:

   ```
   1. All ports (-p-)
   2. Common ports (default)
   ```

### What happens next:

* The tool runs an Nmap scan using your choices (`-sV`, `-A`, timing template, ports)
* Parses the XML output to extract services and versions
* Uses SearchSploit to find public exploits related to detected services
* Prints the results to the console
* Saves a text summary and a PDF report of the findings in the current directory

---

## Output

* `exploit_summary_<target>_<timestamp>.txt` — Text file with detailed SearchSploit results
* `exploit_summary_<target>_<timestamp>.pdf` — PDF report summarizing the scan results

Example files generated:

```
exploit_summary_192_168_1_53_20250611_123456.txt
exploit_summary_192_168_1_53_20250611_123456.pdf
```

---

## Troubleshooting

* **`ModuleNotFoundError: No module named 'fpdf'`**

  Install the `fpdf` Python package:

  ```bash
  pip3 install fpdf
  ```

* **`Nmap scan failed`**

  Ensure you run the script with `sudo`:

  ```bash
  sudo python3 nmap_searchsploit.py <target>
  ```

* **`searchsploit` command not found**

  Make sure exploitdb is installed and your PATH includes the directory:

  ```bash
  sudo apt install exploitdb
  ```

* **Port scan with `-p-` not working**

  The tool supports scanning all ports with `-p-` option, but scanning all ports will take longer.

---

## Contributing

Contributions, suggestions, and feature requests are welcome! Feel free to:

* Open issues for bugs or feature requests
* Submit pull requests with improvements

Potential enhancements:

* Add CVE severity scoring (via NVD API)
* Generate HTML reports for better formatting
* Integrate with Metasploit for exploit testing
* Add multi-threading for faster SearchSploit queries

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

Mohammad Abu Yahya

-

## requirements.txt (optional)

```
pip3 install fpdf

```



