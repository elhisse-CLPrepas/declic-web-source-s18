from pathlib import Path
import shutil, json, subprocess, zipfile, tempfile, hashlib, re
from html.parser import HTMLParser

base = Path(__file__).resolve().parent
out = base / 'livrables'
out.mkdir(exist_ok=True)
name = 'mini-site-declic-web'
if (out/name).exists() or (out/(name+'.zip')).exists():
    n=2
    while (out/f'{name}-V{n}').exists() or (out/f'{name}-V{n}.zip').exists(): n+=1
    name=f'{name}-V{n}'
site=out/name
assert site.resolve().is_relative_to(base)
for d in ['css','js','assets/images','pieces']: (site/d).mkdir(parents=True,exist_ok=True)
def write(p,s): (site/p).write_text(s.strip()+'\n',encoding='utf-8')
for asset in ('logo-LN-IA.png', 'favicon.png'):
    shutil.copy2(base/'entrees'/asset,site/'assets/images'/asset)
shutil.copy2(base/'entrees/affiche.svg',site/'assets/images/affiche.svg')
shutil.copy2(base/'entrees/fiche-web.html',site/'pieces/fiche-web.html')
shutil.copy2(base/'entrees/guide-source.md',site/'pieces/guide-source.md')
write('index.html','''<!doctype html>
<html lang="fr" prefix="og: https://ogp.me/ns#">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Déclic Web : observer HTML, CSS et JavaScript dans une page locale. Exemple pédagogique fictif S18.">
<link rel="icon" type="image/png" href="assets/images/favicon.png">
<link rel="canonical" href="https://elhisse-clprepas.github.io/declic-web-source-s18/">
<link rel="author" href="https://elhisse-clprepas.github.io/auteur-ln-ia/">
<meta name="author" content="Prof. Abderrahman EL HISSE · LN-IA">
<meta name="theme-color" content="#091d35">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Déclic Web · LN-IA">
<meta property="og:title" content="Déclic Web · Observer, expliquer, essayer">
<meta property="og:description" content="Une initiation locale à HTML, CSS et JavaScript. Un support pédagogique LN-IA de Prof. Abderrahman EL HISSE.">
<meta property="og:url" content="https://elhisse-clprepas.github.io/declic-web-source-s18/">
<meta property="og:image" content="https://elhisse-clprepas.github.io/declic-web-source-s18/assets/images/logo-LN-IA.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1774">
<meta property="og:image:height" content="887">
<meta property="og:image:alt" content="Logo LN-IA bleu nuit et or sur fond blanc">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Déclic Web · LN-IA">
<meta name="twitter:description" content="Observer les rôles de HTML, CSS et JavaScript avec un support pédagogique LN-IA.">
<meta name="twitter:image" content="https://elhisse-clprepas.github.io/declic-web-source-s18/assets/images/logo-LN-IA.png">
<meta name="twitter:image:alt" content="Logo LN-IA bleu nuit et or sur fond blanc">
<title>Déclic Web · Observer, expliquer, essayer</title><link rel="stylesheet" href="css/styles.css"><script src="js/app.js" defer></script></head>
<body><a class="skip" href="#contenu">Aller au contenu</a>
<header><a class="brand" href="#titre"><img class="brand-logo" src="assets/images/logo-LN-IA.png" width="1774" height="887" alt="LN-IA"><span class="brand-name">Déclic<span>Web</span></span></a><nav aria-label="Navigation principale"><a href="#accroche">Observer</a><a href="#probleme">Comprendre</a><a href="#promesse">Essayer</a><a href="#benefice">Se tester</a><a href="#action">Explorer</a></nav></header>
<main id="contenu">
<section id="titre" class="hero" aria-labelledby="grand-titre"><div><p class="eyebrow">LN-IA · MODULE 05 · S18</p><h1 id="grand-titre">Déclic Web<span>Observer.<br>Expliquer.<br>Essayer.</span></h1><p class="lead">Trois fichiers, une page locale : un premier repère pour comprendre ce que le navigateur affiche.</p><p class="tag">Initiation · Exemple fictif</p></div><figure><a href="assets/images/affiche.svg" aria-label="Ouvrir l’affiche Déclic Web en taille réelle"><img src="assets/images/affiche.svg" width="600" height="800" alt="Affiche Déclic Web : observer, expliquer, essayer ; HTML, CSS et JavaScript."></a><figcaption>Affiche pédagogique LN-IA · Cliquez pour l’ouvrir.</figcaption></figure></section>
<section id="accroche" class="intro" aria-labelledby="titre-accroche"><p class="eyebrow">LE POINT DE DÉPART</p><h2 id="titre-accroche">Observer les rôles de trois fichiers dans une page locale.</h2><p>Ouvrez <code>index.html</code> dans votre navigateur. Repérez les trois fichiers, puis faites une modification à la fois. Comparez avant et après.</p><p class="source">D’après le guide source · SRC-01</p></section>
<section id="probleme" aria-labelledby="titre-probleme"><p class="eyebrow">COMPRENDRE LES RÔLES</p><h2 id="titre-probleme">Qui fait quoi dans la page ?</h2><p>HTML, CSS, JavaScript et le navigateur coopèrent. Voici les repères pour les distinguer.</p><div class="roles"><article><p class="file">index.html</p><h3>HTML organise.</h3><p>Repérez le titre, les paragraphes, l’image et les liens : c’est la structure du contenu.</p></article><article><p class="file">css/styles.css</p><h3>CSS présente.</h3><p>Changez une couleur dans ce fichier et observez la présentation.</p></article><article><p class="file">js/app.js</p><h3>JavaScript réagit.</h3><p>Déclenchez le bouton qui affiche puis masque une explication.</p></article></div><aside><strong>Et le navigateur ?</strong> Il lit les fichiers et affiche la page. Aucun compte ni serveur n’est requis pour ce support.</aside><p class="source">SRC-01 · SRC-03</p></section>
<section id="promesse" class="demo" aria-labelledby="titre-promesse"><div><p class="eyebrow">PASSER À L’OBSERVATION</p><h2 id="titre-promesse">Un clic, un changement visible.</h2><p>Essayez le bouton. Reliez ensuite ce changement au fichier JavaScript.</p></div><div class="experiment"><p class="file">Démonstration locale</p><button id="explication-bouton" type="button" aria-expanded="false" aria-controls="explication">Afficher une explication</button><p id="explication" hidden>HTML contient ce texte, CSS le présente et JavaScript change sa visibilité quand vous activez le bouton. Le navigateur affiche le résultat.</p><noscript><p>Activez JavaScript pour essayer le bouton et le quiz. Repère : HTML structure, CSS présente, JavaScript change la visibilité de l’explication.</p></noscript></div></section>
<section id="benefice" aria-labelledby="titre-benefice"><p class="eyebrow">RETROUVER LE BON FICHIER</p><h2 id="titre-benefice">Voir une interaction et savoir d’où elle vient.</h2><p>Vérifiez vos repères avec trois questions. La correction s’affiche ici, sans envoi de données.</p><form id="quiz"><fieldset><legend>Quel fichier organise le contenu ?</legend><label><input type="radio" name="q1" value="html"> index.html</label><label><input type="radio" name="q1" value="css"> css/styles.css</label><label><input type="radio" name="q1" value="js"> js/app.js</label><p id="r1" class="correction"></p></fieldset><fieldset><legend>Où changer une couleur ?</legend><label><input type="radio" name="q2" value="js"> js/app.js</label><label><input type="radio" name="q2" value="css"> css/styles.css</label><label><input type="radio" name="q2" value="html"> index.html</label><p id="r2" class="correction"></p></fieldset><fieldset><legend>Quel fichier affiche puis masque l’explication ?</legend><label><input type="radio" name="q3" value="css"> css/styles.css</label><label><input type="radio" name="q3" value="html"> index.html</label><label><input type="radio" name="q3" value="js"> js/app.js</label><p id="r3" class="correction"></p></fieldset><div class="quiz-actions"><button type="submit">Corriger mes réponses</button><button type="reset" class="secondary">Recommencer</button></div><p id="resultat" role="status" aria-live="polite"></p></form><p class="source">Questions créées à partir de SRC-01 · Résultat indicatif d’entraînement.</p></section>
<section id="action" class="closing" aria-labelledby="titre-action"><p class="eyebrow">À VOUS D’ESSAYER</p><h2 id="titre-action">Une modification à la fois.</h2><p>Gardez la fiche à portée de main pour repérer le contenu, changer une couleur et observer l’interaction.</p><a class="button" href="pieces/fiche-web.html">Explorer les trois fichiers</a><p class="limit">Ce parcours est une initiation. Il ne promet pas la maîtrise complète du développement web et ne traite ni serveur, ni API, ni mise en ligne automatique.</p></section>
</main><footer><p>Déclic Web · LN-IA · Création pédagogique S18, 23 novembre 2026.</p><p>Cas et documents fictifs. Réutilisation autorisée dans cet atelier avec cette mention.</p><p><a href="pieces/guide-source.md">Guide source</a> · <a href="SOURCES.md">Sources et crédits</a></p><p class="author-credit">Un support de <a href="https://elhisse-clprepas.github.io/auteur-ln-ia/" rel="author">Prof. Abderrahman EL HISSE · À propos de l’auteur</a> <span>(lien externe)</span></p></footer></body></html>''')
write('css/styles.css','''/* Modifier ces couleurs pour personnaliser la présentation. */
:root{--night:#091d35;--blue:#173d69;--gold:#f2ce83;--paper:#fff;--ink:#122b46;--muted:#496077;--line:#d3dde8}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:2rem}body{margin:0;background:var(--paper);color:var(--ink);font:1.125rem/1.7 system-ui,-apple-system,"Segoe UI",sans-serif}a{color:inherit;text-underline-offset:.23em}button,input{font:inherit}button,.button{display:inline-block;padding:.85rem 1.3rem;border:2px solid var(--gold);border-radius:.4rem;background:var(--gold);color:var(--night);font-weight:750;cursor:pointer;text-decoration:none}button:hover,.button:hover{background:#ffe4ad}button.secondary{background:transparent;color:var(--ink);border-color:var(--ink)}:focus-visible{outline:3px solid #a44c00;outline-offset:5px}header :focus-visible,.hero :focus-visible,.closing :focus-visible{outline-color:var(--gold)}.skip{position:absolute;top:-8rem;left:1rem;padding:1rem;background:#fff;z-index:10}.skip:focus{top:1rem}header{background:var(--night);color:white;display:flex;align-items:center;justify-content:space-between;gap:2rem;padding:1.4rem max(5%,calc((100% - 1160px)/2))}.brand{font-size:1.6rem;font-weight:850;text-decoration:none;white-space:nowrap}.brand span{color:var(--gold)}nav{display:flex;gap:1.4rem;flex-wrap:wrap}nav a{font-size:1rem;text-decoration:none}nav a:hover{text-decoration:underline}section{padding:5rem max(6%,calc((100% - 1120px)/2));scroll-margin-top:1rem}h1,h2,h3{line-height:1.13;letter-spacing:-.035em}h1{font-size:clamp(3rem,6vw,5.5rem);margin:1rem 0 1.5rem}h1 span{display:block;color:var(--gold);font-size:.66em;margin-top:1.1rem}h2{font-size:clamp(2rem,3.5vw,3rem);max-width:820px;margin:.6rem 0 1.5rem}h3{font-size:1.5rem}.eyebrow{font-size:.875rem;font-weight:750;letter-spacing:.12em}.hero{background:var(--night);color:white;display:grid;grid-template-columns:1.2fr .8fr;align-items:center;gap:4rem;padding-top:3rem;padding-bottom:4rem}.hero .lead{max-width:36rem;font-size:1.3rem;color:#e1e9f3}.tag{display:inline-block;border-top:1px solid #698099;padding-top:1rem;font-size:.95rem}.hero figure{margin:0;max-width:350px;justify-self:end}.hero img{width:100%;height:auto;display:block;border:1px solid #647e9c;box-shadow:14px 14px 0 #173d69}.hero figcaption{font-size:.875rem;color:#e1e9f3;margin-top:1.5rem}.intro{background:#edf3fa}.intro p:not(.eyebrow){max-width:780px}code,.file{font-family:ui-monospace,Consolas,monospace;overflow-wrap:anywhere}.file{font-size:.95rem;color:var(--blue);font-weight:700}.roles{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin:2.5rem 0}.roles article{border-top:4px solid var(--blue);padding-top:1rem}.roles article:nth-child(2){border-color:#a27322}.roles p{margin:.6rem 0}aside{background:#edf3fa;padding:1.5rem;border-left:4px solid var(--blue)}.source{font-size:.875rem;color:var(--muted)}.demo{background:#f0f4f9;display:grid;grid-template-columns:1fr 1fr;gap:3rem}.experiment{background:white;border:1px solid var(--line);padding:2rem;align-self:start;border-radius:.6rem}.experiment p[hidden]{display:none}#explication{border-top:1px solid var(--line);padding-top:1rem}form{margin-top:2rem}fieldset{border:1px solid var(--line);padding:1.2rem 1.5rem;margin:0 0 1.5rem;min-width:0}legend{font-weight:750;padding:0 .5rem}label{display:inline-flex;align-items:center;gap:.5rem;padding:.5rem 1rem .5rem 0;cursor:pointer}input{width:1.15rem;height:1.15rem;accent-color:var(--blue)}.correction{margin:.5rem 0 0;color:var(--blue);font-weight:650}.correction:empty{display:none}.quiz-actions{display:flex;gap:1rem;flex-wrap:wrap}#resultat{font-weight:750}.closing{background:var(--blue);color:white}.closing .eyebrow{color:var(--gold)}.closing>p{max-width:760px}.limit{border-top:1px solid #8194ad;padding-top:1.5rem;margin-top:2rem;font-size:1rem}footer{background:var(--night);color:#dbe5f0;padding:2rem 6%;font-size:.875rem}footer p{margin:.4rem 0}p{overflow-wrap:break-word}
@media(max-width:760px){header{align-items:flex-start;flex-direction:column;gap:.8rem}nav{gap:.6rem 1rem}.hero,.demo{grid-template-columns:1fr;gap:2rem}.hero figure{justify-self:start;max-width:280px}section{padding:3rem 6%}.roles{grid-template-columns:1fr;gap:1rem}.experiment{padding:1.3rem}label{display:flex}h1{font-size:3.4rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
/* Identité LN-IA : image complète, proportions conservées. */
.brand{display:flex;align-items:center;gap:.8rem;flex-shrink:0;font-size:1.3rem}
.brand-logo{display:block;width:132px;max-width:35vw;height:auto;background:#fff;border-radius:.25rem}
.brand .brand-name{color:#fff}.brand-name>span{color:var(--gold)}
.author-credit{font-size:1rem}.author-credit>span{font-size:.875rem}
@media(min-width:761px) and (max-width:1100px){header{align-items:flex-start;flex-direction:column;gap:1rem}}
''')
write('js/app.js','''/* Interaction 1 : garder le texte et l’état accessible synchronisés. */
'use strict';
const toggle = document.getElementById('explication-bouton');
const explanation = document.getElementById('explication');
toggle.addEventListener('click', () => {
  const expanded = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!expanded));
  explanation.hidden = expanded;
  toggle.textContent = expanded ? 'Afficher une explication' : 'Masquer l’explication';
});
/* Interaction 2 : correction locale ; aucune réponse n’est transmise. */
const quiz = document.getElementById('quiz');
const result = document.getElementById('resultat');
const answers = [
  {name:'q1', value:'html', explanation:'index.html organise le contenu.'},
  {name:'q2', value:'css', explanation:'css/styles.css règle les couleurs et la présentation.'},
  {name:'q3', value:'js', explanation:'js/app.js change la visibilité de l’explication.'}
];
quiz.addEventListener('submit', event => {
  event.preventDefault();
  let score = 0;
  let missing = 0;
  answers.forEach((answer, index) => {
    const checked = quiz.querySelector('input[name="' + answer.name + '"]:checked');
    const correct = checked && checked.value === answer.value;
    if (correct) score++;
    if (!checked) missing++;
    document.getElementById('r' + (index + 1)).textContent =
      (correct ? 'Correct. ' : checked ? 'À revoir. ' : 'Sans réponse. ') + answer.explanation;
  });
  result.textContent = score + ' / 3 bonnes réponses.' + (missing ? ' Questions sans réponse : ' + missing + '.' : '') + ' Consultez la correction sous chaque question.';
});
quiz.addEventListener('reset', () => {
  answers.forEach((_, index) => {document.getElementById('r' + (index + 1)).textContent = '';});
  result.textContent = '';
});''')
write('README.md',f'''# Déclic Web — V1

Initiation pour les participants débutants du Module 05. Observer HTML, CSS, JavaScript et le navigateur à partir des sources fictives fournies. Production locale du 22 novembre 2026 ; les sources portent la date pédagogique du 23 novembre 2026.

## Ouvrir
Extraire entièrement `{name}.zip`, puis ouvrir `{name}/index.html` par double-clic dans un navigateur récent. Aucun serveur, compte, réseau ou installation nécessaire. Conserver les sous-dossiers ensemble lors d’un déplacement. JavaScript doit être activé pour le bouton et le quiz.

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
Compress-Archive -LiteralPath './{name}' -DestinationPath './{name}-copie.zip'
```
Le dossier du site doit être l’unique racine du ZIP. Extraire la nouvelle archive et refaire les essais de CONTROLE.md.

## Limites et reprise S19
Initiation uniquement : ni serveur, ni API, ni publication automatique. Aucun résultat d’apprentissage garanti. Sources fictives réutilisables dans cet atelier avec leur mention ; les droits hors atelier sont à compléter avant diffusion. Les essais visuels et clavier restent à effectuer par le participant, voir CONTROLE.md. Décision du pilote : À examiner.

Pour preuve-S18.md : reporter les fichiers obtenus et les contrôles effectivement réalisés. Pour relais-S19.md : noter vos essais réels, leurs anomalies et les améliorations souhaitées après revue. Ne pas présenter ces suggestions comme des observations déjà réalisées.

Classement conseillé : conserver le prompt personnalisé et AGENT.md dans `02-PROMPTS/`, le pack dans `04-WEB/livrables-S18/` et vos observations dans `06-PORTFOLIO/`. Aucun de ces dossiers personnels n’a été modifié automatiquement.
''')
write('SOURCES.md','''# Sources et crédits

Le site est une synthèse pédagogique créée à partir des trois sources ci-dessous. Les questions du quiz et leurs corrections sont des reformulations du guide ; elles ne constituent pas une évaluation certifiante.

| ID | Titre et original | Auteur / date | Usage et copie dans le pack | Diffusion |
| --- | --- | --- | --- | --- |
| SRC-01 | Déclic Web — Guide source fictif ; entrees/guide-source.md | LN-IA, Module 05 S18 ; 23 novembre 2026 | Six sections, rôles, consignes, limites et correction du quiz ; pieces/guide-source.md, copie inchangée | Cas et documents inventés pour l’exercice ; réutilisation autorisée dans cet atelier avec cette mention |
| SRC-02 | Déclic Web — affiche fictive S18 ; entrees/affiche.svg | LN-IA ; date propre non indiquée | Visuel et lien taille réelle ; assets/images/affiche.svg, copie inchangée | Même ensemble pédagogique fictif ; mention du guide conservée sur le site |
| SRC-03 | Explorer les trois fichiers ; entrees/fiche-web.html | LN-IA selon le dossier ; auteur propre et date non indiqués | Destination de l’action principale ; pieces/fiche-web.html, copie inchangée | Même ensemble pédagogique fictif ; usage dans l’atelier |

Crédit : LN-IA · Module 05 · S18 · Création pédagogique. Cas, valeurs et documents inventés pour l’exercice. Réutilisation autorisée dans cet atelier avec cette mention. Autorisation hors atelier : À compléter.

Documents de cadrage lus : AGENT.md, INSTRUCTIONS-PARTICIPANTS-S18.md, PROMPT-MAITRE-PRODUCTION-S18.md, PROMPT-PERSONNALISE-S18.md et LIRE-MOI.md. Non intégrés au pack : ils restent dans le dossier source. Le brief personnalisé détermine le nom de livraison mini-site-declic-web et le quiz de trois questions, en priorité sur le modèle générique.

Référence S17 : index.html de la démonstration consulté en lecture seule, architecture HTML/CSS/JS et principes d’interaction observés. Aucun fichier S17 copié lors de la production initiale ; logo ajouté ensuite sur demande explicite du participant. Dates, liens vers l’atelier et validations S17 exclus. Aucun visuel externe, coordonnées, tarif ou témoignage ajouté.

## Identité et auteur — mise à jour
SRC-04 : logo-LN-IA.png et favicon.png, fournis par le participant pour intégration au mini-site publié. Copies inchangées : entrees/logo-LN-IA.png et entrees/favicon.png vers assets/images/ aux mêmes noms. Dimensions : 1774 × 887 pixels pour chaque fichier. Le favicon fourni est rectangulaire ; son apparence dans l’onglet reste à vérifier visuellement.

Crédit auteur : Prof. Abderrahman EL HISSE · LN-IA. Lien fourni : https://elhisse-clprepas.github.io/auteur-ln-ia/ (externe, nécessite Internet). Logo utilisé dans l’en-tête et comme image Open Graph/Twitter. Aucune licence générale supplémentaire attribuée. Cette intégration remplace l’exclusion initiale du logo S17 ; les autres fichiers S17 restent exclus.

''')
print(json.dumps({'site':str(site),'files':len(list(site.rglob('*')))},ensure_ascii=False))
