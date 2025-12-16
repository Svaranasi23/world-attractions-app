import React, { useState, useEffect, useMemo } from 'react'
import { createPortal } from 'react-dom'
import { findNearbyParks, findNearbyAirports, calculateDistance } from '../services/dataService'
import './CustomPinModal.css'

const CustomPinModal = ({ isOpen, onClose, onSave, lat, lon, parks = [], airports = [] }) => {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')

  // Find nearby locations
  const nearbyLocations = useMemo(() => {
    if (!isOpen || !parks || parks.length === 0) return { attractions: [], airports: [] }

    // Determine radius based on country (similar to MapView logic)
    // For now, use a standard 50 miles radius for suggestions
    const suggestionRadius = 50 // miles

    // Find nearby attractions
    const nearbyAttractions = findNearbyParks(lat, lon, 'Custom Location', parks, suggestionRadius)
      .slice(0, 5) // Limit to top 5

    // Find nearby airports
    const nearbyAirportsList = findNearbyAirports(lat, lon, airports, suggestionRadius)
      .slice(0, 3) // Limit to top 3

    return {
      attractions: nearbyAttractions,
      airports: nearbyAirportsList
    }
  }, [isOpen, lat, lon, parks, airports])

  if (!isOpen) return null

  const handleSubmit = (e) => {
    e.preventDefault()
    if (name.trim()) {
      onSave(lat, lon, name.trim(), description.trim())
      setName('')
      setDescription('')
      onClose()
    }
  }

  const handleCancel = () => {
    setName('')
    setDescription('')
    onClose()
  }

  return createPortal(
    <div className="custom-pin-modal-overlay" onClick={handleCancel}>
      <div className="custom-pin-modal" onClick={(e) => e.stopPropagation()}>
        <div className="custom-pin-modal-header">
          <h2>📍 Add Custom Pin</h2>
          <button className="close-button" onClick={handleCancel}>×</button>
        </div>
        <form onSubmit={handleSubmit} className="custom-pin-form">
          <div className="form-group">
            <label htmlFor="pin-name">Location Name *</label>
            <input
              id="pin-name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g., My Favorite Spot"
              required
              autoFocus
            />
          </div>
          <div className="form-group">
            <label htmlFor="pin-description">Description (optional)</label>
            <textarea
              id="pin-description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Add notes about this location..."
              rows="3"
            />
          </div>
          <div className="form-group">
            <p className="coordinates-info">
              Coordinates: {lat.toFixed(6)}°N, {lon.toFixed(6)}°W
            </p>
          </div>

          {/* Nearby Locations Suggestions */}
          {(nearbyLocations.attractions.length > 0 || nearbyLocations.airports.length > 0) && (
            <div className="nearby-locations-section">
              <h3 className="nearby-locations-title">📍 Nearby Locations</h3>
              
              {nearbyLocations.attractions.length > 0 && (
                <div className="nearby-attractions">
                  <strong>🏞️ Nearby Attractions (within 50 mi):</strong>
                  <ul className="nearby-list">
                    {nearbyLocations.attractions.map((attraction, index) => {
                      const distance = attraction.distance
                      const unit = 'mi'
                      return (
                        <li key={index} className="nearby-item">
                          <span className="attraction-name">{attraction.name}</span>
                          <span className="attraction-distance">({distance.toFixed(1)} {unit})</span>
                        </li>
                      )
                    })}
                  </ul>
                </div>
              )}

              {nearbyLocations.airports.length > 0 && (
                <div className="nearby-airports">
                  <strong>✈️ Nearby Airports (within 50 mi):</strong>
                  <ul className="nearby-list">
                    {nearbyLocations.airports.map((airport, index) => {
                      const distance = airport.distance
                      const unit = 'mi'
                      return (
                        <li key={index} className="nearby-item">
                          <span className="airport-code">{airport.iata}</span>
                          <span className="airport-name">{airport.name}</span>
                          <span className="airport-distance">({distance.toFixed(1)} {unit})</span>
                        </li>
                      )
                    })}
                  </ul>
                </div>
              )}
            </div>
          )}

          <div className="form-actions">
            <button type="button" onClick={handleCancel} className="cancel-button">
              Cancel
            </button>
            <button type="submit" className="save-button">
              Save Pin
            </button>
          </div>
        </form>
      </div>
    </div>,
    document.body
  )
}

export default CustomPinModal

