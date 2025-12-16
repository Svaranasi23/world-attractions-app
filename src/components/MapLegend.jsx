import React, { useState, useMemo } from 'react'
import './MapLegend.css'

function MapLegend({ visibleRegions, regions, showAirports, airports, currentMapView }) {
  const [isOpen, setIsOpen] = useState(false)

  // Determine if we're in a country-focused view (India, Nepal, or Sri Lanka)
  const indiaRegionsVisible = visibleRegions && (
    visibleRegions['India-Parks'] === true || 
    visibleRegions['India-UNESCO'] === true || 
    visibleRegions['India-Jyotirlinga'] === true || 
    visibleRegions['India-ShaktiPeetha'] === true || 
    visibleRegions['India-OtherTemples'] === true || 
    visibleRegions['India-Matham'] === true || 
    visibleRegions['India-DivyaDesam'] === true || 
    visibleRegions['India-Forts'] === true
  )
  
  const nepalRegionsVisible = visibleRegions && (
    visibleRegions['Nepal-Parks'] === true || 
    visibleRegions['Nepal-Temples'] === true || 
    visibleRegions['Nepal-UNESCO'] === true || 
    visibleRegions['Nepal-TrekkingFlights'] === true
  )
  
  const sriLankaRegionsVisible = visibleRegions && (
    visibleRegions['Sri Lanka-Parks'] === true || 
    visibleRegions['Sri Lanka-Temples'] === true || 
    visibleRegions['Sri Lanka-UNESCO'] === true
  )
  
  // Check if map is showing the whole world (low zoom level)
  const isWorldView = !currentMapView || !currentMapView.zoom || currentMapView.zoom <= 3
  
  // Check if map is zoomed into India, Nepal, or Sri Lanka based on center and zoom
  const isMapZoomedIntoIndia = currentMapView && 
                               currentMapView.center && 
                               currentMapView.zoom >= 4 &&
                               !isWorldView &&
                               currentMapView.center.lat >= 6.0 && currentMapView.center.lat <= 37.0 &&
                               currentMapView.center.lng >= 68.0 && currentMapView.center.lng <= 97.0
  
  const isMapZoomedIntoNepal = currentMapView && 
                               currentMapView.center && 
                               currentMapView.zoom >= 5 &&
                               !isWorldView &&
                               currentMapView.center.lat >= 26.0 && currentMapView.center.lat <= 31.0 &&
                               currentMapView.center.lng >= 80.0 && currentMapView.center.lng <= 89.0
  
  const isMapZoomedIntoSriLanka = currentMapView && 
                                  currentMapView.center && 
                                  currentMapView.zoom >= 5 &&
                                  !isWorldView &&
                                  currentMapView.center.lat >= 5.5 && currentMapView.center.lat <= 10.0 &&
                                  currentMapView.center.lng >= 79.0 && currentMapView.center.lng <= 82.0
  
  const allRegionsVisible = visibleRegions && Object.values(visibleRegions).every(value => value === true)
  const isCountryFocusedByRegions = !allRegionsVisible && (indiaRegionsVisible || nepalRegionsVisible || sriLankaRegionsVisible)
  const isCountryFocusedByZoom = isMapZoomedIntoIndia || isMapZoomedIntoNepal || isMapZoomedIntoSriLanka
  
  const isCountryFocusedView = isCountryFocusedByZoom || isCountryFocusedByRegions
  
  // Check if airports are available
  const hasAirports = airports && airports.length > 0 && showAirports
  
  // Check if specific temple types are available
  const hasJyotirlinga = regions && regions['India-Jyotirlinga'] && regions['India-Jyotirlinga'].length > 0 && 
                         visibleRegions && visibleRegions['India-Jyotirlinga'] === true
  const hasShaktiPeetha = regions && regions['India-ShaktiPeetha'] && regions['India-ShaktiPeetha'].length > 0 && 
                          visibleRegions && visibleRegions['India-ShaktiPeetha'] === true
  const hasMatham = regions && regions['India-Matham'] && regions['India-Matham'].length > 0 && 
                    visibleRegions && visibleRegions['India-Matham'] === true
  const hasDivyaDesam = regions && regions['India-DivyaDesam'] && regions['India-DivyaDesam'].length > 0 && 
                        visibleRegions && visibleRegions['India-DivyaDesam'] === true
  const hasTemples = (regions && regions['India-OtherTemples'] && regions['India-OtherTemples'].length > 0 && 
                     visibleRegions && visibleRegions['India-OtherTemples'] === true) ||
                    (regions && regions['Nepal-Temples'] && regions['Nepal-Temples'].length > 0 && 
                     visibleRegions && visibleRegions['Nepal-Temples'] === true) ||
                    (regions && regions['Sri Lanka-Temples'] && regions['Sri Lanka-Temples'].length > 0 && 
                     visibleRegions && visibleRegions['Sri Lanka-Temples'] === true)

  const legendItems = useMemo(() => {
    const items = [
      {
        icon: '🌲',
        label: 'National Parks',
        color: '#90EE90',
        borderColor: '#7CB342'
      },
      {
        icon: '🏛️',
        label: 'UNESCO Sites',
        color: '#81D4FA',
        borderColor: '#4FC3F7'
      },
      {
        icon: '📷',
        label: 'Most Photographed',
        color: '#FFB6C1',
        borderColor: '#FF8C9F',
        note: 'Includes National Parks (🌲 on light red)'
      }
    ]
    
    // In country-focused view, show temple types separately; otherwise group under "Temples"
    if (isCountryFocusedView) {
      // Show separate temple types when India/Nepal/Sri Lanka are focused
      if (hasTemples) {
        items.push({
          icon: '🕉️',
          label: 'Temples',
          color: '#FF9933',
          borderColor: '#FF8C00'
        })
      }
      if (hasJyotirlinga) {
        items.push({
          icon: '🔱',
          label: 'Jyotirlinga',
          color: '#FF9933',
          borderColor: '#FF8C00',
          note: '(Trishul icon on saffron)'
        })
      }
      if (hasShaktiPeetha) {
        items.push({
          icon: '🌸',
          label: 'Shakti Peetha',
          color: '#FF9933',
          borderColor: '#FF8C00',
          note: '(Lotus icon on saffron)'
        })
      }
      if (hasMatham) {
        items.push({
          icon: '🏛️',
          label: 'Matham',
          color: '#FF9933',
          borderColor: '#FF8C00',
          note: '(Monastery icon)'
        })
      }
      if (hasDivyaDesam) {
        items.push({
          icon: '🐚',
          label: 'Divya Desam',
          color: '#FF9933',
          borderColor: '#FF8C00',
          note: '(Conch shell icon)'
        })
      }
    } else {
      // In general view, group all temple types under "Temples"
      if (hasTemples || hasJyotirlinga || hasShaktiPeetha || hasMatham || hasDivyaDesam) {
        items.push({
          icon: '🕉️',
          label: 'Temples',
          color: '#FF9933',
          borderColor: '#FF8C00',
          note: '(Includes Jyotirlinga, Shakti Peetha, Matham, Divya Desam)'
        })
      }
    }
    
    items.push({
      icon: '🕉️',
      label: 'UNESCO Temples',
      color: '#81D4FA',
      borderColor: '#4FC3F7',
      note: '(Om icon on light blue)'
    })
    
    items.push({
      icon: '🏰',
      label: 'Forts',
      color: '#8B4513',
      borderColor: '#654321'
    })
    
    // Show airports dynamically when available
    if (hasAirports) {
      items.push({
        icon: '✈️',
        label: 'Airports',
        color: '#FFFFFF',
        borderColor: '#666666',
        note: '(White background)'
      })
    }
    
    return items
  }, [isCountryFocusedView, hasTemples, hasJyotirlinga, hasShaktiPeetha, hasMatham, hasDivyaDesam, hasAirports, currentMapView])

  return (
    <div className="map-legend-container">
      <button
        className="map-legend-toggle"
        onClick={() => setIsOpen(!isOpen)}
        aria-label={isOpen ? 'Hide legend' : 'Show legend'}
        title={isOpen ? 'Hide legend' : 'Show legend'}
      >
        <span className="legend-icon">📋</span>
        <span className="legend-toggle-text">Legend</span>
      </button>

      {isOpen && (
        <div className="map-legend-content">
          <div className="legend-header">
            <h3>Map Legend</h3>
            <button
              className="legend-close-button"
              onClick={() => setIsOpen(false)}
              aria-label="Close legend"
            >
              ×
            </button>
          </div>
          <div className="legend-items">
            {legendItems.map((item, index) => (
              <div key={index} className="legend-item">
                <div className="legend-icon-wrapper">
                  <div
                    className="legend-marker-preview"
                    style={{
                      backgroundColor: item.color,
                      borderColor: item.borderColor
                    }}
                  >
                    <span className="legend-marker-icon">{item.icon}</span>
                  </div>
                </div>
                <div className="legend-item-info">
                  <div className="legend-item-label">{item.label}</div>
                  {item.note && (
                    <div className="legend-item-note">{item.note}</div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default MapLegend

