---
template: document.html
title: Introducció a la Intel·ligència Artificial
icon: material/book-open-variant
comments: true
tags:
    - aprenentatge automàtic
    - machine learning (ML)
    - intel·ligència artificial (IA)
    - IA feble
    - IA forta
---

*[DNN]: Deep Neural Networks
*[IA]: Intel·ligència Artificial
*[ML]: Machine Learning
*[NN]: Neural Networks
*[SL]: Supervised Learning
*[UNS]: Unsupervised Learning


## Què és la Intel·ligència Artificial?
La __Intel·ligència Artificial (IA)__ consisteix en un programa informàtic capaç d'executar
tasques i processos que tradicionalment requerien d'una intel·ligència humana.
En molts casos, aquests programes són capaços de realitzar les tasques de forma més
eficient i precisa que els humans.

No obstant això, no tots el programes que realitzen tasques de manera eficient que
els humans són considerats IA.

<figure>
  <img src="../img/ia-if-meme.jpeg" alt="" style="max-height: 400px">
  <figcaption class="attribution">Autor desconegut</figcaption>
</figure>

Determinar si un ordinador realment es comporta de manera intel·ligent és complex.
Hi ha moltes definicions de què és exactament la IA.
La més estesa és la de John McCarthy (1995): 

!!! quote
    És la ciència i l'enginyeria de fer màquines intel·ligents.

    > Artificial Intelligence is the science and engineering of making intelligent machines.

Hi ha molts programes que es comporten de manera intel·ligent,
però hui en dia es dóna molta importància a les següents característiques:

- __Capacitat d'aprenentatge__: Les màquines poden apendre i millorar el seu rendiment (semblant a com ho fem els humans).
- __Autonomia__: Les màquines poden prendre decisions i realitzar tasques en entors complexos sense la intervenció humana.
- __Adaptabilitat__: Les màquines poden adaptar-se a nous entorns i situacions.

### Exemples d'ús de la IA
Alguns exemples d'ús de la IA més estesos i fins i tot, quotidians són:

- __Reconeixement de veu__: utilitzat en assistents virtuals com Siri, Alexa o Google Assistant.
- __Sistemes de recomanació__: Sistemes de recomanació que es basen en les preferències de l'usuari i el contingut consumit:
    - __Spotify__: recomana música basant-se en les cançons que més escoltem.
    - __Serveis de distribució audiovisual (_Netflix, HBO, ..._)__: recomana sèries i pel·lícules basant-se en les que hem vist.
    - __Xarxes socials (_Instagram, X, Facebook_)__: recomanen contingut basant-se en les publicacions que més ens agraden (o fins i tot visualitzem!).
- __Processament d'imatges__:
    - Aplicacions com Google Photos que permeten cercar imatges per contingut.
    - Reconeixement facial (com en les càmeres dels mòbils).
    - Sistemes de conducció autònoma.
    - Filtratge i classificació d'imatges.
- __Sistemes de traducció automàtica__: com Google Translate o [SoftCatalà](https://www.softcatala.org/traductor/).

## IA feble vs IA forta
Imagina't un robot o un ordinador que no sols puga fer tasques específiques, sinó que
també pense i entenga el món exactament com el fem nosaltres, els humans.
Això es coneix com __intel·ligència artificial forta__(1), que a dia d'avui, sols existeix en la ciència ficció.
{ .annotate }

1. [Artificial General Intelligence (AGI)](https://en.wikipedia.org/wiki/Artificial_general_intelligence)

Aquesta és la IA que veiem en pel·lícules com _Ex Machina_, _Her_, _Blade Runner_ o llibres com _Jo, Robot_ i altres d'_Isaac Asimov_.
Aquest tipus de IA és capaç de realitzar qualsevol tasca que un ésser humà puga fer, entenent el món i prenent decisions de manera autònoma.

<figure>
  <img src="../img/strong-ai.jpg" alt="" style="max-height: 400px">
  <figcaption class="attribution">Image via www.vpnsrus.com</figcaption>
</figure>

En canvi, la __intel·ligència artificial feble__(1) és el tipus de IA que coneixem avui en dia.
Aquesta és capaç de realitzar tasques específiques de manera molt eficient, però no pot realitzar tasques
per a les quals no ha estat dissenyada, és a dir, estan __orientades a un objectiu__.
{ .annotate }

1. [Artificial Narrow Intelligence (ANI)](https://en.wikipedia.org/wiki/Artificial_narrow_intelligence)

<figure>
  <img src="../img/infografia-editorial-huawei-ia.png" alt="" style="max-width: 350px">
  <figcaption class="attribution">Huawei</figcaption>
</figure>

## Classificació i conceptes relacionats

<figure>
  <img src="../img/ia-venn.webp" alt="" style="max-width: 500px">
  <figcaption class="attribution">VENN diagram of AI, Big Data and Data Science Fraunhofer FOKUS</figcaption>
</figure>

- __Intel·ligència Artificial (IA)__: és la ciència i l'enginyeria de fer màquines intel·ligents.
- __Aprenentatge Automàtic (_Machine Learning_ o _ML_)__: és una branca de la IA que es basa
    en la idea que les màquines poden aprendre de les dades per si mateixes.
- __Xarxes Neuronals (_Neural Networks_ o _NN_)__: és un model computacional inspirat en el cervell humà
    que es basa en la interconnexió de neurones artificials.
- __Aprenentatge Profund (_Deep Learning_)__: és una branca de l'aprenentatge automàtic que es basa en xarxes neuronals
    profundes (_Deep Neural Networks_ o _DNN_).

Altres conceptes relacionats són:

- __Big Data__: és la disciplina que es basa en l'anàlisi de grans volums de dades, que poden ser utilitzats —o no—,
    en sistemes d'IA.
- __Data Science__: és la disciplina que es basa en l'anàlisi de dades per a obtenir coneixement i informació útil.


## Aprenentatge Automàtic
L'__Aprenentatge Automàtic (*Machine Learning o ML*)__ és un camp de la IA
que es basa en la idea que les màquines poden aprendre de les dades per si mateixes,
sense ser programades explícitament per a realitzar una tasca concreta.

### Aprenentatge Supervisat
L'__Aprenentatge Supervisat (*Supervised Learning o SL*)__ és un tipus de ML en el qual
l'aprenentatge es basa en un conjunt de dades etiquetades, de les quals es coneix el resultat esperat.

<figure>
  <img src="../img/supervised-learning.jpg" alt="Supervised Learning">
  <figcaption class="attribution">Autor desconegut</figcaption>
</figure>

Dins del SL, trobem dos principals tipus de problemes: __classificació__ i __regressió__.

!!! example
    En aquest example de __classificació__, el model ha segut entrenat amb imatges de gats, gossos i gallines,
    indicant-li al model l'animal (__etiqueta__) que apareix en cada imatge.

    El model __aprén__ a diferenciar entre aquests animals.

    Després, el model pot ser utilitzat per a predir l'animal en una imatge que no ha vist abans.

#### Classificació
En un problema de __classificació__, el model ha de predir a quina categoria o classe (valors discrets)
pertany una observació (imatge, text, etc.).

Durant el procés d'entrenament, el model aprén a diferenciar entre les diferents classes
a partir de les dades d'entrenament i les etiquetes associades.

<figure>
  <img src="../img/classificacio.png" alt="Classificació">
  <figcaption class="attribution">Autor desconegut</figcaption>
</figure>

Alguns exemples de classificació són:

- __Correu no desitjat__: classificar els correus electrònics en _spam_ o _no spam_.
- __Anàlisi de sentiments__: classificar els textos en _positius_, _negatius_ o _neutres_ respecte a un tema.
- __Classificació d'imatges__: classificar les imatges en diferents categories.
    - Imatge mèdica, reconeixement facial, conducció autònoma, ...
- __Reconeixement de veu__: classificar les paraules pronunciades en diferents categories.

#### Regressió
En un problema de __regressió__, el model ha de predir un valor numèric (valors contínus)
a partir de les dades d'entrada.

Durant el procés d'entrenament, el model aprén a predir aquest valor numèric a partir de les característiques
de les dades d'entrenament.G

<figure>
  <img src="../img/regressio.png" alt="Regressió">
  <figcaption class="attribution">Autor desconegut</figcaption>
</figure>

Alguns exemples de regressió són:

- __Preu d'una casa__: predir el preu d'una casa a partir de les seves característiques (_m², nº habitacions, ..._).
- __Assegurances, crèdits, hipoteques...__: predir el risc associat a un client.
- __Sistemes de recomanació__: predir la puntuació que un usuari donarà a un producte o l'interès que tindrà en ell.

### Aprenentatge No Supervisat
D'un altre costat, l'__Aprenentatge No Supervisat (*Unsupervised Learning o UNS*)__ és un tipus de ML en el qual
l'aprenentatge es basa en un conjunt de dades sense etiquetar, és a dir, sense saber el resultat esperat.

<figure>
  <img src="../img/unsupervised-learning.png" alt="Unsupervised Learning">
  <figcaption class="attribution">Autor desconegut</figcaption>
</figure>



## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/) de César Guijarro Rosaleny
- Material del curs "Iniciació a la Intel·ligència Artificial amb Python" impartit per David Campoy Miñarro
- Artificial general intelligence, Wikipedia: https://en.wikipedia.org/wiki/Artificial_general_intelligence
- Weak artificial intelligence, Wikipedia: https://en.wikipedia.org/wiki/Weak_artificial_intelligence
- Aprenentatge Automàtic, Viquipèdia: https://ca.wikipedia.org/wiki/Aprenentatge_autom%C3%A0tic
- Supervised learning, Wikipedia: https://en.wikipedia.org/wiki/Supervised_learning
- Unsupervised learning, Wikipedia: https://en.wikipedia.org/wiki/Unsupervised_learning
