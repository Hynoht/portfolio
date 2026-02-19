# 🎯 Arthinez - Portfolio

Portfolio professionnel de **Tolotra Anthony RANDRIAMBOLOLONA**, étudiant à la 42 Antananarivo Antananarivo.

[![Netlify Status](https://api.netlify.com/api/v1/badges/your-badge-id/deploy-status)](https://arthinez.netlify.app/)

## 🚀 Demo

[arthinez.netlify.app](https://arthinez.netlify.app/)

## 📋 À propos

Portfolio moderne et accessible présentant :
- Mon parcours à la 42 Antananarivo
- Mes compétences techniques (C, C++, Docker, TypeScript, etc.)
- Mes statistiques et réalisations
- Mes projets et hackathons

## 🛠️ Technologies

- **Frontend** : HTML5, CSS3, JavaScript (Vanilla)
- **Icônes** : SVG auto-hébergées (pas de dépendance externe)
- **Fonts** : Google Fonts (Inter)
- **Hébergement** : Netlify
- **Build** : Minification automatique CSS/JS

## ⚡ Performance & Optimisations

- ✅ Aucun cookie tiers (RGPD compliant)
- ✅ Accessibilité WCAG 2.1 (ARIA, navigation clavier)
- ✅ CSS/JS minifiés automatiquement sur Netlify
- ✅ Images optimisées avec attributs width/height
- ✅ Score Lighthouse optimisé
- ✅ En-têtes de sécurité HTTP

## 📦 Installation locale

```bash
# Cloner le repo
git clone https://github.com/Hynoht/portfolio.git
cd portfolio

# Option 1: Ouvrir directement dans le navigateur
open index.html

# Option 2: Utiliser un serveur local
python -m http.server 8000
# Puis ouvrir http://localhost:8000
```

## 🔨 Build (optionnel)

Pour minifier les fichiers CSS et JS localement :

```bash
# Installer les dépendances
npm install

# Build (créer styles.min.css et script.min.js)
npm run build

# Ou utiliser le script bash
./build.sh
```

**Note** : Sur Netlify, la minification est automatique via `netlify.toml` - pas besoin de build manuel.

## 📁 Structure

```
portfolio/
├── index.html              # Page principale
├── css/
│   ├── styles.css         # Styles (développement)
│   └── script.js          # Scripts (développement)
├── assets/
│   ├── cv_anthony.pdf     # CV téléchargeable
│   └── icons.svg          # Sprite d'icônes SVG
├── image/
│   └── image.jpg          # Photo de profil
├── netlify.toml           # Config Netlify (minification auto)
├── package.json           # Scripts de build
└── build.sh               # Script de build bash
```

## 🌐 Déploiement

Le site est déployé automatiquement sur Netlify à chaque push sur la branche principale.

### Configuration Netlify

Le fichier `netlify.toml` gère :
- Minification automatique CSS/JS
- En-têtes de sécurité HTTP
- Cache-Control optimisé
- Redirections SEO

## 🎨 Personnalisation

### Modifier les couleurs

Dans `css/styles.css` :

```css
:root {
  --primary-blue: #3b82f6;
  --primary-purple: #8b5cf6;
  --gradient-primary: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
}
```

### Ajouter des compétences

Dans `index.html`, section Skills :

```html
<div class="skill-badge">Nouvelle Compétence</div>
```

## 📊 SEO & Analytics

- **Structured Data** : JSON-LD pour améliorer le référencement
- **Meta Tags** : Open Graph et Twitter Card
- **Sitemap** : `sitemap.xml`
- **Robots** : `robots.txt`
- **Analytics** : Désactivé par défaut (alternatives recommandées : Plausible, Umami)

## ♿ Accessibilité

- Navigation au clavier complète
- Lecteurs d'écran compatibles (ARIA)
- Contraste conforme WCAG 2.1
- Skip link pour navigation rapide
- Reduced motion supporté
- High contrast mode supporté

## 📱 Contact

- **GitHub** : [@Hynoht](https://github.com/Hynoht)
- **LinkedIn** : [tolotra-anthony](https://www.linkedin.com/in/tolotra-anthony/)
- **Facebook** : [@arthinez](https://www.facebook.com/arthinez/)

## 📄 License

Ce projet est personnel. Tous droits réservés © 2025 Arthinez.

## 🙏 Remerciements

Réalisé dans le cadre de mon parcours à la **42 Antananarivo Antananarivo**.

---

**Arthinez** - 42 Antananarivo Developer & Cybersecurity Student
