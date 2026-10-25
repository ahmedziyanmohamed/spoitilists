# SpoitiLists — Spotify playlists and liked songs in SpotiFLAC

SpoitiLists is a free extension for SpotiFLAC Mobile that shows your Spotify playlists and saved tracks in the app.

This repo now supports the modern Spotify Web API flow and playback controls using your own Spotify Client ID entered in the extension settings at runtime.

Important:
- No Spotify key is required in the app build or extension package.
- Enter your own Client ID in SpotiFLAC settings when connecting.
- Playback support uses Spotify Web API endpoints and requires an active Spotify device.

## Features
- Home feed with your Spotify playlists
- Saved tracks / liked songs
- Playlist, album, artist, and track lookup
- Spotify OAuth PKCE login
- Playback state + play/pause/skip controls
- Runtime Client ID configuration (not baked into the build)

## Install

Open SpotiFLAC → Store → Extension Repository URL and paste:

https://raw.githubusercontent.com/ahmedziyanmohamed/spoitilists/main/registry.json

Then install SpotiLists from the list.

## Spotify setup

1. Go to https://developer.spotify.com/dashboard
2. Create an app
3. Add redirect URI:
   spotiflac://callback
4. Copy the Client ID
5. In SpotiFLAC → Settings → Extensions → SpoitiLists, paste the Client ID
6. Tap Connect to Spotify

No Client Secret is needed for this extension. The app uses PKCE and your runtime Client ID only.

## Playback support

The extension includes Web API playback helpers for:
- current playback state
- play / pause toggle
- next track
- previous track
- start a specific track

These actions require:
- valid Spotify OAuth
- user-read-playback-state scope
- user-modify-playback-state scope
- an active Spotify device playing in the background or on another device

## Build the extension package

From the repo root:

- macOS / Linux:
  chmod +x scripts/package.sh && ./scripts/package.sh

- Windows PowerShell:
  powershell -ExecutionPolicy Bypass -File scripts/package.ps1

This creates the packaged extension file and copies it into the extensions folder.

## Repo notes

- manifest.json contains the extension metadata and settings
- index.js contains the Spotify API integration and playback handlers
- registry.json is used by SpotiFLAC Store installs

## Credits

- SpotiFLAC Mobile
- Spotify Web API
- PKCE OAuth flow

License: MIT
