import csv

def get_jyotirlinga_temples():
    """
    Create India 12 Jyotirlinga Temples CSV data
    The 12 Jyotirlinga temples are the most sacred Shiva temples in India
    """
    
    jyotirlinga_temples = [
        {
            'Park_Code': 'SOM',
            'Name': 'Somnath Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Gujarat',
            'Latitude': '20.8883',
            'Longitude': '70.4011',
            'Description': 'Somnath Temple - First of the 12 Jyotirlinga temples. Located in Prabhas Patan, Gujarat. One of the oldest and most revered Shiva temples.',
            'URL': 'https://en.wikipedia.org/wiki/Somnath_temple',
            'Country': 'India',
            'Jyotirlinga_Number': '1'
        },
        {
            'Park_Code': 'MAL',
            'Name': 'Mallikarjuna Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Andhra Pradesh',
            'Latitude': '16.2400',
            'Longitude': '78.8083',
            'Description': 'Mallikarjuna Temple (Srisailam) - Second Jyotirlinga. Located on the banks of Krishna River in Andhra Pradesh. Also known as Srisailam.',
            'URL': 'https://en.wikipedia.org/wiki/Srisailam',
            'Country': 'India',
            'Jyotirlinga_Number': '2'
        },
        {
            'Park_Code': 'MAH',
            'Name': 'Mahakaleshwar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Madhya Pradesh',
            'Latitude': '23.1833',
            'Longitude': '75.7667',
            'Description': 'Mahakaleshwar Temple - Third Jyotirlinga. Located in Ujjain, Madhya Pradesh. One of the most powerful Jyotirlingas, facing south.',
            'URL': 'https://en.wikipedia.org/wiki/Mahakaleshwar_Jyotirlinga',
            'Country': 'India',
            'Jyotirlinga_Number': '3'
        },
        {
            'Park_Code': 'OMK',
            'Name': 'Omkareshwar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Madhya Pradesh',
            'Latitude': '22.2500',
            'Longitude': '76.1500',
            'Description': 'Omkareshwar Temple - Fourth Jyotirlinga. Located on Mandhata island in the Narmada River, Madhya Pradesh. The island is shaped like the sacred "Om" symbol.',
            'URL': 'https://en.wikipedia.org/wiki/Omkareshwar',
            'Country': 'India',
            'Jyotirlinga_Number': '4'
        },
        {
            'Park_Code': 'KED',
            'Name': 'Kedarnath Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.7353',
            'Longitude': '79.0669',
            'Description': 'Kedarnath Temple - Fifth Jyotirlinga. Located in the Garhwal Himalayas, Uttarakhand. Highest of the 12 Jyotirlingas at 3,583 meters.',
            'URL': 'https://en.wikipedia.org/wiki/Kedarnath_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '5'
        },
        {
            'Park_Code': 'BHI',
            'Name': 'Bhimashankar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Maharashtra',
            'Latitude': '19.0717',
            'Longitude': '73.5350',
            'Description': 'Bhimashankar Temple - Sixth Jyotirlinga. Located in the Sahyadri hills of Maharashtra. Surrounded by dense forests and wildlife.',
            'URL': 'https://en.wikipedia.org/wiki/Bhimashankar_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '6'
        },
        {
            'Park_Code': 'KAS',
            'Name': 'Kashi Vishwanath Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Uttar Pradesh',
            'Latitude': '25.3111',
            'Longitude': '83.0100',
            'Description': 'Kashi Vishwanath Temple - Seventh Jyotirlinga. Located in Varanasi (Kashi), Uttar Pradesh. One of the holiest temples in Hinduism.',
            'URL': 'https://en.wikipedia.org/wiki/Kashi_Vishwanath_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '7'
        },
        {
            'Park_Code': 'TRI',
            'Name': 'Trimbakeshwar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Maharashtra',
            'Latitude': '19.9333',
            'Longitude': '73.5500',
            'Description': 'Trimbakeshwar Temple - Eighth Jyotirlinga. Located near Nashik, Maharashtra. Source of the Godavari River.',
            'URL': 'https://en.wikipedia.org/wiki/Trimbakeshwar_Shiva_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '8'
        },
        {
            'Park_Code': 'VAI',
            'Name': 'Vaidyanath Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Jharkhand',
            'Latitude': '24.0167',
            'Longitude': '86.8500',
            'Description': 'Vaidyanath Temple (Baidyanath Dham) - Ninth Jyotirlinga. Located in Deoghar, Jharkhand. Also known as Baidyanath Dham.',
            'URL': 'https://en.wikipedia.org/wiki/Baidyanath_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '9'
        },
        {
            'Park_Code': 'NAG',
            'Name': 'Nageshwar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Gujarat',
            'Latitude': '22.1667',
            'Longitude': '69.1167',
            'Description': 'Nageshwar Temple - Tenth Jyotirlinga. Located near Dwarka, Gujarat. Also known as Aundha Nagnath or Jageshwar.',
            'URL': 'https://en.wikipedia.org/wiki/Nageshvara_Jyotirlinga',
            'Country': 'India',
            'Jyotirlinga_Number': '10'
        },
        {
            'Park_Code': 'RAM',
            'Name': 'Ramanathaswamy Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Tamil Nadu',
            'Latitude': '9.2881',
            'Longitude': '79.3172',
            'Description': 'Ramanathaswamy Temple - Eleventh Jyotirlinga. Located in Rameswaram, Tamil Nadu. One of the Char Dham pilgrimage sites.',
            'URL': 'https://en.wikipedia.org/wiki/Ramanathaswamy_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '11'
        },
        {
            'Park_Code': 'GRI',
            'Name': 'Grishneshwar Temple',
            'Designation': 'Jyotirlinga Temple',
            'States': 'Maharashtra',
            'Latitude': '20.0167',
            'Longitude': '75.1833',
            'Description': 'Grishneshwar Temple - Twelfth Jyotirlinga. Located near Ellora, Maharashtra. Also known as Ghushmeshwar or Grushneshwar.',
            'URL': 'https://en.wikipedia.org/wiki/Grishneshwar_Temple',
            'Country': 'India',
            'Jyotirlinga_Number': '12'
        }
    ]
    
    return jyotirlinga_temples

def save_jyotirlinga_csv(data, filename):
    """
    Save Jyotirlinga temples data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Jyotirlinga_Number']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Jyotirlinga temples to {filename}")

if __name__ == '__main__':
    print("Creating India 12 Jyotirlinga Temples data...")
    
    temples_data = get_jyotirlinga_temples()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Jyotirlinga_Temples.csv')
    save_jyotirlinga_csv(temples_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

