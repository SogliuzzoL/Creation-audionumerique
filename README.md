# Creation AudioNumérique

Un projet Python interactif pour contrôler des paramètres audio via OSC (Open Sound Control). L'interface graphique, construite avec Pygame, permet d'ajuster en temps réel le volume maître, le volume de pistes, les paramètres d'effets (FX), ainsi que d'autres fonctions telles que la mise en sourdine des pistes.

## Description

Ce projet envoie des messages OSC via la bibliothèque [python-osc](https://pypi.org/project/python-osc/) à un serveur (par défaut à l'adresse `127.0.0.1` sur le port `8000`). Il propose une interface utilisateur simple grâce à Pygame, organisée en une grille de boutons qui permettent de :

- **Contrôler le volume maître et de piste**
- **Modifier dynamiquement les paramètres d’effets (FX)**
- **Naviguer entre différentes pistes et effets**
- **Basculer l’état de mise en sourdine d’une piste**

Le projet inclut également un fichier `Reaper.OSC` qui sert de modèle de configuration pour intégrer l’interface avec REAPER via OSC.

## Fonctionnalités

- **Intégration OSC :** Envoi de messages OSC pour commander des logiciels audio.
- **Interface Graphique :** Utilisation de Pygame pour afficher une interface interactive.
- **Contrôle en Temps Réel :** Ajustement des volumes, sélection de pistes, modification des paramètres FX et basculement de la sourdine.
- **Configuration REAPER :** Fichier `Reaper.OSC` fourni pour faciliter l'intégration avec REAPER.

## Prérequis

- Python 3.x
- [pygame](https://www.pygame.org/)
- [python-osc](https://pypi.org/project/python-osc/)
