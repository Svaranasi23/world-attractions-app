import csv

def get_sri_lanka_parks():
    """
    Create Sri Lanka National Parks and Protected Areas CSV data
    """
    
    sri_lanka_parks = [
        {
            'Park_Code': 'YAL',
            'Name': 'Yala National Park',
            'Designation': 'National Park',
            'States': 'Southern Province, Uva Province',
            'Latitude': '6.3667',
            'Longitude': '81.4167',
            'Description': 'Yala National Park - Most visited national park in Sri Lanka. Home to leopards and elephants.',
            'URL': 'https://en.wikipedia.org/wiki/Yala_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'WIL',
            'Name': 'Wilpattu National Park',
            'Designation': 'National Park',
            'States': 'North Western Province, Northern Province',
            'Latitude': '8.4500',
            'Longitude': '80.0000',
            'Description': 'Wilpattu National Park - Largest national park in Sri Lanka. Known for natural lakes.',
            'URL': 'https://en.wikipedia.org/wiki/Wilpattu_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'SIN',
            'Name': 'Sinharaja Forest Reserve',
            'Designation': 'National Park',
            'States': 'Sabaragamuwa Province, Southern Province',
            'Latitude': '6.4167',
            'Longitude': '80.4167',
            'Description': 'Sinharaja Forest Reserve - UNESCO World Heritage Site. Last remaining primary rainforest in Sri Lanka.',
            'URL': 'https://en.wikipedia.org/wiki/Sinharaja_Forest_Reserve',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'UDW',
            'Name': 'Udawalawe National Park',
            'Designation': 'National Park',
            'States': 'Sabaragamuwa Province, Uva Province',
            'Latitude': '6.4333',
            'Longitude': '80.8833',
            'Description': 'Udawalawe National Park - Important elephant sanctuary.',
            'URL': 'https://en.wikipedia.org/wiki/Udawalawe_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'MIN',
            'Name': 'Minneriya National Park',
            'Designation': 'National Park',
            'States': 'North Central Province',
            'Latitude': '8.0333',
            'Longitude': '80.9000',
            'Description': 'Minneriya National Park - Famous for the "Gathering" of elephants.',
            'URL': 'https://en.wikipedia.org/wiki/Minneriya_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'HOR',
            'Name': 'Horton Plains National Park',
            'Designation': 'National Park',
            'States': 'Central Province',
            'Latitude': '6.8000',
            'Longitude': '80.8000',
            'Description': 'Horton Plains National Park - High-altitude montane grassland and cloud forest.',
            'URL': 'https://en.wikipedia.org/wiki/Horton_Plains_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'BUN',
            'Name': 'Bundala National Park',
            'Designation': 'National Park',
            'States': 'Southern Province',
            'Latitude': '6.1833',
            'Longitude': '81.2167',
            'Description': 'Bundala National Park - UNESCO Biosphere Reserve. Important bird sanctuary.',
            'URL': 'https://en.wikipedia.org/wiki/Bundala_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'KAU',
            'Name': 'Kaudulla National Park',
            'Designation': 'National Park',
            'States': 'North Central Province',
            'Latitude': '8.1333',
            'Longitude': '80.9000',
            'Description': 'Kaudulla National Park - Elephant gathering site.',
            'URL': 'https://en.wikipedia.org/wiki/Kaudulla_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'GAL',
            'Name': 'Gal Oya National Park',
            'Designation': 'National Park',
            'States': 'Eastern Province, Uva Province',
            'Latitude': '7.2167',
            'Longitude': '81.4500',
            'Description': 'Gal Oya National Park - Home to Senanayake Samudraya reservoir.',
            'URL': 'https://en.wikipedia.org/wiki/Gal_Oya_National_Park',
            'Country': 'Sri Lanka'
        },
        {
            'Park_Code': 'KUM',
            'Name': 'Kumana National Park',
            'Designation': 'National Park',
            'States': 'Eastern Province',
            'Latitude': '6.5167',
            'Longitude': '81.6833',
            'Description': 'Kumana National Park - Important bird nesting and breeding ground.',
            'URL': 'https://en.wikipedia.org/wiki/Kumana_National_Park',
            'Country': 'Sri Lanka'
        }
    ]
    
    return sri_lanka_parks

def save_sri_lanka_csv(data, filename):
    """Save Sri Lanka parks data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} Sri Lanka parks to {filename}")

if __name__ == '__main__':
    print("Creating Sri Lanka National Parks data...")
    
    parks_data = get_sri_lanka_parks()
    
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'Sri_Lanka_National_Parks.csv')
    save_sri_lanka_csv(parks_data, output_file)
    
    print(f"✅ Successfully created {output_file}")

