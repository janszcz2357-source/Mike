# Mike Wilds Career File

An unofficial, single-page research site about **Mike Wilds** (born Chiswick, 7 January 1946), the British racing driver who made eight Formula One World Championship entries between 1974 and 1976, raced at Le Mans seven times, won historic and endurance titles into the 2010s, and published the memoir *Life on the Wilds Side!* in 2022.

Every fact on the page is drawn from the published sources listed in its **Sources** section. Where sources disagree (Le Mans count, the 1986 C2 title, his total of championships), the page says so.

## Files

| Path | What it is |
|---|---|
| `src/page.html` | The page source: title, styles and content in one file. Edit this. |
| `build.py` | Wraps `src/page.html` in a full HTML document (doctype, meta, favicon) and writes `index.html`. |
| `index.html` | The built, standalone page. Open it in any browser or upload it to any static host. |

## Editing

1. Change text or styles in `src/page.html`. Colours and fonts are tokens at the top of the `<style>` block.
2. Run `python3 build.py`.
3. Open `index.html` to check the result.

## Deploying

`index.html` has no build step or dependencies beyond Google Fonts. It can be hosted as-is on GitHub Pages (Settings → Pages → deploy from this branch, root folder), Netlify, Vercel or Cloudflare Pages.

## Notes

- No photographs are included, because published photos of him belong to their photographers. The helmet drawing is an illustration of his yellow helmet with a ring of black diamonds.
- The page is not affiliated with or endorsed by Mike Wilds. His own site is <https://mikewilds.com/>.
