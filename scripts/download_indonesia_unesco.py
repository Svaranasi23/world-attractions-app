import csv

def get_indonesia_unesco_sites():
    """
    Create Indonesia UNESCO World Heritage Sites CSV data
    Indonesia has 9 UNESCO World Heritage Sites (5 cultural, 4 natural)
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'BOROBUDUR',
            'Name': 'Borobudur Temple Compounds',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Java',
            'Latitude': '-7.6081',
            'Longitude': '110.2044',
            'Description': 'Borobudur Temple Compounds - UNESCO World Heritage Site. 9th-century Mahayana Buddhist temple, one of the largest Buddhist temples in the world.',
            'URL': 'https://whc.unesco.org/en/list/592',
            'Country': 'Indonesia',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'PRAMBANAN',
            'Name': 'Prambanan Temple Compounds',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Java, Yogyakarta',
            'Latitude': '-7.7520',
            'Longitude': '110.4915',
            'Description': 'Prambanan Temple Compounds - UNESCO World Heritage Site. 9th-century Hindu temple complex dedicated to Trimurti.',
            'URL': 'https://whc.unesco.org/en/list/642',
            'Country': 'Indonesia',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'SANGIRAN',
            'Name': 'Sangiran Early Man Site',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Central Java',
            'Latitude': '-7.4500',
            'Longitude': '110.8333',
            'Description': 'Sangiran Early Man Site - UNESCO World Heritage Site. Archaeological site with important hominid fossils.',
            'URL': 'https://whc.unesco.org/en/list/593',
            'Country': 'Indonesia',
            'UNESCO_Year': '1996'
        },
        {
            'Park_Code': 'BALI',
            'Name': 'Cultural Landscape of Bali Province',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Bali',
            'Latitude': '-8.3405',
            'Longitude': '115.0920',
            'Description': 'Cultural Landscape of Bali Province - UNESCO World Heritage Site. Subak system of water management and rice terraces.',
            'URL': 'https://whc.unesco.org/en/list/1194',
            'Country': 'Indonesia',
            'UNESCO_Year': '2012'
        },
        {
            'Park_Code': 'OMBILLIN',
            'Name': 'Ombilin Coal Mining Heritage of Sawahlunto',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'West Sumatra',
            'Latitude': '-0.6833',
            'Longitude': '100.7833',
            'Description': 'Ombilin Coal Mining Heritage - UNESCO World Heritage Site. Industrial heritage of coal mining in Indonesia.',
            'URL': 'https://whc.unesco.org/en/list/1610',
            'Country': 'Indonesia',
            'UNESCO_Year': '2019'
        },
        # Natural Sites
        {
            'Park_Code': 'UJUNG',
            'Name': 'Ujung Kulon National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Banten, Lampung',
            'Latitude': '-6.7833',
            'Longitude': '105.3667',
            'Description': 'Ujung Kulon National Park - UNESCO World Heritage Site. Last remaining natural habitat of Javan rhinoceros.',
            'URL': 'https://whc.unesco.org/en/list/608',
            'Country': 'Indonesia',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'KOMODO',
            'Name': 'Komodo National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'East Nusa Tenggara',
            'Latitude': '-8.5500',
            'Longitude': '119.4500',
            'Description': 'Komodo National Park - UNESCO World Heritage Site. Home to the Komodo dragon, the world\'s largest lizard.',
            'URL': 'https://whc.unesco.org/en/list/609',
            'Country': 'Indonesia',
            'UNESCO_Year': '1991'
        },
        {
            'Park_Code': 'LORENTZ',
            'Name': 'Lorentz National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Papua',
            'Latitude': '-4.7500',
            'Longitude': '137.8333',
            'Description': 'Lorentz National Park - UNESCO World Heritage Site. Largest protected area in Southeast Asia with diverse ecosystems.',
            'URL': 'https://whc.unesco.org/en/list/955',
            'Country': 'Indonesia',
            'UNESCO_Year': '1999'
        },
        {
            'Park_Code': 'SUMATRA',
            'Name': 'Tropical Rainforest Heritage of Sumatra',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Aceh, North Sumatra, West Sumatra, Jambi, Bengkulu, South Sumatra',
            'Latitude': '-0.5000',
            'Longitude': '101.0000',
            'Description': 'Tropical Rainforest Heritage of Sumatra - UNESCO World Heritage Site. Three national parks with diverse flora and fauna.',
            'URL': 'https://whc.unesco.org/en/list/1167',
            'Country': 'Indonesia',
            'UNESCO_Year': '2004'
        }
    ]
    
    return unesco_sites

def save_indonesia_unesco_csv(data, filename):
    """Save Indonesia UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Indonesia UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Indonesia UNESCO World Heritage Sites data...")
    
    unesco_data = get_indonesia_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Indonesia_UNESCO_Sites.csv')
    save_indonesia_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

