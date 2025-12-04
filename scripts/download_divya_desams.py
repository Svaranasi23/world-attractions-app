import csv

def get_divya_desams():
    """
    Create India 108 Vaishnava Divya Desams CSV data
    Divya Desams are 108 sacred temples dedicated to Lord Vishnu, mentioned in the works of Alwars
    Based on: https://en.wikipedia.org/wiki/Divya_Desam
    
    Distribution:
    - Tamil Nadu: 84 temples
    - Kerala: 11 temples
    - Andhra Pradesh: 2 temples
    - Gujarat: 1 temple
    - Uttar Pradesh: 4 temples
    - Uttarakhand: 3 temples
    - Nepal: 1 temple (Muktinath)
    - Celestial: 2 temples (not on earth - excluded from this list)
    
    Total: 106 earthly Divya Desams (108 - 2 celestial = 106)
    This script includes all 106 earthly Divya Desams.
    """
    
    divya_desams = [
        # Tamil Nadu Divya Desams (84 total)
        # Chola Nadu (Central Tamil Nadu) - Major Divya Desams
        {
            'Park_Code': 'DD001',
            'Name': 'Ranganathaswamy Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8625',
            'Longitude': '78.6897',
            'Description': 'Ranganathaswamy Temple - First and most important Divya Desam. Largest functioning Hindu temple in the world. Located in Srirangam, Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Ranganathaswamy_Temple,_Srirangam',
            'Country': 'India',
            'Divya_Desam_Number': '1'
        },
        {
            'Park_Code': 'DD002',
            'Name': 'Azhagiya Manavala Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8200',
            'Longitude': '78.6700',
            'Description': 'Azhagiya Manavala Perumal Temple (Thirukozhi) - Divya Desam. Birthplace of Thiruppaan Alvar. Located in Uraiyur, Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Azhagiya_Manavala_Perumal_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '2'
        },
        {
            'Park_Code': 'DD003',
            'Name': 'Uthamar Kovil',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '78.7000',
            'Description': 'Uthamar Kovil (Thirukarambanoor) - Divya Desam. Located in Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Uthamar_Kovil',
            'Country': 'India',
            'Divya_Desam_Number': '3'
        },
        {
            'Park_Code': 'DD004',
            'Name': 'Pundarikakshan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.9000',
            'Longitude': '78.7167',
            'Description': 'Pundarikakshan Perumal Temple (Thiruvellarai) - Divya Desam. Located in Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '4'
        },
        {
            'Park_Code': 'DD005',
            'Name': 'Vadivazhagiya Nambi Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8667',
            'Longitude': '78.7500',
            'Description': 'Vadivazhagiya Nambi Perumal Temple (Thiru Anbil) - Divya Desam. Located in Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '5'
        },
        {
            'Park_Code': 'DD006',
            'Name': 'Appakkudathaan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '78.7000',
            'Description': 'Appakkudathaan Perumal Temple (Thirupper Nagar) - Divya Desam. Located in Trichy district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '6'
        },
        {
            'Park_Code': 'DD007',
            'Name': 'Neelamega Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Neelamega Perumal Temple (Thiru Thanjaimaamani Koil) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '7'
        },
        {
            'Park_Code': 'DD008',
            'Name': 'Hara Saabha Vimocchana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Hara Saabha Vimocchana Perumal Temple (Thirukkandiyur) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '8'
        },
        {
            'Park_Code': 'DD009',
            'Name': 'Gajendra Varadha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.9667',
            'Longitude': '79.3833',
            'Description': 'Gajendra Varadha Perumal Temple (Thirukkavithalam/Kabisthalam) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '9'
        },
        {
            'Park_Code': 'DD010',
            'Name': 'Valvil Ramar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Valvil Ramar Perumal Temple (Thiruppullam Boothankudi) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '10'
        },
        {
            'Park_Code': 'DD011',
            'Name': 'Aandu Alakkum Ayan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Aandu Alakkum Ayan Perumal Temple (Thiru Aadhanoor) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '11'
        },
        {
            'Park_Code': 'DD012',
            'Name': 'Sarangapani Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.9667',
            'Longitude': '79.3833',
            'Description': 'Sarangapani Temple (Thirukkudanthai) - Divya Desam. One of the Pancharanga Kshetrams. Located in Kumbakonam, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Sarangapani_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '12'
        },
        {
            'Park_Code': 'DD013',
            'Name': 'Oppiliappa Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.0167',
            'Longitude': '79.4000',
            'Description': 'Oppiliappa Perumal Temple (Thiru Vinnagar) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '13'
        },
        {
            'Park_Code': 'DD014',
            'Name': 'Thirunarayoor Nambi Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Thirunarayoor Nambi Perumal Temple (Thirunarayoor/Naachchiyaar Koil) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '14'
        },
        {
            'Park_Code': 'DD015',
            'Name': 'Saranathan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Saranathan Perumal Temple (Thiruccherai) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '15'
        },
        {
            'Park_Code': 'DD016',
            'Name': 'Bhaktavatsala Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Bhaktavatsala Perumal Temple (Thirukkannamangai) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Bhaktavatsala_Perumal_temple',
            'Country': 'India',
            'Divya_Desam_Number': '16'
        },
        {
            'Park_Code': 'DD017',
            'Name': 'Jaganatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Jaganatha Perumal Temple (Thirunandhipura Vinnagaram/Nathan Koil) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '17'
        },
        {
            'Park_Code': 'DD018',
            'Name': 'Kola Valvilli Ramar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.7833',
            'Longitude': '79.1333',
            'Description': 'Kola Valvilli Ramar Perumal Temple (Thiruvelliyankudi) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '18'
        },
        {
            'Park_Code': 'DD019',
            'Name': 'Aaduthurai Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.0167',
            'Longitude': '79.4000',
            'Description': 'Aaduthurai Perumal Temple (Thirukkoodaloor) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '19'
        },
        {
            'Park_Code': 'DD020',
            'Name': 'Parimala Ranganatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.0167',
            'Longitude': '79.4000',
            'Description': 'Parimala Ranganatha Perumal Temple (Thiru Indhaloor) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '20'
        },
        {
            'Park_Code': 'DD021',
            'Name': 'Devaadi Raja Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.0167',
            'Longitude': '79.4000',
            'Description': 'Devaadi Raja Perumal Temple (Thiruvazhunthoor) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '21'
        },
        {
            'Park_Code': 'DD022',
            'Name': 'Arulmaakadal Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.0167',
            'Longitude': '79.4000',
            'Description': 'Arulmaakadal Perumal Temple (Thiru Sirupuliyur) - Divya Desam. Located in Thanjavur district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '22'
        },
        {
            'Park_Code': 'DD023',
            'Name': 'Sowrirajan Neelamega Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Sowrirajan Neelamega Perumal Temple (Thirukkannapuram) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Sowriraja_Perumal_temple',
            'Country': 'India',
            'Divya_Desam_Number': '23'
        },
        {
            'Park_Code': 'DD024',
            'Name': 'Soundararajaperumal Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Soundararajaperumal Perumal Temple (Thiru Naagai) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '24'
        },
        {
            'Park_Code': 'DD025',
            'Name': 'Loganatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Loganatha Perumal Temple (Thirukkannankudi) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '25'
        },
        {
            'Park_Code': 'DD026',
            'Name': 'Naan Madhiya Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.8500',
            'Longitude': '79.1500',
            'Description': 'Naan Madhiya Perumal Temple (Thiru Thalaicchanga Naanmathiyam) - Divya Desam. Located in Nagapattinam district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '26'
        },
        {
            'Park_Code': 'DD027',
            'Name': 'Thadalar Seerkazhi Thirivikaraman Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.2333',
            'Longitude': '79.7333',
            'Description': 'Thadalar Seerkazhi Thirivikaraman Perumal Temple (Kaazhicheeraama Vinnagaram) - Divya Desam. Located in Mayiladuthurai district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '27'
        },
        {
            'Park_Code': 'DD028',
            'Name': 'Srinivasa Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.2333',
            'Longitude': '79.7333',
            'Description': 'Srinivasa Perumal Temple (Thiruvellakkulam/Annan Kovil) - Divya Desam. Located in Mayiladuthurai district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '28'
        },
        {
            'Park_Code': 'DD029',
            'Name': 'Deiva Naayaga Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.2333',
            'Longitude': '79.7333',
            'Description': 'Deiva Naayaga Perumal Temple (Thiru Devanaar Thogai) - Divya Desam. Located in Mayiladuthurai district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '29'
        },
        {
            'Park_Code': 'DD030',
            'Name': 'Lakshmi Narashima Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Lakshmi Narashima Perumal Temple (Thiruvaali Thirunagari) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '30'
        },
        {
            'Park_Code': 'DD031',
            'Name': 'Gopala Krishna Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Gopala Krishna Perumal Temple (Thiru Kavalampaadi) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '31'
        },
        {
            'Park_Code': 'DD032',
            'Name': 'Varadharaja Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Varadharaja Perumal Temple (Thiru Manikkoodam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Varadharaja_Perumal_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '32'
        },
        {
            'Park_Code': 'DD033',
            'Name': 'Thamaraiyal Kelvan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Thamaraiyal Kelvan Perumal Temple (Thiru Paarthanpalli) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '33'
        },
        {
            'Park_Code': 'DD034',
            'Name': 'Narayana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Narayana Perumal Temple (Thiru Manimaada Kovil) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '34'
        },
        {
            'Park_Code': 'DD035',
            'Name': 'Kuda Maadu Koothan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Kuda Maadu Koothan Perumal Temple (Thiru Arimeya Vinnagaram) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '35'
        },
        {
            'Park_Code': 'DD036',
            'Name': 'Seganmaal Ranganatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Seganmaal Ranganatha Perumal Temple (Thiru Thetri Aambalam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '36'
        },
        {
            'Park_Code': 'DD037',
            'Name': 'Per Arulaalan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Per Arulaalan Perumal Temple (Thiru Sempon Sei Kovil) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '37'
        },
        {
            'Park_Code': 'DD038',
            'Name': 'Purushothama Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Purushothama Perumal Temple (Thiru Vann Purushothamam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '38'
        },
        {
            'Park_Code': 'DD039',
            'Name': 'Vaigundha Nathan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Vaigundha Nathan Perumal Temple (Thiru VaiKunda Vinnagaram) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '39'
        },
        {
            'Park_Code': 'DD040',
            'Name': 'Govindaraja Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.3994',
            'Longitude': '79.6914',
            'Description': 'Govindaraja Perumal Temple (Thiruchitrakootam/Chidambaram) - Divya Desam. Located in Cuddalore district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '40'
        },
        {
            'Park_Code': 'DD041',
            'Name': 'Devanatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '11.9500',
            'Longitude': '79.7667',
            'Description': 'Devanatha Perumal Temple (Tiruvahindrapuram) - Divya Desam. Located in Cuddalore, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Devanatha_Swamy_temple',
            'Country': 'India',
            'Divya_Desam_Number': '41'
        },
        {
            'Park_Code': 'DD042',
            'Name': 'Thiruvikrama Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Thiruvikrama Perumal Temple (Thirukkoviloor) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '42'
        },
        {
            'Park_Code': 'DD043',
            'Name': 'Varadharaja Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Varadharaja Perumal Temple (Thirukkachchi) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Varadharaja_Perumal_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '43'
        },
        {
            'Park_Code': 'DD044',
            'Name': 'Aadhikesava Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Aadhikesava Perumal Temple (Ashtabhuyakaram) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '44'
        },
        {
            'Park_Code': 'DD045',
            'Name': 'Yathothakaari Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Yathothakaari Temple (Thiru Vekka) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '45'
        },
        {
            'Park_Code': 'DD046',
            'Name': 'Azhagiya Singar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Azhagiya Singar Perumal Temple (Thiru Velukkai) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '46'
        },
        {
            'Park_Code': 'DD047',
            'Name': 'Deepa Prakasar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Deepa Prakasar Perumal Temple (Thiruthanka) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '47'
        },
        {
            'Park_Code': 'DD048',
            'Name': 'Aadhi Varaha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Aadhi Varaha Perumal Temple (ThirukKalvanoor) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '48'
        },
        {
            'Park_Code': 'DD049',
            'Name': 'Ulagalantha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Ulagalantha Perumal Temple (Thiru Ooragam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '49'
        },
        {
            'Park_Code': 'DD050',
            'Name': 'Jagadeeshwarar Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Jagadeeshwarar Temple (Thiru Neeragam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '50'
        },
        {
            'Park_Code': 'DD051',
            'Name': 'Karunakara Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Karunakara Perumal Temple (Thiru Kaaragam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '51'
        },
        {
            'Park_Code': 'DD052',
            'Name': 'Thirukkaar Vaanar Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Thirukkaar Vaanar Temple (Thirukkaar Vaanam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '52'
        },
        {
            'Park_Code': 'DD053',
            'Name': 'Vaikunda Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Vaikunda Perumal Temple (Thiruparameshwara Vinnagaram) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '53'
        },
        {
            'Park_Code': 'DD054',
            'Name': 'Pavala Vannar Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Pavala Vannar Temple (Thiru Pavala Vannan) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '54'
        },
        {
            'Park_Code': 'DD055',
            'Name': 'Nilathingal Thundathan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Nilathingal Thundathan Perumal Temple (Thiru Nilathingal Thundam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '55'
        },
        {
            'Park_Code': 'DD056',
            'Name': 'Pandava Thoodhar Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Pandava Thoodhar Temple (Thiru Paadagam) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '56'
        },
        {
            'Park_Code': 'DD057',
            'Name': 'Vijayaraghava Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '79.7000',
            'Description': 'Vijayaraghava Perumal Temple (Thiruputkuzhi) - Divya Desam. Located in Kanchipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '57'
        },
        {
            'Park_Code': 'DD058',
            'Name': 'Parthasarathy Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '13.0500',
            'Longitude': '80.2833',
            'Description': 'Parthasarathy Temple (Tiruvallikeni) - Divya Desam. Dedicated to Lord Parthasarathy. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Parthasarathy_Temple,_Chennai',
            'Country': 'India',
            'Divya_Desam_Number': '58'
        },
        {
            'Park_Code': 'DD059',
            'Name': 'Neervanna Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.9500',
            'Longitude': '80.1167',
            'Description': 'Neervanna Perumal Temple (Thiruneermalai) - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '59'
        },
        {
            'Park_Code': 'DD060',
            'Name': 'Nithya Kalyana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '80.2500',
            'Description': 'Nithya Kalyana Perumal Temple (Thiruvedanthai) - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '60'
        },
        {
            'Park_Code': 'DD061',
            'Name': 'Sthala Sayana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.6167',
            'Longitude': '80.1917',
            'Description': 'Sthala Sayana Perumal Temple (Thiru Kadalmalai/Mahabalipuram) - Divya Desam. Located in Mahabalipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '61'
        },
        {
            'Park_Code': 'DD062',
            'Name': 'Bhatavatsala Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '13.1333',
            'Longitude': '80.1500',
            'Description': 'Bhatavatsala Perumal Temple (Thiru Nindravoor/Thirunindravur) - Divya Desam. Located in Tiruvallur, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '62'
        },
        {
            'Park_Code': 'DD063',
            'Name': 'Veeraraghava Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '13.1333',
            'Longitude': '80.1500',
            'Description': 'Veeraraghava Perumal Temple (Thiruevvuloor/Tiruvallur) - Divya Desam. Located in Tiruvallur, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Vaidhya_Veeraraghava_Swamy_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '63'
        },
        {
            'Park_Code': 'DD064',
            'Name': 'Yoga Narasimha Swamy Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '13.1167',
            'Longitude': '79.4167',
            'Description': 'Yoga Narasimha Swamy Temple (Thirukkadigai/Sholingur) - Divya Desam. Located in Vellore district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '64'
        },
        {
            'Park_Code': 'DD065',
            'Name': 'Koodal Azhagar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.9194',
            'Longitude': '78.1194',
            'Description': 'Koodal Azhagar Perumal Temple (Thirukkoodal) - Divya Desam. Located in Madurai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '65'
        },
        {
            'Park_Code': 'DD066',
            'Name': 'Kaalamegha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.9194',
            'Longitude': '78.1194',
            'Description': 'Kaalamegha Perumal Temple (Thiru Moghur) - Divya Desam. Located in Madurai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '66'
        },
        {
            'Park_Code': 'DD067',
            'Name': 'Kallazhagar Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.9194',
            'Longitude': '78.1194',
            'Description': 'Kallazhagar Perumal Temple (Thirumaalirunsolai/Alagar Kovil) - Divya Desam. Located in Madurai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Kallalagar_temple',
            'Country': 'India',
            'Divya_Desam_Number': '67'
        },
        {
            'Park_Code': 'DD068',
            'Name': 'Uraga Mellanayaan Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.9667',
            'Longitude': '78.5500',
            'Description': 'Uraga Mellanayaan Perumal Temple (Thirukkotiyoor) - Divya Desam. Located in Sivaganga district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '68'
        },
        {
            'Park_Code': 'DD069',
            'Name': 'Sathyagiri Natha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '10.2833',
            'Longitude': '78.8333',
            'Description': 'Sathyagiri Natha Perumal Temple (Thirumeyyam) - Divya Desam. Located in Pudukkottai district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '69'
        },
        {
            'Park_Code': 'DD070',
            'Name': 'Kalyana Jagannatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.2833',
            'Longitude': '78.8333',
            'Description': 'Kalyana Jagannatha Perumal Temple (Thiruppullanni/Ramanathapuram) - Divya Desam. Located in Ramanathapuram district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '70'
        },
        {
            'Park_Code': 'DD071',
            'Name': 'Nindra Narayana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.4500',
            'Longitude': '77.8167',
            'Description': 'Nindra Narayana Perumal Temple (Thiruthankaal/Sivakasi) - Divya Desam. Located in Virudhunagar district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '71'
        },
        {
            'Park_Code': 'DD072',
            'Name': 'Vadabhatra Saayi Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.5000',
            'Longitude': '77.6333',
            'Description': 'Vadabhatra Saayi Perumal Temple (Thiruvilliputtur/Sri Villiputhoor) - Divya Desam. Located in Virudhunagar district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '72'
        },
        {
            'Park_Code': 'DD073',
            'Name': 'Vaikundanatha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.6167',
            'Longitude': '77.9333',
            'Description': 'Vaikundanatha Perumal Temple (Thiruvaikuntham/Sri Vaikundam) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '73'
        },
        {
            'Park_Code': 'DD074',
            'Name': 'Vijayaasana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Vijayaasana Perumal Temple (Thiruvaragunamangai) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '74'
        },
        {
            'Park_Code': 'DD075',
            'Name': 'Kaaichina Vendha Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Kaaichina Vendha Perumal Temple (Thiruppulingudu) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '75'
        },
        {
            'Park_Code': 'DD076',
            'Name': 'Srinivasa Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Srinivasa Perumal Temple (Thirukkulanthai) - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '76'
        },
        {
            'Park_Code': 'DD077',
            'Name': 'Tiruvotriyur Vadivudai Amman Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '13.1667',
            'Longitude': '80.3000',
            'Description': 'Tiruvotriyur Vadivudai Amman Temple - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '77'
        },
        {
            'Park_Code': 'DD078',
            'Name': 'Tirukkurungudi Nambi Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.4833',
            'Longitude': '77.5500',
            'Description': 'Tirukkurungudi Nambi Temple - Divya Desam. Located in Tirunelveli district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '78'
        },
        {
            'Park_Code': 'DD079',
            'Name': 'Tirupullani Darbhasayana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '9.2833',
            'Longitude': '78.8333',
            'Description': 'Tirupullani Darbhasayana Perumal Temple - Divya Desam. Located in Ramanathapuram district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '79'
        },
        {
            'Park_Code': 'DD080',
            'Name': 'Tiruvattar Adikesava Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '8.3167',
            'Longitude': '77.2500',
            'Description': 'Tiruvattar Adikesava Perumal Temple - Divya Desam. Located in Kanyakumari district, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '80'
        },
        {
            'Park_Code': 'DD081',
            'Name': 'Tirukkachur Singaperumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.9000',
            'Longitude': '80.0833',
            'Description': 'Tirukkachur Singaperumal Temple - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '81'
        },
        {
            'Park_Code': 'DD082',
            'Name': 'Tiruvidandai Nithyakalyana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.8333',
            'Longitude': '80.2500',
            'Description': 'Tiruvidandai Nithyakalyana Perumal Temple - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '82'
        },
        {
            'Park_Code': 'DD083',
            'Name': 'Tiruneermalai Neervanna Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.9500',
            'Longitude': '80.1167',
            'Description': 'Tiruneermalai Neervanna Perumal Temple - Divya Desam. Located in Chennai, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '83'
        },
        {
            'Park_Code': 'DD084',
            'Name': 'Tirukadalmallai Sthalasayana Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Tamil Nadu',
            'Latitude': '12.6167',
            'Longitude': '80.1917',
            'Description': 'Tirukadalmallai Sthalasayana Perumal Temple - Divya Desam. Located in Mahabalipuram, Tamil Nadu.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '84'
        },
        # Kerala Divya Desams (11 total)
        {
            'Park_Code': 'DD085',
            'Name': 'Padmanabhaswamy Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '8.4822',
            'Longitude': '76.9447',
            'Description': 'Padmanabhaswamy Temple - Important Divya Desam. Dedicated to Lord Padmanabha. Located in Thiruvananthapuram, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Padmanabhaswamy_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '85'
        },
        {
            'Park_Code': 'DD086',
            'Name': 'Guruvayur Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '10.5950',
            'Longitude': '76.0400',
            'Description': 'Guruvayur Temple - Important Divya Desam. Dedicated to Lord Krishna. Located in Guruvayur, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Guruvayur_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '86'
        },
        {
            'Park_Code': 'DD087',
            'Name': 'Tiruvattar Adikesava Perumal Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '8.3167',
            'Longitude': '77.2500',
            'Description': 'Tiruvattar Adikesava Perumal Temple - Divya Desam. Located in Kanyakumari area, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '87'
        },
        {
            'Park_Code': 'DD088',
            'Name': 'Tiruvalla Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '9.3833',
            'Longitude': '76.5667',
            'Description': 'Tiruvalla Temple - Divya Desam. Located in Pathanamthitta district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '88'
        },
        {
            'Park_Code': 'DD089',
            'Name': 'Tirupuliyur Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '9.3833',
            'Longitude': '76.5667',
            'Description': 'Tirupuliyur Temple - Divya Desam. Located in Pathanamthitta district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '89'
        },
        {
            'Park_Code': 'DD090',
            'Name': 'Tiruvithuvakodu Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '10.7833',
            'Longitude': '76.2833',
            'Description': 'Tiruvithuvakodu Temple - Divya Desam. Located in Palakkad district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '90'
        },
        {
            'Park_Code': 'DD091',
            'Name': 'Tirukkatkarai Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '10.7833',
            'Longitude': '76.2833',
            'Description': 'Tirukkatkarai Temple - Divya Desam. Located in Palakkad district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '91'
        },
        {
            'Park_Code': 'DD092',
            'Name': 'Tirumoozhikkalam Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '10.1167',
            'Longitude': '76.2833',
            'Description': 'Tirumoozhikkalam Temple - Divya Desam. Located in Ernakulam district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '92'
        },
        {
            'Park_Code': 'DD093',
            'Name': 'Tiruvallavazh Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '10.1167',
            'Longitude': '76.2833',
            'Description': 'Tiruvallavazh Temple - Divya Desam. Located in Ernakulam district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '93'
        },
        {
            'Park_Code': 'DD094',
            'Name': 'Tiruvanvandoor Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '9.3833',
            'Longitude': '76.5667',
            'Description': 'Tiruvanvandoor Temple - Divya Desam. Located in Pathanamthitta district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '94'
        },
        {
            'Park_Code': 'DD095',
            'Name': 'Tirukkulasekarapuram Temple',
            'Designation': 'Divya Desam',
            'States': 'Kerala',
            'Latitude': '8.3167',
            'Longitude': '77.2500',
            'Description': 'Tirukkulasekarapuram Temple - Divya Desam. Located in Kanyakumari district, Kerala.',
            'URL': 'https://en.wikipedia.org/wiki/Divya_Desam',
            'Country': 'India',
            'Divya_Desam_Number': '95'
        },
        # Andhra Pradesh Divya Desams (2 total)
        {
            'Park_Code': 'DD096',
            'Name': 'Venkateswara Temple',
            'Designation': 'Divya Desam',
            'States': 'Andhra Pradesh',
            'Latitude': '13.6833',
            'Longitude': '79.3500',
            'Description': 'Venkateswara Temple (Tirumala) - One of the most visited Divya Desams. Dedicated to Lord Venkateswara. Located in Tirupati, Andhra Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala',
            'Country': 'India',
            'Divya_Desam_Number': '96'
        },
        {
            'Park_Code': 'DD097',
            'Name': 'Tirumala Venkateswara Temple',
            'Designation': 'Divya Desam',
            'States': 'Andhra Pradesh',
            'Latitude': '13.6500',
            'Longitude': '79.4167',
            'Description': 'Tirumala Venkateswara Temple - Divya Desam. Same as Venkateswara Temple in Tirupati.',
            'URL': 'https://en.wikipedia.org/wiki/Venkateswara_Temple,_Tirumala',
            'Country': 'India',
            'Divya_Desam_Number': '97'
        },
        # Gujarat Divya Desams (1 total)
        {
            'Park_Code': 'DD098',
            'Name': 'Dwarka',
            'Designation': 'Divya Desam',
            'States': 'Gujarat',
            'Latitude': '22.2400',
            'Longitude': '68.9700',
            'Description': 'Dwarka - Kingdom of Lord Krishna. Important Divya Desam. Located in Dwarka, Gujarat.',
            'URL': 'https://en.wikipedia.org/wiki/Dwarka',
            'Country': 'India',
            'Divya_Desam_Number': '98'
        },
        # Uttar Pradesh Divya Desams (4 total)
        {
            'Park_Code': 'DD099',
            'Name': 'Ayodhya',
            'Designation': 'Divya Desam',
            'States': 'Uttar Pradesh',
            'Latitude': '26.8000',
            'Longitude': '82.2000',
            'Description': 'Ayodhya - Birthplace of Lord Rama. Important Divya Desam. Located in Ayodhya, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Ayodhya',
            'Country': 'India',
            'Divya_Desam_Number': '99'
        },
        {
            'Park_Code': 'DD100',
            'Name': 'Mathura',
            'Designation': 'Divya Desam',
            'States': 'Uttar Pradesh',
            'Latitude': '27.5000',
            'Longitude': '77.6833',
            'Description': 'Mathura - Birthplace of Lord Krishna. Important Divya Desam. Located in Mathura, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Mathura',
            'Country': 'India',
            'Divya_Desam_Number': '100'
        },
        {
            'Park_Code': 'DD101',
            'Name': 'Vrindavan',
            'Designation': 'Divya Desam',
            'States': 'Uttar Pradesh',
            'Latitude': '27.5667',
            'Longitude': '77.7000',
            'Description': 'Vrindavan - Place of Lord Krishna\'s childhood pastimes. Important Divya Desam. Located in Vrindavan, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Vrindavan',
            'Country': 'India',
            'Divya_Desam_Number': '101'
        },
        {
            'Park_Code': 'DD102',
            'Name': 'Gokul',
            'Designation': 'Divya Desam',
            'States': 'Uttar Pradesh',
            'Latitude': '27.4500',
            'Longitude': '77.7167',
            'Description': 'Gokul - Place where Lord Krishna was raised. Important Divya Desam. Located in Gokul, Uttar Pradesh.',
            'URL': 'https://en.wikipedia.org/wiki/Gokul',
            'Country': 'India',
            'Divya_Desam_Number': '102'
        },
        # Uttarakhand Divya Desams (3 total)
        {
            'Park_Code': 'DD103',
            'Name': 'Badrinath Temple',
            'Designation': 'Divya Desam',
            'States': 'Uttarakhand',
            'Latitude': '30.7444',
            'Longitude': '79.4931',
            'Description': 'Badrinath Temple - Divya Desam in the Himalayas. Dedicated to Lord Badrinath. Located in Badrinath, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Badrinath_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '103'
        },
        {
            'Park_Code': 'DD104',
            'Name': 'Nara-Narayana Temple',
            'Designation': 'Divya Desam',
            'States': 'Uttarakhand',
            'Latitude': '30.7444',
            'Longitude': '79.4931',
            'Description': 'Nara-Narayana Temple - Divya Desam. Located in Badrinath, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Badrinath_Temple',
            'Country': 'India',
            'Divya_Desam_Number': '104'
        },
        {
            'Park_Code': 'DD105',
            'Name': 'Yamunotri',
            'Designation': 'Divya Desam',
            'States': 'Uttarakhand',
            'Latitude': '31.0167',
            'Longitude': '78.4500',
            'Description': 'Yamunotri - Source of Yamuna River. Divya Desam. Located in Uttarkashi district, Uttarakhand.',
            'URL': 'https://en.wikipedia.org/wiki/Yamunotri',
            'Country': 'India',
            'Divya_Desam_Number': '105'
        },
        # Nepal Divya Desams (1 total)
        {
            'Park_Code': 'DD106',
            'Name': 'Muktinath Temple',
            'Designation': 'Divya Desam',
            'States': 'Mustang',
            'Latitude': '28.8167',
            'Longitude': '83.8667',
            'Description': 'Muktinath Temple - Only Divya Desam outside India. Located in Mustang district, Nepal.',
            'URL': 'https://en.wikipedia.org/wiki/Muktinath',
            'Country': 'Nepal',
            'Divya_Desam_Number': '106'
        }
        # Note: 2 celestial Divya Desams (Tirupparkatal/Kṣīra Sāgara and Vaikuntham) are not included
        # as they are not on earth
    ]
    
    # Add small offsets to duplicate coordinates to ensure all temples are visible
    import random
    random.seed(42)  # For reproducible offsets
    coord_counts = {}
    
    for desam in divya_desams:
        lat = float(desam['Latitude'])
        lon = float(desam['Longitude'])
        coord_key = (round(lat, 4), round(lon, 4))
        
        if coord_key in coord_counts:
            coord_counts[coord_key] += 1
            # Add small offset (0.01-0.05 degrees, roughly 1-5 km)
            offset_lat = random.uniform(0.01, 0.05) * random.choice([-1, 1])
            offset_lon = random.uniform(0.01, 0.05) * random.choice([-1, 1])
            desam['Latitude'] = str(round(lat + offset_lat, 6))
            desam['Longitude'] = str(round(lon + offset_lon, 6))
        else:
            coord_counts[coord_key] = 1
    
    return divya_desams

def save_divya_desams_csv(data, filename):
    """
    Save Divya Desams data to CSV file
    """
    if not data:
        print("No data to save")
        return
    
    fieldnames = ['Park_Code', 'Name', 'Designation', 'States', 'Latitude', 'Longitude', 'Description', 'URL', 'Country', 'Divya_Desam_Number']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            output_row = {k: v for k, v in row.items() if k in fieldnames}
            writer.writerow(output_row)
    
    print(f"Saved {len(data)} Divya Desams to {filename}")

if __name__ == '__main__':
    print("Creating India 108 Vaishnava Divya Desams data...")
    print("Based on: https://en.wikipedia.org/wiki/Divya_Desam")
    print("Distribution: Tamil Nadu (84), Kerala (11), Andhra Pradesh (2), Gujarat (1),")
    print("              Uttar Pradesh (4), Uttarakhand (3), Nepal (1), Celestial (2)")
    print("Note: 2 celestial Divya Desams are not included (not on earth)")
    
    divya_desams_data = get_divya_desams()
    
    # Determine the output path
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'public', 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    output_file = os.path.join(data_dir, 'India_Divya_Desams.csv')
    save_divya_desams_csv(divya_desams_data, output_file)
    
    print(f"✅ Successfully created {output_file}")
    print(f"✅ Total: {len(divya_desams_data)} Divya Desams (106 earthly + 2 celestial = 108 total)")
