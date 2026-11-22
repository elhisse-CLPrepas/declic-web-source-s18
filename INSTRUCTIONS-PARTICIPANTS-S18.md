# Séance 18 — De vos sources à un pack mini-site

Module 05 · Challenge 100 Jours · LN-IA · Prof. Abderrahman EL HISSE  
Lundi 23 novembre 2026 · Parcours proposé : 90 minutes  
Objectif : produire une première version de votre mini-site et un pack ZIP que vous pourrez extraire, ouvrir, expliquer et reprendre en S19.

Dans `OUVRIR-SEANCE-18.html`, ouvrez **Mon carnet d’essai**. Il comporte trois étapes : « Mon projet et mes sources », « Le contenu de mon mini-site » et « Préparer la production du pack ». Les réglages avancés sont repliés ; les consignes, le prompt maître et `AGENT.md` sont consultables sous le formulaire et dans **Mes 3 documents**. **Exemples & sources** fournit quatre dossiers fictifs avec guide, affiche dédiée et prompt prérempli.

## 1. Préparer votre dossier avant la séance

Apportez un projet et au moins une source exploitable : guide, affiche, fiche, texte, PDF, photographie ou document de référence. Choisissez des documents que vous pouvez utiliser et partager. Préparez aussi votre logo et vos images si vous en avez.

Conservez les originaux. Pour chaque source, notez son titre, son auteur ou organisme, sa date si elle est connue, son fichier ou son adresse et ce que vous souhaitez en reprendre. Retirez les informations privées inutiles à la diffusion.

Retrouvez votre carnet S17, vos observations et votre plan si vous en avez préparé un. Un participant sans plan peut le rédiger pendant S18 à partir de ses propres sources.

Créez un dossier de travail personnel, distinct des ateliers du formateur :

```text
mon-projet-S18/
  entrees/                         copies des sources et visuels
  AGENT.md                        étapes de travail de l'agent
  INSTRUCTIONS-PARTICIPANTS-S18.md  parcours du participant
  PROMPT-MAITRE-PRODUCTION-S18.md   prompt personnalisé
  livrables/                      destination de production
```

Choisissez un nom court sans espaces pour votre projet, par exemple `guide-jardin`. Ne travaillez pas directement dans le mini-site de démonstration S17.

## 2. Reprendre les acquis S17 — 0 à 8 minutes

Avec le formateur, ouvrez le support de référence :

```text
D:\ATELIERS-Challenge-100-AUTOMNE\ATELIERS-MODULE-05\atelier-seance-17-ln-ia\mini-site-demonstration-seance-17\index.html
```

Ce chemin désigne l'installation du formateur. Sur votre ordinateur, utilisez la copie fournie ou le support accessible depuis l'atelier.

Repérez `index.html` pour le contenu et la structure, `css/styles.css` pour la présentation, `js/app.js` pour les interactions et `assets/` pour les images. Essayez le bouton afficher/masquer et l'agrandissement de l'affiche, à la souris puis au clavier.

Expliquez avec vos mots ce qui change dans la page et quel fichier intervient. S18 reprend cette organisation pour votre propre sujet ; les résultats des tests S17 ne valident pas votre futur site.

## 3. Définir votre mini-site — 8 à 20 minutes

Écrivez en quelques lignes :

- Mon projet et son public.
- Le besoin du lecteur et ce que le site lui permettra de comprendre ou de faire.
- Les sources disponibles, leurs limites et les éléments encore manquants.
- Mon action principale : consulter une fiche, ouvrir un guide, télécharger un document ou accéder à une information précise.

Préparez six éléments éditoriaux : titre, accroche, problème du lecteur, promesse appuyée par vos sources, bénéfice et action principale avec sa destination réelle. Ils peuvent être regroupés dans des sections adaptées au sujet.

Exemple : transformer un guide et une affiche de jardinage en un mini-site de présentation, avec une synthèse, une affiche agrandissable, des conseils tirés du guide et un bouton « Ouvrir le guide ». Cet exemple ne fournit aucun fait à réutiliser sans vérification.

## 4. Choisir la présentation — 20 à 35 minutes

Parcourez les démonstrations de l'atelier S18 si elles vous aident à démarrer. Choisissez une page principale pour une V1 simple, vos couleurs, les documents à proposer et une ou deux interactions utiles.

Vous pouvez reprendre les principes S17 : explication afficher/masquer, affiche en miniature puis agrandie, navigation par ancres. Chaque fonction doit servir votre lecteur. Une affiche ne remplace pas le texte essentiel : présentez aussi ses informations utiles sous forme lisible.

## 5. Personnaliser et lancer le prompt — 35 à 65 minutes

1. Copiez [PROMPT-MAITRE-PRODUCTION-S18.md](PROMPT-MAITRE-PRODUCTION-S18.md), [AGENT.md](AGENT.md) et ce fichier d'instructions dans votre dossier personnel. Conservez-les ensemble pour que leurs liens restent utilisables.
2. Complétez le bloc « Mon projet ». Indiquez les noms exacts des fichiers présents dans `entrees/` et la destination `livrables/`.
3. Vérifiez les sources, les droits d'utilisation, les faits, l'action principale et sa destination. Laissez « À compléter » pour une information inconnue.
4. Ouvrez votre dossier personnel dans VS Code et utilisez votre agent habituel, ou transmettez le prompt et les pièces à l'outil utilisé pendant l'atelier. Un chemin local écrit dans un message ne transmet pas le fichier : l'agent doit réellement y avoir accès.
5. Demandez à l'agent de lire les trois fichiers et d'exécuter le prompt selon les dix étapes de `AGENT.md` : création des fichiers, documentation, contrôles puis ZIP. Vous pouvez copier la consigne de lancement placée au début de `AGENT.md`. Le résultat attendu est un pack téléchargeable ou enregistré sur disque, au-delà d'une réponse présentant du code.
6. Relisez le résultat et demandez des corrections précises : information sans source, document absent, lien cassé, texte peu lisible ou interaction sans effet.

L'atelier S18 peut préparer un prompt depuis ses formulaires ; il ne lance pas lui-même l'agent de production. La génération peut se poursuivre après la séance. Si elle reste incomplète, conservez les fichiers obtenus et notez ce qui manque.

## 6. Essayer le pack — 65 à 80 minutes

Extrayez le ZIP dans un autre emplacement, puis ouvrez `index.html` dans le dossier extrait. Ne testez pas seulement la version encore ouverte dans VS Code.

- Vérifiez textes, images et fidélité aux documents apportés.
- Essayez la navigation, l'action principale, les documents et chaque interaction.
- Utilisez Tab, Entrée et Échap lorsque pertinent ; vérifiez que le focus est visible.
- Réduisez la fenêtre et essayez le zoom à 200 %.
- Vérifiez le fonctionnement de base sans connexion ; les liens vers des sites externes restent dépendants d'Internet.
- Ouvrez la console si possible et relevez les erreurs éventuelles.

Notez chaque essai réellement effectué, son résultat et les corrections attendues. Les essais du participant, ceux de l'agent et la décision du pilote restent distincts.

## 7. Conserver et remettre — 80 à 90 minutes

Remettez le dossier du mini-site et son ZIP. Ils doivent contenir les sources modifiables HTML/CSS/JS, les ressources utiles, les documents diffusables, `README.md`, `SOURCES.md` et `CONTROLE.md`.

Conservez également votre prompt personnalisé et vos pièces de suivi dans votre dossier Challenge :

```text
02-PROMPTS/prompt-maitre-mini-site-S18.md
02-PROMPTS/AGENT.md                  méthode utilisée par l'agent
04-WEB/contenu-page-projet.md
04-WEB/livrables-S18/                 dossier du site et ZIP
06-PORTFOLIO/preuve-S18.md
06-PORTFOLIO/index-portfolio.md        ajouter une entrée S18
06-PORTFOLIO/relais-S19.md
```

Dans la preuve, indiquez les fichiers produits, les sources utilisées, l'agent employé, vos essais et les limites. Dans le relais S19, listez les corrections et améliorations à poursuivre. Exportez aussi le carnet JSON si vous avez utilisé le formulaire S18.

Le binôme essaie le pack et donne un retour précis. Le pilote consigne sa propre décision ; aucun document généré ne vaut validation humaine automatique. Gardez S17, votre production S18 et les autres ateliers dans leurs dossiers respectifs.
