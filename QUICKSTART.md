# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Development Server
```bash
npm run dev
```

### 3. Open in Browser
The app will automatically open at `http://localhost:3000`

## 📋 What You Get

- ✅ Interactive map with world attractions (parks, temples, UNESCO sites)
- ✅ Multi-country support (USA, Canada, India, Nepal, Sri Lanka, Costa Rica)
- ✅ Regional filtering by country and region
- ✅ Statistics dashboard
- ✅ Attraction details with nearby airports and attractions
- ✅ Responsive design for all devices

## 🔧 Next Steps

### Update Data (Optional)
```bash
npm run download-data
```

### Build for Production
```bash
npm run build
```

## 📁 Project Structure

- `src/` - React source code
- `public/data/` - CSV data files
- `scripts/` - Python scripts for data management
- `data/` - Original data files (backup)

## 🎯 Key Features

1. **Map View**: Interactive Leaflet map showing all world attractions
2. **Statistics Tab**: View attraction counts by country, region, state, and province
3. **Filters Tab**: Toggle countries and regions to show/hide attractions
4. **Attraction Popups**: Click any marker for detailed information

## 🐛 Troubleshooting

### Data not loading?
- Check that CSV files are in `public/data/`
- Run `npm run download-data` to refresh data

### Port already in use?
- Change port in `vite.config.js`
- Or kill the process using port 3000

### Build errors?
- Run `npm install` again
- Check Node.js version (requires v16+)

## 📚 Learn More

See `README.md` for complete documentation.

