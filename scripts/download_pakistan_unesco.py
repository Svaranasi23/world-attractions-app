import csv

def get_pakistan_unesco_sites():
    """
    Create Pakistan UNESCO World Heritage Sites CSV data
    Pakistan has 6 UNESCO World Heritage Sites (all cultural)
    """
    
    unesco_sites = [
        {
            'Park_Code': 'TAXILA',
            'Name': 'Taxila',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Punjab',
            'Latitude': '33.7500',
            'Longitude': '72.8333',
            'Description': 'Taxila - UNESCO World Heritage Site. Ancient archaeological site with ruins from multiple civilizations including Gandhara.',
            'URL': 'https://whc.unesco.org/en/list/139',
            'Country': 'Pakistan',
            'UNESCO_Year': '1980'
        },
        {
            'Park_Code': 'MOENJODARO',
            'Name': 'Archaeological Ruins at Moenjodaro',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Sindh',
            'Latitude': '27.3292',
            'Longitude': '68.1389',
            'Description': 'Archaeological Ruins at Moenjodaro - UNESCO World Heritage Site. Best preserved urban ruins of the Indus Valley Civilization.',
            'URL': 'https://whc.unesco.org/en/list/138',
            'Country': 'Pakistan',
            'UNESCO_Year': '1980'
        },
        {
            'Park_Code': 'LAHORE',
            'Name': 'Fort and Shalimar Gardens in Lahore',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Punjab',
            'Latitude': '31.5889',
            'Longitude': '74.3153',
            'Description': 'Fort and Shalimar Gardens in Lahore - UNESCO World Heritage Site. Mughal fort and gardens from the 16th-17th centuries.',
            'URL': 'https://whc.unesco.org/en/list/171',
            'Country': 'Pakistan',
            'UNESCO_Year': '1981'
        },
        {
            'Park_Code': 'MAKLI',
            'Name': 'Historical Monuments at Makli, Thatta',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Sindh',
            'Latitude': '24.7500',
            'Longitude': '67.9000',
            'Description': 'Historical Monuments at Makli, Thatta - UNESCO World Heritage Site. Vast necropolis with tombs and monuments from 14th-18th centuries.',
            'URL': 'https://whc.unesco.org/en/list/143',
            'Country': 'Pakistan',
            'UNESCO_Year': '1981'
        },
        {
            'Park_Code': 'ROHTAS',
            'Name': 'Rohtas Fort',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Punjab',
            'Latitude': '32.9667',
            'Longitude': '73.5833',
            'Description': 'Rohtas Fort - UNESCO World Heritage Site. 16th-century fortress built by Sher Shah Suri, never conquered.',
            'URL': 'https://whc.unesco.org/en/list/586',
            'Country': 'Pakistan',
            'UNESCO_Year': '1997'
        },
        {
            'Park_Code': 'TAKHT',
            'Name': 'Buddhist Ruins of Takht-i-Bahi and Neighbouring City Remains at Sahr-i-Bahlol',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Khyber Pakhtunkhwa',
            'Latitude': '34.2833',
            'Longitude': '71.9500',
            'Description': 'Buddhist Ruins of Takht-i-Bahi - UNESCO World Heritage Site. Well-preserved Buddhist monastery complex from 1st century CE.',
            'URL': 'https://whc.unesco.org/en/list/140',
            'Country': 'Pakistan',
            'UNESCO_Year': '1980'
        }
    ]
    
    return unesco_sites

def save_pakistan_unesco_csv(data, filename):
    """Save Pakistan UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Pakistan UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Pakistan UNESCO World Heritage Sites data...")
    
    unesco_data = get_pakistan_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Pakistan_UNESCO_Sites.csv')
    save_pakistan_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

