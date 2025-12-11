// Firebase configuration
// Replace these values with your Firebase project configuration
// Get these from: Firebase Console > Project Settings > General > Your apps

import { initializeApp } from 'firebase/app'
import { getAuth } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'

// Your web app's Firebase configuration
// Configuration for world-attractions-explorer Firebase project
const firebaseConfig = {
  apiKey: "YOUR_FIREBASE_API_KEY_HERE",
  authDomain: "world-attractions-explorer.firebaseapp.com",
  projectId: "world-attractions-explorer",
  storageBucket: "world-attractions-explorer.appspot.com",
  messagingSenderId: "219161346422",
  appId: "1:219161346422:web:b1c38dea46bb73142bba57"
}

// Initialize Firebase with error handling
let app, auth, db

try {
  app = initializeApp(firebaseConfig)
  auth = getAuth(app)
  db = getFirestore(app)
} catch (error) {
  console.error('Firebase initialization error:', error)
  // Create fallback objects to prevent crashes
  app = null
  auth = null
  db = null
}

// Initialize Firebase Authentication and get a reference to the service
export { auth }

// Initialize Cloud Firestore and get a reference to the service
export { db }

export default app

