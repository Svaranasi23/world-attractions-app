"""
Download Indian National Parks data from Wikipedia
This script scrapes Wikipedia for Indian National Parks information
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time

def get_indian_parks_data():
    """
    Scrape Indian National Parks from Wikipedia
    Returns a list of park dictionaries
    """
    parks = []
    
    # Wikipedia page for Indian National Parks
    url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_India"
    
    try:
        print("Fetching Indian National Parks data from Wikipedia...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main table with park data
        tables = soup.find_all('table', {'class': 'wikitable'})
        
        if not tables:
            print("No tables found. Trying alternative method...")
            # Try finding any table
            tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            
            # Skip header row
            for row in rows[1:]:
                cells = row.find_all(['td', 'th'])
                
                if len(cells) >= 3:
                    try:
                        # Extract park name (usually first column)
                        name = cells[0].get_text(strip=True)
                        
                        # Skip if it's a header or empty
                        if not name or name.lower() in ['name', 'park name', 'state', '']:
                            continue
                        
                        # Extract state (usually second column)
                        state = cells[1].get_text(strip=True) if len(cells) > 1 else ''
                        
                        # Extract year (optional)
                        year = cells[2].get_text(strip=True) if len(cells) > 2 else ''
                        
                        # Try to find coordinates from links or infobox
                        lat = None
                        lon = None
                        
                        # Look for coordinate links
                        coord_links = row.find_all('a', href=lambda x: x and 'geohack' in x)
                        if coord_links:
                            href = coord_links[0].get('href', '')
                            # Extract coordinates from geohack URL
                            # Format: /w/index.php?title=Special:Geohack&params=28.5931_N_83.6250_E
                            if 'params=' in href:
                                params = href.split('params=')[1].split('&')[0]
                                parts = params.split('_')
                                if len(parts) >= 4:
                                    try:
                                        lat = float(parts[0])
                                        if parts[1] == 'S':
                                            lat = -lat
                                        lon = float(parts[2])
                                        if parts[3] == 'W':
                                            lon = -lon
                                    except:
                                        pass
                        
                        # If no coordinates found, try to get from name link
                        if lat is None or lon is None:
                            name_link = cells[0].find('a')
                            if name_link:
                                park_url = f"https://en.wikipedia.org{name_link.get('href', '')}"
                                lat, lon = get_coordinates_from_page(park_url)
                        
                        # Clean up name (remove references, notes, etc.)
                        name = name.split('[')[0].split('(')[0].strip()
                        
                        if name and name.lower() not in ['name', 'park name']:
                            park = {
                                'Park_Code': name[:3].upper().replace(' ', ''),
                                'Name': name,
                                'Designation': 'National Park',
                                'States': state,
                                'Latitude': str(lat) if lat else '0',
                                'Longitude': str(lon) if lon else '0',
                                'Description': f"Indian National Park in {state}. Established: {year}" if year else f"Indian National Park in {state}",
                                'URL': '',
                                'Country': 'India'
                            }
                            parks.append(park)
                            print(f"  Found: {name} ({state})")
                            
                    except Exception as e:
                        print(f"  Error processing row: {e}")
                        continue
        
        print(f"\nTotal Indian National Parks found: {len(parks)}")
        return parks
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def get_coordinates_from_page(url):
    """Try to get coordinates from a Wikipedia page"""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Look for coordinates in the infobox
        coord_span = soup.find('span', {'class': 'geo'})
        if coord_span:
            text = coord_span.get_text()
            if ';' in text:
                parts = text.split(';')
                if len(parts) == 2:
                    try:
                        lat = float(parts[0].strip())
                        lon = float(parts[1].strip())
                        return lat, lon
                    except:
                        pass
        
        # Look for geohack link
        coord_link = soup.find('a', href=lambda x: x and 'geohack' in x)
        if coord_link:
            href = coord_link.get('href', '')
            if 'params=' in href:
                params = href.split('params=')[1].split('&')[0]
                parts = params.split('_')
                if len(parts) >= 4:
                    try:
                        lat = float(parts[0])
                        if parts[1] == 'S':
                            lat = -lat
                        lon = float(parts[2])
                        if parts[3] == 'W':
                            lon = -lon
                        return lat, lon
                    except:
                        pass
    except:
        pass
    
    return None, None

def save_to_csv(parks, filename='Indian_National_Parks.csv'):
    """Save parks data to CSV file"""
    if not parks:
        print("No parks to save.")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parks)
    
    print(f"\n✅ Saved {len(parks)} parks to {filename}")

if __name__ == '__main__':
    print("=" * 60)
    print("Indian National Parks Data Downloader")
    print("=" * 60)
    
    parks = get_indian_parks_data()
    
    if parks:
        # Save to current directory
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        csv_path = os.path.join(data_dir, 'Indian_National_Parks.csv')
        save_to_csv(parks, csv_path)
        
        # Also save to public/data for the app
        public_data_dir = os.path.join(script_dir, '..', 'public', 'data')
        os.makedirs(public_data_dir, exist_ok=True)
        public_csv_path = os.path.join(public_data_dir, 'Indian_National_Parks.csv')
        save_to_csv(parks, public_csv_path)
        
        print(f"\n✅ Data saved to:")
        print(f"   - {csv_path}")
        print(f"   - {public_csv_path}")
    else:
        print("\n❌ No parks data retrieved. Please check your internet connection and try again.")

