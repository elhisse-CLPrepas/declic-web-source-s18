/* Interaction 1 : garder le texte et l’état accessible synchronisés. */
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
});
