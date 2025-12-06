import csv

def get_sri_lanka_unesco_sites():
    """
    Create Sri Lanka UNESCO World Heritage Sites CSV data
    Sri Lanka has 8 UNESCO World Heritage Sites (6 cultural, 2 natural)
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'POL',
            'Name': 'Ancient City of Polonnaruwa',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'North Central Province',
            'Latitude': '7.9333',
            'Longitude': '81.0000',
            'Description': 'Ancient City of Polonnaruwa - UNESCO World Heritage Site. Medieval capital of Sri Lanka with well-preserved ruins of ancient palaces, temples, and monuments.',
            'URL': 'https://whc.unesco.org/en/list/201',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1982'
        },
        {
            'Park_Code': 'SIG',
            'Name': 'Ancient City of Sigiriya',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Province',
            'Latitude': '7.9569',
            'Longitude': '80.7597',
            'Description': 'Ancient City of Sigiriya - UNESCO World Heritage Site. Ancient rock fortress and palace ruins with famous frescoes and water gardens.',
            'URL': 'https://whc.unesco.org/en/list/202',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1982'
        },
        {
            'Park_Code': 'ANU',
            'Name': 'Sacred City of Anuradhapura',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'North Central Province',
            'Latitude': '8.3111',
            'Longitude': '80.4036',
            'Description': 'Sacred City of Anuradhapura - UNESCO World Heritage Site. Ancient capital of Sri Lanka with sacred Buddhist sites including the Sri Maha Bodhi tree.',
            'URL': 'https://whc.unesco.org/en/list/200',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1982'
        },
        {
            'Park_Code': 'GAL',
            'Name': 'Old Town of Galle and its Fortifications',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Southern Province',
            'Latitude': '6.0333',
            'Longitude': '80.2167',
            'Description': 'Old Town of Galle and its Fortifications - UNESCO World Heritage Site. Historic fortified city built by Portuguese and Dutch colonizers.',
            'URL': 'https://whc.unesco.org/en/list/451',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1988'
        },
        {
            'Park_Code': 'KAN',
            'Name': 'Sacred City of Kandy',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Province',
            'Latitude': '7.2944',
            'Longitude': '80.6414',
            'Description': 'Sacred City of Kandy - UNESCO World Heritage Site. Home to the Temple of the Tooth (Sri Dalada Maligawa), which houses the relic of the tooth of Buddha.',
            'URL': 'https://whc.unesco.org/en/list/450',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1988'
        },
        {
            'Park_Code': 'DAM',
            'Name': 'Golden Temple of Dambulla',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Province',
            'Latitude': '7.8567',
            'Longitude': '80.6492',
            'Description': 'Golden Temple of Dambulla - UNESCO World Heritage Site. Largest and best-preserved cave temple complex in Sri Lanka with over 150 Buddha statues.',
            'URL': 'https://whc.unesco.org/en/list/561',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1991'
        },
        # Natural Sites
        {
            'Park_Code': 'SIN',
            'Name': 'Sinharaja Forest Reserve',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Sabaragamuwa Province, Southern Province',
            'Latitude': '6.4167',
            'Longitude': '80.4167',
            'Description': 'Sinharaja Forest Reserve - UNESCO World Heritage Site. Last remaining primary tropical rainforest in Sri Lanka with high biodiversity.',
            'URL': 'https://whc.unesco.org/en/list/405',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '1988'
        },
        {
            'Park_Code': 'CEN',
            'Name': 'Central Highlands of Sri Lanka',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Central Province',
            'Latitude': '7.5000',
            'Longitude': '80.7500',
            'Description': 'Central Highlands of Sri Lanka - UNESCO World Heritage Site. Includes Peak Wilderness, Horton Plains, and Knuckles Conservation Forest with unique montane ecosystems.',
            'URL': 'https://whc.unesco.org/en/list/1203',
            'Country': 'Sri Lanka',
            'UNESCO_Year': '2010'
        }
    ]
    
    return unesco_sites

def save_sri_lanka_unesco_csv(data, filename):
    """Save Sri Lanka UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Sri Lanka UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Sri Lanka UNESCO World Heritage Sites data...")
    
    unesco_data = get_sri_lanka_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Sri_Lanka_UNESCO_Sites.csv')
    save_sri_lanka_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

