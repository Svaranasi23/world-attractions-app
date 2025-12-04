# Installing Node.js and npm

## Option 1: Using nvm (Node Version Manager) - Recommended

If nvm was just installed, you need to:

1. **Close and reopen your terminal**, OR run:
   ```bash
   source ~/.zshrc
   ```

2. **Load nvm and install Node.js:**
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   nvm install --lts
   nvm use --lts
   ```

3. **Verify installation:**
   ```bash
   node --version
   npm --version
   ```

## Option 2: Direct Download (Easier)

1. **Visit:** https://nodejs.org/
2. **Download** the LTS (Long Term Support) version for macOS
3. **Run the installer** and follow the prompts
4. **Restart your terminal**
5. **Verify:**
   ```bash
   node --version
   npm --version
   ```

## Option 3: Using Homebrew (if you install it)

```bash
# First install Homebrew (if not installed):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Node.js:
brew install node
```

## After Installation

Once Node.js is installed, navigate to your project and run:

```bash
cd "/Users/srivaranasi/Library/CloudStorage/GoogleDrive-pvsvnc04@gmail.com/My Drive/PVSVNC_Documents/Sri/Sri_Gigs/national-parks-app"
npm install
npm run dev
```

## Troubleshooting

- **"command not found" after installation**: Close and reopen your terminal
- **nvm not found**: Run `source ~/.zshrc` or restart terminal
- **Permission errors**: You may need to use `sudo` (not recommended) or fix permissions

