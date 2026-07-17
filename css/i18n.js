// Traductions
const translations = {
  fr: {
    // Navigation
    skip: "Aller au contenu principal",
    about: "À propos",
    experience: "Expérience",
    stats: "Statistiques",
    skills: "Compétences",
    projects: "Projets",
    achievements: "Réalisations",
    
    // Hero Section
    hello: "Bonjour, je m'appelle",
    studentAt: "Étudiant à",
    heroDesc: "Je suis motivé par la curiosité, l'apprentissage continu et l'ambition de contribuer de manière significative au monde numérique de demain.",
    github: "GitHub",
    linkedin: "LinkedIn",
    downloadCV: "Télécharger CV",
    
    // About Section
    aboutTitle: "À propos de moi",
    aboutSubtitle: "Apprenez-en davantage sur mon parcours et mes centres d'intérêt",
    journeyTitle: "Mon parcours à la 42 Antananarivo",
    journeySubtitle: "Actuellement dans le Tronc Commun depuis février 2024",
    focusAreas: "Domaines d'intérêt",
    cybersecurity: "Cybersécurité",
    cybersecurityDesc: "Passionné par la protection des systèmes et des informations",
    dataScience: "Data Science",
    dataScienceDesc: "Intérêt croissant pour la combinaison de compétences techniques et de pensée analytique pour extraire des informations à partir des données",
    formation: "Formation",
    formation42: "Tronc Commun depuis février 2024",
    formationAxian: "Certification \"Concevoir et animer des Formations\" (Juillet 2024)",
    
    // Experience Section
    experienceTitle: "Expérience professionnelle",
    experienceSubtitle: "Mes expériences et engagements",
    exp5Date: "Mars 2026 - Juillet 2026 (4 mois)",
    exp5Title: "Stagiaire - Yas Madagascar",
    exp5Company: "Yas Madagascar",
    exp5Desc: "Conception et déploiement d'un système d'authentification centralisée basé sur Keycloak, avec sécurisation d'une API OSGi Apache Karaf dans un cluster Kubernetes.",
    exp1Date: "Décembre 2025 - Janvier 2026",
    exp1Title: "Formateur - Grandir Dignement Madagascar",
    exp1Desc: "Animation de deux formations numériques (informatique, Internet, IA, prompting et éthique) pour une quinzaine de jeunes. Projet à impact social.",
    exp2Date: "Mars 2025 - Présent",
    exp2Title: "Responsable communication",
    exp2Company: "Bureau des étudiants (BDE) - 42 Antananarivo",
    exp2Desc: "Communication interne entre le BDE et les étudiants, ainsi que gestion des réseaux sociaux du BDE.",
    exp3Date: "Novembre 2024 - Juillet 2025",
    exp3Title: "Formateur - Parklife",
    exp3Desc: "Animation de deux formations informatiques pour 130 collaborateurs de Parklife : initiation aux outils numériques puis approfondissement pour renforcer leur autonomie.",
    exp4Date: "Mars 2024 - Présent",
    exp4Title: "Trésorier et Organisateur d'événements",
    exp4Company: "Bureau des étudiants (BDE) - 42 Antananarivo",
    exp4Desc: "Gestion des finances du BDE avec transparence pour réaliser des projets et offrir aux étudiants des événements et services de qualité (sorties, ateliers, conférences).",
    
    // Stats Section
    statsTitle: "Statistiques d'apprentissage",
    statsSubtitle: "Ma progression à la 42 Antananarivo",
    years: "Années",
    yearsDesc: "Expérience Tronc Commun",
    milestones: "Jalons",
    milestonesDesc: "Jalons complétés",
    overallLevel: "Niveau global",
    totalScore: "Score total",
    pointsEarned: "Points gagnés",
    levelProgress: "Progression du niveau global",
    
    // Skills Section
    skillsTitle: "Compétences",
    skillsSubtitle: "Technologies et outils que j'utilise",
    
    // Projects Section
    projectsTitle: "Projets réalisés",
    projectsSubtitle: "Mes projets techniques et créatifs",
    project1Title: "Transcendence",
    project1Desc: "Plateforme web immobilière : conception et développement d'APIs REST sécurisées avec authentification et contrôle d'accès, gestion des utilisateurs, des réservations et d'un système de crédits. Défis : modélisation des données avec Prisma et conteneurisation complète avec Docker.",
    project2Title: "Webserv",
    project2Desc: "Serveur web HTTP/1.1 écrit en C++ from scratch, sans bibliothèque externe : parsing du protocole, méthodes GET, POST et DELETE, clients simultanés gérés en I/O non bloquantes. Défi : rester conforme au protocole tout en garantissant stabilité et performance.",
    project3Title: "Inception",
    project3Desc: "Infrastructure multi-conteneurs orchestrée avec Docker Compose : chaque service tourne dans une image personnalisée écrite from scratch, sans images du Docker Hub. Défis : réseau inter-conteneurs, persistance des données et durcissement de la configuration.",
    viewCode: "Code source sur GitHub →",
    
    // Achievements Section
    achievementsTitle: "Réalisations",
    achievementsSubtitle: "Accomplissements et reconnaissances notables",
    hackathon4th: "4ème place - Hackathon Interne",
    hackathon4thDesc: "Démonstration de compétences en résolution de problèmes et travail d'équipe dans un environnement compétitif",
    viewDetails: "Voir les détails du hackathon",
    homerAward: "PRIX HOMER SIMPSON",
    homerAwardDesc: "Meilleur pitch de projet au Hackathon stupide.",
    
    // Footer
    copyright: "© 2026 Arthinez — fait à la main, sans framework. exit 0",

    // Aria labels
    ariaViewCode: "Voir le code source du projet sur GitHub (s'ouvre dans un nouvel onglet)",
    ariaGithub: "Visiter mon profil GitHub",
    ariaLinkedin: "Visiter mon profil LinkedIn",
    ariaFacebook: "Visiter ma page Facebook",
    ariaDownloadCV: "Télécharger mon CV au format PDF",
    ariaViewHackathon: "Voir les détails du hackathon (s'ouvre dans un nouvel onglet)",
    ariaToggleMenu: "Basculer le menu de navigation",
    ariaSocialNav: "Liens réseaux sociaux",
    ariaFooterSocial: "Liens réseaux sociaux du pied de page"
  },
  en: {
    // Navigation
    skip: "Skip to main content",
    about: "About",
    experience: "Experience",
    stats: "Stats",
    skills: "Skills",
    projects: "Projects",
    achievements: "Achievements",
    
    // Hero Section
    hello: "Hello, my name is",
    studentAt: "Student at",
    heroDesc: "I'm driven by curiosity, continuous learning, and the ambition to contribute meaningfully to tomorrow's digital world.",
    github: "GitHub",
    linkedin: "LinkedIn",
    downloadCV: "Download CV",
    
    // About Section
    aboutTitle: "About Me",
    aboutSubtitle: "Get to know more about my journey and interests",
    journeyTitle: "My Journey at 42 Antananarivo",
    journeySubtitle: "Currently in the Common Core since February 2024",
    focusAreas: "Focus Areas",
    cybersecurity: "Cybersecurity",
    cybersecurityDesc: "Passionate about protecting systems and information",
    dataScience: "Data Science",
    dataScienceDesc: "Growing interest in combining technical skills with analytical thinking to extract insights from data",
    formation: "Education",
    formation42: "Common Core since February 2024",
    formationAxian: "Certification \"Training Design and Delivery\" (July 2024)",
    
    // Experience Section
    experienceTitle: "Professional Experience",
    experienceSubtitle: "My experiences and commitments",
    exp5Date: "March 2026 - July 2026 (4 months)",
    exp5Title: "Intern - Yas Madagascar",
    exp5Company: "Yas Madagascar",
    exp5Desc: "Design and deployment of a centralized authentication system based on Keycloak, including securing an OSGi Apache Karaf API in a Kubernetes cluster.",
    exp1Date: "December 2025 - January 2026",
    exp1Title: "Trainer - Grandir Dignement Madagascar",
    exp1Desc: "Facilitated two digital literacy training sessions (computers, Internet, AI, prompting, and ethics) for fifteen young people. Social impact project.",
    exp2Date: "March 2025 - Present",
    exp2Title: "Communications Manager",
    exp2Company: "Student Council (BDE) - 42 Antananarivo",
    exp2Desc: "Internal communication between BDE and students, as well as managing BDE social media.",
    exp3Date: "November 2024 - July 2025",
    exp3Title: "Trainer - Parklife",
    exp3Desc: "Facilitated two computer training sessions for 130 Parklife employees: introduction to digital tools followed by advanced training to strengthen their autonomy.",
    exp4Date: "March 2024 - Present",
    exp4Title: "Treasurer and Event Organizer",
    exp4Company: "Student Council (BDE) - 42 Antananarivo",
    exp4Desc: "Managing BDE finances transparently to deliver projects and provide students with quality events and services (outings, workshops, conferences).",
    
    // Stats Section
    statsTitle: "Learning Statistics",
    statsSubtitle: "My progress at 42 Antananarivo",
    years: "Years",
    yearsDesc: "Common Core experience",
    milestones: "Milestones",
    milestonesDesc: "Completed milestones",
    overallLevel: "Overall Level",
    totalScore: "Total Score",
    pointsEarned: "Points earned",
    levelProgress: "Overall level progress",
    
    // Skills Section
    skillsTitle: "Skills",
    skillsSubtitle: "Technologies and tools I work with",
    
    // Projects Section
    projectsTitle: "Completed Projects",
    projectsSubtitle: "My technical and creative projects",
    project1Title: "Transcendence",
    project1Desc: "Real estate web platform: design and development of secure REST APIs with authentication and access control, user management, reservations, and a credit system. Challenges: data modeling with Prisma and full containerization with Docker.",
    project2Title: "Webserv",
    project2Desc: "HTTP/1.1 web server written in C++ from scratch, with no external library: protocol parsing, GET, POST and DELETE methods, simultaneous clients handled with non-blocking I/O. Challenge: staying protocol-compliant while guaranteeing stability and performance.",
    project3Title: "Inception",
    project3Desc: "Multi-container infrastructure orchestrated with Docker Compose: every service runs in a custom image written from scratch, without Docker Hub images. Challenges: inter-container networking, data persistence, and configuration hardening.",
    viewCode: "Source code on GitHub →",
    
    // Achievements Section
    achievementsTitle: "Achievements",
    achievementsSubtitle: "Notable accomplishments and recognitions",
    hackathon4th: "4th Place - Internal Hackathon",
    hackathon4thDesc: "Demonstrated problem-solving skills and teamwork in a competitive environment",
    viewDetails: "View Hackathon Details",
    homerAward: "HOMER SIMPSON AWARD",
    homerAwardDesc: "Best project pitch at the stupid Hackathon.",
    
    // Footer
    copyright: "© 2026 Arthinez — handcrafted, no framework. exit 0",

    // Aria labels
    ariaViewCode: "View the project source code on GitHub (opens in a new tab)",
    ariaGithub: "Visit my GitHub profile",
    ariaLinkedin: "Visit my LinkedIn profile",
    ariaFacebook: "Visit my Facebook page",
    ariaDownloadCV: "Download my CV in PDF format",
    ariaViewHackathon: "View hackathon details (opens in new tab)",
    ariaToggleMenu: "Toggle navigation menu",
    ariaSocialNav: "Social media links",
    ariaFooterSocial: "Footer social media links"
  }
};

// Langue par défaut
let currentLang = localStorage.getItem('lang') || 'fr';

// Fonction pour changer de langue
function setLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('lang', lang);
  document.documentElement.lang = lang;
  
  // Mettre à jour tous les éléments avec data-i18n
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (translations[lang] && translations[lang][key]) {
      element.textContent = translations[lang][key];
    }
  });
  
  // Mettre à jour les attributs aria-label
  document.querySelectorAll('[data-i18n-aria]').forEach(element => {
    const key = element.getAttribute('data-i18n-aria');
    if (translations[lang] && translations[lang][key]) {
      element.setAttribute('aria-label', translations[lang][key]);
    }
  });
  
  // Mettre à jour les Meta tags pour le SEO
  updateMetaTags(lang);
  
  // Mettre à jour l'état du sélecteur de langue
  updateLanguageSelector(lang);
}

// Mettre à jour les meta tags
function updateMetaTags(lang) {
  const metaDesc = document.querySelector('meta[name="description"]');
  const metaLang = document.querySelector('meta[name="language"]');
  const ogTitle = document.querySelector('meta[property="og:title"]');
  const ogDesc = document.querySelector('meta[property="og:description"]');
  const ogLocale = document.querySelector('meta[property="og:locale"]');
  const twitterTitle = document.querySelector('meta[name="twitter:title"]');
  const twitterDesc = document.querySelector('meta[name="twitter:description"]');
  const pageTitle = document.querySelector('title');
  
  if (lang === 'fr') {
    if (pageTitle) pageTitle.textContent = 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Développeur Full Stack, Étudiant 42 Antananarivo';
    if (metaDesc) metaDesc.setAttribute('content', 'Portfolio de Tolotra Anthony RANDRIAMBOLOLONA (Arthinez), développeur full stack et étudiant à 42 Antananarivo : projets en TypeScript, C, C++, Docker, Kubernetes, cybersécurité et data science.');
    if (metaLang) metaLang.setAttribute('content', 'French');
    if (ogTitle) ogTitle.setAttribute('content', 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Développeur Full Stack, Étudiant 42 Antananarivo');
    if (ogDesc) ogDesc.setAttribute('content', 'Développeur full stack en formation à 42 Antananarivo. Découvrez mes projets en TypeScript, C, C++, Docker, Kubernetes, cybersécurité et data science.');
    if (ogLocale) ogLocale.setAttribute('content', 'fr_FR');
    if (twitterTitle) twitterTitle.setAttribute('content', 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Développeur Full Stack, Étudiant 42 Antananarivo');
    if (twitterDesc) twitterDesc.setAttribute('content', 'Développeur full stack en formation à 42 Antananarivo : TypeScript, C, C++, Docker, Kubernetes, cybersécurité et data science.');
  } else {
    if (pageTitle) pageTitle.textContent = 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Full Stack Developer, 42 Antananarivo Student';
    if (metaDesc) metaDesc.setAttribute('content', 'Portfolio of Tolotra Anthony RANDRIAMBOLOLONA (Arthinez), full stack developer and 42 Antananarivo student: projects in TypeScript, C, C++, Docker, Kubernetes, cybersecurity and data science.');
    if (metaLang) metaLang.setAttribute('content', 'English');
    if (ogTitle) ogTitle.setAttribute('content', 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Full Stack Developer, 42 Antananarivo Student');
    if (ogDesc) ogDesc.setAttribute('content', 'Full stack developer in training at 42 Antananarivo. Discover my projects in TypeScript, C, C++, Docker, Kubernetes, cybersecurity and data science.');
    if (ogLocale) ogLocale.setAttribute('content', 'en_US');
    if (twitterTitle) twitterTitle.setAttribute('content', 'Arthinez | Tolotra Anthony RANDRIAMBOLOLONA — Full Stack Developer, 42 Antananarivo Student');
    if (twitterDesc) twitterDesc.setAttribute('content', 'Full stack developer in training at 42 Antananarivo: TypeScript, C, C++, Docker, Kubernetes, cybersecurity and data science.');
  }
}

// Mettre à jour le sélecteur de langue
function updateLanguageSelector(lang) {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.remove('active');
    if (btn.getAttribute('data-lang') === lang) {
      btn.classList.add('active');
    }
  });
}

// Initialiser la langue au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
  setLanguage(currentLang);
  
  // Ajouter les événements de clic sur les boutons de langue
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.getAttribute('data-lang');
      setLanguage(lang);
    });
  });
});
