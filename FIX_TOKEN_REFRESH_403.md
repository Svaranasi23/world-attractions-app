# Fix: 403 Forbidden Error on Token Refresh

## Problem
You're seeing this error:
```
POST https://securetoken.googleapis.com/v1/token?key=AIzaSy... 403 (Forbidden)
```

This happens when Firebase tries to automatically refresh the authentication token, but the request is being blocked.

## Root Cause
The API key restrictions are blocking the Secure Token API endpoint, which is used for token refresh. This is part of the Identity Toolkit API.

## Solution

### Step 1: Check API Restrictions
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select project: **world-attractions-explorer**
3. Navigate to **APIs & Services** → **Credentials**
4. Click on your API key (it starts with `AIzaSy...`)

### Step 2: Verify API Restrictions Include Identity Toolkit
1. Under **API restrictions**, make sure **Identity Toolkit API** is checked ✅
2. The Secure Token API is part of Identity Toolkit, so this should be sufficient

### Step 3: Check HTTP Referrer Restrictions
The most common issue is that your current domain is not in the allowed referrers list.

1. Under **Application restrictions**, select **HTTP referrers (web sites)**
2. Make sure your current domain is listed. Add if missing:
   - `https://world-attractions-explorer.vercel.app/*` (production)
   - `https://world-attractions-explorer.firebaseapp.com/*` (Firebase hosting)
   - `http://localhost/*` (local development)
   - `http://localhost:3000/*` (if using port 3000)
   - `http://localhost:5173/*` (if using Vite default port)
   - `https://*.vercel.app/*` (for Vercel preview deployments)

### Step 4: Verify APIs are Enabled
1. Go to **APIs & Services** → **Enabled APIs**
2. Make sure these are enabled:
   - ✅ **Identity Toolkit API**
   - ✅ **Cloud Firestore API**

### Step 5: Check Authorized Domains in Firebase
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select project: **world-attractions-explorer**
3. Go to **Authentication** → **Settings** → **Authorized domains**
4. Make sure your domain is listed:
   - `localhost` (for development)
   - `world-attractions-explorer.firebaseapp.com`
   - Your production domain (if different)

## Quick Fix Checklist

- [ ] Identity Toolkit API is enabled
- [ ] Identity Toolkit API is in API key restrictions
- [ ] Current domain is in HTTP referrer restrictions
- [ ] Domain is in Firebase authorized domains
- [ ] Wait 2-3 minutes after making changes for them to propagate

## Testing
After making changes:
1. Clear browser cache and cookies
2. Sign out and sign back in
3. Check browser console for errors
4. The token refresh should work automatically in the background

## Alternative: Temporarily Remove Restrictions (NOT RECOMMENDED)
If you need to test immediately:
1. Set **Application restrictions** to **None** (temporary)
2. Test that token refresh works
3. **IMPORTANT**: Re-add restrictions after testing

## Why This Happens
Firebase automatically refreshes authentication tokens in the background to keep users logged in. The refresh happens via the Secure Token API endpoint (`securetoken.googleapis.com`), which requires:
1. Identity Toolkit API to be enabled
2. API key to allow Identity Toolkit API
3. Domain to be in HTTP referrer restrictions
4. Domain to be in Firebase authorized domains

If any of these are missing, you'll get a 403 Forbidden error.


