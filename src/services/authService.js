// Authentication service using Firebase Auth

import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  GoogleAuthProvider,
  signInWithPopup,
  updateProfile
} from 'firebase/auth'
import { auth } from './firebaseConfig'

// Check if Firebase is initialized
const isFirebaseAvailable = () => {
  return auth !== null && auth !== undefined
}

// Sign up with email and password
export const signUp = async (email, password, displayName = '') => {
  if (!isFirebaseAvailable()) {
    return { success: false, error: 'Firebase is not initialized. Please check your configuration.' }
  }
  try {
    const userCredential = await createUserWithEmailAndPassword(auth, email, password)
    if (displayName && userCredential.user) {
      await updateProfile(userCredential.user, { displayName })
    }
    return { success: true, user: userCredential.user }
  } catch (error) {
    console.error('Sign up error:', error)
    return { success: false, error: error.message || 'Sign up failed' }
  }
}

// Sign in with email and password
export const signIn = async (email, password) => {
  if (!isFirebaseAvailable()) {
    return { success: false, error: 'Firebase is not initialized. Please check your configuration.' }
  }
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password)
    return { success: true, user: userCredential.user }
  } catch (error) {
    console.error('Sign in error:', error)
    return { success: false, error: error.message || 'Sign in failed' }
  }
}

// Sign in with Google
export const signInWithGoogle = async () => {
  if (!isFirebaseAvailable()) {
    return { success: false, error: 'Firebase is not initialized. Please check your configuration.' }
  }
  try {
    const provider = new GoogleAuthProvider()
    const userCredential = await signInWithPopup(auth, provider)
    return { success: true, user: userCredential.user }
  } catch (error) {
    console.error('Google sign in error:', error)
    // Handle popup closed by user
    if (error.code === 'auth/popup-closed-by-user') {
      return { success: false, error: 'Sign in was cancelled' }
    }
    return { success: false, error: error.message || 'Google sign in failed' }
  }
}

// Sign out
export const signOutUser = async () => {
  if (!isFirebaseAvailable()) {
    return { success: false, error: 'Firebase is not initialized' }
  }
  try {
    await signOut(auth)
    return { success: true }
  } catch (error) {
    console.error('Sign out error:', error)
    return { success: false, error: error.message || 'Sign out failed' }
  }
}

// Get current user
export const getCurrentUser = () => {
  if (!isFirebaseAvailable()) {
    return null
  }
  try {
    return auth.currentUser
  } catch (error) {
    console.error('Get current user error:', error)
    return null
  }
}

// Listen to auth state changes
export const onAuthStateChange = (callback) => {
  if (!isFirebaseAvailable()) {
    console.warn('Firebase auth not available, returning no-op unsubscribe')
    return () => {} // Return a no-op function
  }
  try {
    return onAuthStateChanged(auth, callback)
  } catch (error) {
    console.error('Auth state change listener error:', error)
    return () => {} // Return a no-op function
  }
}

