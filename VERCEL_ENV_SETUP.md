# Vercel Environment Variables Setup

## Required Environment Variables

Add these environment variables in your Vercel project settings:

### Firebase Configuration Variables

| Variable Name | Value | Description |
|--------------|-------|-------------|
| `VITE_FIREBASE_API_KEY` | `YOUR_FIREBASE_API_KEY` | Firebase API Key (get from Firebase Console) |
| `VITE_FIREBASE_AUTH_DOMAIN` | `your-project.firebaseapp.com` | Firebase Auth Domain |
| `VITE_FIREBASE_PROJECT_ID` | `your-project-id` | Firebase Project ID |
| `VITE_FIREBASE_STORAGE_BUCKET` | `your-project.appspot.com` | Firebase Storage Bucket |
| `VITE_FIREBASE_MESSAGING_SENDER_ID` | `YOUR_SENDER_ID` | Firebase Messaging Sender ID |
| `VITE_FIREBASE_APP_ID` | `YOUR_APP_ID` | Firebase App ID |

## How to Add Environment Variables in Vercel

### Step 1: Go to Vercel Dashboard
1. Open [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project: **world-attractions-app** (or your project name)

### Step 2: Navigate to Settings
1. Click on your project
2. Go to **Settings** tab
3. Click on **Environment Variables** in the left sidebar

### Step 3: Add Each Variable
For each variable above:
1. Click **Add New**
2. Enter the **Key** (e.g., `VITE_FIREBASE_API_KEY`)
3. Enter the **Value** (get from your `.env` file or Firebase Console)
4. Select the environments where it should be available:
   - ✅ **Production**
   - ✅ **Preview**
   - ✅ **Development** (optional, if you use Vercel CLI)
5. Click **Save**

### Step 4: Redeploy
After adding all variables:
1. Go to **Deployments** tab
2. Click the **⋯** (three dots) on the latest deployment
3. Click **Redeploy**
4. Or push a new commit to trigger automatic deployment

## Quick Copy-Paste Template

**⚠️ IMPORTANT:** Replace the placeholder values below with your actual Firebase credentials from Firebase Console or your local `.env` file.

```
VITE_FIREBASE_API_KEY=YOUR_FIREBASE_API_KEY_HERE
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=YOUR_SENDER_ID
VITE_FIREBASE_APP_ID=YOUR_APP_ID
```

**Where to get these values:**
- Firebase Console → Project Settings → General → Your apps → Web app config
- Or copy from your local `.env` file (never commit `.env` to git)

## Important Notes

⚠️ **Note:** 
- All variable names must start with `VITE_` for Vite to expose them to the client-side code
- After adding variables, you **must redeploy** for changes to take effect
- Environment variables are encrypted and secure in Vercel
- You can add different values for Production, Preview, and Development environments

## ⚠️ Vercel Warning About VITE_FIREBASE_AUTH_DOMAIN

**You may see a warning:** "This key, which is prefixed with VITE_ and includes the term AUTH, might expose sensitive information to the browser."

**This is SAFE to ignore** for Firebase configuration values. Here's why:

### Why Firebase Config Values Are Public:
1. **Firebase is designed for client-side use** - All Firebase configuration values (API key, auth domain, project ID, etc.) are meant to be exposed to the browser
2. **Security comes from restrictions, not secrecy**:
   - ✅ **API Key Restrictions** (we set these in Google Cloud Console)
   - ✅ **Firebase Security Rules** (for Firestore database)
   - ✅ **Authentication rules** (who can sign up/sign in)
3. **The `VITE_` prefix is intentional** - It tells Vite to expose these to the browser, which is required for Firebase to work

### What IS Secret:
- ❌ **Firebase Admin SDK keys** (server-side only - NOT used in this app)
- ❌ **Service account keys** (server-side only - NOT used in this app)
- ❌ **Private API keys** (not Firebase config)

### What is NOT Secret (Safe to Expose):
- ✅ Firebase Web API Key (restricted by domain/API)
- ✅ Firebase Auth Domain
- ✅ Firebase Project ID
- ✅ Firebase Storage Bucket
- ✅ Firebase App ID

**Bottom line:** You can safely ignore this Vercel warning. Firebase configuration values are public by design, and your security comes from the API key restrictions we set up in Google Cloud Console.

## Verification

After deployment, check the browser console to ensure:
- No warnings about missing Firebase API key
- Firebase authentication works
- Firestore operations work

If you see warnings, verify:
1. All variables are set correctly
2. Variable names match exactly (case-sensitive)
3. Deployment was successful after adding variables
