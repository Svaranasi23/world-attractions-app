/**
 * Script to update UNESCO_SUMMARY.md with current site counts
 * Run with: node scripts/update_unesco_summary.js
 */

const fs = require('fs');
const path = require('path');
const Papa = require('papaparse');

const dataDir = path.join(__dirname, '../public/data');
const summaryFile = path.join(__dirname, '../UNESCO_SUMMARY.md');

// Country to region mapping
const countryRegions = {
  // Central America
  'Belize': 'Central America',
  'Guatemala': 'Central America',
  'Honduras': 'Central America',
  'El Salvador': 'Central America',
  'Nicaragua': 'Central America',
  'Panama': 'Central America',
  'Mexico': 'Central America',
  'Costa Rica': 'Central America',
  
  // Southern Asia
  'India': 'Southern Asia',
  'Nepal': 'Southern Asia',
  'Sri Lanka': 'Southern Asia',
  'Bangladesh': 'Southern Asia',
  'Pakistan': 'Southern Asia',
  'Afghanistan': 'Southern Asia',
  'Bhutan': 'Southern Asia',
  'Maldives': 'Southern Asia',
  
  // South-eastern Asia
  'Thailand': 'South-eastern Asia',
  'Indonesia': 'South-eastern Asia',
  'Vietnam': 'South-eastern Asia',
  'Cambodia': 'South-eastern Asia',
  'Myanmar': 'South-eastern Asia',
  'Philippines': 'South-eastern Asia',
  'Malaysia': 'South-eastern Asia',
  'Singapore': 'South-eastern Asia',
  'Laos': 'South-eastern Asia',
  'Brunei': 'South-eastern Asia',
  'East Timor': 'South-eastern Asia',
  
  // Eastern Asia
  'China': 'Eastern Asia',
  'Japan': 'Eastern Asia',
  'South Korea': 'Eastern Asia',
  'North Korea': 'Eastern Asia',
  'Mongolia': 'Eastern Asia',
  
  // Central Asia
  'Kazakhstan': 'Central Asia',
  'Kyrgyzstan': 'Central Asia',
  'Tajikistan': 'Central Asia',
  'Turkmenistan': 'Central Asia',
  'Uzbekistan': 'Central Asia',
  
  // Western Asia
  'Iran': 'Western Asia',
  'Iraq': 'Western Asia',
  'Jordan': 'Western Asia',
  'Lebanon': 'Western Asia',
  'Saudi Arabia': 'Western Asia',
  'Syria': 'Western Asia',
  'Turkey': 'Western Asia',
  'UAE': 'Western Asia',
  'Yemen': 'Western Asia',
  'Oman': 'Western Asia',
  'Qatar': 'Western Asia',
  'Kuwait': 'Western Asia',
  'Bahrain': 'Western Asia',
  'Israel': 'Western Asia',
  'Palestine': 'Western Asia',
};

function countSitesInFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.trim().split('\n');
    // Subtract 1 for header, but only if there are data rows
    return Math.max(0, lines.length - 1);
  } catch (error) {
    return 0;
  }
}

function getCountryFromFilename(filename) {
  // Extract country name from filename like "Iran_UNESCO_Sites.csv"
  const match = filename.match(/^(.+)_UNESCO_Sites\.csv$/);
  if (match) {
    return match[1].replace(/_/g, ' ');
  }
  return null;
}

function updateSummary() {
  const files = fs.readdirSync(dataDir);
  const unescoFiles = files.filter(f => f.endsWith('_UNESCO_Sites.csv'));
  
  const counts = {
    'Central America': {},
    'Southern Asia': {},
    'South-eastern Asia': {},
    'Eastern Asia': {},
    'Central Asia': {},
    'Western Asia': {},
  };
  
  let totalSites = 0;
  
  unescoFiles.forEach(file => {
    const filePath = path.join(dataDir, file);
    const country = getCountryFromFilename(file);
    const siteCount = countSitesInFile(filePath);
    
    if (country && siteCount > 0) {
      const region = countryRegions[country] || 'Other';
      if (counts[region]) {
        counts[region][country] = siteCount;
        totalSites += siteCount;
      }
    }
  });
  
  // Generate updated summary
  console.log('UNESCO Site Counts by Region:');
  console.log('=============================\n');
  
  Object.keys(counts).forEach(region => {
    const regionCounts = counts[region];
    const regionTotal = Object.values(regionCounts).reduce((a, b) => a + b, 0);
    if (regionTotal > 0) {
      console.log(`${region}: ${regionTotal} sites`);
      Object.keys(regionCounts).sort().forEach(country => {
        console.log(`  - ${country}: ${regionCounts[country]} sites`);
      });
      console.log('');
    }
  });
  
  console.log(`Total UNESCO Sites: ${totalSites}`);
  
  return { counts, totalSites };
}

// Run if called directly
if (require.main === module) {
  updateSummary();
}

module.exports = { updateSummary, countSitesInFile };

