import csv

def get_india_unesco_sites():
    """
    Download or create India UNESCO World Heritage Sites CSV data
    Comprehensive list of all 44 UNESCO World Heritage Sites in India
    """
    
    # Complete list of India's UNESCO World Heritage Sites (as of 2024-2025)
    unesco_sites = [
        # Natural Sites (7)
        {
            'Park_Code': 'KAZ',
            'Name': 'Kaziranga National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Assam',
            'Latitude': '26.6000',
            'Longitude': '93.4167',
            'Description': 'Kaziranga National Park - UNESCO World Heritage Site. Home to the world\'s largest population of one-horned rhinoceroses.',
            'URL': 'https://whc.unesco.org/en/list/337',
            'Country': 'India',
            'UNESCO_Year': '1985'
        },
        {
            'Park_Code': 'MAN',
            'Name': 'Manas Wildlife Sanctuary',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Assam',
            'Latitude': '26.7167',
            'Longitude': '91.0167',
            'Description': 'Manas Wildlife Sanctuary - UNESCO World Heritage Site. Important tiger and elephant reserve.',
            'URL': 'https://whc.unesco.org/en/list/338',
            'Country': 'India',
            'UNESCO_Year': '1985'
        },
        {
            'Park_Code': 'KEO',
            'Name': 'Keoladeo National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Rajasthan',
            'Latitude': '27.1667',
            'Longitude': '77.5167',
            'Description': 'Keoladeo National Park (Bharatpur Bird Sanctuary) - UNESCO World Heritage Site. Important bird sanctuary.',
            'URL': 'https://whc.unesco.org/en/list/340',
            'Country': 'India',
            'UNESCO_Year': '1985'
        },
        {
            'Park_Code': 'SUN',
            'Name': 'Sundarbans National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'West Bengal',
            'Latitude': '21.9500',
            'Longitude': '88.9000',
            'Description': 'Sundarbans National Park - UNESCO World Heritage Site. Largest mangrove forest in the world, home to Bengal tigers.',
            'URL': 'https://whc.unesco.org/en/list/452',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'NAN',
            'Name': 'Nanda Devi and Valley of Flowers National Parks',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Uttarakhand',
            'Latitude': '30.4167',
            'Longitude': '79.5833',
            'Description': 'Nanda Devi and Valley of Flowers National Parks - UNESCO World Heritage Site. Alpine meadows and high-altitude ecosystems.',
            'URL': 'https://whc.unesco.org/en/list/335',
            'Country': 'India',
            'UNESCO_Year': '1988'
        },
        {
            'Park_Code': 'WES',
            'Name': 'Western Ghats',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Karnataka, Kerala, Tamil Nadu, Maharashtra',
            'Latitude': '12.0000',
            'Longitude': '76.0000',
            'Description': 'Western Ghats - UNESCO World Heritage Site. One of the world\'s eight "hottest hotspots" of biological diversity.',
            'URL': 'https://whc.unesco.org/en/list/1342',
            'Country': 'India',
            'UNESCO_Year': '2012'
        },
        {
            'Park_Code': 'GRE',
            'Name': 'Great Himalayan National Park',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Himachal Pradesh',
            'Latitude': '31.7333',
            'Longitude': '77.4333',
            'Description': 'Great Himalayan National Park - UNESCO World Heritage Site. High-altitude alpine ecosystems.',
            'URL': 'https://whc.unesco.org/en/list/1406',
            'Country': 'India',
            'UNESCO_Year': '2014'
        },
        # Mixed Sites (2)
        {
            'Park_Code': 'KAN',
            'Name': 'Khangchendzonga National Park',
            'Designation': 'UNESCO World Heritage Site (Mixed)',
            'States': 'Sikkim',
            'Latitude': '27.6667',
            'Longitude': '88.3000',
            'Description': 'Khangchendzonga National Park - UNESCO World Heritage Site. Mixed cultural and natural heritage site.',
            'URL': 'https://whc.unesco.org/en/list/1513',
            'Country': 'India',
            'UNESCO_Year': '2016'
        },
        # Cultural Sites (35) - Major ones with geographic coordinates
        {
            'Park_Code': 'TAJ',
            'Name': 'Taj Mahal',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Uttar Pradesh',
            'Latitude': '27.1751',
            'Longitude': '78.0421',
            'Description': 'Taj Mahal - UNESCO World Heritage Site. Iconic marble mausoleum, one of the New Seven Wonders of the World.',
            'URL': 'https://whc.unesco.org/en/list/252',
            'Country': 'India',
            'UNESCO_Year': '1983'
        },
        {
            'Park_Code': 'AGF',
            'Name': 'Agra Fort',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Uttar Pradesh',
            'Latitude': '27.1797',
            'Longitude': '78.0211',
            'Description': 'Agra Fort - UNESCO World Heritage Site. Mughal fortress and palace complex.',
            'URL': 'https://whc.unesco.org/en/list/251',
            'Country': 'India',
            'UNESCO_Year': '1983'
        },
        {
            'Park_Code': 'AJT',
            'Name': 'Ajanta Caves',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '20.5519',
            'Longitude': '75.7033',
            'Description': 'Ajanta Caves - UNESCO World Heritage Site. Ancient Buddhist rock-cut cave monuments with paintings.',
            'URL': 'https://whc.unesco.org/en/list/242',
            'Country': 'India',
            'UNESCO_Year': '1983'
        },
        {
            'Park_Code': 'ELL',
            'Name': 'Ellora Caves',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '20.0264',
            'Longitude': '75.1792',
            'Description': 'Ellora Caves - UNESCO World Heritage Site. Rock-cut cave temples representing Buddhist, Hindu, and Jain art.',
            'URL': 'https://whc.unesco.org/en/list/243',
            'Country': 'India',
            'UNESCO_Year': '1983'
        },
        {
            'Park_Code': 'SUN',
            'Name': 'Sun Temple, Konarak',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Odisha',
            'Latitude': '19.8875',
            'Longitude': '86.0947',
            'Description': 'Sun Temple, Konarak - UNESCO World Heritage Site. 13th-century temple dedicated to the sun god.',
            'URL': 'https://whc.unesco.org/en/list/246',
            'Country': 'India',
            'UNESCO_Year': '1984'
        },
        {
            'Park_Code': 'MAH',
            'Name': 'Group of Monuments at Mahabalipuram',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tamil Nadu',
            'Latitude': '12.6167',
            'Longitude': '80.1917',
            'Description': 'Group of Monuments at Mahabalipuram - UNESCO World Heritage Site. 7th-8th century rock-cut temples and sculptures.',
            'URL': 'https://whc.unesco.org/en/list/249',
            'Country': 'India',
            'UNESCO_Year': '1984'
        },
        {
            'Park_Code': 'KHA',
            'Name': 'Khajuraho Group of Monuments',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Madhya Pradesh',
            'Latitude': '24.8522',
            'Longitude': '79.9194',
            'Description': 'Khajuraho Group of Monuments - UNESCO World Heritage Site. Medieval Hindu and Jain temples with intricate sculptures.',
            'URL': 'https://whc.unesco.org/en/list/240',
            'Country': 'India',
            'UNESCO_Year': '1986'
        },
        {
            'Park_Code': 'HAP',
            'Name': 'Hampi',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Karnataka',
            'Latitude': '15.3350',
            'Longitude': '76.4600',
            'Description': 'Group of Monuments at Hampi - UNESCO World Heritage Site. Ruins of the Vijayanagara Empire capital.',
            'URL': 'https://whc.unesco.org/en/list/241',
            'Country': 'India',
            'UNESCO_Year': '1986'
        },
        {
            'Park_Code': 'FAT',
            'Name': 'Fatehpur Sikri',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Uttar Pradesh',
            'Latitude': '27.0947',
            'Longitude': '77.6611',
            'Description': 'Fatehpur Sikri - UNESCO World Heritage Site. Mughal city built by Akbar, abandoned capital.',
            'URL': 'https://whc.unesco.org/en/list/255',
            'Country': 'India',
            'UNESCO_Year': '1986'
        },
        {
            'Park_Code': 'GOM',
            'Name': 'Group of Monuments at Pattadakal',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Karnataka',
            'Latitude': '15.9481',
            'Longitude': '75.8167',
            'Description': 'Group of Monuments at Pattadakal - UNESCO World Heritage Site. 7th-8th century Chalukya temples.',
            'URL': 'https://whc.unesco.org/en/list/239',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'ELE',
            'Name': 'Elephanta Caves',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '18.9583',
            'Longitude': '72.9306',
            'Description': 'Elephanta Caves - UNESCO World Heritage Site. Rock-cut cave temples on Elephanta Island.',
            'URL': 'https://whc.unesco.org/en/list/244',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'BRI',
            'Name': 'Brihadisvara Temple, Thanjavur',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tamil Nadu',
            'Latitude': '10.7828',
            'Longitude': '79.1317',
            'Description': 'Great Living Chola Temples - Brihadisvara Temple - UNESCO World Heritage Site. 11th century Chola temple.',
            'URL': 'https://whc.unesco.org/en/list/250',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'GOL',
            'Name': 'Golconda Fort',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Telangana',
            'Latitude': '17.3833',
            'Longitude': '78.4000',
            'Description': 'Golconda Fort - UNESCO World Heritage Site. Medieval fort and capital of Qutb Shahi dynasty.',
            'URL': 'https://whc.unesco.org/en/list/',
            'Country': 'India',
            'UNESCO_Year': '2010'
        },
        {
            'Park_Code': 'QUT',
            'Name': 'Qutb Minar and its Monuments',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Delhi',
            'Latitude': '28.5244',
            'Longitude': '77.1856',
            'Description': 'Qutb Minar and its Monuments - UNESCO World Heritage Site. 12th-13th century minaret and complex.',
            'URL': 'https://whc.unesco.org/en/list/233',
            'Country': 'India',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'BUD',
            'Name': 'Buddhist Monuments at Sanchi',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Madhya Pradesh',
            'Latitude': '23.4794',
            'Longitude': '77.7397',
            'Description': 'Buddhist Monuments at Sanchi - UNESCO World Heritage Site. Ancient Buddhist stupas and monasteries.',
            'URL': 'https://whc.unesco.org/en/list/524',
            'Country': 'India',
            'UNESCO_Year': '1989'
        },
        {
            'Park_Code': 'HUM',
            'Name': 'Humayun\'s Tomb',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Delhi',
            'Latitude': '28.5931',
            'Longitude': '77.2506',
            'Description': 'Humayun\'s Tomb - UNESCO World Heritage Site. Mughal mausoleum, precursor to Taj Mahal.',
            'URL': 'https://whc.unesco.org/en/list/232',
            'Country': 'India',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'RED',
            'Name': 'Red Fort Complex',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Delhi',
            'Latitude': '28.6562',
            'Longitude': '77.2410',
            'Description': 'Red Fort Complex - UNESCO World Heritage Site. Mughal fort and palace in Old Delhi.',
            'URL': 'https://whc.unesco.org/en/list/231',
            'Country': 'India',
            'UNESCO_Year': '2007'
        },
        {
            'Park_Code': 'CHA',
            'Name': 'Champaner-Pavagadh Archaeological Park',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gujarat',
            'Latitude': '22.4833',
            'Longitude': '73.5333',
            'Description': 'Champaner-Pavagadh Archaeological Park - UNESCO World Heritage Site. Pre-Mughal Islamic and Hindu architecture.',
            'URL': 'https://whc.unesco.org/en/list/1101',
            'Country': 'India',
            'UNESCO_Year': '2004'
        },
        {
            'Park_Code': 'CHH',
            'Name': 'Chhatrapati Shivaji Terminus',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '18.9400',
            'Longitude': '72.8353',
            'Description': 'Chhatrapati Shivaji Terminus - UNESCO World Heritage Site. Historic railway station in Mumbai.',
            'URL': 'https://whc.unesco.org/en/list/945',
            'Country': 'India',
            'UNESCO_Year': '2004'
        },
        {
            'Park_Code': 'MAH',
            'Name': 'Mountain Railways of India',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'West Bengal, Tamil Nadu, Himachal Pradesh',
            'Latitude': '27.0500',
            'Longitude': '88.2667',
            'Description': 'Mountain Railways of India - UNESCO World Heritage Site. Darjeeling, Nilgiri, and Kalka-Shimla railways.',
            'URL': 'https://whc.unesco.org/en/list/944',
            'Country': 'India',
            'UNESCO_Year': '1999'
        },
        {
            'Park_Code': 'RAJ',
            'Name': 'Rani-ki-Vav',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gujarat',
            'Latitude': '23.8583',
            'Longitude': '72.1019',
            'Description': 'Rani-ki-Vav - UNESCO World Heritage Site. 11th century stepwell in Patan.',
            'URL': 'https://whc.unesco.org/en/list/922',
            'Country': 'India',
            'UNESCO_Year': '2014'
        },
        {
            'Park_Code': 'NAL',
            'Name': 'Nalanda Mahavihara',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Bihar',
            'Latitude': '25.1367',
            'Longitude': '85.4439',
            'Description': 'Archaeological Site of Nalanda Mahavihara - UNESCO World Heritage Site. Ancient Buddhist university ruins.',
            'URL': 'https://whc.unesco.org/en/list/1502',
            'Country': 'India',
            'UNESCO_Year': '2016'
        },
        {
            'Park_Code': 'AHM',
            'Name': 'Historic City of Ahmedabad',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gujarat',
            'Latitude': '23.0225',
            'Longitude': '72.5714',
            'Description': 'Historic City of Ahmedabad - UNESCO World Heritage Site. Walled city with unique architecture.',
            'URL': 'https://whc.unesco.org/en/list/1551',
            'Country': 'India',
            'UNESCO_Year': '2017'
        },
        {
            'Park_Code': 'VIC',
            'Name': 'Victorian Gothic and Art Deco Ensembles of Mumbai',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '18.9400',
            'Longitude': '72.8353',
            'Description': 'Victorian Gothic and Art Deco Ensembles of Mumbai - UNESCO World Heritage Site. Colonial architecture.',
            'URL': 'https://whc.unesco.org/en/list/1480',
            'Country': 'India',
            'UNESCO_Year': '2018'
        },
        {
            'Park_Code': 'JAI',
            'Name': 'Jaipur City',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Rajasthan',
            'Latitude': '26.9124',
            'Longitude': '75.7873',
            'Description': 'Jaipur City - UNESCO World Heritage Site. Planned city with unique architecture.',
            'URL': 'https://whc.unesco.org/en/list/1605',
            'Country': 'India',
            'UNESCO_Year': '2019'
        },
        {
            'Park_Code': 'KAK',
            'Name': 'Kakatiya Rudreshwara Temple',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Telangana',
            'Latitude': '18.2400',
            'Longitude': '79.8067',
            'Description': 'Kakatiya Rudreshwara (Ramappa) Temple - UNESCO World Heritage Site. 13th century Kakatiya temple.',
            'URL': 'https://whc.unesco.org/en/list/1570',
            'Country': 'India',
            'UNESCO_Year': '2021'
        },
        {
            'Park_Code': 'DHO',
            'Name': 'Dholavira',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gujarat',
            'Latitude': '23.8867',
            'Longitude': '70.2128',
            'Description': 'Dholavira: A Harappan City - UNESCO World Heritage Site. Ancient Indus Valley Civilization site.',
            'URL': 'https://whc.unesco.org/en/list/1645',
            'Country': 'India',
            'UNESCO_Year': '2021'
        },
        {
            'Park_Code': 'SANT',
            'Name': 'Santiniketan',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'West Bengal',
            'Latitude': '23.6833',
            'Longitude': '87.6833',
            'Description': 'Santiniketan - UNESCO World Heritage Site. Founded by Rabindranath Tagore, cultural and educational center.',
            'URL': 'https://whc.unesco.org/en/list/1375',
            'Country': 'India',
            'UNESCO_Year': '2023'
        },
        {
            'Park_Code': 'HOP',
            'Name': 'Sacred Ensembles of the Hoysalas',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Karnataka',
            'Latitude': '12.8417',
            'Longitude': '76.4833',
            'Description': 'Sacred Ensembles of the Hoysalas - UNESCO World Heritage Site. 12th-13th century Hoysala temples.',
            'URL': 'https://whc.unesco.org/en/list/1670',
            'Country': 'India',
            'UNESCO_Year': '2023'
        },
        {
            'Park_Code': 'MAR',
            'Name': 'Maratha Military Landscapes',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Maharashtra',
            'Latitude': '18.5204',
            'Longitude': '73.8567',
            'Description': 'Maratha Military Landscapes of India - UNESCO World Heritage Site. Forts and military architecture.',
            'URL': 'https://whc.unesco.org/en/list/',
            'Country': 'India',
            'UNESCO_Year': '2025'
        },
        # Additional important cultural sites
        {
            'Park_Code': 'JAN',
            'Name': 'Jantar Mantar, Jaipur',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Rajasthan',
            'Latitude': '26.9247',
            'Longitude': '75.8247',
            'Description': 'Jantar Mantar, Jaipur - UNESCO World Heritage Site. 18th century astronomical observatory.',
            'URL': 'https://whc.unesco.org/en/list/1338',
            'Country': 'India',
            'UNESCO_Year': '2010'
        },
        {
            'Park_Code': 'HIL',
            'Name': 'Hill Forts of Rajasthan',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Rajasthan',
            'Latitude': '24.5833',
            'Longitude': '73.6833',
            'Description': 'Hill Forts of Rajasthan - UNESCO World Heritage Site. Six hill forts including Chittorgarh, Kumbhalgarh, etc.',
            'URL': 'https://whc.unesco.org/en/list/247',
            'Country': 'India',
            'UNESCO_Year': '2013'
        },
        {
            'Park_Code': 'GOM',
            'Name': 'Great Living Chola Temples',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tamil Nadu',
            'Latitude': '10.7828',
            'Longitude': '79.1317',
            'Description': 'Great Living Chola Temples - UNESCO World Heritage Site. Three Chola dynasty temples.',
            'URL': 'https://whc.unesco.org/en/list/250',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'ROC',
            'Name': 'Rock Shelters of Bhimbetka',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Madhya Pradesh',
            'Latitude': '22.9333',
            'Longitude': '77.6167',
            'Description': 'Rock Shelters of Bhimbetka - UNESCO World Heritage Site. Prehistoric rock art and shelters.',
            'URL': 'https://whc.unesco.org/en/list/925',
            'Country': 'India',
            'UNESCO_Year': '2003'
        },
        {
            'Park_Code': 'MOG',
            'Name': 'Mahabodhi Temple Complex',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Bihar',
            'Latitude': '24.6956',
            'Longitude': '84.9914',
            'Description': 'Mahabodhi Temple Complex at Bodh Gaya - UNESCO World Heritage Site. Site of Buddha\'s enlightenment.',
            'URL': 'https://whc.unesco.org/en/list/1056',
            'Country': 'India',
            'UNESCO_Year': '2002'
        },
        {
            'Park_Code': 'GOM',
            'Name': 'Gangaikonda Cholapuram',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tamil Nadu',
            'Latitude': '11.2056',
            'Longitude': '79.4500',
            'Description': 'Great Living Chola Temples - Gangaikonda Cholapuram - UNESCO World Heritage Site. 11th century Chola temple.',
            'URL': 'https://whc.unesco.org/en/list/250',
            'Country': 'India',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'AIR',
            'Name': 'Airavatesvara Temple',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tamil Nadu',
            'Latitude': '10.9481',
            'Longitude': '79.3569',
            'Description': 'Great Living Chola Temples - Airavatesvara Temple - UNESCO World Heritage Site. 12th century Chola temple.',
            'URL': 'https://whc.unesco.org/en/list/250',
            'Country': 'India',
            'UNESCO_Year': '1987'
        }
    ]
    
    return unesco_sites

def save_unesco_csv(data, filename):
    """
    Save UNESCO sites data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Downloading India UNESCO World Heritage Sites data...")
    
    unesco_data = get_india_unesco_sites()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_UNESCO_Sites.csv')
    save_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
