# GitHub Upload Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the "+" icon → "New repository"
3. Name: `us-national-parks-map` (or your choice)
4. Description: "Interactive map of US and Canadian National Parks"
5. Choose Public or Private
6. **DO NOT** check "Initialize with README" (we already have one)
7. Click "Create repository"

## Step 2: Push to GitHub

After creating the repository, run these commands (replace `YOUR_USERNAME` with your GitHub username):

```bash
cd "/Users/srivaranasi/Library/CloudStorage/GoogleDrive-pvsvnc04@gmail.com/My Drive/PVSVNC_Documents/Sri/Sri_Gigs/US national parks"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/Svaranasi23/us-national-parks-map.git

# Rename branch to main if needed (GitHub uses 'main' by default)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Alternative: Using SSH (if you have SSH keys set up)

```bash
git remote add origin git@github.com:Svaranasi23/us-national-parks-map.git
git branch -M main
git push -u origin main
```

## Step 3: Verify

After pushing, refresh your GitHub repository page. You should see all your files!

## Future Updates

To push future changes:

```bash
git add .
git commit -m "Description of your changes"
git push
```

## Troubleshooting

If you get authentication errors:
- Use GitHub Personal Access Token instead of password
- Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

