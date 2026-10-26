# SpoitiLists — Spotify playlists and liked songs in Mornye

SpoitiLists is a free extension for Mornye that shows your Spotify playlists and saved tracks in the app.

This repo uses the modern Spotify Web API flow and runtime Client ID setup. Your Client ID is entered in the extension settings at runtime.

Important:
- No Spotify key is required in the app build or extension package.
- Enter your own Client ID in Mornye settings when connecting.
- The OAuth redirect URI is set to mornye://callback by default.

## Features
- Home feed with your Spotify playlists
- Saved tracks / liked songs
- Playlist, album, artist, and track lookup
- Spotify OAuth PKCE login
- Runtime Client ID configuration (not baked into the build)

## Install

Open Mornye → Store → Extension Repository URL and paste:

https://raw.githubusercontent.com/ahmedziyanmohamed/spoitilists/main/registry.json

Then install SpotiLists from the list.

## Spotify setup

1. Go to https://developer.spotify.com/dashboard
2. Create an app
3. Add redirect URI:
   mornye://callback
4. Copy the Client ID
5. In Mornye → Settings → Extensions → SpoitiLists, paste the Client ID
6. Tap Connect to Spotify

No Client Secret is needed for this extension. The app uses PKCE and your runtime Client ID only.

## Build the extension package

From the repo root:

- macOS / Linux:
  chmod +x scripts/package.sh && ./scripts/package.sh

- Windows PowerShell:
  powershell -ExecutionPolicy Bypass -File scripts/package.ps1

This creates the packaged extension file and copies it into the extensions folder.

## Repo notes

- manifest.json contains the extension metadata and settings
- index.js contains the Spotify API integration and handlers
- registry.json is used by Mornye Store installs

## Credits

- Mornye
- Spotify Web API
- PKCE OAuth flow

License: MIT
