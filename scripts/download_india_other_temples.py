import csv

def get_india_other_temples():
    """
    Create India Other Major Temples CSV data
    Includes: Char Dham, Pancha Bhoota Stalam, Navagraha temples, and other famous temples
    Excludes: Jyotirlinga temples and Shakti Peethas (already in separate files)
    """
    
    # List of existing temples to avoid duplicates
    existing_temples = [
        'Somnath Temple', 'Mallikarjuna Temple', 'Mahakaleshwar Temple', 'Omkareshwar Temple',
        'Kedarnath Temple', 'Bhimashankar Temple', 'Kashi Vishwanath Temple', 'Trimbakeshwar Temple',
        'Vaidyanath Temple', 'Nageshwar Temple', 'Ramanathaswamy Temple', 'Grishneshwar Temple',
        'Kamakhya Temple', 'Kamakshi Amman Temple', 'Shrunkala Devi Temple', 'Chamundeshwari Temple',
        'Jogulamba Temple', 'Bhramaramba Temple', 'Mahalakshmi Temple', 'Ekaveerika Temple',
        'Mahakali Temple', 'Puruhutika Temple', 'Girija Devi Temple', 'Manikyamba Temple',
        'Madhaveswari Temple', 'Jwalamukhi Temple', 'Sarvamangala Temple', 'Vishalakshi Temple',
        'Sharada Peeth', 'Shankari Temple', 'Rameswaram'  # Rameswaram is Ramanathaswamy
    ]
    
    other_temples = [
        # Char Dham (4 major pilgrimage sites) - excluding Rameswaram (already in Jyotirlinga)
        {
            'Park_Code': 'BAD',
            'Name': 'Badrinath Temple',
            'Designation': 'Char Dham Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.7444',
            'Longitude': '79.4931',
            'Description': 'Badrinath Temple - One of the Char Dham pilgrimage sites. Dedicated to Lord Vishnu. Located in the Garhwal Himalayas, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Badrinath_Temple',
            'Country': 'India',
            'Temple_Category': 'Char Dham'
        },
        {
            'Park_Code': 'DWA',
            'Name': 'Dwarkadhish Temple',
            'Designation': 'Char Dham Temple',
            'States': 'Gujarat',
            'Latitude': '22.2400',
            'Longitude': '68.9700',
            'Description': 'Dwarkadhish Temple - One of the Char Dham pilgrimage sites. Dedicated to Lord Krishna. Located in Dwarka, Gujarat.',
            'URL': 'https://en.wikipedia.org/wiki/Dwarkadhish_Temple',
            'Country': 'India',
            'Temple_Category': 'Char Dham'
        },
        {
            'Park_Code': 'JAG',
            'Name': 'Jagannath Temple',
            'Designation': 'Char Dham Temple',
            'States': 'Odisha',
            'Latitude': '19.8056',
            'Longitude': '85.8181',
            'Description': 'Jagannath Temple - One of the Char Dham pilgrimage sites. Dedicated to Lord Jagannath. Famous for Rath Yatra. Located in Puri, Odisha.',
            'URL': 'https://en.wikipedia.org/wiki/Jagannath_Temple,_Puri',
            'Country': 'India',
            'Temple_Category': 'Char Dham'
        },
        
        # Pancha Bhoota Stalam (5 elements temples)
        {
            'Park_Code': 'EKA',
            'Name': 'Ekambareswarar Temple',
            'Designation': 'Pancha Bhoota Stalam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Ekambareswarar Temple - Earth element (Prithvi). One of the Pancha Bhoota Stalam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Ekambareswarar_Temple',
            'Country': 'India',
            'Temple_Category': 'Pancha Bhoota Stalam',
            'Element': 'Earth'
        },
        {
            'Park_Code': 'JAM',
            'Name': 'Jambukeswarar Temple',
            'Designation': 'Pancha Bhoota Stalam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '78.7000',
            'Description': 'Jambukeswarar Temple - Water element (Jala). One of the Pancha Bhoota Stalam. Located in Thiruvanaikaval, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Jambukeswarar_Temple,_Thiruvanaikaval',
            'Country': 'India',
            'Temple_Category': 'Pancha Bhoota Stalam',
            'Element': 'Water'
        },
        {
            'Park_Code': 'ANN',
            'Name': 'Annamalaiyar Temple',
            'Designation': 'Pancha Bhoota Stalam',
            'States': 'Tamil Nadu',
            'Latitude': '12.6167',
            'Longitude': '79.0667',
            'Description': 'Annamalaiyar Temple (Arunachaleswarar) - Fire element (Agni). One of the Pancha Bhoota Stalam. Located in Tiruvannamalai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Annamalaiyar_Temple',
            'Country': 'India',
            'Temple_Category': 'Pancha Bhoota Stalam',
            'Element': 'Fire'
        },
        {
            'Park_Code': 'KAL',
            'Name': 'Srikalahasti Temple',
            'Designation': 'Pancha Bhoota Stalam',
            'States': 'Andhra Pradesh',
            'Latitude': '13.7500',
            'Longitude': '79.7000',
            'Description': 'Srikalahasti Temple - Air element (Vayu). One of the Pancha Bhoota Stalam. Located in Srikalahasti, Andhra Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Srikalahasteeswara_Temple',
            'Country': 'India',
            'Temple_Category': 'Pancha Bhoota Stalam',
            'Element': 'Air'
        },
        {
            'Park_Code': 'NAT',
            'Name': 'Nataraja Temple',
            'Designation': 'Pancha Bhoota Stalam',
            'States': 'Tamil Nadu',
            'Latitude': '11.4000',
            'Longitude': '79.7000',
            'Description': 'Nataraja Temple (Chidambaram) - Space element (Akasha). One of the Pancha Bhoota Stalam. Located in Chidambaram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Thillai_Nataraja_Temple,_Chidambaram',
            'Country': 'India',
            'Temple_Category': 'Pancha Bhoota Stalam',
            'Element': 'Space'
        },
        
        # Navagraha Temples (9 planets)
        {
            'Park_Code': 'SUR',
            'Name': 'Suryanar Kovil',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Suryanar Kovil - Sun (Surya) temple. One of the Navagraha temples. Located in Suryanar Kovil, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Suryanar_Kovil',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Sun'
        },
        {
            'Park_Code': 'CHAN',
            'Name': 'Chandran Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Chandran Temple - Moon (Chandra) temple. One of the Navagraha temples. Located near Suryanar Kovil, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Moon'
        },
        {
            'Park_Code': 'ANG',
            'Name': 'Angarakan Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Angarakan Temple - Mars (Mangal) temple. One of the Navagraha temples. Located in Vaitheeswarankoil, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Mars'
        },
        {
            'Park_Code': 'BUD',
            'Name': 'Budhan Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Budhan Temple - Mercury (Budha) temple. One of the Navagraha temples. Located in Thiruvenkadu, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Mercury'
        },
        {
            'Park_Code': 'GUR',
            'Name': 'Guru Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Guru Temple - Jupiter (Guru/Brihaspati) temple. One of the Navagraha temples. Located in Alangudi, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Jupiter'
        },
        {
            'Park_Code': 'SHU',
            'Name': 'Shukran Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Shukran Temple - Venus (Shukra) temple. One of the Navagraha temples. Located in Kanjanur, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Venus'
        },
        {
            'Park_Code': 'SHAN',
            'Name': 'Shani Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Shani Temple - Saturn (Shani) temple. One of the Navagraha temples. Located in Thirunallar, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Saturn'
        },
        {
            'Park_Code': 'RAH',
            'Name': 'Rahu Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Rahu Temple - Rahu temple. One of the Navagraha temples. Located in Thirunageswaram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Rahu'
        },
        {
            'Park_Code': 'KET',
            'Name': 'Ketu Temple',
            'Designation': 'Navagraha Temple',
            'States': 'Tamil Nadu',
            'Latitude': '11.1333',
            'Longitude': '79.7833',
            'Description': 'Ketu Temple - Ketu temple. One of the Navagraha temples. Located in Keezhperumpallam, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Navagraha_temples',
            'Country': 'India',
            'Temple_Category': 'Navagraha',
            'Planet': 'Ketu'
        },
        
        # Other Famous Temples
        {
            'Park_Code': 'TIR',
            'Name': 'Tirupati Balaji Temple',
            'Designation': 'Major Temple',
            'States': 'Andhra Pradesh',
            'Latitude': '13.6500',
            'Longitude': '79.4167',
            'Description': 'Tirupati Balaji Temple (Venkateswara Temple) - One of the richest and most visited temples in the world. Dedicated to Lord Venkateswara. Located in Tirupati, Andhra Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'MEE',
            'Name': 'Meenakshi Amman Temple',
            'Designation': 'Major Temple',
            'States': 'Tamil Nadu',
            'Latitude': '9.9194',
            'Longitude': '78.1194',
            'Description': 'Meenakshi Amman Temple - Famous temple dedicated to Goddess Meenakshi and Lord Sundareswarar. Located in Madurai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Meenakshi_Temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'GOL',
            'Name': 'Golden Temple',
            'Designation': 'Sikh Temple',
            'States': 'Punjab',
            'Latitude': '31.6200',
            'Longitude': '74.8764',
            'Description': 'Golden Temple (Harmandir Sahib) - Most sacred gurdwara of Sikhism. Located in Amritsar, Punjab.',
            'URL': 'https://en.wikipedia.org/wiki/Golden_Temple',
            'Country': 'India',
            'Temple_Category': 'Sikh Temple'
        },
        {
            'Park_Code': 'AKS',
            'Name': 'Akshardham Temple',
            'Designation': 'Major Temple',
            'States': 'Delhi',
            'Latitude': '28.6128',
            'Longitude': '77.2775',
            'Description': 'Akshardham Temple - Modern Hindu temple complex. Dedicated to Swaminarayan. Located in New Delhi.',
            'URL': 'https://en.wikipedia.org/wiki/Akshardham_(Delhi)',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'VIR',
            'Name': 'Virupaksha Temple',
            'Designation': 'Major Temple',
            'States': 'Karnataka',
            'Latitude': '15.3350',
            'Longitude': '76.3922',
            'Description': 'Virupaksha Temple - Ancient temple dedicated to Lord Shiva. Part of Hampi UNESCO World Heritage Site. Located in Hampi, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Virupaksha_Temple,_Hampi',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'BEL',
            'Name': 'Belur Math',
            'Designation': 'Temple',
            'States': 'West Bengal',
            'Latitude': '22.6300',
            'Longitude': '88.3567',
            'Description': 'Belur Math - Headquarters of Ramakrishna Math and Mission. Located in Belur, West Bengal.',
            'URL': 'https://en.wikipedia.org/wiki/Belur_Math',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'KON',
            'Name': 'Konark Sun Temple',
            'Designation': 'UNESCO Temple',
            'States': 'Odisha',
            'Latitude': '19.8875',
            'Longitude': '86.0944',
            'Description': 'Konark Sun Temple - UNESCO World Heritage Site. Dedicated to the Sun God. Located in Konark, Odisha.',
            'URL': 'https://en.wikipedia.org/wiki/Konark_Sun_Temple',
            'Country': 'India',
            'Temple_Category': 'UNESCO Temple'
        },
        {
            'Park_Code': 'KHA',
            'Name': 'Khajuraho Temples',
            'Designation': 'UNESCO Temple',
            'States': 'Madhya Pradesh',
            'Latitude': '24.8500',
            'Longitude': '79.9333',
            'Description': 'Khajuraho Group of Monuments - UNESCO World Heritage Site. Famous for erotic sculptures. Located in Khajuraho, Madhya Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Khajuraho_Group_of_Monuments',
            'Country': 'India',
            'Temple_Category': 'UNESCO Temple'
        },
        {
            'Park_Code': 'RAN',
            'Name': 'Ranganathaswamy Temple',
            'Designation': 'Major Temple',
            'States': 'Tamil Nadu',
            'Latitude': '10.8667',
            'Longitude': '78.8167',
            'Description': 'Ranganathaswamy Temple - One of the largest temple complexes in India. Dedicated to Lord Ranganatha. Located in Srirangam, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Srirangam_Ranganathaswamy_temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'PAD',
            'Name': 'Padmanabhaswamy Temple',
            'Designation': 'Major Temple',
            'States': 'Kerala',
            'Latitude': '8.4822',
            'Longitude': '76.9447',
            'Description': 'Padmanabhaswamy Temple - One of the richest temples in the world. Dedicated to Lord Vishnu. Located in Thiruvananthapuram, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Padmanabhaswamy_Temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'HAR',
            'Name': 'Haridwar',
            'Designation': 'Major Pilgrimage Site',
            'States': 'Uttarakhand',
            'Latitude': '29.9457',
            'Longitude': '78.1642',
            'Description': 'Haridwar - One of the seven holiest places in Hinduism. Gateway to the Char Dham. Famous for Ganga Aarti. Located in Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Haridwar',
            'Country': 'India',
            'Temple_Category': 'Major Pilgrimage Site'
        },
        {
            'Park_Code': 'UDU',
            'Name': 'Udupi Krishna Temple',
            'Designation': 'Major Temple',
            'States': 'Karnataka',
            'Latitude': '13.3389',
            'Longitude': '74.7451',
            'Description': 'Udupi Krishna Temple - Famous temple dedicated to Lord Krishna. Founded by Madhvacharya. Located in Udupi, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Udupi_Krishna_Temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'SAB',
            'Name': 'Sabarimala Ayyappa Temple',
            'Designation': 'Major Temple',
            'States': 'Kerala',
            'Latitude': '9.4333',
            'Longitude': '77.0833',
            'Description': 'Sabarimala Ayyappa Temple - One of the largest annual pilgrimages in the world. Dedicated to Lord Ayyappa. Located in Pathanamthitta, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Sabarimala',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'GVY',
            'Name': 'Guruvayur Temple',
            'Designation': 'Major Temple',
            'States': 'Kerala',
            'Latitude': '10.5950',
            'Longitude': '76.0400',
            'Description': 'Guruvayur Temple - Famous temple dedicated to Lord Krishna. Known as "Bhooloka Vaikuntha" (Heaven on Earth). Located in Guruvayur, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Guruvayur_Temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        # Uttarakhand/Himalayan Region Temples
        {
            'Park_Code': 'RIS',
            'Name': 'Rishikesh',
            'Designation': 'Major Pilgrimage Site',
            'States': 'Uttarakhand',
            'Latitude': '30.0869',
            'Longitude': '78.2676',
            'Description': 'Rishikesh - Gateway to the Himalayas and Char Dham. Known as the "Yoga Capital of the World". Home to many temples and ashrams along the Ganges.',
            'URL': 'https://en.wikipedia.org/wiki/Rishikesh',
            'Country': 'India',
            'Temple_Category': 'Major Pilgrimage Site'
        },
        {
            'Park_Code': 'GOT',
            'Name': 'Gangotri Temple',
            'Designation': 'Char Dham Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.9944',
            'Longitude': '78.9411',
            'Description': 'Gangotri Temple - Source of the Ganges River. One of the Char Dham pilgrimage sites. Located in Uttarkashi district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Gangotri',
            'Country': 'India',
            'Temple_Category': 'Char Dham'
        },
        {
            'Park_Code': 'YAM',
            'Name': 'Yamunotri Temple',
            'Designation': 'Char Dham Temple',
            'States': 'Uttarakhand',
            'Latitude': '31.0167',
            'Longitude': '78.4500',
            'Description': 'Yamunotri Temple - Source of the Yamuna River. One of the Char Dham pilgrimage sites. Located in Uttarkashi district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Yamunotri',
            'Country': 'India',
            'Temple_Category': 'Char Dham'
        },
        {
            'Park_Code': 'HEM',
            'Name': 'Hemkund Sahib',
            'Designation': 'Sikh Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.6833',
            'Longitude': '79.6167',
            'Description': 'Hemkund Sahib - High-altitude Sikh gurdwara. Located at 4,632 meters above sea level. Dedicated to Guru Gobind Singh.',
            'URL': 'https://en.wikipedia.org/wiki/Hemkund',
            'Country': 'India',
            'Temple_Category': 'Sikh Temple'
        },
        {
            'Park_Code': 'TUN',
            'Name': 'Tungnath Temple',
            'Designation': 'Major Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.4833',
            'Longitude': '79.2167',
            'Description': 'Tungnath Temple - Highest Shiva temple in the world at 3,680 meters. Part of the Panch Kedar. Located in Rudraprayag district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Tungnath',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'MHM',
            'Name': 'Madhyamaheshwar Temple',
            'Designation': 'Major Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.5667',
            'Longitude': '79.2833',
            'Description': 'Madhyamaheshwar Temple - One of the Panch Kedar temples. Dedicated to Lord Shiva. Located in Rudraprayag district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Madhyamaheshwar',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'RUD',
            'Name': 'Rudranath Temple',
            'Designation': 'Major Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.5167',
            'Longitude': '79.3167',
            'Description': 'Rudranath Temple - One of the Panch Kedar temples. Dedicated to Lord Shiva. Located in Chamoli district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Rudranath',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'KPS',
            'Name': 'Kalpeshwar Temple',
            'Designation': 'Major Temple',
            'States': 'Uttarakhand',
            'Latitude': '30.5167',
            'Longitude': '79.2500',
            'Description': 'Kalpeshwar Temple - One of the Panch Kedar temples. Dedicated to Lord Shiva. Located in Chamoli district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Kalpeshwar',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'JOS',
            'Name': 'Joshimath',
            'Designation': 'Major Pilgrimage Site',
            'States': 'Uttarakhand',
            'Latitude': '30.5500',
            'Longitude': '79.5667',
            'Description': 'Joshimath - Important pilgrimage town and winter seat of Badrinath. Home to Narasimha Temple and other sacred sites.',
            'URL': 'https://en.wikipedia.org/wiki/Joshimath',
            'Country': 'India',
            'Temple_Category': 'Major Pilgrimage Site'
        },
        {
            'Park_Code': 'DEV',
            'Name': 'Devprayag',
            'Designation': 'Major Pilgrimage Site',
            'States': 'Uttarakhand',
            'Latitude': '30.1500',
            'Longitude': '78.6000',
            'Description': 'Devprayag - Confluence of Alaknanda and Bhagirathi rivers forming the Ganges. Important pilgrimage site with Raghunath Temple.',
            'URL': 'https://en.wikipedia.org/wiki/Devprayag',
            'Country': 'India',
            'Temple_Category': 'Major Pilgrimage Site'
        },
        {
            'Park_Code': 'KAN',
            'Name': 'Kanaka Durga Temple',
            'Designation': 'Major Temple',
            'States': 'Andhra Pradesh',
            'Latitude': '16.5162',
            'Longitude': '80.6125',
            'Description': 'Kanaka Durga Temple - Famous temple dedicated to Goddess Kanaka Durga. Located on Indrakeeladri Hill in Vijayawada, Andhra Pradesh. One of the most visited temples in South India.',
            'URL': 'https://en.wikipedia.org/wiki/Kanaka_Durga_Temple',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'RAM',
            'Name': 'Ram Mandir',
            'Designation': 'Major Temple',
            'States': 'Uttar Pradesh',
            'Latitude': '26.7956',
            'Longitude': '82.1944',
            'Description': 'Ram Mandir - Grand temple dedicated to Lord Rama. Located in Ayodhya, Uttar Pradesh. Birthplace of Lord Rama and one of the most important pilgrimage sites in India.',
            'URL': 'https://en.wikipedia.org/wiki/Ram_Mandir',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        },
        {
            'Park_Code': 'KRS',
            'Name': 'Krishna Janmasthan Temple',
            'Designation': 'Major Temple',
            'States': 'Uttar Pradesh',
            'Latitude': '27.5019',
            'Longitude': '77.6833',
            'Description': 'Krishna Janmasthan Temple - Temple marking the birthplace of Lord Krishna. Located in Mathura, Uttar Pradesh. One of the most sacred sites for Vaishnavas.',
            'URL': 'https://en.wikipedia.org/wiki/Krishna_Janmasthan_Temple_Complex',
            'Country': 'India',
            'Temple_Category': 'Major Temple'
        }
    ]
    
    # Filter out any duplicates (check by name)
    filtered_temples = []
    for temple in other_temples:
        temple_name = temple['Name'].lower()
        is_duplicate = False
        for existing in existing_temples:
            if existing.lower() in temple_name or temple_name in existing.lower():
                is_duplicate = True
                break
        if not is_duplicate:
            filtered_temples.append(temple)
    
    return filtered_temples

def save_india_other_temples_csv(data, filename):
    """
    Save India Other Temples data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Temple_Category', 'Element', 'Planet']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            # Only include Element and Planet if they exist
            output_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(output_row)
    
    print(f"Saved {len(data)} other temples to {filename}")

if __name__ == '__main__':
    print("Creating India Other Major Temples data...")
    print("Excluding Jyotirlinga and Shakti Peethas (already in separate files)")
    
    temples_data = get_india_other_temples()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Other_Temples.csv')
    save_india_other_temples_csv(temples_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(temples_data)} other major temples")

