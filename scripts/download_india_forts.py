import csv

def get_india_forts():
    """
    Create India Major Forts CSV data
    Includes major historical forts and fortresses across India
    """
    
    forts = [
        {
            'Park_Code': 'FORT1',
            'Name': 'Red Fort',
            'Designation': 'Historic Fort',
            'States': 'Delhi',
            'Latitude': '28.6562',
            'Longitude': '77.2410',
            'Description': 'Red Fort - UNESCO World Heritage Site. Historic fort built by Mughal Emperor Shah Jahan. Located in Old Delhi, Delhi.',
            'URL': 'https://en.wikipedia.org/wiki/Red_Fort',
            'Country': 'India',
            'Fort_Category': 'Mughal Fort'
        },
        {
            'Park_Code': 'FORT2',
            'Name': 'Agra Fort',
            'Designation': 'Historic Fort',
            'States': 'Uttar Pradesh',
            'Latitude': '27.1792',
            'Longitude': '78.0211',
            'Description': 'Agra Fort - UNESCO World Heritage Site. Historic fort built by Mughal emperors. Located in Agra, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Agra_Fort',
            'Country': 'India',
            'Fort_Category': 'Mughal Fort'
        },
        {
            'Park_Code': 'FORT3',
            'Name': 'Mehrangarh Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '26.2940',
            'Longitude': '73.0190',
            'Description': 'Mehrangarh Fort - One of the largest forts in India. Built by Rao Jodha in 1459. Located in Jodhpur, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Mehrangarh',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT4',
            'Name': 'Chittorgarh Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '24.8867',
            'Longitude': '74.6472',
            'Description': 'Chittorgarh Fort - UNESCO World Heritage Site. Largest fort in India. Located in Chittorgarh, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Chittor_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT5',
            'Name': 'Amber Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '27.1733',
            'Longitude': '75.8511',
            'Description': 'Amber Fort - UNESCO World Heritage Site. Historic fort and palace complex. Located in Amer, near Jaipur, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Amber_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT6',
            'Name': 'Jaisalmer Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '26.9124',
            'Longitude': '70.9129',
            'Description': 'Jaisalmer Fort - UNESCO World Heritage Site. One of the largest fully preserved fortified cities. Located in Jaisalmer, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Jaisalmer_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT7',
            'Name': 'Gwalior Fort',
            'Designation': 'Historic Fort',
            'States': 'Madhya Pradesh',
            'Latitude': '26.2306',
            'Longitude': '78.1681',
            'Description': 'Gwalior Fort - Historic fort known as the "Pearl of India". Located in Gwalior, Madhya Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Gwalior_Fort',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT8',
            'Name': 'Golconda Fort',
            'Designation': 'Historic Fort',
            'States': 'Telangana',
            'Latitude': '17.3833',
            'Longitude': '78.4000',
            'Description': 'Golconda Fort - Historic fort known for its diamond mines. Located in Hyderabad, Telangana.',
            'URL': 'https://en.wikipedia.org/wiki/Golconda',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT9',
            'Name': 'Raigad Fort',
            'Designation': 'Historic Fort',
            'States': 'Maharashtra',
            'Latitude': '18.2333',
            'Longitude': '73.4500',
            'Description': 'Raigad Fort - Capital fort of the Maratha Empire under Shivaji. Located in Raigad district, Maharashtra.',
            'URL': 'https://en.wikipedia.org/wiki/Raigad_Fort',
            'Country': 'India',
            'Fort_Category': 'Maratha Fort'
        },
        {
            'Park_Code': 'FORT10',
            'Name': 'Sinhagad Fort',
            'Designation': 'Historic Fort',
            'States': 'Maharashtra',
            'Latitude': '18.3667',
            'Longitude': '73.7500',
            'Description': 'Sinhagad Fort - Historic fort with great significance in Maratha history. Located near Pune, Maharashtra.',
            'URL': 'https://en.wikipedia.org/wiki/Sinhagad',
            'Country': 'India',
            'Fort_Category': 'Maratha Fort'
        },
        {
            'Park_Code': 'FORT11',
            'Name': 'Lohagarh Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '27.2167',
            'Longitude': '77.5000',
            'Description': 'Lohagarh Fort - Iron Fort, known for never being conquered. Located in Bharatpur, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Lohagarh_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT12',
            'Name': 'Kumbhalgarh Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '25.1475',
            'Longitude': '73.5831',
            'Description': 'Kumbhalgarh Fort - UNESCO World Heritage Site. Birthplace of Maharana Pratap. Located in Rajsamand district, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Kumbhalgarh',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT13',
            'Name': 'Ranthambore Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '26.0167',
            'Longitude': '76.5000',
            'Description': 'Ranthambore Fort - UNESCO World Heritage Site. Historic fort within Ranthambore National Park. Located in Sawai Madhopur, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Ranthambore_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT14',
            'Name': 'Junagarh Fort',
            'Designation': 'Historic Fort',
            'States': 'Rajasthan',
            'Latitude': '28.0167',
            'Longitude': '73.3167',
            'Description': 'Junagarh Fort - Historic fort that was never conquered. Located in Bikaner, Rajasthan.',
            'URL': 'https://en.wikipedia.org/wiki/Junagarh_Fort',
            'Country': 'India',
            'Fort_Category': 'Rajasthani Fort'
        },
        {
            'Park_Code': 'FORT15',
            'Name': 'Kangra Fort',
            'Designation': 'Historic Fort',
            'States': 'Himachal Pradesh',
            'Latitude': '32.1000',
            'Longitude': '76.2667',
            'Description': 'Kangra Fort - Largest fort in the Himalayas. Located in Kangra, Himachal Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Kangra_Fort',
            'Country': 'India',
            'Fort_Category': 'Himalayan Fort'
        },
        {
            'Park_Code': 'FORT16',
            'Name': 'Daulatabad Fort',
            'Designation': 'Historic Fort',
            'States': 'Maharashtra',
            'Latitude': '19.9333',
            'Longitude': '75.2167',
            'Description': 'Daulatabad Fort - Historic fort known for its complex defense system. Located in Daulatabad, Maharashtra.',
            'URL': 'https://en.wikipedia.org/wiki/Daulatabad_Fort',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT17',
            'Name': 'Puri Fort',
            'Designation': 'Historic Fort',
            'States': 'Odisha',
            'Latitude': '19.8056',
            'Longitude': '85.8181',
            'Description': 'Puri Fort - Historic fort near Jagannath Temple. Located in Puri, Odisha.',
            'URL': 'https://en.wikipedia.org/wiki/Puri',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT18',
            'Name': 'Vellore Fort',
            'Designation': 'Historic Fort',
            'States': 'Tamil Nadu',
            'Latitude': '12.9167',
            'Longitude': '79.1333',
            'Description': 'Vellore Fort - Historic fort with a unique architectural style. Located in Vellore, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Vellore_Fort',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT19',
            'Name': 'Bekal Fort',
            'Designation': 'Historic Fort',
            'States': 'Kerala',
            'Latitude': '12.3833',
            'Longitude': '75.0333',
            'Description': 'Bekal Fort - Largest fort in Kerala. Located in Kasaragod district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Bekal_Fort',
            'Country': 'India',
            'Fort_Category': 'Coastal Fort'
        },
        {
            'Park_Code': 'FORT20',
            'Name': 'Murud-Janjira Fort',
            'Designation': 'Historic Fort',
            'States': 'Maharashtra',
            'Latitude': '18.3000',
            'Longitude': '72.9667',
            'Description': 'Murud-Janjira Fort - Island fort that was never conquered. Located in Raigad district, Maharashtra.',
            'URL': 'https://en.wikipedia.org/wiki/Murud-Janjira',
            'Country': 'India',
            'Fort_Category': 'Coastal Fort'
        },
        {
            'Park_Code': 'FORT21',
            'Name': 'Fort St. George',
            'Designation': 'Historic Fort',
            'States': 'Tamil Nadu',
            'Latitude': '13.0833',
            'Longitude': '80.2833',
            'Description': 'Fort St. George - First English fortress in India. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Fort_St._George,_India',
            'Country': 'India',
            'Fort_Category': 'Colonial Fort'
        },
        {
            'Park_Code': 'FORT22',
            'Name': 'Fort William',
            'Designation': 'Historic Fort',
            'States': 'West Bengal',
            'Latitude': '22.5500',
            'Longitude': '88.3333',
            'Description': 'Fort William - Historic British fort. Located in Kolkata, West Bengal.',
            'URL': 'https://en.wikipedia.org/wiki/Fort_William,_India',
            'Country': 'India',
            'Fort_Category': 'Colonial Fort'
        },
        {
            'Park_Code': 'FORT23',
            'Name': 'Srirangapatna Fort',
            'Designation': 'Historic Fort',
            'States': 'Karnataka',
            'Latitude': '12.4167',
            'Longitude': '76.7000',
            'Description': 'Srirangapatna Fort - Historic fort of Tipu Sultan. Located in Srirangapatna, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Srirangapatna',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT24',
            'Name': 'Bidar Fort',
            'Designation': 'Historic Fort',
            'States': 'Karnataka',
            'Latitude': '17.9167',
            'Longitude': '77.5167',
            'Description': 'Bidar Fort - Historic fort of the Bahmani Sultanate. Located in Bidar, Karnataka.',
            'URL': 'https://en.wikipedia.org/wiki/Bidar_Fort',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        },
        {
            'Park_Code': 'FORT25',
            'Name': 'Chunar Fort',
            'Designation': 'Historic Fort',
            'States': 'Uttar Pradesh',
            'Latitude': '25.1333',
            'Longitude': '82.8833',
            'Description': 'Chunar Fort - Historic fort on the banks of Ganges. Located in Mirzapur district, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Chunar_Fort',
            'Country': 'India',
            'Fort_Category': 'Historic Fort'
        }
    ]
    
    return forts

def save_india_forts_csv(data, filename):
    """
    Save India Forts data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Fort_Category']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            output_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(output_row)
    
    print(f"Saved {len(data)} forts to {filename}")

if __name__ == '__main__':
    print("Creating India Major Forts data...")
    
    forts_data = get_india_forts()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Forts.csv')
    save_india_forts_csv(forts_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(forts_data)} major forts")

