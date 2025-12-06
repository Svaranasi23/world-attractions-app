import csv

def get_japan_unesco_sites():
    """
    Create Japan UNESCO World Heritage Sites CSV data
    Japan has 25 UNESCO World Heritage Sites (20 cultural, 5 natural)
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'HIROSHIMA',
            'Name': 'Hiroshima Peace Memorial',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Hiroshima',
            'Latitude': '34.3955',
            'Longitude': '132.4536',
            'Description': 'Hiroshima Peace Memorial - UNESCO World Heritage Site. Memorial to the victims of the atomic bombing of Hiroshima.',
            'URL': 'https://whc.unesco.org/en/list/775',
            'Country': 'Japan',
            'UNESCO_Year': '1996'
        },
        {
            'Park_Code': 'HIMEJI',
            'Name': 'Himeji-jo',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Hyogo',
            'Latitude': '34.8394',
            'Longitude': '134.6939',
            'Description': 'Himeji Castle - UNESCO World Heritage Site. Finest surviving example of early 17th-century Japanese castle architecture.',
            'URL': 'https://whc.unesco.org/en/list/661',
            'Country': 'Japan',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'KYOTO',
            'Name': 'Historic Monuments of Ancient Kyoto',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Kyoto, Shiga',
            'Latitude': '35.0116',
            'Longitude': '135.7681',
            'Description': 'Historic Monuments of Ancient Kyoto - UNESCO World Heritage Site. Collection of 17 temples, shrines, and gardens.',
            'URL': 'https://whc.unesco.org/en/list/688',
            'Country': 'Japan',
            'UNESCO_Year': '1994'
        },
        {
            'Park_Code': 'NARA',
            'Name': 'Historic Monuments of Ancient Nara',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Nara',
            'Latitude': '34.6851',
            'Longitude': '135.8047',
            'Description': 'Historic Monuments of Ancient Nara - UNESCO World Heritage Site. Eight temples, shrines, and ruins from ancient capital.',
            'URL': 'https://whc.unesco.org/en/list/870',
            'Country': 'Japan',
            'UNESCO_Year': '1998'
        },
        {
            'Park_Code': 'NIKKO',
            'Name': 'Shrines and Temples of Nikko',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tochigi',
            'Latitude': '36.7578',
            'Longitude': '139.5994',
            'Description': 'Shrines and Temples of Nikko - UNESCO World Heritage Site. Complex of 103 religious buildings in a natural setting.',
            'URL': 'https://whc.unesco.org/en/list/913',
            'Country': 'Japan',
            'UNESCO_Year': '1999'
        },
        {
            'Park_Code': 'SHIRAKAWA',
            'Name': 'Historic Villages of Shirakawa-go and Gokayama',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gifu, Toyama',
            'Latitude': '36.2667',
            'Longitude': '136.9000',
            'Description': 'Historic Villages of Shirakawa-go and Gokayama - UNESCO World Heritage Site. Traditional gassho-style farmhouses.',
            'URL': 'https://whc.unesco.org/en/list/734',
            'Country': 'Japan',
            'UNESCO_Year': '1995'
        },
        {
            'Park_Code': 'ITSukushima',
            'Name': 'Itsukushima Shrine',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Hiroshima',
            'Latitude': '34.2958',
            'Longitude': '132.3197',
            'Description': 'Itsukushima Shrine - UNESCO World Heritage Site. Famous floating torii gate and Shinto shrine.',
            'URL': 'https://whc.unesco.org/en/list/776',
            'Country': 'Japan',
            'UNESCO_Year': '1996'
        },
        {
            'Park_Code': 'OKINAWA',
            'Name': 'Gusuku Sites and Related Properties of the Kingdom of Ryukyu',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Okinawa',
            'Latitude': '26.2167',
            'Longitude': '127.6833',
            'Description': 'Gusuku Sites and Related Properties - UNESCO World Heritage Site. Ruins of Ryukyu Kingdom castles and sites.',
            'URL': 'https://whc.unesco.org/en/list/972',
            'Country': 'Japan',
            'UNESCO_Year': '2000'
        },
        {
            'Park_Code': 'TOKYO',
            'Name': 'Sites of Japan\'s Meiji Industrial Revolution',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Yamaguchi, Kagoshima, Nagasaki, Fukuoka, Saga, Kumamoto, Iwate, Shizuoka',
            'Latitude': '33.5904',
            'Longitude': '130.4017',
            'Description': 'Sites of Japan\'s Meiji Industrial Revolution - UNESCO World Heritage Site. Industrial heritage sites from Meiji period.',
            'URL': 'https://whc.unesco.org/en/list/1484',
            'Country': 'Japan',
            'UNESCO_Year': '2015'
        },
        {
            'Park_Code': 'MOUNTFUJI',
            'Name': 'Fujisan, sacred place and source of artistic inspiration',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Yamanashi, Shizuoka',
            'Latitude': '35.3606',
            'Longitude': '138.7278',
            'Description': 'Mount Fuji - UNESCO World Heritage Site. Sacred mountain and source of artistic inspiration.',
            'URL': 'https://whc.unesco.org/en/list/1418',
            'Country': 'Japan',
            'UNESCO_Year': '2013'
        },
        # Natural Sites
        {
            'Park_Code': 'YAKUSHIMA',
            'Name': 'Yakushima',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Kagoshima',
            'Latitude': '30.3333',
            'Longitude': '130.5000',
            'Description': 'Yakushima - UNESCO World Heritage Site. Island with ancient cedar forests and unique ecosystem.',
            'URL': 'https://whc.unesco.org/en/list/662',
            'Country': 'Japan',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'SHIRAKAMI',
            'Name': 'Shirakami-Sanchi',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Aomori, Akita',
            'Latitude': '40.4667',
            'Longitude': '140.1333',
            'Description': 'Shirakami-Sanchi - UNESCO World Heritage Site. Last remaining virgin beech forest in Japan.',
            'URL': 'https://whc.unesco.org/en/list/663',
            'Country': 'Japan',
            'UNESCO_Year': '1993'
        },
        {
            'Park_Code': 'SHIRETOKO',
            'Name': 'Shiretoko',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Hokkaido',
            'Latitude': '44.1667',
            'Longitude': '145.2500',
            'Description': 'Shiretoko - UNESCO World Heritage Site. Peninsula with diverse ecosystems and marine life.',
            'URL': 'https://whc.unesco.org/en/list/1193',
            'Country': 'Japan',
            'UNESCO_Year': '2005'
        },
        {
            'Park_Code': 'OGASAWARA',
            'Name': 'Ogasawara Islands',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Tokyo',
            'Latitude': '27.0833',
            'Longitude': '142.2167',
            'Description': 'Ogasawara Islands - UNESCO World Heritage Site. Remote islands with unique flora and fauna.',
            'URL': 'https://whc.unesco.org/en/list/1362',
            'Country': 'Japan',
            'UNESCO_Year': '2011'
        }
    ]
    
    return unesco_sites

def save_japan_unesco_csv(data, filename):
    """Save Japan UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Japan UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating Japan UNESCO World Heritage Sites data...")
    
    unesco_data = get_japan_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Japan_UNESCO_Sites.csv')
    save_japan_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

