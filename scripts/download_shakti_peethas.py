import csv

def get_shakti_peethas():
    """
    Create India 18 Ashtadasha Maha Shakti Peethas CSV data
    Based on Wikipedia: https://en.wikipedia.org/wiki/Shakta_pithas
    The 18 Maha Shakti Peethas are the most sacred Goddess temples in India
    where body parts of Goddess Sati fell
    """
    
    shakti_peethas = [
        {
            'Park_Code': 'KAM',
            'Name': 'Kamakhya Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Assam',
            'Latitude': '26.1667',
            'Longitude': '91.7167',
            'Description': 'Kamakhya Temple (Kamarupa) - Yoni (Vulva) of Sati fell here. One of the most powerful Shakti Peethas, located in Guwahati, Assam. Part of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Kamakhya_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '1',
            'Body_Part': 'Yoni (Vulva)'
        },
        {
            'Park_Code': 'KAK',
            'Name': 'Kamakshi Amman Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Kamakshi Amman Temple - Navel of Sati fell here. Located in Kanchipuram, Tamil Nadu. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Kamakshi_Amman_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '2',
            'Body_Part': 'Navel'
        },
        {
            'Park_Code': 'SHR',
            'Name': 'Shrunkala Devi Temple',
            'Designation': 'Shakti Peetha',
            'States': 'West Bengal',
            'Latitude': '22.4333',
            'Longitude': '87.3167',
            'Description': 'Shrunkala Devi Temple (Pradyumnam) - Stomach of Sati fell here. Located in Pradyumnam, West Bengal. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Shakta_pithas',
            'Country': 'India',
            'Shakti_Peetha_Number': '3',
            'Body_Part': 'Stomach'
        },
        {
            'Park_Code': 'CHM',
            'Name': 'Chamundeshwari Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Karnataka',
            'Latitude': '12.3056',
            'Longitude': '76.6528',
            'Description': 'Chamundeshwari Temple - Hair of Sati fell here. Located in Mysore, Karnataka. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Chamundeshwari_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '4',
            'Body_Part': 'Hair'
        },
        {
            'Park_Code': 'JOG',
            'Name': 'Jogulamba Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Telangana',
            'Latitude': '15.8667',
            'Longitude': '78.1333',
            'Description': 'Jogulamba Temple - Upper Teeth of Sati fell here. Located in Alampur, Telangana. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Jogulamba_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '5',
            'Body_Part': 'Upper Teeth'
        },
        {
            'Park_Code': 'BHR',
            'Name': 'Bhramaramba Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Andhra Pradesh',
            'Latitude': '16.0833',
            'Longitude': '78.8667',
            'Description': 'Bhramaramba Temple - Neck of Sati fell here. Located in Srisailam, Andhra Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Srisailam',
            'Country': 'India',
            'Shakti_Peetha_Number': '6',
            'Body_Part': 'Neck'
        },
        {
            'Park_Code': 'MAH',
            'Name': 'Mahalakshmi Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Maharashtra',
            'Latitude': '16.7000',
            'Longitude': '74.2333',
            'Description': 'Mahalakshmi Temple - Left Eye of Sati fell here. Located in Kolhapur, Maharashtra. One of the 18 Ashtadasha Maha Shakti Peethas and one of the six abodes of Lakshmi.',
            'URL': 'https://en.wikipedia.org/wiki/Mahalaxmi_Temple,_Kolhapur',
            'Country': 'India',
            'Shakti_Peetha_Number': '7',
            'Body_Part': 'Left Eye'
        },
        {
            'Park_Code': 'EKA',
            'Name': 'Ekaveerika Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Maharashtra',
            'Latitude': '19.5500',
            'Longitude': '77.7333',
            'Description': 'Ekaveerika Temple (Renuka Devi) - Right Hand of Sati fell here. Located in Mahur, Maharashtra. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Renuka',
            'Country': 'India',
            'Shakti_Peetha_Number': '8',
            'Body_Part': 'Right Hand'
        },
        {
            'Park_Code': 'MHK',
            'Name': 'Mahakali Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Madhya Pradesh',
            'Latitude': '23.1833',
            'Longitude': '75.7667',
            'Description': 'Mahakali Temple - Upper Lip of Sati fell here. Located in Ujjain, Madhya Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Mahakaleshwar_Jyotirlinga',
            'Country': 'India',
            'Shakti_Peetha_Number': '9',
            'Body_Part': 'Upper Lip'
        },
        {
            'Park_Code': 'PUR',
            'Name': 'Puruhutika Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Andhra Pradesh',
            'Latitude': '17.1167',
            'Longitude': '82.2667',
            'Description': 'Puruhutika Temple - Left Hand of Sati fell here. Located in Pithapuram, Andhra Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Pithapuram',
            'Country': 'India',
            'Shakti_Peetha_Number': '10',
            'Body_Part': 'Left Hand'
        },
        {
            'Park_Code': 'GIR',
            'Name': 'Girija Devi Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Odisha',
            'Latitude': '20.8500',
            'Longitude': '86.3333',
            'Description': 'Girija Devi Temple (Biraja Temple) - Navel of Sati fell here. Located in Jajpur, Odisha. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Biraja_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '11',
            'Body_Part': 'Navel'
        },
        {
            'Park_Code': 'MAN',
            'Name': 'Manikyamba Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Andhra Pradesh',
            'Latitude': '16.7833',
            'Longitude': '82.0167',
            'Description': 'Manikyamba Temple - Left Cheek of Sati fell here. Located in Draksharamam, Andhra Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Draksharama',
            'Country': 'India',
            'Shakti_Peetha_Number': '12',
            'Body_Part': 'Left Cheek'
        },
        {
            'Park_Code': 'MAD',
            'Name': 'Madhaveswari Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Uttar Pradesh',
            'Latitude': '25.4350',
            'Longitude': '81.8461',
            'Description': 'Madhaveswari Temple (Lalita Devi) - Fingers of Sati fell here. Located in Prayagraj (Allahabad), Uttar Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Shakta_pithas',
            'Country': 'India',
            'Shakti_Peetha_Number': '13',
            'Body_Part': 'Fingers'
        },
        {
            'Park_Code': 'JWA',
            'Name': 'Jwalamukhi Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Himachal Pradesh',
            'Latitude': '31.8667',
            'Longitude': '76.3167',
            'Description': 'Jwalamukhi Temple - Tongue of Sati fell here. Located in Kangra district, Himachal Pradesh. Natural flames burn continuously. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Jwalamukhi',
            'Country': 'India',
            'Shakti_Peetha_Number': '14',
            'Body_Part': 'Tongue'
        },
        {
            'Park_Code': 'SAR',
            'Name': 'Sarvamangala Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Bihar',
            'Latitude': '24.7833',
            'Longitude': '85.0000',
            'Description': 'Sarvamangala Temple (Mangalagauri) - Breast of Sati fell here. Located in Gaya, Bihar. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Mangla_Gauri_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '15',
            'Body_Part': 'Breast'
        },
        {
            'Park_Code': 'VIS',
            'Name': 'Vishalakshi Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Uttar Pradesh',
            'Latitude': '25.3111',
            'Longitude': '83.0100',
            'Description': 'Vishalakshi Temple - Earrings of Sati fell here. Located in Varanasi, Uttar Pradesh. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Vishalakshi_Temple',
            'Country': 'India',
            'Shakti_Peetha_Number': '16',
            'Body_Part': 'Earrings'
        },
        {
            'Park_Code': 'SHA',
            'Name': 'Sharada Peeth',
            'Designation': 'Shakti Peetha',
            'States': 'Jammu and Kashmir',
            'Latitude': '34.3167',
            'Longitude': '74.5167',
            'Description': 'Sharada Peeth - Right Hand of Sati fell here. Located in Kashmir (now in Pakistan-administered Kashmir). One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Sharada_Peeth',
            'Country': 'India',
            'Shakti_Peetha_Number': '17',
            'Body_Part': 'Right Hand'
        },
        {
            'Park_Code': 'SHK',
            'Name': 'Shankari Temple',
            'Designation': 'Shakti Peetha',
            'States': 'Sri Lanka',
            'Latitude': '8.5833',
            'Longitude': '81.2333',
            'Description': 'Shankari Temple - Thigh of Sati fell here. Located in Trincomalee, Sri Lanka. One of the 18 Ashtadasha Maha Shakti Peethas.',
            'URL': 'https://en.wikipedia.org/wiki/Koneswaram_temple',
            'Country': 'Sri Lanka',
            'Shakti_Peetha_Number': '18',
            'Body_Part': 'Thigh'
        }
    ]
    
    return shakti_peethas

def save_shakti_peethas_csv(data, filename):
    """
    Save Shakti Peethas data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Shakti_Peetha_Number', 'Body_Part']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Shakti Peethas to {filename}")

if __name__ == '__main__':
    print("Creating India 18 Ashtadasha Maha Shakti Peethas data...")
    print("Based on: https://en.wikipedia.org/wiki/Shakta_pithas")
    
    peethas_data = get_shakti_peethas()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Shakti_Peethas.csv')
    save_shakti_peethas_csv(peethas_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(peethas_data)} Ashtadasha Maha Shakti Peethas")
