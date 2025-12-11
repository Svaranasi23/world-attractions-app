# Quick Firebase Setup Checklist

Your Firebase project "world-attractions-explorer" is partially configured. Follow these steps to complete the setup:

## ✅ Step 1: Get Your API Key

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **world-attractions-explorer**
3. Click the gear icon ⚙️ next to "Project Overview"
4. Select **Project settings**
5. Scroll down to "Your apps" section
6. You should see your web app listed. Click on it or the gear icon next to it
7. Find the **apiKey** field in the config
8. Copy the API key (it looks like: `AIzaSy...`)

## ✅ Step 2: Update firebaseConfig.js

Replace `"YOUR_API_KEY"` in `src/services/firebaseConfig.js` with your actual API key.

## ✅ Step 3: Enable Authentication

1. In Firebase Console, go to **Authentication** (left sidebar)
2. Click **Get Started** if you haven't already
3. Go to the **Sign-in method** tab
4. Enable:
   - **Email/Password**: Click → Enable → Save
   - **Google**: Click → Enable → Enter support email → Save

## ✅ Step 4: Create Firestore Database

1. In Firebase Console, go to **Firestore Database** (left sidebar)
2. Click **Create database** if you haven't already
3. Choose **Start in test mode** (for development)
4. Select a location (choose closest to your users)
5. Click **Enable**

## ✅ Step 5: Set Firestore Security Rules

1. In Firestore Database, go to the **Rules** tab
2. Replace the rules with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own visited places
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

3. Click **Publish**

## ✅ Step 6: Add Authorized Domains

1. In Firebase Console, go to **Authentication** → **Settings**
2. Scroll to **Authorized domains**
3. Make sure these are listed:
   - `localhost` (for development)
   - Your production domain (if deployed)
   - `world-attractions-explorer.firebaseapp.com` (should be there by default)

## ✅ Step 7: Test the Setup

1. Run: `npm run dev`
2. Open the app in your browser
3. Click the hamburger menu (☰)
4. Click "Sign In to Sync"
5. Try creating an account with email/password
6. Mark a place as visited
7. Check Firebase Console → Firestore Database to see if data was saved

## Quick Verification

After completing the steps above, you should be able to:
- ✅ Sign up with email/password
- ✅ Sign in with Google
- ✅ Mark places as visited
- ✅ See data in Firestore under `users/{userId}/visitedPlaces`
- ✅ Sign in from another device and see your visited places sync



