import csv

def get_nepal_trekking_flights():
    """
    Create Nepal Himalayan Trekking Routes CSV data
    """
    
    trekking_flights = [
        # Major Trekking Routes
        {
            'Park_Code': 'EBC',
            'Name': 'Everest Base Camp Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Solukhumbu',
            'Latitude': '27.9881',
            'Longitude': '86.9250',
            'Description': 'Everest Base Camp Trek - One of the world\'s most famous treks leading to the base camp of Mount Everest. Duration: 12-14 days. Highlights: Namche Bazaar, Tengboche Monastery, Kala Patthar viewpoint.',
            'URL': 'https://en.wikipedia.org/wiki/Everest_Base_Camp',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '12-14',
            'Difficulty': 'Moderate to Challenging'
        },
        {
            'Park_Code': 'ANC',
            'Name': 'Annapurna Circuit Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Manang, Mustang',
            'Latitude': '28.6000',
            'Longitude': '84.0000',
            'Description': 'Annapurna Circuit Trek - Classic trek encircling the Annapurna Massif. Duration: 15-20 days. Highlights: Thorong La Pass (5,416m), diverse landscapes, traditional villages.',
            'URL': 'https://en.wikipedia.org/wiki/Annapurna_Circuit',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '15-20',
            'Difficulty': 'Moderate to Challenging'
        },
        {
            'Park_Code': 'ABC',
            'Name': 'Annapurna Base Camp Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Kaski, Myagdi',
            'Latitude': '28.5833',
            'Longitude': '83.8333',
            'Description': 'Annapurna Base Camp Trek - Popular trek to the base of Annapurna I. Duration: 10-12 days. Highlights: Machapuchare views, hot springs, Gurung villages.',
            'URL': 'https://en.wikipedia.org/wiki/Annapurna_Base_Camp',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '10-12',
            'Difficulty': 'Moderate'
        },
        {
            'Park_Code': 'LTV',
            'Name': 'Langtang Valley Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Rasuwa',
            'Latitude': '28.2167',
            'Longitude': '85.5167',
            'Description': 'Langtang Valley Trek - Scenic trek into the "Valley of Glaciers" near Kathmandu. Duration: 6-8 days. Highlights: Tamang culture, Langtang Lirung views, Kyanjin Gompa.',
            'URL': 'https://en.wikipedia.org/wiki/Langtang_Valley',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '6-8',
            'Difficulty': 'Moderate'
        },
        {
            'Park_Code': 'PHL',
            'Name': 'Poon Hill Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Kaski',
            'Latitude': '28.4000',
            'Longitude': '83.7000',
            'Description': 'Poon Hill Trek - Accessible trek ideal for beginners. Duration: 5-7 days. Highlights: Sunrise views over Annapurna and Dhaulagiri ranges, Ghorepani village.',
            'URL': 'https://en.wikipedia.org/wiki/Poon_Hill',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '5-7',
            'Difficulty': 'Easy to Moderate'
        },
        {
            'Park_Code': 'MAN',
            'Name': 'Manaslu Circuit Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Gorkha, Manang',
            'Latitude': '28.5500',
            'Longitude': '84.5500',
            'Description': 'Manaslu Circuit Trek - Remote trek around Mount Manaslu. Duration: 14-16 days. Highlights: Larkya La Pass (5,106m), Tibetan culture, pristine wilderness.',
            'URL': 'https://en.wikipedia.org/wiki/Manaslu',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '14-16',
            'Difficulty': 'Challenging'
        },
        {
            'Park_Code': 'UMT',
            'Name': 'Upper Mustang Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Mustang',
            'Latitude': '29.1667',
            'Longitude': '83.8333',
            'Description': 'Upper Mustang Trek - Journey to the ancient Kingdom of Lo. Duration: 12-14 days. Highlights: Tibetan culture, Lo Manthang, desert-like landscapes.',
            'URL': 'https://en.wikipedia.org/wiki/Upper_Mustang',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '12-14',
            'Difficulty': 'Moderate'
        },
        {
            'Park_Code': 'GOK',
            'Name': 'Gokyo Lakes Trek',
            'Designation': 'Himalayan Trekking Route',
            'States': 'Solukhumbu',
            'Latitude': '27.9500',
            'Longitude': '86.7000',
            'Description': 'Gokyo Lakes Trek - Alternative route in Everest region with stunning glacial lakes. Duration: 12-14 days. Highlights: Gokyo Lakes, Gokyo Ri viewpoint, Cho La Pass.',
            'URL': 'https://en.wikipedia.org/wiki/Gokyo_Lakes',
            'Country': 'Nepal',
            'Activity_Type': 'Trekking',
            'Duration_Days': '12-14',
            'Difficulty': 'Moderate to Challenging'
        }
    ]
    
    return trekking_flights

def save_nepal_trekking_flights_csv(data, filename):
    """Save Nepal trekking and flights data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Activity_Type', 'Duration_Days', 'Difficulty']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Nepal trekking routes to {filename}")

if __name__ == '__main__':
    print("Creating Nepal Himalayan Trekking Routes data...")
    
    trekking_flights_data = get_nepal_trekking_flights()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Nepal_Trekking_Flights.csv')
    save_nepal_trekking_flights_csv(trekking_flights_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

