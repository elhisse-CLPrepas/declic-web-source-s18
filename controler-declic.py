from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re, subprocess, json, zipfile, tempfile, hashlib, sys
base=Path(__file__).resolve().parent
site=base/'livrables/mini-site-declic-web'
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=[]; self.refs=[]; self.sections=0; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='section':self.sections+=1
        for key in ['href','src']:
            if key in a:self.refs.append(a[key])
def check(root):
    pages={p:Page(p.read_text(encoding='utf-8')) for p in root.rglob('*.html')}
    count=0
    for p,doc in pages.items():
        assert len(doc.ids)==len(set(doc.ids)),f'Duplicate ID {p}'
        for ref in doc.refs:
            u=urlsplit(ref)
            if u.scheme or u.netloc:
                assert ref in {'https://elhisse-clprepas.github.io/declic-we-source-s18/', 'https://elhisse-clprepas.github.io/auteur-ln-ia/'}, ref
                continue
            assert not u.path.startswith('/'),ref
            target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
            assert target.is_relative_to(root.resolve()) and target.is_file(),ref
            if u.fragment:
                other=pages.get(target) or Page(target.read_text(encoding='utf-8'))
                assert u.fragment in other.ids,ref
            count+=1
    assert pages[root/'index.html'].sections==6
    assert len(re.findall(r'<fieldset>',(root/'index.html').read_text(encoding='utf-8')))==3
    return count
links=check(site)
import struct
for asset in ('logo-LN-IA.png', 'favicon.png'):
    assert (base/'entrees'/asset).read_bytes()==(site/'assets/images'/asset).read_bytes()
    assert struct.unpack('>II', (site/'assets/images'/asset).read_bytes()[16:24])==(1774,887)
html=(site/'index.html').read_text(encoding='utf-8')
for field in ('og:title','og:type','og:url','og:image','og:image:width','og:image:height','og:image:alt'):
    assert len(re.findall('property="'+field+'"', html))==1, field
assert 'rel="author"' in html and 'rel="icon"' in html

subprocess.run(['node','--check',str(site/'js/app.js')],check=True)
test=r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
function element(){return {textContent:'',hidden:true,attrs:{'aria-expanded':'false'},handlers:{},addEventListener(n,f){this.handlers[n]=f},getAttribute(n){return this.attrs[n]},setAttribute(n,v){this.attrs[n]=v}}}
const ids={};for(const id of ['explication-bouton','explication','quiz','resultat','r1','r2','r3'])ids[id]=element();
let selections={};ids.quiz.querySelector=s=>{const name=s.match(/name="(q\d)"/)[1];return selections[name]?{value:selections[name]}:null};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{document:{getElementById:id=>ids[id]}});
const button=ids['explication-bouton'];button.handlers.click();assert.equal(button.attrs['aria-expanded'],'true');assert.equal(ids.explication.hidden,false);assert.equal(button.textContent,'Masquer l’explication');button.handlers.click();assert.equal(button.attrs['aria-expanded'],'false');assert.equal(ids.explication.hidden,true);
let prevented=false;const submit=()=>ids.quiz.handlers.submit({preventDefault(){prevented=true}});
submit();assert(prevented);assert(ids.resultat.textContent.includes('0 / 3'));assert(ids.resultat.textContent.includes('sans réponse : 3'));
selections={q1:'html',q2:'css',q3:'js'};submit();assert(ids.resultat.textContent.includes('3 / 3'));assert(ids.r1.textContent.startsWith('Correct.'));
selections={q1:'css',q2:'js',q3:'html'};submit();assert(ids.resultat.textContent.includes('0 / 3'));assert(ids.r2.textContent.startsWith('À revoir.'));
selections={q1:'html',q2:'js'};submit();assert(ids.resultat.textContent.includes('1 / 3'));assert(ids.r3.textContent.startsWith('Sans réponse.'));
ids.quiz.handlers.reset();assert.equal(ids.resultat.textContent,'');assert.equal(ids.r1.textContent,'');assert.equal(ids.r2.textContent,'');assert.equal(ids.r3.textContent,'');
console.log('Affichage/masquage et quiz : cas vide, correct, incorrect, partiel, remise à zéro réussis (DOM simulé).');
'''
test_result=subprocess.run(['node','-e',test,str(site/'js/app.js')],check=True,capture_output=True,text=True,encoding='utf-8').stdout.strip()
for original,copy in [('affiche.svg','assets/images/affiche.svg'),('fiche-web.html','pieces/fiche-web.html'),('guide-source.md','pieces/guide-source.md')]:
    assert (base/'entrees'/original).read_bytes()==(site/copy).read_bytes()
control=f'''# Contrôles — Déclic Web V1

Contrôles agent exécutés le 22 novembre 2026, Windows, Python 3.14 et Node.js. Inspection des fichiers et tests avec DOM simulé : ce ne sont pas des essais navigateur.

| Vérification | Méthode et environnement | Résultat observé | Statut | Correction ou suite |
| --- | --- | --- | --- | --- |
| Structure et contenu | Analyse HTML Python ; comparaison au guide et au brief | Six sections, trois questions, action vers la fiche réelle ; mention fictive et limites conservées | Réussi | Relecture humaine à faire |
| Liens, ancres et ressources | Résolution de chaque href/src sur les deux pages HTML, identifiants uniques | {links} références valides ; aucun chemin absolu local ; liens canonique et auteur identifiés | Réussi | Refaire après modification |
| JavaScript | node --check js/app.js | Syntaxe acceptée | Réussi | Aucun correctif requis |
| Afficher/masquer et quiz | Node vm, DOM simulé, assertions | Deux bascules avec état accessible ; quiz vide, correct, incorrect, partiel et remise à zéro vérifiés | Réussi | Essayer les événements réels dans le navigateur |
| Copies des sources | Comparaison binaire Python | Affiche, fiche et guide identiques aux originaux | Réussi | Conserver les crédits |
| Périmètre des fichiers | Inventaire du pack | Onze fichiers utiles, sans secret, dépendance, métadonnées Git ou archive imbriquée | Réussi | Aucun ajout privé |
| Archive extraite | zipfile Python, extraction dans un dossier temporaire neuf, liens recontrôlés | Une racine, fichiers extraits identiques par SHA-256 au dossier livré | Réussi | Refaire après régénération |
| Navigation et action en navigateur | Pilotage navigateur indisponible : outil node_repl absent de la session | Non observé | Non exécuté | Ouvrir la copie extraite, activer chaque ancre et Explorer les trois fichiers |
| Bouton et quiz en navigateur | Même limite ; DOM simulé seulement | Non observé dans un moteur de rendu | Non exécuté | Afficher/masquer ; corriger réponses justes, fausses et manquantes ; recommencer |
| Clavier et focus | Aucun essai navigateur | Non observé | Non exécuté | Tab puis Entrée/Espace ; suivre le focus visible ; pas de dialogue donc Échap sans objet |
| Mobile et zoom 200 % | CSS adaptatif inspecté seulement | Aucun rendu observé | Non exécuté | Tester à 375 px de large puis zoom navigateur 200 %, relever navigateur et largeur ; vérifier débordements et lisibilité |
| Console et hors ligne | Dépendances locales inspectées seulement | Aucune console observée | Non exécuté | Couper le réseau, rouvrir la copie extraite en fichier local ; parcourir pages et interactions, relever la console |

## Mise à jour identité et partage
| Vérification | Méthode et environnement | Résultat observé | Statut | Correction ou suite |
| --- | --- | --- | --- | --- |
| Logo et favicon | Comparaison binaire ; en-tête PNG via Python | Images intactes, 1774 × 887 pixels ; CSS conserve les proportions | Réussi | Vérification visuelle à faire |
| Open Graph et auteur | Analyse HTML Python | Balises requises présentes une seule fois ; liens auteur, favicon et canonique présents | Réussi | Aperçu réel sur réseau social non exécuté, cache possible |
| Lien auteur | Requête HTTPS PowerShell | HTTP 200 au moment de la mise à jour | Réussi | Nécessite Internet |

## Essais participant
Non exécuté. Extraire le ZIP dans un autre dossier, ouvrir index.html et effectuer les essais ci-dessus. Renseigner pour chaque essai la date, le navigateur et sa version, la largeur, le résultat et les corrections attendues. Les observations personnelles restent à compléter.

## Revue du pilote
Décision : À examiner. Aucune validation pédagogique attribuée. Publication GitHub Pages autorisée par le participant et effectuée ; la revue pédagogique reste distincte.

## Points pour S18 et S19
Pièces produites : site modifiable, fiche, affiche, guide, trois documents et ZIP. La preuve S18 peut citer les contrôles agent ci-dessus. Priorité S19 : exécuter les essais navigateur et clavier, puis corriger les anomalies réellement constatées. Ne pas assimiler les tests du DOM simulé aux essais humains.
'''
(site/'CONTROLE.md').write_text(control,encoding='utf-8')
archive=site.with_suffix('.zip')
assert not archive.exists() or '--rebuild-archive' in sys.argv, 'Archive existante : utiliser --rebuild-archive pour la mise à jour explicite'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(site.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(site.parent).as_posix())
with tempfile.TemporaryDirectory(prefix='declic-verification-') as temp:
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert {n.split('/')[0] for n in z.namelist()}=={site.name}
        z.extractall(temp)
    extracted=Path(temp)/site.name
    assert check(extracted)==links
    original={p.relative_to(site).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in site.rglob('*') if p.is_file()}
    copied={p.relative_to(extracted).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in extracted.rglob('*') if p.is_file()}
    assert original==copied
    assert len(original)==11
print(json.dumps({'liens_valides':links,'fichiers':len(original),'zip':str(archive),'taille_octets':archive.stat().st_size,'tests_js':test_result,'extraction_et_empreintes':'identiques'},ensure_ascii=False))
