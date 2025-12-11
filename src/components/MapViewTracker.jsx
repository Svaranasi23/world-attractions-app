import { useEffect, useState } from 'react'
import { useMap, useMapEvents } from 'react-leaflet'

// Component to track current map view (center and zoom)
function MapViewTracker({ onViewChange }) {
  const map = useMap()
  const [currentView, setCurrentView] = useState({
    center: map.getCenter(),
    zoom: map.getZoom()
  })

  useMapEvents({
    moveend: () => {
      const newView = {
        center: map.getCenter(),
        zoom: map.getZoom()
      }
      setCurrentView(newView)
      if (onViewChange) {
        onViewChange(newView)
      }
    },
    zoomend: () => {
      const newView = {
        center: map.getCenter(),
        zoom: map.getZoom()
      }
      setCurrentView(newView)
      if (onViewChange) {
        onViewChange(newView)
      }
    }
  })

  useEffect(() => {
    // Initial view
    const initialView = {
      center: map.getCenter(),
      zoom: map.getZoom()
    }
    setCurrentView(initialView)
    if (onViewChange) {
      onViewChange(initialView)
    }
  }, [map, onViewChange])

  return null
}

export default MapViewTracker

