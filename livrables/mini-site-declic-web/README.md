# Déclic Web — V1

Initiation pour les participants débutants du Module 05. Observer HTML, CSS, JavaScript et le navigateur à partir des sources fictives fournies. Production locale du 22 novembre 2026 ; les sources portent la date pédagogique du 23 novembre 2026.

## Ouvrir
Extraire entièrement `mini-site-declic-web.zip`, puis ouvrir `mini-site-declic-web/index.html` par double-clic dans un navigateur récent. Aucun serveur, compte, réseau ou installation nécessaire. Conserver les sous-dossiers ensemble lors d’un déplacement. JavaScript doit être activé pour le bouton et le quiz.

## Fichiers et modifications
- `index.html` : textes, six sections et navigation. Modifier le contenu ici.
- `css/styles.css` : mise en page, caractères, couleurs ; variables au début du fichier.
- `js/app.js` : afficher/masquer, correction et remise à zéro du quiz.
- `assets/images/affiche.svg` : copie inchangée de l’affiche.
- `pieces/fiche-web.html` : destination réelle du lien principal, copie inchangée.
- `pieces/guide-source.md` : guide original fourni, consultable comme texte.
- `README.md`, `SOURCES.md`, `CONTROLE.md` : utilisation, provenance, contrôles.

Le navigateur lit les fichiers et affiche la page. Faire une modification à la fois et comparer avant/après. Le plan demandé suit titre, accroche, problème, promesse, bénéfice et action. Les titres visibles sont adaptés à la lecture. La démonstration S17 a été consultée en lecture seule : séparation des fichiers, navigation et affichage/masquage repris comme principes ; aucune validation S17 reprise. L’affiche s’ouvre par un lien ordinaire dans le navigateur, sans fenêtre modale.

## Refaire le ZIP
Depuis le dossier `livrables`, dans PowerShell, en choisissant un nouveau nom d’archive :
```powershell
Compress-Archive -LiteralPath './mini-site-declic-web' -DestinationPath './mini-site-declic-web-copie.zip'
```
Le dossier du site doit être l’unique racine du ZIP. Extraire la nouvelle archive et refaire les essais de CONTROLE.md.

## Limites et reprise S19
Initiation uniquement : ni serveur, ni API, ni publication automatique. Aucun résultat d’apprentissage garanti. Sources fictives réutilisables dans cet atelier avec leur mention ; les droits hors atelier sont à compléter avant diffusion. Les essais visuels et clavier restent à effectuer par le participant, voir CONTROLE.md. Décision du pilote : À examiner.

Pour preuve-S18.md : reporter les fichiers obtenus et les contrôles effectivement réalisés. Pour relais-S19.md : noter vos essais réels, leurs anomalies et les améliorations souhaitées après revue. Ne pas présenter ces suggestions comme des observations déjà réalisées.

Classement conseillé : conserver le prompt personnalisé et AGENT.md dans `02-PROMPTS/`, le pack dans `04-WEB/livrables-S18/` et vos observations dans `06-PORTFOLIO/`. Aucun de ces dossiers personnels n’a été modifié automatiquement.


## Identité et partage
Logo et favicon fournis dans assets/images/. Logo dans l’en-tête et lien auteur en pied de page. index.html contient les métadonnées Open Graph et Twitter et les liens canonique et auteur. Les URL de partage désignent GitHub Pages ; les fonctions de base restent utilisables localement. Le lien auteur nécessite Internet. Les plateformes peuvent conserver leur aperçu en cache.
