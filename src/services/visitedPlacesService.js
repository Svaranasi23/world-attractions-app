// Service to manage visited places with localStorage persistence and Firebase sync

import { doc, getDoc, setDoc, updateDoc, serverTimestamp } from 'firebase/firestore'
import { db } from './firebaseConfig'
import { getCurrentUser } from './authService'

const VISITED_PLACES_KEY = 'world-attractions-visited-places'
const USER_PROFILE_KEY = 'world-attractions-user-profile'
const SYNC_TIMESTAMP_KEY = 'world-attractions-sync-timestamp'

// Get a unique ID for a park/attraction
export const getPlaceId = (park) => {
  // Use coordinates as unique identifier (most reliable)
  const lat = parseFloat(park.Latitude)
  const lon = parseFloat(park.Longitude)
  if (!isNaN(lat) && !isNaN(lon)) {
    return `${lat.toFixed(6)}_${lon.toFixed(6)}`
  }
  // Fallback to name + country
  return `${park.Name || 'unknown'}_${park.Country || 'unknown'}`.replace(/[^a-zA-Z0-9_]/g, '_')
}

// Load visited places from localStorage
export const loadVisitedPlaces = () => {
  try {
    const stored = localStorage.getItem(VISITED_PLACES_KEY)
    if (stored) {
      return JSON.parse(stored)
    }
  } catch (error) {
    console.error('Error loading visited places:', error)
  }
  return {}
}

// Load visited places from Firestore for authenticated user
export const loadVisitedPlacesFromFirestore = async (userId) => {
  try {
    if (!userId || !db) return null
    
    const userDocRef = doc(db, 'users', userId)
    const userDoc = await getDoc(userDocRef)
    
    if (userDoc.exists()) {
      const data = userDoc.data()
      return data.visitedPlaces || {}
    }
    return {}
  } catch (error) {
    console.error('Error loading visited places from Firestore:', error)
    return null
  }
}

// Save visited places to Firestore for authenticated user
export const saveVisitedPlacesToFirestore = async (userId, visitedPlaces) => {
  try {
    if (!userId || !db) return false
    
    const userDocRef = doc(db, 'users', userId)
    await setDoc(userDocRef, {
      visitedPlaces,
      lastUpdated: serverTimestamp(),
      updatedAt: new Date().toISOString()
    }, { merge: true })
    
    // Update sync timestamp in localStorage
    localStorage.setItem(SYNC_TIMESTAMP_KEY, new Date().toISOString())
    return true
  } catch (error) {
    console.error('Error saving visited places to Firestore:', error)
    return false
  }
}

// Sync visited places: merge Firestore data with localStorage
export const syncVisitedPlaces = async () => {
  const user = getCurrentUser()
  if (!user) {
    // Not logged in, just use localStorage
    return loadVisitedPlaces()
  }
  
  try {
    // Load from Firestore
    const firestorePlaces = await loadVisitedPlacesFromFirestore(user.uid)
    if (firestorePlaces === null) {
      // Error loading from Firestore, use localStorage
      return loadVisitedPlaces()
    }
    
    // Load from localStorage
    const localPlaces = loadVisitedPlaces()
    
    // Merge: Firestore takes precedence (more recent), but include any local-only entries
    const merged = { ...localPlaces, ...firestorePlaces }
    
    // Save merged data to both localStorage and Firestore
    saveVisitedPlaces(merged)
    await saveVisitedPlacesToFirestore(user.uid, merged)
    
    return merged
  } catch (error) {
    console.error('Error syncing visited places:', error)
    return loadVisitedPlaces()
  }
}

// Save visited places to localStorage
export const saveVisitedPlaces = (visitedPlaces) => {
  try {
    localStorage.setItem(VISITED_PLACES_KEY, JSON.stringify(visitedPlaces))
    return true
  } catch (error) {
    console.error('Error saving visited places:', error)
    return false
  }
}

// Mark a place as visited
export const markAsVisited = async (park) => {
  const visitedPlaces = loadVisitedPlaces()
  const placeId = getPlaceId(park)
  visitedPlaces[placeId] = {
    name: park.Name,
    country: park.Country,
    visitedAt: new Date().toISOString(),
    coordinates: {
      lat: parseFloat(park.Latitude),
      lon: parseFloat(park.Longitude)
    }
  }
  saveVisitedPlaces(visitedPlaces)
  
  // Sync to Firestore if user is logged in
  const user = getCurrentUser()
  if (user) {
    await saveVisitedPlacesToFirestore(user.uid, visitedPlaces)
  }
  
  return visitedPlaces
}

// Mark a place as not visited
export const markAsNotVisited = async (park) => {
  const visitedPlaces = loadVisitedPlaces()
  const placeId = getPlaceId(park)
  delete visitedPlaces[placeId]
  saveVisitedPlaces(visitedPlaces)
  
  // Sync to Firestore if user is logged in
  const user = getCurrentUser()
  if (user) {
    await saveVisitedPlacesToFirestore(user.uid, visitedPlaces)
  }
  
  return visitedPlaces
}

// Check if a place is visited
export const isPlaceVisited = (park, visitedPlaces = null) => {
  const places = visitedPlaces || loadVisitedPlaces()
  const placeId = getPlaceId(park)
  return !!places[placeId]
}

// Get visited count
export const getVisitedCount = (parks = []) => {
  const visitedPlaces = loadVisitedPlaces()
  return parks.filter(park => isPlaceVisited(park, visitedPlaces)).length
}

// Get visited places details
export const getVisitedPlacesDetails = () => {
  const visitedPlaces = loadVisitedPlaces()
  return Object.values(visitedPlaces)
}

// Clear all visited places
export const clearAllVisitedPlaces = () => {
  try {
    localStorage.removeItem(VISITED_PLACES_KEY)
    return true
  } catch (error) {
    console.error('Error clearing visited places:', error)
    return false
  }
}

// User Profile Management
export const loadUserProfile = () => {
  try {
    const stored = localStorage.getItem(USER_PROFILE_KEY)
    if (stored) {
      return JSON.parse(stored)
    }
  } catch (error) {
    console.error('Error loading user profile:', error)
  }
  return {
    name: '',
    preferences: {
      showVisitedOnly: false,
      showUnvisitedOnly: false,
      highlightVisited: true
    }
  }
}

export const saveUserProfile = (profile) => {
  try {
    localStorage.setItem(USER_PROFILE_KEY, JSON.stringify(profile))
    return true
  } catch (error) {
    console.error('Error saving user profile:', error)
    return false
  }
}

