import csv

def get_nepal_temples():
    """
    Create Nepal Famous Temples CSV data
    """
    
    nepal_temples = [
        {
            'Park_Code': 'PAS',
            'Name': 'Pashupatinath Temple',
            'Designation': 'Hindu Temple',
            'States': 'Kathmandu',
            'Latitude': '27.7106',
            'Longitude': '85.3486',
            'Description': 'Pashupatinath Temple - UNESCO World Heritage Site. One of the most sacred Hindu temples dedicated to Lord Shiva.',
            'URL': 'https://en.wikipedia.org/wiki/Pashupatinath_Temple',
            'Country': 'Nepal',
            'Temple_Type': 'Hindu'
        },
        {
            'Park_Code': 'SWA',
            'Name': 'Swayambhunath Stupa',
            'Designation': 'Buddhist Temple',
            'States': 'Kathmandu',
            'Latitude': '27.7147',
            'Longitude': '85.2903',
            'Description': 'Swayambhunath Stupa - UNESCO World Heritage Site. Ancient Buddhist stupa, also known as Monkey Temple.',
            'URL': 'https://en.wikipedia.org/wiki/Swayambhunath',
            'Country': 'Nepal',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'BOU',
            'Name': 'Boudhanath Stupa',
            'Designation': 'Buddhist Temple',
            'States': 'Kathmandu',
            'Latitude': '27.7214',
            'Longitude': '85.3622',
            'Description': 'Boudhanath Stupa - UNESCO World Heritage Site. One of the largest spherical stupas in Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Boudhanath',
            'Country': 'Nepal',
            'Temple_Type': 'Buddhist'
        },
        {
            'Park_Code': 'CHA',
            'Name': 'Changu Narayan Temple',
            'Designation': 'Hindu Temple',
            'States': 'Bhaktapur',
            'Latitude': '27.7144',
            'Longitude': '85.4281',
            'Description': 'Changu Narayan Temple - UNESCO World Heritage Site. Oldest temple in Nepal dedicated to Lord Vishnu.',
            'URL': 'https://en.wikipedia.org/wiki/Changu_Narayan_Temple',
            'Country': 'Nepal',
            'Temple_Type': 'Hindu'
        },
        {
            'Park_Code': 'MUK',
            'Name': 'Muktinath Temple',
            'Designation': 'Hindu Temple',
            'States': 'Mustang',
            'Latitude': '28.8167',
            'Longitude': '83.8667',
            'Description': 'Muktinath Temple - Sacred temple for both Hindus and Buddhists. Located at 3,800 meters altitude.',
            'URL': 'https://en.wikipedia.org/wiki/Muktinath',
            'Country': 'Nepal',
            'Temple_Type': 'Hindu'
        },
        {
            'Park_Code': 'JAN',
            'Name': 'Janaki Mandir',
            'Designation': 'Hindu Temple',
            'States': 'Janakpur',
            'Latitude': '26.7281',
            'Longitude': '85.9250',
            'Description': 'Janaki Mandir - Temple dedicated to Goddess Sita. Birthplace of Sita according to Ramayana.',
            'URL': 'https://en.wikipedia.org/wiki/Janaki_Mandir',
            'Country': 'Nepal',
            'Temple_Type': 'Hindu'
        }
    ]
    
    return nepal_temples

def save_nepal_temples_csv(data, filename):
    """Save Nepal temples data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Temple_Type']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Nepal temples to {filename}")

if __name__ == '__main__':
    print("Creating Nepal Temples data...")
    
    temples_data = get_nepal_temples()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Nepal_Temples.csv')
    save_nepal_temples_csv(temples_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

