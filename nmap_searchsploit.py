import subprocess
import xml.etree.ElementTree as ET
import tempfile
import os
import sys
from collections import defaultdict
from datetime import datetime
from fpdf import FPDF

def get_user_input():
    print("\n[+] Select Nmap timing template:")
    print("   T1: Paranoid\n   T2: Sneaky\n   T3: Normal\n   T4: Aggressive\n   T5: Insane")
    timing = input("Enter timing template (T1/T2/T3/T4/T5): ").strip().upper()
    if timing not in ["T1", "T2", "T3", "T4", "T5"]:
        print("Invalid timing template. Defaulting to T3.")
        timing = "T3"

    print("\n[+] Port scan options:")
    print("   1. All ports (-p-)")
    print("   2. Common ports (default)")
    port_choice = input("Scan all ports? (1 for -p-, 2 for default): ").strip()
    port_flag = "-p-" if port_choice == "1" else ""

    return timing, port_flag

def run_nmap_scan(target, timing, port_flag):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as temp_file:
        output_file = temp_file.name
    try:
        print(f"\n[+] Running Nmap scan: timing={timing}, ports={port_flag or 'default'}, aggressive mode enabled")
        cmd = ["sudo", "nmap", "-sV", "-A", f"-{timing}"]
        if port_flag:
            cmd.append(port_flag)
        cmd += ["-oX", output_file, target]
        subprocess.run(cmd, check=True)
        return output_file
    except subprocess.CalledProcessError:
        print("Nmap scan failed.")
        return None

def parse_services_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    services = []
    for service in root.findall(".//service"):
        product = service.attrib.get("product")
        version = service.attrib.get("version")
        if product:
            if version:
                short_version = version.split(".")[0]
                search_term = f"{product} {short_version}"
            else:
                search_term = product
            services.append(search_term)
    return list(set(services))  # Remove duplicates

def search_exploits(services):
    results = defaultdict(str)
    for service in services:
        print(f"\n🔍 Searching exploits for: {service}")
        try:
            result = subprocess.run(["searchsploit", service], capture_output=True, text=True)
            clean_output = result.stdout.strip()
            if clean_output:
                results[service] = clean_output
                print(clean_output)
            else:
                print("No known exploits found.")
        except Exception as e:
            print(f"❌ Error with SearchSploit: {str(e)}")
    return results

def save_summary_to_file(results, target):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"exploit_summary_{target.replace('.', '_')}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Exploit Search Summary for Target: {target}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        for service, output in results.items():
            f.write(f"\n--- {service} ---\n")
            f.write(output + "\n")
        f.write("\n" + "=" * 60 + "\n")
    print(f"\n[+] Summary saved to {filename}")
    return filename

def generate_pdf_report(text_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(text_file, "r") as f:
        for line in f:
            pdf.multi_cell(0, 10, line)

    pdf_file = text_file.replace(".txt", ".pdf")
    pdf.output(pdf_file)
    print(f"[+] PDF report generated: {pdf_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 nmap_searchsploit.py <target-ip-or-domain>")
        return

    target = sys.argv[1]
    timing, port_flag = get_user_input()

    xml_file = run_nmap_scan(target, timing, port_flag)
    if not xml_file:
        return

    print("\n[+] Parsing detected services...")
    services = parse_services_from_xml(xml_file)
    os.remove(xml_file)

    if not services:
        print("No services detected.")
        return

    print("\n[+] Starting exploit search...")
    results = search_exploits(services)

    summary_file = save_summary_to_file(results, target)
    generate_pdf_report(summary_file)

if __name__ == "__main__":
    main()
