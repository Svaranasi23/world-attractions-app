import csv

def get_sri_lanka_unesco():
    """
    Create Sri Lanka UNESCO World Heritage Sites CSV data
    """
    
    sri_lanka_unesco = [
        {
            'Park_Code': 'SLUN1',
            'Name': 'Ancient City of Polonnaruwa',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'North Central Province',
            'Latitude': '7.9333',
            'Longitude': '81.0000',
            'Description': 'Ancient City of Polonnaruwa - UNESCO World Heritage Site. Medieval capital of Sri Lanka. Located in Polonnaruwa, North Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Polonnaruwa',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN2',
            'Name': 'Ancient City of Sigiriya',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Central Province',
            'Latitude': '7.9569',
            'Longitude': '80.7597',
            'Description': 'Ancient City of Sigiriya - UNESCO World Heritage Site. Ancient rock fortress and palace. Located in Sigiriya, Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Sigiriya',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN3',
            'Name': 'Sacred City of Anuradhapura',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'North Central Province',
            'Latitude': '8.3111',
            'Longitude': '80.4036',
            'Description': 'Sacred City of Anuradhapura - UNESCO World Heritage Site. Ancient capital of Sri Lanka. Located in Anuradhapura, North Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Anuradhapura',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN4',
            'Name': 'Old Town of Galle and its Fortifications',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Southern Province',
            'Latitude': '6.0333',
            'Longitude': '80.2167',
            'Description': 'Old Town of Galle and its Fortifications - UNESCO World Heritage Site. Historic fortified city. Located in Galle, Southern Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Galle_Fort',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN5',
            'Name': 'Sacred City of Kandy',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Central Province',
            'Latitude': '7.2944',
            'Longitude': '80.6414',
            'Description': 'Sacred City of Kandy - UNESCO World Heritage Site. Home to Temple of the Tooth. Located in Kandy, Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Kandy',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN6',
            'Name': 'Sinharaja Forest Reserve',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Sabaragamuwa Province',
            'Latitude': '6.4167',
            'Longitude': '80.4167',
            'Description': 'Sinharaja Forest Reserve - UNESCO World Heritage Site. Last remaining primary tropical rainforest in Sri Lanka. Located in Sabaragamuwa Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Sinharaja_Forest_Reserve',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Natural'
        },
        {
            'Park_Code': 'SLUN7',
            'Name': 'Golden Temple of Dambulla',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Central Province',
            'Latitude': '7.8567',
            'Longitude': '80.6492',
            'Description': 'Golden Temple of Dambulla - UNESCO World Heritage Site. Largest and best-preserved cave temple complex in Sri Lanka. Located in Dambulla, Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Dambulla_cave_temple',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'SLUN8',
            'Name': 'Central Highlands of Sri Lanka',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Central Province',
            'Latitude': '7.5000',
            'Longitude': '80.7500',
            'Description': 'Central Highlands of Sri Lanka - UNESCO World Heritage Site. Includes Peak Wilderness, Horton Plains, and Knuckles Conservation Forest. Located in Central Province, Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Central_Highlands_of_Sri_Lanka',
            'Country': 'Sri Lanka',
            'UNESCO_Category': 'Natural'
        }
    ]
    
    return sri_lanka_unesco

def save_sri_lanka_unesco_csv(data, filename):
    """
    Save Sri Lanka UNESCO data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Category']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            output_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(output_row)
    
    print(f"Saved {len(data)} Sri Lanka UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Sri Lanka UNESCO World Heritage Sites data...")
    
    unesco_data = get_sri_lanka_unesco()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Sri_Lanka_UNESCO_Sites.csv')
    save_sri_lanka_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(unesco_data)} UNESCO sites")


