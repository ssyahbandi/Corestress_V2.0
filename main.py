# main.py
from setupcore import create_template
from cust import process_customer
from goods import populate_detail_faktur
from db import full_vlookup
from colorama import init, Fore, Style

init(autoreset=True)

LOCATION_CONFIG = {
    '1': {
        'name': 'Surabaya',
        'npwp': '0947793543518000',
        'id_tku': '0947793543518000000000',
        'ktp_sheet': 'NPWPKTP BBN SBY-BJM (NEW)'
    },
    '2': {
        'name': 'Semarang',
        'npwp': '0947793543518000',
        'id_tku': '0947793543518000000001',
        'ktp_sheet': 'NPWPKTP BBN SMG (NEW)'
    },
    '3': {
        'name': 'Samarinda',
        'npwp': '0947793543518000',
        'id_tku': '0947793543518000000002',
        'ktp_sheet': 'NPWPKTP BBN SMD-BPP (NEW)'
    },
    '4': {
        'name': 'Bagong Jaya',
        'npwp': '0712982594609000',
        'id_tku': '0712982594609000000000',
        'ktp_sheet': 'NPWPKTP BJ (NEW)'
    }
}

def get_location():
    print(Fore.YELLOW + "Pilih lokasi:" + Style.RESET_ALL)
    print("1. Surabaya\n2. Semarang\n3. Samarinda\n4. Bagong Jaya")
    location = input(Fore.GREEN + "Masukkan nomor: " + Style.RESET_ALL).strip()
    if location not in LOCATION_CONFIG:
        raise ValueError(Fore.RED + "Lokasi tidak valid!" + Style.RESET_ALL)
    return LOCATION_CONFIG[location]

def main():
    print(Fore.CYAN + "\n=== MEMULAI PROSES ===" + Style.RESET_ALL)
    
    loc_data = get_location()
    output_file = input(Fore.GREEN + "Masukkan nama file output (tanpa .xlsx): " + Style.RESET_ALL).strip()
    
    # Step 1: Create Template
    print(Fore.YELLOW + "\n=== STEP 1: BUAT TEMPLATE ===" + Style.RESET_ALL)
    create_template(output_file, loc_data)
    
    # Step 2: Process Customer
    print(Fore.YELLOW + "\n=== STEP 2: INPUT DATA CUSTOMER ===" + Style.RESET_ALL)
    source_file = input(Fore.GREEN + "Masukkan nama file sumber data: " + Style.RESET_ALL).strip()
    if not source_file.endswith('.xlsx'):
        source_file += '.xlsx'
    use_ref = input(Fore.GREEN + "Gunakan referensi? (y/n): ").lower() == 'y'
    process_customer(f"{output_file}.xlsx", source_file, use_ref, loc_data['id_tku'])
    
    # Step 3: Process Goods
    print(Fore.YELLOW + "\n=== STEP 3: INPUT DATA BARANG ===" + Style.RESET_ALL)
    populate_detail_faktur(f"{output_file}.xlsx", source_file)
    
    # Step 4: VLOOKUP
    print(Fore.YELLOW + "\n=== STEP 4: VLOOKUP DATA ===" + Style.RESET_ALL)
    full_vlookup(f"{output_file}.xlsx", loc_data)
    
    print(Fore.GREEN + "\n✅ Semua proses selesai! File output:", f"{output_file}.xlsx" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
