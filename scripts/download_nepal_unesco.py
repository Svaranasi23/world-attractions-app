import csv

def get_nepal_unesco():
    """
    Create Nepal UNESCO World Heritage Sites CSV data
    """
    
    nepal_unesco = [
        {
            'Park_Code': 'NPUN1',
            'Name': 'Kathmandu Valley',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Kathmandu Valley',
            'Latitude': '27.7172',
            'Longitude': '85.3240',
            'Description': 'Kathmandu Valley - UNESCO World Heritage Site. Includes seven groups of monuments and buildings. Located in Kathmandu Valley, Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Kathmandu_Valley',
            'Country': 'Nepal',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'NPUN2',
            'Name': 'Lumbini',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Lumbini',
            'Latitude': '27.4833',
            'Longitude': '83.2833',
            'Description': 'Lumbini - UNESCO World Heritage Site. Birthplace of Lord Buddha. Located in Lumbini, Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Lumbini',
            'Country': 'Nepal',
            'UNESCO_Category': 'Cultural'
        },
        {
            'Park_Code': 'NPUN3',
            'Name': 'Chitwan National Park',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Chitwan',
            'Latitude': '27.5000',
            'Longitude': '84.3333',
            'Description': 'Chitwan National Park - UNESCO World Heritage Site. First national park in Nepal. Located in Chitwan district, Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Chitwan_National_Park',
            'Country': 'Nepal',
            'UNESCO_Category': 'Natural'
        },
        {
            'Park_Code': 'NPUN4',
            'Name': 'Sagarmatha National Park',
            'Designation': 'UNESCO World Heritage Site',
            'States': 'Solukhumbu',
            'Latitude': '27.9667',
            'Longitude': '86.9167',
            'Description': 'Sagarmatha National Park - UNESCO World Heritage Site. Home to Mount Everest. Located in Solukhumbu district, Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Sagarmatha_National_Park',
            'Country': 'Nepal',
            'UNESCO_Category': 'Natural'
        }
    ]
    
    return nepal_unesco

def save_nepal_unesco_csv(data, filename):
    """
    Save Nepal UNESCO data to CSV file
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
    
    print(f"Saved {len(data)} Nepal UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Nepal UNESCO World Heritage Sites data...")
    
    unesco_data = get_nepal_unesco()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Nepal_UNESCO_Sites.csv')
    save_nepal_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(unesco_data)} UNESCO sites")


