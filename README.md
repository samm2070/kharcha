# Kharcha 💸 — Personal Expense Tracker PWA

A mobile-first PWA to track your monthly food expenses.

## Files
```
kharcha-pwa/
├── index.html       ← The entire app
├── manifest.json    ← PWA config
├── sw.js            ← Service worker (offline support)
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

---

## How to host for free (GitHub Pages) — 5 min setup

1. Go to https://github.com and create a new repository, name it `kharcha`
2. Upload all files (drag & drop the entire folder contents)
3. Go to **Settings → Pages → Source → Deploy from branch → main → / (root)**
4. Your app will be live at: `https://YOUR-USERNAME.github.io/kharcha`

## Install on Android phone

1. Open Chrome on your phone
2. Visit your GitHub Pages URL
3. Tap the **⋮ menu → Add to Home screen**
4. Done! It works like a real app, even offline.

## Install on iPhone (iOS Safari)

1. Open Safari → visit your URL
2. Tap the **Share button → Add to Home Screen**

---

## Features
- Monthly budget with live balance
- Log hostel food (free) or outside meals (enter amount)
- GitHub-style heatmap — green = hostel day, red = expensive day
- Tap any past day to see/delete entries
- Works fully offline after first load
- Data stored on your phone (localStorage)
