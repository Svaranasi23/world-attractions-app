# Firebase Password Reset Email Setup

If you're not receiving password reset emails, follow these steps:

## Step 1: Configure Email Templates in Firebase

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **world-attractions-explorer**
3. Go to **Authentication** → **Templates** tab
4. Click on **Password reset** template
5. Configure the email template:
   - **Subject**: "Reset your password"
   - **Action URL**: Your app URL (e.g., `https://your-app.vercel.app` or `http://localhost:5173`)
   - Customize the email body if needed
6. Click **Save**

## Step 2: Verify Email Domain Authorization

1. In Firebase Console, go to **Authentication** → **Settings** → **Authorized domains**
2. Make sure your domain is listed:
   - `localhost` (for development)
   - Your production domain (e.g., `your-app.vercel.app`)
3. If not listed, click **Add domain** and add it

## Step 3: Check Email Provider Settings

1. Go to **Authentication** → **Settings** → **Users**
2. Make sure **Email/Password** sign-in method is enabled
3. Check that **Email link (passwordless sign-in)** is configured if needed

## Step 4: Test the Reset Flow

1. Try requesting a password reset
2. Check the browser console for any errors
3. Check your email inbox AND spam/junk folder
4. Wait a few minutes - emails can sometimes be delayed

## Troubleshooting

- **Email not received**: Check spam folder, wait a few minutes, verify email address
- **"User not found" error**: Make sure you've signed up with that email first
- **"Too many requests"**: Wait a few minutes before trying again
- **Email in spam**: Mark Firebase emails as "Not Spam" to improve delivery

## Improving Email Deliverability (Reducing Spam)

### Why Emails Go to Spam

Firebase uses a generic email sender (`noreply@[project-id].firebaseapp.com`), which email providers often flag as spam because:
- It's a generic sender address
- It's not from a verified domain
- The email content is generic/template-based

### Solutions to Reduce Spam Filtering

#### Option 1: Customize Email Template (Recommended)

1. Go to Firebase Console → **Authentication** → **Templates**
2. Click on **Password reset** template
3. Customize the email:
   - **Subject**: Make it more specific (e.g., "Reset your World Attractions Explorer password")
   - **Email body**: Add your app name and branding
   - **Action URL**: Use your production domain
4. Click **Save**

**Example Subject:**
```
Reset your World Attractions Explorer password
```

**Example Email Body:**
```
Hello,

You requested to reset your password for World Attractions Explorer.

Click the link below to reset your password:
[Reset Password Button]

If you didn't request this, you can safely ignore this email.

Thanks,
World Attractions Explorer Team
```

#### Option 2: Use Custom SMTP (Advanced - Requires Firebase Blaze Plan)

For better deliverability, you can use a custom SMTP server:
1. Upgrade to Firebase Blaze plan (pay-as-you-go)
2. Configure custom SMTP in Firebase Console
3. Use a verified domain email (e.g., `noreply@yourdomain.com`)

#### Option 3: User Actions (Immediate Help)

**For Users:**
1. **Mark as "Not Spam"**: When you receive the email in spam, mark it as "Not Spam"
2. **Add to Contacts**: Add `noreply@world-attractions-explorer.firebaseapp.com` to your email contacts
3. **Create Filter**: Set up an email filter to always move Firebase emails to inbox
4. **Check Spam Folder**: Always check spam folder for the first few emails

**For Gmail:**
- Click "Not spam" button
- Or: Settings → Filters and Blocked Addresses → Create filter → Add sender → Never send to Spam

**For Outlook:**
- Right-click email → Junk → Never Block Sender

**For Apple Mail:**
- Select email → Message → Mark → Not Junk Mail

#### Option 4: Wait and Retry

- Sometimes emails are delayed by 5-10 minutes
- Check spam folder after waiting a few minutes
- Try requesting reset again if needed

### Best Practices

1. **Customize the email template** with your app name and branding
2. **Use a clear, specific subject line** (not generic "Reset password")
3. **Include your app name** in the email body
4. **Tell users to check spam folder** in your app's UI
5. **Consider upgrading to Blaze plan** for custom SMTP if spam is a major issue

## Firebase Email Limits

- **Free tier (Spark)**: Limited emails per day (varies by provider)
- **Blaze plan**: Higher limits, plus option for custom SMTP
- If you hit the limit, wait 24 hours or upgrade your Firebase plan

## Current Status

✅ **Email is being sent** (you're receiving it in spam)
⚠️ **Spam filtering** is a common issue with Firebase's default email sender
💡 **Solution**: Customize email template and have users mark as "Not Spam"

