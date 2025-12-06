import csv

def get_myanmar_unesco_sites():
    """
    Create Myanmar UNESCO World Heritage Sites CSV data
    Myanmar has 2 UNESCO World Heritage Sites (both cultural)
    """
    
    unesco_sites = [
        {
            'Park_Code': 'PYU',
            'Name': 'Pyu Ancient Cities',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Mandalay, Bago, Magway',
            'Latitude': '22.4667',
            'Longitude': '95.8167',
            'Description': 'Pyu Ancient Cities - UNESCO World Heritage Site. Remains of three brick, walled and moated cities from the Pyu Kingdom.',
            'URL': 'https://whc.unesco.org/en/list/1444',
            'Country': 'Myanmar',
            'UNESCO_Year': '2014'
        },
        {
            'Park_Code': 'BAGAN',
            'Name': 'Bagan',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Mandalay',
            'Latitude': '21.1722',
            'Longitude': '94.8603',
            'Description': 'Bagan - UNESCO World Heritage Site. Ancient city with over 2,000 Buddhist temples, pagodas, and monasteries.',
            'URL': 'https://whc.unesco.org/en/list/1588',
            'Country': 'Myanmar',
            'UNESCO_Year': '2019'
        }
    ]
    
    return unesco_sites

def save_myanmar_unesco_csv(data, filename):
    """Save Myanmar UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Myanmar UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Myanmar UNESCO World Heritage Sites data...")
    
    unesco_data = get_myanmar_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Myanmar_UNESCO_Sites.csv')
    save_myanmar_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

