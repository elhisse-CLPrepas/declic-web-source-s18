# Déclic Web — Sources et mini-site S18

Exemple pédagogique fictif LN-IA, Module 05 : comprendre les rôles de HTML, CSS, JavaScript et du navigateur.

## Consulter le mini-site

Ouvrir `livrables/mini-site-declic-web/index.html` dans un navigateur, ou extraire `livrables/mini-site-declic-web.zip` puis ouvrir son `index.html`. Aucun serveur ni installation nécessaire.

## Organisation

- `entrees/` : guide, affiche et fiche fournis, conservés dans leur état original.
- `livrables/mini-site-declic-web/` : site modifiable et documents README, SOURCES et CONTROLE.
- `livrables/mini-site-declic-web.zip` : pack autonome contrôlé après extraction.
- `PROMPT-PERSONNALISE-S18.md` : brief du projet ; les autres documents S18 expliquent la méthode.
- `produire-declic.py` : génération locale ; crée une nouvelle version si la destination existe déjà.
- `controler-declic.py` : contrôle de la V1 avec Python et Node.js ; refuse de remplacer une archive existante sauf avec l’option explicite `--rebuild-archive`.

Le rapport `livrables/mini-site-declic-web/CONTROLE.md` distingue les contrôles exécutés des essais navigateur restant à effectuer. La validation pédagogique reste à examiner par le pilote.

## Réutilisation

Cas et documents fictifs. Réutilisation autorisée dans cet atelier avec cette mention. Les crédits et limites figurent dans `livrables/mini-site-declic-web/SOURCES.md`. Les droits de diffusion hors atelier restent à compléter ; aucune licence générale supplémentaire n’est attribuée par ce dépôt.

## Publication GitHub Pages

Le workflow `.github/workflows/pages.yml` publie `livrables/mini-site-declic-web/` sur GitHub Pages. Il se declenche lors des modifications de ce dossier ou du workflow sur `main`, et peut etre lance manuellement depuis Actions.

Adresse prevue : https://elhisse-clprepas.github.io/declic-web-source-s18/

Pour publier une correction, modifier le mini-site dans ce dossier, creer un commit et pousser sur `main`. Verifier ensuite la reussite du workflow dans Actions. Les sources de travail et le ZIP restent dans le depot.

## Logo et partage

Les images LN-IA fournies sont conservées dans `entrees/` et copiées dans le mini-site. Le logo figure dans l’en-tête et dans les métadonnées Open Graph/Twitter ; le pied de page renvoie à [l’auteur](https://elhisse-clprepas.github.io/auteur-ln-ia/). Après modification de la V1, exécuter `python controler-declic.py --rebuild-archive` pour contrôler et mettre à jour le ZIP.
