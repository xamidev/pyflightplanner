# Cahier des charges

Le programme doit pouvoir faire un dossier complet de vol pour l'aviation légère en VFR. (SportStar RTC pour l'instant)

Dans ce dossier il y aura:
- calcul de carburant
- météo
- notams
- masse et centrage

Le programme utilisera la bibliothèque Scrapy pour trouver des informations météo, notam.. sur Internet.

### Idées

- on pourra faire des classes avion avec de la POO (classe avion etc) afin de supporter le plus de modèles possibles
- lire les cartes avec une IA et faire une route simplement a partir de l'aérodrome de départ et d'arrivée (tensorflow?)
- prendre en compte les zones interdites, SUP AIP etc
- interface graphique
- configuration de profils d'avions ou d'aérodromes et stockage dans une db Sqlite
- fabrication et impression automatisée d'un log de navigation