import csv

def get_india_mutts():
    """
    Create India Major Mutts (Monasteries) CSV data
    Mutts are important monastic institutions in Hinduism, especially in the Advaita Vedanta tradition
    """
    
    mutts = [
        {
            'Park_Code': 'SRG',
            'Name': 'Sringeri Sharada Peetham',
            'Designation': 'Mutt',
            'States': 'Karnataka',
            'Latitude': '13.4167',
            'Longitude': '75.2500',
            'Description': 'Sringeri Sharada Peetham - First of the four Advaita Vedanta mutts established by Adi Shankaracharya. Located in Sringeri, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Sringeri_Sharada_Peetham',
            'Country': 'India',
            'Mutt_Category': 'Advaita Peetham'
        },
        {
            'Park_Code': 'DWP',
            'Name': 'Dwaraka Sharada Peetham',
            'Designation': 'Mutt',
            'States': 'Gujarat',
            'Latitude': '22.2400',
            'Longitude': '68.9700',
            'Description': 'Dwaraka Sharada Peetham - Second of the four Advaita Vedanta mutts established by Adi Shankaracharya. Located in Dwarka, Gujarat.',
            'URL': 'https://en.wikipedia.org/wiki/Dwarka_Peetham',
            'Country': 'India',
            'Mutt_Category': 'Advaita Peetham'
        },
        {
            'Park_Code': 'JYM',
            'Name': 'Jyotir Math',
            'Designation': 'Mutt',
            'States': 'Uttarakhand',
            'Latitude': '30.5500',
            'Longitude': '79.5667',
            'Description': 'Jyotir Math (Joshimath) - Third of the four Advaita Vedanta mutts established by Adi Shankaracharya. Located in Joshimath, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Jyotir_Math',
            'Country': 'India',
            'Mutt_Category': 'Advaita Peetham'
        },
        {
            'Park_Code': 'GVM',
            'Name': 'Govardhana Math',
            'Designation': 'Mutt',
            'States': 'Odisha',
            'Latitude': '19.8056',
            'Longitude': '85.8181',
            'Description': 'Govardhana Math - Fourth of the four Advaita Vedanta mutts established by Adi Shankaracharya. Located in Puri, Odisha.',
            'URL': 'https://en.wikipedia.org/wiki/Govardhana_Math',
            'Country': 'India',
            'Mutt_Category': 'Advaita Peetham'
        },
        {
            'Park_Code': 'KCP',
            'Name': 'Kanchi Kamakoti Peetham',
            'Designation': 'Mutt',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Kanchi Kamakoti Peetham - Important Advaita Vedanta mutt. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Kanchi_Kamakoti_Peetham',
            'Country': 'India',
            'Mutt_Category': 'Advaita Peetham'
        },
        {
            'Park_Code': 'UAM',
            'Name': 'Udupi Ashta Mathas',
            'Designation': 'Mutt',
            'States': 'Karnataka',
            'Latitude': '13.3389',
            'Longitude': '74.7451',
            'Description': 'Udupi Ashta Mathas - Eight mutts established by Madhvacharya around the Udupi Krishna Temple. Located in Udupi, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Udupi',
            'Country': 'India',
            'Mutt_Category': 'Dvaita Peetham'
        },
        {
            'Park_Code': 'MYS',
            'Name': 'Mysore Parakala Mutt',
            'Designation': 'Mutt',
            'States': 'Karnataka',
            'Latitude': '12.3056',
            'Longitude': '76.6528',
            'Description': 'Mysore Parakala Mutt - Important Sri Vaishnava mutt. Located in Mysore, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Parakala_Mutt',
            'Country': 'India',
            'Mutt_Category': 'Sri Vaishnava'
        },
        {
            'Park_Code': 'MEL',
            'Name': 'Melkote Cheluvanarayana Swamy Temple Mutt',
            'Designation': 'Mutt',
            'States': 'Karnataka',
            'Latitude': '12.6667',
            'Longitude': '76.6500',
            'Description': 'Melkote Cheluvanarayana Swamy Temple Mutt - Important Sri Vaishnava mutt. Located in Melkote, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Melkote',
            'Country': 'India',
            'Mutt_Category': 'Sri Vaishnava'
        },
        {
            'Park_Code': 'AHO',
            'Name': 'Ahobila Math',
            'Designation': 'Mutt',
            'States': 'Andhra Pradesh',
            'Latitude': '14.5000',
            'Longitude': '79.7000',
            'Description': 'Ahobila Math - Important Sri Vaishnava mutt. Located in Ahobilam, Andhra Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Ahobila_Math',
            'Country': 'India',
            'Mutt_Category': 'Sri Vaishnava'
        },
        {
            'Park_Code': 'SRM',
            'Name': 'Srirangam Ranganatha Swamy Temple Mutt',
            'Designation': 'Mutt',
            'States': 'Tamil Nadu',
            'Latitude': '10.8667',
            'Longitude': '78.8167',
            'Description': 'Srirangam Ranganatha Swamy Temple Mutt - Important Sri Vaishnava mutt. Located in Srirangam, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Srirangam_Ranganathaswamy_temple',
            'Country': 'India',
            'Mutt_Category': 'Sri Vaishnava'
        }
    ]
    
    return mutts

def save_india_mutts_csv(data, filename):
    """
    Save India Mutts data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Mutt_Category']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            output_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(output_row)
    
    print(f"Saved {len(data)} mutts to {filename}")

if __name__ == '__main__':
    print("Creating India Major Mutts data...")
    
    mutts_data = get_india_mutts()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Mutts.csv')
    save_india_mutts_csv(mutts_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(mutts_data)} major mutts")

