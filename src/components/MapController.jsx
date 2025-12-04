import { useEffect } from 'react'
import { useMap } from 'react-leaflet'

function MapController({ center, zoom, bounds }) {
  const map = useMap()

  useEffect(() => {
    if (bounds && Array.isArray(bounds) && bounds.length === 2) {
      // Fit map to bounds
      try {
        map.fitBounds(bounds, { 
          padding: [50, 50], 
          maxZoom: 8,
          animate: true,
          duration: 1.0
        })
      } catch (error) {
        console.error('Error fitting bounds:', error)
      }
    } else if (center && Array.isArray(center) && center.length === 2) {
      // Center and zoom to specific location
      map.setView(center, zoom || 6, { animate: true, duration: 1.0 })
    }
  }, [map, center, zoom, bounds])

  return null
}

export default MapController

