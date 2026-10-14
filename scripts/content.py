SITE_URL = "https://arthinez.netlify.app"

PERSON = {
    "name": "Tolotra Anthony RANDRIAMBOLOLONA",
    "short": "Tolotra Anthony",
    "alias": "Arthinez",
    "headline": {
        "fr": "Développeur Full-Stack",
        "en": "Full-Stack Developer",
    },
    "tagline": {
        "fr": "Full-Stack Developer · Cloud & DevOps · 42 Antananarivo · Formateur certifié Axian University",
        "en": "Full-Stack Developer · Cloud & DevOps · 42 Antananarivo · Certified Trainer at Axian University",
    },
    "location": "Antananarivo, Madagascar",
    "email": "dinandrianom@gmail.com",
    "cv": "/assets/cv_anthony.pdf",
    "social": {
        "github": "https://github.com/Hynoht",
        "linkedin": "https://www.linkedin.com/in/tolotra-anthony/",
    },
    "languages": {"fr": ["Français", "Anglais", "Malgache"], "en": ["French", "English", "Malagasy"]},
}


EXPERIENCES = [
    {
        "id": "hango",
        "group": "work",
        "title": {"fr": "Développeur junior", "en": "Junior Developer"},
        "org": "Hango",
        "start": (2026, 5),
        "end": None,
        "location": None,
        "type": {"fr": "Emploi", "en": "Job"},
        "summary": {
            "fr": "Conception d'un système de scraping qui extrait des données d'événements et les enrichit afin de les intégrer et de les afficher dans la base de données de Hango.",
            "en": "Designing a scraping system that extracts event data and enriches it so it can be stored in and displayed from Hango's database.",
        },
        "highlights": [
            {"fr": "Extraction automatisée de données d'événements depuis des sources externes",
             "en": "Automated extraction of event data from external sources"},
            {"fr": "Enrichissement des informations collectées sur chaque événement",
             "en": "Enrichment of the information collected for each event"},
            {"fr": "Intégration des événements enrichis dans la base de données de la plateforme",
             "en": "Integration of the enriched events into the platform's database"},
        ],
        "tech": [],
        "image": None,
    },
    {
        "id": "hango-front",
        "url": "https://app.hango.ch",
        "group": "work",
        "title": {"fr": "Développeur Front-End", "en": "Front-End Developer"},
        "org": "Hango",
        "start": (2026, 1),
        "end": (2026, 3),
        "location": None,
        "type": {"fr": "Emploi", "en": "Job"},
        "summary": {
            "fr": "Développement de l'interface web d'une plateforme dédiée à la découverte et à la mise en avant des événements en Suisse, permettant aux utilisateurs de trouver facilement des soirées, des sorties et des événements culturels.",
            "en": "Built the web interface of a platform for discovering and promoting events in Switzerland, helping users easily find parties, outings and cultural events.",
        },
        "highlights": [
            {"fr": "Conception et développement d'interfaces web modernes, intuitives et responsive",
             "en": "Designed and built modern, intuitive and responsive web interfaces"},
            {"fr": "Création de pages de présentation des événements et intégration de fonctionnalités de recherche et de filtrage",
             "en": "Created event pages and integrated search and filtering features"},
            {"fr": "Amélioration de l'expérience utilisateur, de la navigation et de la cohérence visuelle de la plateforme",
             "en": "Improved the platform's user experience, navigation and visual consistency"},
            {"fr": "Optimisation des performances et contribution au référencement naturel (SEO) des pages",
             "en": "Optimized performance and contributed to the pages' search engine optimization (SEO)"},
        ],
        "note": {
            "fr": "Autonomie et organisation : projet mené en parallèle de mes études à 42 Antananarivo et de mon stage professionnel, en conciliant développement web, apprentissage technique et responsabilités professionnelles.",
            "en": "Autonomy and organization: delivered alongside my studies at 42 Antananarivo and my internship, balancing web development, technical learning and professional responsibilities.",
        },
        "tech": [],
        "image": None,
    },
    {
        "id": "yas",
        "group": "work",
        "title": {"fr": "Stagiaire intégration", "en": "Integration Intern"},
        "org": "Yas Madagascar",
        "start": (2026, 3),
        "end": (2026, 7),
        "location": "Galaxy Andraharo, Antananarivo",
        "type": {"fr": "Stage", "en": "Internship"},
        "summary": {
            "fr": "Conception et déploiement d'un système d'authentification centralisée basé sur Keycloak, avec la sécurisation d'une API au sein d'un cluster Kubernetes.",
            "en": "Designed and deployed a centralized authentication system based on Keycloak, and secured an API running in a Kubernetes cluster.",
        },
        "highlights": [
            {"fr": "Mise en place d'une authentification centralisée (SSO) avec Keycloak",
             "en": "Set up centralized authentication (SSO) with Keycloak"},
            {"fr": "Sécurisation d'une API existante",
             "en": "Secured an existing API"},
            {"fr": "Déploiement dans un cluster Kubernetes",
             "en": "Deployment in a Kubernetes cluster"},
        ],
        "tech": ["Keycloak", "Kubernetes"],
        "image": None,
    },
    {
        "id": "42-transcender",
        "group": "school",
        "title": "Transcender",
        "org": "42 Antananarivo",
        "start": (2026, 3),
        "end": None,
        "location": "Antananarivo",
        "type": {"fr": "Cursus", "en": "Curriculum"},
        "summary": {
            "fr": "Étape du cursus 42 atteinte après la validation du Tronc Commun, clôturé par le projet Transcendence.",
            "en": "42 curriculum stage reached after completing the Common Core, concluded by the Transcendence project.",
        },
        "highlights": [],
        "tech": [],
        "image": None,
    },
    {
        "id": "42-cadet",
        "group": "school",
        "title": {"fr": "Cadet — Tronc Commun", "en": "Cadet — Common Core"},
        "org": "42 Antananarivo",
        "start": (2024, 2),
        "end": (2026, 3),
        "location": "Antananarivo",
        "type": {"fr": "Cursus", "en": "Curriculum"},
        "summary": {
            "fr": "Formation au sein de 42, école reconnue pour sa pédagogie 100 % pratique et collaborative : résolution de problèmes complexes par projets, en peer-learning, avec des bases solides en C, Linux et algorithmique.",
            "en": "Training at 42, a school known for its fully hands-on, peer-to-peer pedagogy: solving complex problems through projects, with solid foundations in C, Linux and algorithms.",
        },
        "highlights": [],
        "tech": ["C", "C++", "Linux", {"fr": "Algorithmique", "en": "Algorithms"}],
        "image": None,
    },
]


BDE_ROLES = [
    {
        "title": {"fr": "Trésorier", "en": "Treasurer"},
        "start": (2024, 3),
        "end": (2026, 9),
        "summary": {
            "fr": "Gestion saine et transparente des finances pour permettre au BDE de mener ses projets et d'offrir aux étudiants des événements et services de qualité (sorties, ateliers, conférences).",
            "en": "Sound and transparent financial management so the Student Council could run its projects and offer students quality events and services (outings, workshops, talks).",
        },
    },
    {
        "title": {"fr": "Responsable communication", "en": "Communications Manager"},
        "start": (2025, 3),
        "end": (2026, 9),
        "summary": {
            "fr": "Communication interne entre le BDE et les étudiants, et gestion des réseaux sociaux du BDE.",
            "en": "Internal communication between the Student Council and students, and management of its social media.",
        },
    },
]

BDE = {
    "id": "bde",
    "org": {"fr": "Bureau des Étudiants — 42 Antananarivo", "en": "Student Council (BDE) — 42 Antananarivo"},
    "start": (2024, 3),
    "end": (2026, 9),
    "skills": [
        {"fr": "Gestion financière", "en": "Financial management"},
        {"fr": "Communication", "en": "Communication"},
        {"fr": "Organisation d'événements", "en": "Event organization"},
        {"fr": "Travail d'équipe", "en": "Teamwork"},
    ],
    "image": {
        "src": "beyond-the-game", "w": 800, "h": 600, "sizes": [480, 800],
        "alt": {"fr": "Étudiants réunis autour des postes de jeu lors de l'événement Beyond the Game organisé par le BDE de 42 Antananarivo",
                "en": "Students gathered around gaming stations at the Beyond the Game event run by the 42 Antananarivo Student Council"},
    },
}

EVENTS = [
    {
        "id": "beyond-the-game",
        "title": "Beyond the Game",
        "date": {"fr": "22 novembre 2025", "en": "November 22, 2025"},
        "iso": "2025-11-22",
        "place": "42 Antananarivo, Galaxy Andraharo",
        "partners": ["Mass'in", "Malagasy Federation of Esports", "Yas Madagascar", "SOKA"],
        "summary": {
            "fr": "Journée gaming organisée par le BDE : tournois Tekken 8 et FC25, présentation de jeux créés par des étudiants de 42 et free play.",
            "en": "Gaming day run by the Student Council: Tekken 8 and FC25 tournaments, showcase of games made by 42 students and free play.",
        },
        "image": {
            "src": "beyond-the-game-affiche", "w": 480, "h": 605, "sizes": [480], "pos": "50% 30%",
            "alt": {"fr": "Affiche de l'événement Beyond the Game du 22 novembre 2025 à 42 Antananarivo",
                    "en": "Poster for the Beyond the Game event on November 22, 2025 at 42 Antananarivo"},
        },
    },
    {
        "id": "bcode-mada",
        "title": "BCode Mada",
        "date": {"fr": "20 juin 2026", "en": "June 20, 2026"},
        "iso": "2026-06-20",
        "place": "42 Antananarivo",
        "summary": {
            "fr": "Tournoi de programmation organisé avec AlgoMada, accueilli par 42 Antananarivo avec le soutien officiel de Yas.",
            "en": "Programming contest organized with AlgoMada, hosted by 42 Antananarivo with official support from Yas.",
        },
        "image": {
            "src": "bcode-mada", "w": 800, "h": 800, "sizes": [480, 800], "pos": "50% 35%",
            "alt": {"fr": "Affiche du tournoi de programmation BCode Mada du 20 juin 2026",
                    "en": "Poster for the BCode Mada programming contest on June 20, 2026"},
        },
    },
    {
        "id": "trail-kvaa-2025",
        "title": "Trail KVAA 2025",
        "date": {"fr": "2025", "en": "2025"},
        "iso": "2025",
        "place": {"fr": "Station forestière d'Angavokely", "en": "Angavokely forest station"},
        "summary": {
            "fr": "Participation au trail avec l'équipe du BDE 404.42 et aide à l'organisation : une expérience humaine faite de rencontres, de sourires et de convivialité.",
            "en": "Took part in the trail with the 404.42 Student Council team and helped with the organization: a human experience full of encounters, smiles and friendliness.",
        },
        "link": "https://www.facebook.com/permalink.php?story_fbid=pfbid0cHuTBYfyiXwv8aD8KywzuStXsVkCkqmMMdAPs3tmAMPQQxPJ2e3m2XqDPhn5tvkKl&id=61559375627522",
        "image": {
            "src": "trail-kvaa-2025", "w": 480, "h": 599, "sizes": [480], "pos": "50% 50%",
            "alt": {"fr": "L'équipe du BDE 404.42 sous la banderole d'arrivée du trail KVAA 2025, à la station forestière d'Angavokely",
                    "en": "The 404.42 Student Council team under the finish banner of the KVAA 2025 trail at the Angavokely forest station"},
        },
    },
]

TRAININGS = [
    {
        "id": "parklife",
        "org": "Parklife",
        "title": {"fr": "Formateur — initiation à l'informatique", "en": "Trainer — introduction to computing"},
        "sessions": [
            {"start": (2024, 11), "end": (2024, 12),
             "text": {"fr": "Formation d'initiation à l'informatique pour le personnel de Parklife : les bases essentielles pour mieux maîtriser les outils numériques au quotidien.",
                      "en": "Introductory computer training for Parklife staff: the essential basics to use digital tools confidently every day."}},
            {"start": (2025, 5), "end": (2025, 7),
             "text": {"fr": "Deuxième session approfondissant les notions de la première formation, pour rendre les participants plus autonomes.",
                      "en": "A second session deepening the first training's content to make participants more autonomous."}},
        ],
        "impact": {"fr": "130 collaborateurs formés", "en": "130 employees trained"},
        "skills": [{"fr": "Pédagogie", "en": "Teaching"}, {"fr": "Accessibilité numérique", "en": "Digital inclusion"}],
        "image": {
            "src": "formation-parklife", "w": 480, "h": 638, "sizes": [480], "pos": "50% 55%",
            "alt": {"fr": "Participants de la formation Parklife sur les postes informatiques de 42 Antananarivo",
                    "en": "Parklife training participants at the 42 Antananarivo computer lab"},
        },
    },
    {
        "id": "grandir-dignement",
        "org": "Grandir Dignement Madagascar",
        "title": {"fr": "Formateur — numérique et IA", "en": "Trainer — digital skills and AI"},
        "sessions": [
            {"start": (2025, 12), "end": (2025, 12),
             "text": {"fr": "Deux jours de formation pour initier des jeunes à l'informatique et à l'usage d'Internet, dans le cadre d'un projet à impact social.",
                      "en": "Two training days introducing young people to computers and the Internet, as part of a social impact project."}},
            {"start": (2026, 1), "end": (2026, 1),
             "text": {"fr": "Deuxième formation : concepts clés de l'intelligence artificielle, techniques de prompting et bonnes pratiques éthiques, pour développer esprit critique et autonomie.",
                      "en": "Second training: key AI concepts, prompting techniques and ethical practices, to build critical thinking and autonomy."}},
        ],
        "impact": {"fr": "Une quinzaine de jeunes accompagnés", "en": "Around fifteen young people trained"},
        "skills": [{"fr": "Pédagogie", "en": "Teaching"}, {"fr": "IA & prompting", "en": "AI & prompting"}],
        "image": {
            "src": "formation-grandir-dignement", "w": 480, "h": 640, "sizes": [480], "pos": "50% 30%",
            "alt": {"fr": "Un jeune participant prend la parole au micro à 42 Antananarivo",
                    "en": "A young participant speaking into a microphone at 42 Antananarivo"},
        },
    },
]


PROJECT_FILTERS = [
    ("all", {"fr": "Tous", "en": "All"}),
    ("school", {"fr": "Cursus 42", "en": "42 curriculum"}),
    ("work", {"fr": "Professionnel", "en": "Professional"}),
    ("hackathon", {"fr": "Hackathons", "en": "Hackathons"}),
]

PROJECTS = [
    {
        "id": "hango-scraping",
        "cat": "work",
        "title": {"fr": "Scraping et enrichissement d'événements", "en": "Event scraping and enrichment"},
        "context": {"fr": "Hango, 2026 — en cours", "en": "Hango, 2026 — in progress"},
        "summary": {
            "fr": "Système de scraping qui extrait des données d'événements, les enrichit puis les intègre dans la base de données de Hango pour les afficher sur la plateforme.",
            "en": "Scraping system that extracts event data, enriches it and loads it into Hango's database so the events can be shown on the platform.",
        },
        "tech": [{"fr": "Scraping", "en": "Web scraping"}, {"fr": "Enrichissement de données", "en": "Data enrichment"}, {"fr": "Base de données", "en": "Database"}],
        "links": [],
        "icon": "database",
    },
    {
        "id": "keycloak-sso",
        "cat": "work",
        "title": {"fr": "Authentification centralisée Keycloak", "en": "Centralized authentication with Keycloak"},
        "context": {"fr": "Stage — Yas Madagascar, 2026", "en": "Internship — Yas Madagascar, 2026"},
        "summary": {
            "fr": "Conception et déploiement d'un système d'authentification centralisée, et sécurisation d'une API dans un cluster Kubernetes.",
            "en": "Design and deployment of a centralized authentication system, and securing an API in a Kubernetes cluster.",
        },
        "tech": ["Keycloak", "Kubernetes"],
        "links": [],
        "icon": "shield",
    },
    {
        "id": "transcendence",
        "cat": "school",
        "title": "Transcendence",
        "context": {"fr": "Projet de fin de Tronc Commun — 42", "en": "Common Core final project — 42"},
        "summary": {
            "fr": "Plateforme web immobilière : APIs REST sécurisées avec authentification et contrôle d'accès, gestion des utilisateurs, des réservations et d'un système de crédits. Défis : modélisation des données avec Prisma et conteneurisation complète avec Docker.",
            "en": "Real estate web platform: secure REST APIs with authentication and access control, user management, reservations and a credit system. Challenges: data modeling with Prisma and full containerization with Docker.",
        },
        "tech": ["TypeScript", "Fastify", "Prisma", "Docker"],
        "links": [],
        "icon": "code",
    },
    {
        "id": "webserv",
        "cat": "school",
        "title": "Webserv",
        "context": {"fr": "Cursus 42 — réseau", "en": "42 curriculum — networking"},
        "summary": {
            "fr": "Serveur HTTP/1.1 écrit en C++ from scratch, sans bibliothèque externe : parsing du protocole, méthodes GET, POST et DELETE, clients simultanés gérés en I/O non bloquantes.",
            "en": "HTTP/1.1 server written in C++ from scratch with no external library: protocol parsing, GET, POST and DELETE methods, concurrent clients handled with non-blocking I/O.",
        },
        "tech": ["C++", "HTTP/1.1", {"fr": "Sockets", "en": "Sockets"}],
        "links": [],
        "icon": "server",
    },
    {
        "id": "inception",
        "cat": "school",
        "title": "Inception",
        "context": {"fr": "Cursus 42 — administration système", "en": "42 curriculum — system administration"},
        "summary": {
            "fr": "Infrastructure multi-conteneurs orchestrée avec Docker Compose : chaque service tourne dans une image personnalisée écrite from scratch, sans images du Docker Hub. Défis : réseau inter-conteneurs, persistance des données et durcissement de la configuration.",
            "en": "Multi-container infrastructure orchestrated with Docker Compose: every service runs in a custom image written from scratch, without Docker Hub images. Challenges: inter-container networking, data persistence and configuration hardening.",
        },
        "tech": ["Docker", "Docker Compose", "Linux", "NGINX"],
        "links": [],
        "icon": "box",
    },
    {
        "id": "hackathon-42",
        "cat": "hackathon",
        "title": {"fr": "Hackathon interne 42 — 4e place", "en": "42 internal hackathon — 4th place"},
        "context": {"fr": "Compétition en équipe — 42 Antananarivo", "en": "Team competition — 42 Antananarivo"},
        "summary": {
            "fr": "Prototypage rapide et travail d'équipe sous contrainte de temps, dans un environnement compétitif.",
            "en": "Rapid prototyping and teamwork under time pressure in a competitive setting.",
        },
        "tech": [],
        "links": [("details", "https://hackathon42.netlify.app/")],
        "image": {
            "src": "hackathon-42", "w": 1200, "h": 900, "sizes": [640, 1200], "pos": "50% 50%",
            "alt": {"fr": "L'équipe lauréate du hackathon interne de 42 Antananarivo posant devant une bannière Telma",
                    "en": "The 42 Antananarivo internal hackathon team posing in front of a Telma banner"},
        },
    },
    {
        "id": "stupid-hackathon",
        "cat": "hackathon",
        "title": {"fr": "Prix Homer Simpson — Stupid Hackathon", "en": "Homer Simpson Award — Stupid Hackathon"},
        "context": {"fr": "Distinction", "en": "Award"},
        "summary": {
            "fr": "Récompense du meilleur pitch de projet.",
            "en": "Awarded for the best project pitch.",
        },
        "tech": [],
        "links": [],
        "icon": "trophy",
    },
]


SKILL_GROUPS = [
    {
        "id": "web",
        "icon": "code",
        "title": {"fr": "Développement web & full-stack", "en": "Web & full-stack development"},
        "items": ["TypeScript", "JavaScript", "Node.js", "Fastify", "Next.js", "Prisma ORM", "PostgreSQL", "HTML", "CSS"],
    },
    {
        "id": "devops",
        "icon": "cloud",
        "title": {"fr": "Cloud, DevOps & sécurité", "en": "Cloud, DevOps & security"},
        "items": ["Docker", "Docker Compose", "Kubernetes", "Keycloak", "NGINX"],
    },
    {
        "id": "systems",
        "icon": "cpu",
        "title": {"fr": "Programmation système", "en": "Systems programming"},
        "items": ["C", "C++", "Linux / Unix", {"fr": "Algorithmique", "en": "Algorithms"}, "HTTP / sockets"],
    },
    {
        "id": "soft",
        "icon": "users",
        "title": {"fr": "Compétences transverses", "en": "Soft skills"},
        "items": [
            {"fr": "Conception et animation de formations", "en": "Training design and delivery"},
            {"fr": "Communication", "en": "Communication"},
            {"fr": "Gestion financière associative", "en": "Non-profit financial management"},
            {"fr": "Organisation d'événements", "en": "Event organization"},
            {"fr": "Travail d'équipe & peer-learning", "en": "Teamwork & peer learning"},
        ],
    },
]


LEARNING = {"Kubernetes"}

FEATURED_TECH = [("c", "C"), ("cpp", "C++"), ("docker", "Docker"), ("linux", "Linux")]


EDUCATION = [
    {
        "org": "42 Antananarivo",
        "title": {"fr": "Technologie informatique — Cadet puis Transcender", "en": "Computer technology — Cadet, then Transcender"},
        "period": {"fr": "Depuis février 2024", "en": "Since February 2024"},
    },
    {
        "org": "AXIAN University",
        "title": {"fr": "Certification « Concevoir et animer des formations »", "en": "Certification “Designing and delivering training”"},
        "period": {"fr": "Juillet 2024", "en": "July 2024"},
    },
]

INTERESTS = [
    {"icon": "shield", "title": {"fr": "Cybersécurité", "en": "Cybersecurity"},
     "text": {"fr": "La protection des systèmes et des informations, de l'authentification à l'infrastructure.",
              "en": "Protecting systems and information, from authentication to infrastructure."}},
    {"icon": "cloud", "title": {"fr": "Cloud & DevOps", "en": "Cloud & DevOps"},
     "text": {"fr": "Conteneurisation, orchestration et déploiement d'applications fiables.",
              "en": "Containerization, orchestration and reliable application delivery."}},
    {"icon": "chart", "title": {"fr": "Data science", "en": "Data science"},
     "text": {"fr": "Allier compétences techniques et pensée analytique pour tirer des enseignements des données.",
              "en": "Combining technical skills and analytical thinking to extract insights from data."}},
]
