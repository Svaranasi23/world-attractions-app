import csv

def get_bangladesh_unesco_sites():
    """
    Create Bangladesh UNESCO World Heritage Sites CSV data
    Bangladesh has 3 UNESCO World Heritage Sites (all cultural)
    """
    
    unesco_sites = [
        {
            'Park_Code': 'PAHARPUR',
            'Name': 'Ruins of the Buddhist Vihara at Paharpur',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Naogaon',
            'Latitude': '25.0333',
            'Longitude': '88.9833',
            'Description': 'Ruins of the Buddhist Vihara at Paharpur - UNESCO World Heritage Site. Largest Buddhist monastery south of the Himalayas.',
            'URL': 'https://whc.unesco.org/en/list/322',
            'Country': 'Bangladesh',
            'UNESCO_Year': '1985'
        },
        {
            'Park_Code': 'BAUR',
            'Name': 'Historic Mosque City of Bagerhat',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Bagerhat',
            'Latitude': '22.6667',
            'Longitude': '89.7667',
            'Description': 'Historic Mosque City of Bagerhat - UNESCO World Heritage Site. Medieval Islamic city with numerous mosques and monuments.',
            'URL': 'https://whc.unesco.org/en/list/321',
            'Country': 'Bangladesh',
            'UNESCO_Year': '1985'
        },
        {
            'Park_Code': 'SUNDARBANS',
            'Name': 'The Sundarbans',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Khulna, Satkhira, Bagerhat',
            'Latitude': '21.9500',
            'Longitude': '89.1833',
            'Description': 'The Sundarbans - UNESCO World Heritage Site. Largest mangrove forest in the world, home to Bengal tigers.',
            'URL': 'https://whc.unesco.org/en/list/798',
            'Country': 'Bangladesh',
            'UNESCO_Year': '1997'
        }
    ]
    
    return unesco_sites

def save_bangladesh_unesco_csv(data, filename):
    """Save Bangladesh UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Bangladesh UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Bangladesh UNESCO World Heritage Sites data...")
    
    unesco_data = get_bangladesh_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Bangladesh_UNESCO_Sites.csv')
    save_bangladesh_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

