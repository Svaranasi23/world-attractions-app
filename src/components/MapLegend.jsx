import React, { useState } from 'react'
import './MapLegend.css'

function MapLegend() {
  const [isOpen, setIsOpen] = useState(false)

  const legendItems = [
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
      borderColor: '#FF8C9F'
    },
    {
      icon: '🌲',
      label: 'Most Photographed National Parks',
      color: '#FFB6C1',
      borderColor: '#FF8C9F',
      note: '(Tree icon on light red)'
    },
    {
      icon: '🕉️',
      label: 'Temples',
      color: '#FF9933',
      borderColor: '#FF8C00'
    },
    {
      icon: '🕉️',
      label: 'UNESCO Temples',
      color: '#81D4FA',
      borderColor: '#4FC3F7',
      note: '(Om icon on light blue)'
    },
    {
      icon: '🔱',
      label: 'Jyotirlinga',
      color: '#FF9933',
      borderColor: '#FF8C00',
      note: '(Trishul icon on saffron)'
    },
    {
      icon: '🌸',
      label: 'Shakti Peetha',
      color: '#FF9933',
      borderColor: '#FF8C00',
      note: '(Lotus icon on saffron)'
    },
    {
      icon: '🏛️',
      label: 'Mutts',
      color: '#FF9933',
      borderColor: '#FF8C00',
      note: '(Monastery icon)'
    },
    {
      icon: '🐚',
      label: 'Divya Desam',
      color: '#FF9933',
      borderColor: '#FF8C00',
      note: '(Conch shell icon)'
    },
    {
      icon: '🏰',
      label: 'Forts',
      color: '#8B4513',
      borderColor: '#654321'
    },
    {
      icon: '✈️',
      label: 'Airports',
      color: '#FFFFFF',
      borderColor: '#666666',
      note: '(White background)'
    }
  ]

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

