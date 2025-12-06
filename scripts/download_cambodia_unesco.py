import csv

def get_cambodia_unesco_sites():
    """
    Create Cambodia UNESCO World Heritage Sites CSV data
    Cambodia has 3 UNESCO World Heritage Sites (all cultural)
    """
    
    unesco_sites = [
        {
            'Park_Code': 'ANGKOR',
            'Name': 'Angkor',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Siem Reap',
            'Latitude': '13.4125',
            'Longitude': '103.8670',
            'Description': 'Angkor - UNESCO World Heritage Site. Vast temple complex including Angkor Wat, one of the largest religious monuments in the world.',
            'URL': 'https://whc.unesco.org/en/list/668',
            'Country': 'Cambodia',
            'UNESCO_Year': '1992'
        },
        {
            'Park_Code': 'PREAH',
            'Name': 'Temple of Preah Vihear',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Preah Vihear',
            'Latitude': '14.3900',
            'Longitude': '104.6800',
            'Description': 'Temple of Preah Vihear - UNESCO World Heritage Site. 11th-century Hindu temple dedicated to Shiva, located on a cliff.',
            'URL': 'https://whc.unesco.org/en/list/1224',
            'Country': 'Cambodia',
            'UNESCO_Year': '2008'
        },
        {
            'Park_Code': 'SAMBOR',
            'Name': 'Temple Zone of Sambor Prei Kuk',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Kampong Thom',
            'Latitude': '12.8667',
            'Longitude': '105.0333',
            'Description': 'Temple Zone of Sambor Prei Kuk - UNESCO World Heritage Site. Archaeological site with pre-Angkorian temples from 6th-7th centuries.',
            'URL': 'https://whc.unesco.org/en/list/1532',
            'Country': 'Cambodia',
            'UNESCO_Year': '2017'
        }
    ]
    
    return unesco_sites

def save_cambodia_unesco_csv(data, filename):
    """Save Cambodia UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Cambodia UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Cambodia UNESCO World Heritage Sites data...")
    
    unesco_data = get_cambodia_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Cambodia_UNESCO_Sites.csv')
    save_cambodia_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

