import csv

def get_china_unesco_sites():
    """
    Create China UNESCO World Heritage Sites CSV data
    China has 57 UNESCO World Heritage Sites (39 cultural, 14 natural, 4 mixed)
    This includes major sites like Great Wall, Forbidden City, Terracotta Army, etc.
    """
    
    unesco_sites = [
        # Cultural Sites
        {
            'Park_Code': 'GREATWALL',
            'Name': 'The Great Wall',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Beijing, Hebei, Shanxi, Inner Mongolia, Shaanxi, Gansu, Liaoning, Shandong, Henan, Ningxia, Xinjiang',
            'Latitude': '40.4319',
            'Longitude': '116.5704',
            'Description': 'The Great Wall - UNESCO World Heritage Site. Ancient fortification system built to protect Chinese states and empires from invasions.',
            'URL': 'https://whc.unesco.org/en/list/438',
            'Country': 'China',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'FORBIDDEN',
            'Name': 'Imperial Palaces of the Ming and Qing Dynasties',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Beijing, Liaoning',
            'Latitude': '39.9163',
            'Longitude': '116.3972',
            'Description': 'Forbidden City - UNESCO World Heritage Site. Imperial palace complex in Beijing, home to emperors for nearly 500 years.',
            'URL': 'https://whc.unesco.org/en/list/439',
            'Country': 'China',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'TERRACOTTA',
            'Name': 'Mausoleum of the First Qin Emperor',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Shaanxi',
            'Latitude': '34.3853',
            'Longitude': '109.2789',
            'Description': 'Terracotta Army - UNESCO World Heritage Site. Collection of terracotta sculptures depicting the armies of Qin Shi Huang.',
            'URL': 'https://whc.unesco.org/en/list/441',
            'Country': 'China',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'MOGAO',
            'Name': 'Mogao Caves',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Gansu',
            'Latitude': '40.0378',
            'Longitude': '94.8031',
            'Description': 'Mogao Caves - UNESCO World Heritage Site. System of 492 temples with Buddhist art spanning 1,000 years.',
            'URL': 'https://whc.unesco.org/en/list/440',
            'Country': 'China',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'POTALA',
            'Name': 'Historic Ensemble of the Potala Palace',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Tibet',
            'Latitude': '29.6578',
            'Longitude': '91.1169',
            'Description': 'Potala Palace - UNESCO World Heritage Site. Former residence of the Dalai Lama and important Buddhist site.',
            'URL': 'https://whc.unesco.org/en/list/707',
            'Country': 'China',
            'UNESCO_Year': '1994'
        },
        {
            'Park_Code': 'SUMMER',
            'Name': 'Summer Palace',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Beijing',
            'Latitude': '39.9994',
            'Longitude': '116.2750',
            'Description': 'Summer Palace - UNESCO World Heritage Site. Imperial garden in Beijing with lakes, gardens, and palaces.',
            'URL': 'https://whc.unesco.org/en/list/880',
            'Country': 'China',
            'UNESCO_Year': '1998'
        },
        {
            'Park_Code': 'TEMPLEHEAVEN',
            'Name': 'Temple of Heaven',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Beijing',
            'Latitude': '39.8822',
            'Longitude': '116.4067',
            'Description': 'Temple of Heaven - UNESCO World Heritage Site. Imperial complex of religious buildings where emperors prayed for good harvests.',
            'URL': 'https://whc.unesco.org/en/list/881',
            'Country': 'China',
            'UNESCO_Year': '1998'
        },
        {
            'Park_Code': 'LONGMEN',
            'Name': 'Longmen Grottoes',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Henan',
            'Latitude': '34.5567',
            'Longitude': '112.4706',
            'Description': 'Longmen Grottoes - UNESCO World Heritage Site. Buddhist cave art with over 100,000 statues carved into limestone cliffs.',
            'URL': 'https://whc.unesco.org/en/list/1003',
            'Country': 'China',
            'UNESCO_Year': '2000'
        },
        {
            'Park_Code': 'YUNGANG',
            'Name': 'Yungang Grottoes',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Shanxi',
            'Latitude': '40.1097',
            'Longitude': '113.1208',
            'Description': 'Yungang Grottoes - UNESCO World Heritage Site. Ancient Buddhist temple grottoes with over 51,000 statues.',
            'URL': 'https://whc.unesco.org/en/list/1039',
            'Country': 'China',
            'UNESCO_Year': '2001'
        },
        {
            'Park_Code': 'OLDCITY',
            'Name': 'Old Town of Lijiang',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Yunnan',
            'Latitude': '26.8700',
            'Longitude': '100.2333',
            'Description': 'Old Town of Lijiang - UNESCO World Heritage Site. Ancient town with unique Naxi architecture and culture.',
            'URL': 'https://whc.unesco.org/en/list/811',
            'Country': 'China',
            'UNESCO_Year': '1997'
        },
        {
            'Park_Code': 'PINGYAO',
            'Name': 'Ancient City of Ping Yao',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Shanxi',
            'Latitude': '37.2000',
            'Longitude': '112.1833',
            'Description': 'Ancient City of Ping Yao - UNESCO World Heritage Site. Well-preserved ancient walled city from Ming and Qing dynasties.',
            'URL': 'https://whc.unesco.org/en/list/812',
            'Country': 'China',
            'UNESCO_Year': '1997'
        },
        {
            'Park_Code': 'CLASSIC',
            'Name': 'Classical Gardens of Suzhou',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Jiangsu',
            'Latitude': '31.3167',
            'Longitude': '120.6167',
            'Description': 'Classical Gardens of Suzhou - UNESCO World Heritage Site. Collection of Chinese classical gardens representing garden design.',
            'URL': 'https://whc.unesco.org/en/list/813',
            'Country': 'China',
            'UNESCO_Year': '1997'
        },
        {
            'Park_Code': 'WUTAI',
            'Name': 'Mount Wutai',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Shanxi',
            'Latitude': '39.0333',
            'Longitude': '113.5833',
            'Description': 'Mount Wutai - UNESCO World Heritage Site. Sacred Buddhist mountain with ancient temples and monasteries.',
            'URL': 'https://whc.unesco.org/en/list/1279',
            'Country': 'China',
            'UNESCO_Year': '2009'
        },
        {
            'Park_Code': 'HISTORIC',
            'Name': 'Historic Centre of Macau',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Macau',
            'Latitude': '22.1983',
            'Longitude': '113.5439',
            'Description': 'Historic Centre of Macau - UNESCO World Heritage Site. Blend of Chinese and Portuguese architecture and culture.',
            'URL': 'https://whc.unesco.org/en/list/1110',
            'Country': 'China',
            'UNESCO_Year': '2005'
        },
        {
            'Park_Code': 'YINXU',
            'Name': 'Yin Xu',
            'Designation': 'UNESCO World Heritage Site (Cultural)',
            'States': 'Henan',
            'Latitude': '36.1200',
            'Longitude': '114.3200',
            'Description': 'Yin Xu - UNESCO World Heritage Site. Archaeological site of the ancient capital of the Shang Dynasty.',
            'URL': 'https://whc.unesco.org/en/list/1114',
            'Country': 'China',
            'UNESCO_Year': '2006'
        },
        # Natural Sites
        {
            'Park_Code': 'MOUNTTAI',
            'Name': 'Mount Taishan',
            'Designation': 'UNESCO World Heritage Site (Mixed)',
            'States': 'Shandong',
            'Latitude': '36.2500',
            'Longitude': '117.1000',
            'Description': 'Mount Taishan - UNESCO World Heritage Site. Sacred mountain with cultural and natural significance.',
            'URL': 'https://whc.unesco.org/en/list/437',
            'Country': 'China',
            'UNESCO_Year': '1987'
        },
        {
            'Park_Code': 'HUANGSHAN',
            'Name': 'Mount Huangshan',
            'Designation': 'UNESCO World Heritage Site (Mixed)',
            'States': 'Anhui',
            'Latitude': '30.1333',
            'Longitude': '118.1667',
            'Description': 'Mount Huangshan - UNESCO World Heritage Site. Famous for its scenery, sunsets, and granite peaks.',
            'URL': 'https://whc.unesco.org/en/list/547',
            'Country': 'China',
            'UNESCO_Year': '1990'
        },
        {
            'Park_Code': 'JIUZHAIGOU',
            'Name': 'Jiuzhaigou Valley',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Sichuan',
            'Latitude': '33.2000',
            'Longitude': '103.9000',
            'Description': 'Jiuzhaigou Valley - UNESCO World Heritage Site. Scenic area with colorful lakes, waterfalls, and snow-capped peaks.',
            'URL': 'https://whc.unesco.org/en/list/637',
            'Country': 'China',
            'UNESCO_Year': '1992'
        },
        {
            'Park_Code': 'WULINGYUAN',
            'Name': 'Wulingyuan Scenic Area',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Hunan',
            'Latitude': '29.3167',
            'Longitude': '110.4333',
            'Description': 'Wulingyuan Scenic Area - UNESCO World Heritage Site. Spectacular quartzite sandstone pillars and natural bridges.',
            'URL': 'https://whc.unesco.org/en/list/640',
            'Country': 'China',
            'UNESCO_Year': '1992'
        },
        {
            'Park_Code': 'PANDAS',
            'Name': 'Sichuan Giant Panda Sanctuaries',
            'Designation': 'UNESCO World Heritage Site (Natural)',
            'States': 'Sichuan',
            'Latitude': '30.8333',
            'Longitude': '103.0000',
            'Description': 'Sichuan Giant Panda Sanctuaries - UNESCO World Heritage Site. Home to more than 30% of the world\'s giant pandas.',
            'URL': 'https://whc.unesco.org/en/list/1213',
            'Country': 'China',
            'UNESCO_Year': '2006'
        }
    ]
    
    return unesco_sites

def save_china_unesco_csv(data, filename):
    """Save China UNESCO sites data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'UNESCO_Year']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} China UNESCO sites to {filename}")

if __name__ == '__main__':
    print("Creating China UNESCO World Heritage Sites data...")
    
    unesco_data = get_china_unesco_sites()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'China_UNESCO_Sites.csv')
    save_china_unesco_csv(unesco_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

