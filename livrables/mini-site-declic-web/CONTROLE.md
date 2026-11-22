# Contrôles — Déclic Web V1

Contrôles agent exécutés le 22 novembre 2026, Windows, Python 3.14 et Node.js. Inspection des fichiers et tests avec DOM simulé : ce ne sont pas des essais navigateur.

| Vérification | Méthode et environnement | Résultat observé | Statut | Correction ou suite |
| --- | --- | --- | --- | --- |
| Structure et contenu | Analyse HTML Python ; comparaison au guide et au brief | Six sections, trois questions, action vers la fiche réelle ; mention fictive et limites conservées | Réussi | Relecture humaine à faire |
| Liens, ancres et ressources | Résolution de chaque href/src sur les deux pages HTML, identifiants uniques | 14 références valides ; aucun chemin absolu ou lien externe requis | Réussi | Refaire après modification |
| JavaScript | node --check js/app.js | Syntaxe acceptée | Réussi | Aucun correctif requis |
| Afficher/masquer et quiz | Node vm, DOM simulé, assertions | Deux bascules avec état accessible ; quiz vide, correct, incorrect, partiel et remise à zéro vérifiés | Réussi | Essayer les événements réels dans le navigateur |
| Copies des sources | Comparaison binaire Python | Affiche, fiche et guide identiques aux originaux | Réussi | Conserver les crédits |
| Périmètre des fichiers | Inventaire du pack | Neuf fichiers utiles, sans secret, dépendance, métadonnées Git ou archive imbriquée | Réussi | Aucun ajout privé |
| Archive extraite | zipfile Python, extraction dans un dossier temporaire neuf, liens recontrôlés | Une racine, fichiers extraits identiques par SHA-256 au dossier livré | Réussi | Refaire après régénération |
| Navigation et action en navigateur | Pilotage navigateur indisponible : outil node_repl absent de la session | Non observé | Non exécuté | Ouvrir la copie extraite, activer chaque ancre et Explorer les trois fichiers |
| Bouton et quiz en navigateur | Même limite ; DOM simulé seulement | Non observé dans un moteur de rendu | Non exécuté | Afficher/masquer ; corriger réponses justes, fausses et manquantes ; recommencer |
| Clavier et focus | Aucun essai navigateur | Non observé | Non exécuté | Tab puis Entrée/Espace ; suivre le focus visible ; pas de dialogue donc Échap sans objet |
| Mobile et zoom 200 % | CSS adaptatif inspecté seulement | Aucun rendu observé | Non exécuté | Tester à 375 px de large puis zoom navigateur 200 %, relever navigateur et largeur ; vérifier débordements et lisibilité |
| Console et hors ligne | Dépendances locales inspectées seulement | Aucune console observée | Non exécuté | Couper le réseau, rouvrir la copie extraite en fichier local ; parcourir pages et interactions, relever la console |

## Essais participant
Non exécuté. Extraire le ZIP dans un autre dossier, ouvrir index.html et effectuer les essais ci-dessus. Renseigner pour chaque essai la date, le navigateur et sa version, la largeur, le résultat et les corrections attendues. Les observations personnelles restent à compléter.

## Revue du pilote
Décision : À examiner. Aucune validation pédagogique, publication ou diffusion externe effectuée.

## Points pour S18 et S19
Pièces produites : site modifiable, fiche, affiche, guide, trois documents et ZIP. La preuve S18 peut citer les contrôles agent ci-dessus. Priorité S19 : exécuter les essais navigateur et clavier, puis corriger les anomalies réellement constatées. Ne pas assimiler les tests du DOM simulé aux essais humains.
