# Arthinez — Portfolio

Portfolio de **Tolotra Anthony RANDRIAMBOLOLONA** (Arthinez), développeur full-stack à Antananarivo.

🔗 [arthinez.netlify.app](https://arthinez.netlify.app/) — version anglaise : [/en/](https://arthinez.netlify.app/en/)

## Pages

| Page | FR | EN |
|------|----|----|
| Accueil | `/` | `/en/` |
| Expériences professionnelles | `/experiences/` | `/en/experience/` |
| Engagements associatifs | `/engagements/` | `/en/involvement/` |
| Projets (avec filtres) | `/projets/` | `/en/projects/` |
| Compétences | `/competences/` | `/en/skills/` |
| À propos | `/a-propos/` | `/en/about/` |
| Contact | `/contact/` | `/en/contact/` |

## Stack

- HTML/CSS/JavaScript vanilla, sans framework ni dépendance côté client
- Pages statiques **générées** par un script Python sans dépendance (`scripts/build_site.py`)
- Polices variables auto-hébergées (Jost + Inter), images WebP optimisées
- Hébergement Netlify (en-têtes de sécurité et de cache dans `_headers`)

## Modifier le contenu

Tout le contenu (expériences, engagements, projets, compétences, en FR et en EN) se trouve dans
**`scripts/content.py`**. Ne modifiez pas les fichiers HTML générés à la main.

```bash
python3 scripts/build_site.py   # régénère les 14 pages, 404.html, sitemap.xml et llms.txt
python3 -m http.server 8000     # aperçu local sur http://localhost:8000
```

Les fichiers générés sont commités : Netlify sert le dépôt tel quel. Les URL de `styles.css`
et de `script.js` portent un hash de leur contenu (`?v=…`), ce qui invalide le cache à chaque
régénération.

## Structure

```
scripts/content.py      contenu (source unique, FR/EN)
scripts/build_site.py   gabarits, composants et génération
css/styles.css          système de design (tokens, composants)
css/fonts.css           @font-face Jost / Inter
css/script.js           menu mobile, filtres, apparitions
assets/img/             images optimisées (WebP) utilisées par le site
assets/fonts/           polices variables woff2
images/                 photos originales (conservées telles quelles)
image/                  portrait original, icônes PWA, logos techniques
```

Pour ajouter une image : placez l'original dans `images/`, créez des variantes WebP dans
`assets/img/` (`nom-480.webp`, `nom-800.webp`), référencez-les dans `content.py` avec un `alt`
en FR et en EN, puis relancez le script.

## SEO, GEO et accessibilité

- Titre, description, URL canonique, `hreflang` FR/EN et Open Graph propres à chaque page
- JSON-LD : `Person`, `WebSite`, `ProfilePage`, `BreadcrumbList`, `SoftwareSourceCode`, `Event`
- `sitemap.xml` avec alternates de langue, `llms.txt` généré à partir du contenu
- HTML sémantique, lien d'évitement, navigation au clavier, focus visible
- Contrastes WCAG AA, textes alternatifs, `prefers-reduced-motion` respecté

## Contact

- **GitHub** : [@Hynoht](https://github.com/Hynoht)
- **LinkedIn** : [tolotra-anthony](https://www.linkedin.com/in/tolotra-anthony/)

© 2026 Arthinez. Tous droits réservés.
