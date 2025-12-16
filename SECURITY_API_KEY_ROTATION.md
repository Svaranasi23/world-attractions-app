# Security: API Key Rotation Guide

## ⚠️ Important: Exposed API Key Detected

GitGuardian has detected that a Google API Key was exposed in your GitHub repository. Even though we've removed it from the current code, **it still exists in git history** and should be rotated.

## Why Rotate the Key?

1. **Git History**: The key is still visible in previous commits
2. **Security Best Practice**: Any exposed key should be rotated
3. **Prevent Unauthorized Use**: Rotating invalidates the old key

## Step 1: Create a New API Key in Firebase

### Option A: Create a New Web App (Recommended)

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **world-attractions-explorer**
3. Go to **Project Settings** (gear icon) → **General** tab
4. Scroll down to **Your apps** section
5. Click **Add app** → Select **Web** (</> icon)
6. Register the app with a name (e.g., "world-attractions-explorer-web-v2")
7. Copy the new `apiKey` from the `firebaseConfig` object

### Option B: Use the Same App (If You Only Have One)

If you only have one web app, you'll need to:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select project: **world-attractions-explorer**
3. Go to **APIs & Services** → **Credentials**
4. Find your current API key
5. Click **Create Credentials** → **API Key**
6. Copy the new API key

## Step 2: Restrict the New API Key

**IMPORTANT:** Before using the new key, restrict it immediately:

1. In Google Cloud Console, click on the **new API key** you just created
2. Under **Application restrictions**, select **HTTP referrers (web sites)**
3. Add your domains:
   - `https://world-attractions-explorer.vercel.app/*`
   - `http://localhost/*`
   - `http://localhost:5173/*`
   - `http://localhost:3000/*`
   - `https://*.vercel.app/*` (for preview deployments)
4. Under **API restrictions**, select **Restrict key**
5. Check:
   - ✅ **Identity Toolkit API**
   - ✅ **Cloud Firestore API**
6. Click **Save**

## Step 3: Update Environment Variables

### Update Local `.env` File

1. Open your `.env` file
2. Update `VITE_FIREBASE_API_KEY` with the new key:
   ```
   VITE_FIREBASE_API_KEY=YOUR_NEW_API_KEY_HERE
   ```
3. Save the file

### Update Vercel Environment Variables

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project: **world-attractions-explorer**
3. Go to **Settings** → **Environment Variables**
4. Find `VITE_FIREBASE_API_KEY`
5. Click **Edit** → Update the value with the new API key
6. Click **Save**
7. **Redeploy** your application

## Step 4: Revoke the Old API Key

**After confirming the new key works:**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Select project: **world-attractions-explorer**
3. Go to **APIs & Services** → **Credentials**
4. Find the **old API key** (`YOUR_FIREBASE_API_KEY_HERE`)
5. Click on it → Click **Delete** or **Restrict** → Set restrictions to block all usage
6. Confirm deletion

## Step 5: Test the Application

1. Test authentication (sign up, sign in)
2. Test Google sign-in
3. Test password reset
4. Test visited places sync (Firestore)
5. Test on both localhost and production

## Step 6: Clean Git History (Optional but Recommended)

**Warning:** This rewrites git history. Only do this if:
- You're the only one working on this repository, OR
- You've coordinated with your team

### Option A: Use BFG Repo-Cleaner (Recommended)

1. Install BFG: `brew install bfg` (Mac) or download from [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
2. Create a backup: `git clone --mirror https://github.com/Svaranasi23/world-attractions-explorer.git`
3. Run BFG:
   ```bash
   bfg --replace-text passwords.txt
   ```
   Where `passwords.txt` contains:
   ```
   YOUR_FIREBASE_API_KEY_HERE==>YOUR_NEW_API_KEY_HERE
   ```
4. Force push: `git push --force`

### Option B: Manual Git History Cleanup (Advanced)

This requires rewriting git history. See [GitHub's guide on removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Verification Checklist

- [ ] New API key created
- [ ] New API key restricted (HTTP referrers + API restrictions)
- [ ] Local `.env` file updated
- [ ] Vercel environment variables updated
- [ ] Application tested and working
- [ ] Old API key revoked/deleted
- [ ] Git history cleaned (optional)

## Important Notes

⚠️ **After rotating:**
- The old key will stop working once revoked
- Make sure the new key is working before revoking the old one
- Update all environments (local, Vercel, etc.) before revoking

✅ **Security Best Practices:**
- Never commit API keys to git
- Always use environment variables
- Restrict API keys immediately after creation
- Rotate keys if they're exposed

## Need Help?

If you encounter issues:
1. Check that the new API key has the correct restrictions
2. Verify environment variables are set correctly
3. Check browser console for errors
4. Ensure APIs (Identity Toolkit, Firestore) are enabled


