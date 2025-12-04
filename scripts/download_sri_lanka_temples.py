import csv

def get_sri_lanka_temples():
    """
    Create Sri Lanka Famous Temples CSV data
    """
    
    sri_lanka_temples = [
        {
            'Park_Code': 'TEA',
            'Name': 'Temple of the Tooth',
            'Designation': 'Buddhist Temple',
            'States': 'Central Province',
            'Latitude': '7.2944',
            'Longitude': '80.6414',
            'Description': 'Temple of the Tooth (Sri Dalada Maligawa) - UNESCO World Heritage Site. Houses the relic of the tooth of Buddha.',
            'URL': 'https://en.wikipedia.org/wiki/Temple_of_the_Tooth',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'DAM',
            'Name': 'Dambulla Cave Temple',
            'Designation': 'Buddhist Temple',
            'States': 'Central Province',
            'Latitude': '7.8567',
            'Longitude': '80.6492',
            'Description': 'Dambulla Cave Temple - UNESCO World Heritage Site. Largest and best-preserved cave temple complex in Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Dambulla_cave_temple',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'KEL',
            'Name': 'Kandy Kataragama Devalaya',
            'Designation': 'Hindu Temple',
            'States': 'Central Province',
            'Latitude': '7.2944',
            'Longitude': '80.6414',
            'Description': 'Kandy Kataragama Devalaya - Hindu temple dedicated to God Kataragama in Kandy.',
            'URL': 'https://en.wikipedia.org/wiki/Kataragama_temple',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Hindu'
        },
        {
            'Park_Code': 'KAT',
            'Name': 'Kataragama Temple',
            'Designation': 'Hindu Temple',
            'States': 'Uva Province',
            'Latitude': '6.4167',
            'Longitude': '81.3333',
            'Description': 'Kataragama Temple - Sacred pilgrimage site for Hindus, Buddhists, and Muslims.',
            'URL': 'https://en.wikipedia.org/wiki/Kataragama_temple',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Hindu'
        },
        {
            'Park_Code': 'GAL',
            'Name': 'Gangaramaya Temple',
            'Designation': 'Buddhist Temple',
            'States': 'Western Province',
            'Latitude': '6.9167',
            'Longitude': '79.8500',
            'Description': 'Gangaramaya Temple - One of the most important temples in Colombo.',
            'URL': 'https://en.wikipedia.org/wiki/Gangaramaya_Temple',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'MIR',
            'Name': 'Mihintale',
            'Designation': 'Buddhist Temple',
            'States': 'North Central Province',
            'Latitude': '8.3500',
            'Longitude': '80.5167',
            'Description': 'Mihintale - Ancient Buddhist monastery. Birthplace of Buddhism in Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Mihintale',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'POL',
            'Name': 'Polonnaruwa Vatadage',
            'Designation': 'Buddhist Temple',
            'States': 'North Central Province',
            'Latitude': '7.9333',
            'Longitude': '81.0000',
            'Description': 'Polonnaruwa Vatadage - UNESCO World Heritage Site. Ancient circular relic house.',
            'URL': 'https://en.wikipedia.org/wiki/Polonnaruwa',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'ANU',
            'Name': 'Anuradhapura Sacred City',
            'Designation': 'Buddhist Temple',
            'States': 'North Central Province',
            'Latitude': '8.3111',
            'Longitude': '80.4031',
            'Description': 'Anuradhapura - UNESCO World Heritage Site. Ancient capital with many Buddhist temples and stupas.',
            'URL': 'https://en.wikipedia.org/wiki/Anuradhapura',
            'Country': 'Sri Lanka',
            'Temple_Type': 'Buddhist'
        }
    ]
    
    return sri_lanka_temples

def save_sri_lanka_temples_csv(data, filename):
    """Save Sri Lanka temples data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Temple_Type']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Sri Lanka temples to {filename}")

if __name__ == '__main__':
    print("Creating Sri Lanka Temples data...")
    
    temples_data = get_sri_lanka_temples()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Sri_Lanka_Temples.csv')
    save_sri_lanka_temples_csv(temples_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

