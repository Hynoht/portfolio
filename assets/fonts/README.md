# Font Optimization

## Self-Hosted Fonts

Pour améliorer la performance (éliminer 980ms de render-blocking), ce portfolio utilise des polices self-hosted au lieu de Google Fonts CDN.

## Polices téléchargées

✅ `inter-400.woff2` - Regular (46KB)
✅ `inter-500.woff2` - Medium (74KB)
⚠️ `inter-600.woff2` - SemiBold (manquant - ~47KB)
⚠️ `inter-700.woff2` - Bold (manquant - ~48KB)

## Télécharger les polices manquantes

### Option 1: Script automatique
```bash
chmod +x download-missing-fonts.sh
./download-missing-fonts.sh
```

### Option 2: Téléchargement manuel

Visitez [Google Webfonts Helper](https://gwfh.mranftl.com/fonts/inter) et téléchargez:
- Inter SemiBold (600) - Latin
- Inter Bold (700) - Latin

Ou utilisez ces commandes:
```bash
curl -L -o assets/fonts/inter-600.woff2 \
  "https://fonts.bunny.net/inter/files/inter-latin-600-normal.woff2"

curl -L -o assets/fonts/inter-700.woff2 \
  "https://fonts.bunny.net/inter/files/inter-latin-700-normal.woff2"
```

### Option 3: Utiliser Bunny Fonts (privacy-friendly)

Alternative à Google Fonts qui ne collecte pas de données utilisateur:
```html
<link rel="preconnect" href="https://fonts.bunny.net">
<link href="https://fonts.bunny.net/css?family=inter:300,400,500,600,700" rel="stylesheet" />
```

## Performance Impact

**Avant** (Google Fonts CDN):
- Render blocking: 980ms
- External requests: 2 (googleapis.com + gstatic.com)
- GDPR concerns: ⚠️ Third-party cookies

**Après** (Self-hosted):
- Render blocking: ~0ms (avec preload)
- External requests: 0
- GDPR concerns: ✅ Aucun

## Économies de performance

- **FCP** (First Contentful Paint): -980ms
- **LCP** (Largest Contentful Paint): -490ms  
- **Network requests**: -2 requêtes
- **Privacy**: Conformité GDPR automatique
