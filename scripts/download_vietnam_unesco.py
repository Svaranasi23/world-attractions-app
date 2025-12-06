import csv

def get_vietnam_unesco_sites():
    """
    Create Vietnam UNESCO World Heritage Sites CSV data
    Vietnam has 8 UNESCO World Heritage Sites (5 cultural, 2 natural, 1 mixed)
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'HUE',
            'Name': 'Complex of Hué Monuments',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Thua Thien Hue',
            'Latitude': '16.4667',
            'Longitude': '107.5833',
            'Description': 'Complex of Hué Monuments - UNESCO World Heritage Site. Imperial capital of Vietnam with palaces, temples, and tombs.',
            'URL': 'https://whc.unesco.org/en/list/678',
            'Country': 'Vietnam',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'HOI',
            'Name': 'Hoi An Ancient Town',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Quang Nam',
            'Latitude': '15.8800',
            'Longitude': '108.3300',
            'Description': 'Hoi An Ancient Town - UNESCO World Heritage Site. Well-preserved Southeast Asian trading port from 15th-19th centuries.',
            'URL': 'https://whc.unesco.org/en/list/948',
            'Country': 'Vietnam',
            'UNESCO_Year': '1999'
        },
        {
            'Park_Code': 'MYSON',
            'Name': 'My Son Sanctuary',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Quang Nam',
            'Latitude': '15.7667',
            'Longitude': '108.1167',
            'Description': 'My Son Sanctuary - UNESCO World Heritage Site. Ruins of Hindu temples built by the Champa Kingdom.',
            'URL': 'https://whc.unesco.org/en/list/949',
            'Country': 'Vietnam',
            'UNESCO_Year': '1999'
        },
        {
            'Park_Code': 'HANOI',
            'Name': 'Central Sector of the Imperial Citadel of Thang Long - Hanoi',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Hanoi',
            'Latitude': '21.0333',
            'Longitude': '105.8333',
            'Description': 'Imperial Citadel of Thang Long - UNESCO World Heritage Site. Ancient imperial citadel of Vietnam.',
            'URL': 'https://whc.unesco.org/en/list/1328',
            'Country': 'Vietnam',
            'UNESCO_Year': '2010'
        },
        {
            'Park_Code': 'HO',
            'Name': 'Citadel of the Ho Dynasty',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Thanh Hoa',
            'Latitude': '20.0833',
            'Longitude': '105.6000',
            'Description': 'Citadel of the Ho Dynasty - UNESCO World Heritage Site. 14th-century stone citadel built by the Ho Dynasty.',
            'URL': 'https://whc.unesco.org/en/list/1358',
            'Country': 'Vietnam',
            'UNESCO_Year': '2011'
        },
        # Natural Sites
        {
            'Park_Code': 'HALONG',
            'Name': 'Ha Long Bay',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Quang Ninh',
            'Latitude': '20.9101',
            'Longitude': '107.1839',
            'Description': 'Ha Long Bay - UNESCO World Heritage Site. Spectacular seascape of limestone karsts and islands.',
            'URL': 'https://whc.unesco.org/en/list/672',
            'Country': 'Vietnam',
            'UNESCO_Year': '1994'
        },
        {
            'Park_Code': 'PHONG',
            'Name': 'Phong Nha-Ke Bang National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Quang Binh',
            'Latitude': '17.5500',
            'Longitude': '106.2833',
            'Description': 'Phong Nha-Ke Bang National Park - UNESCO World Heritage Site. Karst landscape with extensive cave systems.',
            'URL': 'https://whc.unesco.org/en/list/951',
            'Country': 'Vietnam',
            'UNESCO_Year': '2003'
        },
        # Mixed Site
        {
            'Park_Code': 'TRANG',
            'Name': 'Trang An Landscape Complex',
            'Designation': 'UNESCO World Heritage Site (Mixed)',
            'States': 'Ninh Binh',
            'Latitude': '20.2667',
            'Longitude': '105.9167',
            'Description': 'Trang An Landscape Complex - UNESCO World Heritage Site. Karst landscape with caves, temples, and archaeological sites.',
            'URL': 'https://whc.unesco.org/en/list/1438',
            'Country': 'Vietnam',
            'UNESCO_Year': '2014'
        }
    ]
    
    return unesco_sites

def save_vietnam_unesco_csv(data, filename):
    """Save Vietnam UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Vietnam UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Vietnam UNESCO World Heritage Sites data...")
    
    unesco_data = get_vietnam_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Vietnam_UNESCO_Sites.csv')
    save_vietnam_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

