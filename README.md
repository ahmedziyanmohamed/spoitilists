# SpoitiLists — Mornye-compatible extension

This repo is the Mornye-compatible version of the Spotify library extension.

## New store format

The Mornye extension store expects a registry-style layout similar to this:

- `registry.json` contains the published extension list
- each entry includes metadata like `id`, `name`, `display_name`, `version`, `description`, `download_url`, `category`, and `tags`
- packaged extensions are placed under `extensions/`
- source and tests are kept under `sources/` and `tests/` for maintainable provider work

This project is intentionally simple at the moment, but it follows the same structure so it can be extended later without a full rewrite.

## Current package layout

- `manifest.json` — runtime extension metadata used by the app
- `index.js` — Spotify API integration and library/home feed logic
- `registry.json` — Mornye store metadata entry
- `scripts/package.sh` and `scripts/package.ps1` — build the packaged extension bundle
- `extensions/` — generated extension archive(s)

## Recommended long-term layout

A future-proof package tree should look like:

```
repo/
  README.md
  registry.json
  manifest.json
  index.js
  sources/
    spoiti-lists/
      index.js
      manifest.json
      tests/
  tests/
    spoiti-lists.test.cjs
  extensions/
    spoiti-lists.sflx
  scripts/
    build_packages.py
```

This keeps the extension store-compatible metadata separate from the provider source, and makes it easier to rebuild packages when Mornye updates the extension format.

## Spotify integration

This extension uses the Spotify Web API only for official metadata access:

- playlist listing
- saved tracks
- artist and album metadata
- search results
- home feed assembly

It does not depend on stream extraction or protected audio capture.

## Runtime Client ID

The Spotify Client ID is entered at runtime in the app settings. No secret or hardcoded key is stored in the extension build.

## Build

- macOS / Linux:
  `chmod +x scripts/package.sh && ./scripts/package.sh`

- Windows PowerShell:
  `powershell -ExecutionPolicy Bypass -File scripts/package.ps1`

## License

MIT
