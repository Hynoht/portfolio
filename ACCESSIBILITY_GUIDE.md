# Guide d'Accessibilité - Attributs ALT des Images

## 🎯 Bonnes Pratiques pour les Attributs ALT

### 1. **Règles Essentielles**
- **Soyez descriptif mais concis** : 100-125 caractères maximum
- **Décrivez le contenu et le contexte**, pas seulement "image"
- **Ne commencez pas par "image de"** ou "photo de" (les lecteurs d'écran le disent déjà)
- **Incluez les éléments pertinents** : personnes, actions, objets, contexte

### 2. **Exemples Pratiques pour votre Portfolio**

#### ✅ BON
```html
<!-- Image de profil -->
<img src="/image/image.webp" alt="Arthinez - Étudiant développeur à 42 School Antananarivo">

<!-- Images de projets/achievements -->
<img src="/projects/hackathon.png" alt="Équipe de développeurs travaillant sur un projet lors du hackathon interne 42">
<img src="/projects/cybersecurity.png" alt="Visualisation d'une architecture de système sécurisé">
```

#### ❌ À ÉVITER
```html
<!-- Trop vague -->
<img src="/image/image.webp" alt="profil">

<!-- Redondant -->
<img src="/image/image.webp" alt="image de Arthinez">

<!-- Trop long -->
<img src="/image/image.webp" alt="Ceci est une photo de moi, Tolotra Anthony, qui suis étudiant à 42 School et qui étudie la cybersécurité et la data science">
```

### 3. **Structure Recommandée**

Pour une image de profil :
```
[Prénom Nom] - [Titre/Rôle] à [Organisation]
```

Pour une image de projet :
```
[Nom du projet] - [Description brève de ce que montre l'image]
```

### 4. **Cas Spéciaux**

#### Images décoratives
```html
<!-- Si l'image est purement décora
tive, utilisez un alt vide -->
<img src="/decoration.svg" alt="">
```

#### Images avec texte important
```html
<!-- Incluez le texte pertinent dans l'alt -->
<img src="/achievement-badge.png" alt="Badge d'accomplissement : 4ème place au Hackathon Interne">
```

#### Logos et icônes
```html
<img src="/42-logo.png" alt="Logo de 42 School Antananarivo">
```

### 5. **Bénéfices de l'Accessibilité**

- ✅ Améliore le SEO (Google valorise l'accessibilité)
- ✅ Rend votre site accessible aux personnes malvoyantes
- ✅ Utilisé par les lecteurs d'écran
- ✅ S'affiche si l'image ne charge pas
- ✅ Améliore l'expérience utilisateur globale

### 6. **Test d'Accessibilité**

- Utilisez l'extension "Lighthouse" dans Chrome DevTools
- Testez votre site avec des lecteurs d'écran (NVDA, JAWS, VoiceOver)
- Vérifiez le contraste des couleurs (ratio minimum 4.5:1)

---

## 📋 Audit Recommandé pour Votre Portfolio

Vérifiez vos images de projet avec cette checklist :

- [ ] Toutes les images ont un attribut `alt`
- [ ] Les `alt` décrivent le contexte pertinent
- [ ] Pas de "image de" ou "photo de" en début
- [ ] Longueur < 125 caractères
- [ ] Inclut les éléments clés (sujets, actions, résultats)
- [ ] Cohérent avec le style du portfolio

