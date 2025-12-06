import csv

def get_thailand_unesco_sites():
    """
    Create Thailand UNESCO World Heritage Sites CSV data
    Thailand has 6 UNESCO World Heritage Sites (4 cultural, 2 natural)
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'AYUTTHAYA',
            'Name': 'Historic City of Ayutthaya',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Ayutthaya',
            'Latitude': '14.3500',
            'Longitude': '100.5667',
            'Description': 'Historic City of Ayutthaya - UNESCO World Heritage Site. Ruins of the ancient capital of Siam with temples and palaces.',
            'URL': 'https://whc.unesco.org/en/list/576',
            'Country': 'Thailand',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'SUKHOTHAI',
            'Name': 'Historic Town of Sukhothai and Associated Historic Towns',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Sukhothai, Kamphaeng Phet, Phitsanulok',
            'Latitude': '17.0167',
            'Longitude': '99.7000',
            'Description': 'Historic Town of Sukhothai - UNESCO World Heritage Site. Remains of the first capital of Siam with Buddhist monuments.',
            'URL': 'https://whc.unesco.org/en/list/574',
            'Country': 'Thailand',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'BANCHIANG',
            'Name': 'Ban Chiang Archaeological Site',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Udon Thani',
            'Latitude': '17.4000',
            'Longitude': '103.2333',
            'Description': 'Ban Chiang Archaeological Site - UNESCO World Heritage Site. Prehistoric settlement with evidence of early bronze metallurgy.',
            'URL': 'https://whc.unesco.org/en/list/575',
            'Country': 'Thailand',
            'UNESCO_Year': '1992'
        },
        {
            'Park_Code': 'DONGPHYAYAYEN',
            'Name': 'Dong Phayayen-Khao Yai Forest Complex',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Nakhon Ratchasima, Prachinburi, Sa Kaeo, Buriram, Nakhon Nayok, Saraburi',
            'Latitude': '14.3333',
            'Longitude': '102.0000',
            'Description': 'Dong Phayayen-Khao Yai Forest Complex - UNESCO World Heritage Site. Important forest ecosystem with diverse wildlife.',
            'URL': 'https://whc.unesco.org/en/list/590',
            'Country': 'Thailand',
            'UNESCO_Year': '2005'
        },
        {
            'Park_Code': 'THUNGYAI',
            'Name': 'Thungyai-Huai Kha Khaeng Wildlife Sanctuaries',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Kanchanaburi, Tak, Uthai Thani',
            'Latitude': '15.3333',
            'Longitude': '99.1667',
            'Description': 'Thungyai-Huai Kha Khaeng Wildlife Sanctuaries - UNESCO World Heritage Site. Large protected area with diverse ecosystems.',
            'URL': 'https://whc.unesco.org/en/list/591',
            'Country': 'Thailand',
            'UNESCO_Year': '1991'
        }
    ]
    
    return unesco_sites

def save_thailand_unesco_csv(data, filename):
    """Save Thailand UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Thailand UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Thailand UNESCO World Heritage Sites data...")
    
    unesco_data = get_thailand_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Thailand_UNESCO_Sites.csv')
    save_thailand_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

