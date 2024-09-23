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
*[RL]: Reinforcement Learning
*[SL]: Supervised Learning
*[UNS]: Unsupervised Learning


## Què és la Intel·ligència Artificial?
La __Intel·ligència Artificial (IA)__ consisteix en un programa informàtic capaç d'executar
tasques i processos que tradicionalment requerien d'una intel·ligència humana.
En molts casos, aquests programes són capaços de realitzar les tasques de forma més
eficient i precisa que els humans.

No obstant això, no tots el programes que realitzen tasques de manera eficient que
els humans són considerats IA.

<figure id="figure-1">
    <img src="../img/ia-if-meme.jpeg" alt="" style="max-height: 400px">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 1: Meme sobre la IA</figcaption>
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

<figure id="figure-2">
    <img src="../img/strong-ai.jpg" alt="" style="max-height: 400px">
    <figcaption class="attribution">Image via www.vpnsrus.com</figcaption>
    <figcaption>Figura 2: Intel·ligència Artificial Forta</figcaption>
</figure>

En canvi, la __intel·ligència artificial feble__(1) és el tipus de IA que coneixem avui en dia.
Aquesta és capaç de realitzar tasques específiques de manera molt eficient, però no pot realitzar tasques
per a les quals no ha estat dissenyada, és a dir, estan __orientades a un objectiu__.
{ .annotate }

1. [Artificial Narrow Intelligence (ANI)](https://en.wikipedia.org/wiki/Artificial_narrow_intelligence)

<figure id="figure-3">
    <img src="../img/infografia-editorial-huawei-ia.png" alt="" style="max-width: 350px">
    <figcaption class="attribution">Huawei</figcaption>
    <figcaption>Figura 3: Comparació entre IA feble i IA forta</figcaption>
</figure>

## Classificació i conceptes relacionats

<figure id="figure-4">
    <img src="../img/ia-venn.webp" alt="" style="max-width: 500px">
    <figcaption class="attribution">VENN diagram of AI, Big Data and Data Science Fraunhofer FOKUS</figcaption>
    <figcaption>Figura 4: Relació entre IA, Big Data i Data Science</figcaption>
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

<figure id="figure-5">
    <img src="../img/supervised-learning.jpg" alt="Supervised Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 5: Aprenentatge Supervisat</figcaption>
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

<figure id="figure-6">
    <img src="../img/classificacio.png" alt="Classificació">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 6: Classificació</figcaption>
</figure>

<figure id="figure-7">
    <img src="../img/classification-examples.png" alt="Comparació d'algorismes de classificació">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 7: Comparació d'algorismes de classificació</figcaption>
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

<figure id="figure-8">
    <img src="../img/regressio.png" alt="Regressió">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 8: Regressió</figcaption>
</figure>

Alguns exemples de regressió són:

- __Preu d'una casa__: predir el preu d'una casa a partir de les seves característiques (_m², nº habitacions, ..._).
- __Assegurances, crèdits, hipoteques...__: predir el risc associat a un client.
- __Sistemes de recomanació__: predir la puntuació que un usuari donarà a un producte o l'interès que tindrà en ell.

### Aprenentatge No Supervisat
D'un altre costat, l'__Aprenentatge No Supervisat (*Unsupervised Learning o UNS*)__ és un tipus de ML en el qual
l'aprenentatge es basa en un conjunt de dades sense etiquetar, és a dir, sense saber el resultat esperat.

<figure id="figure-9">
    <img src="../img/unsupervised-learning.png" alt="Unsupervised Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 9: Aprenentatge No Supervisat</figcaption>
</figure>

Dins de l'UNS, trobem dos principals tipus de problemes: __clustering__ i __reducció de la dimensionalitat__.

#### Clustering
En un problema de __clustering__, el model ha de dividir les dades en diferents grups o clústers,
de manera que les observacions dins d'un mateix clúster siguin similars entre si.

La [Figure 9](#figure-9) mostra un exemple de clustering en el qual les dades són dividides tres clústers.

Alguns exemples de clustering són:

- __Segmentació de clients__: agrupar els clients en diferents segments segons les seves característiques.
    Pot ser útil per a personalitzar ofertes, campanyes de màrqueting o recomanació de contingut.


#### Reducció de la dimensionalitat
En un problema de __reducció de la dimensionalitat__, el model ha de reduir el nombre de dimensions (característiques)
de les dades, mantenint la informació més rellevant.

Aquest tipus de problema és útil per a reduir el temps de càlcul i millorar la precisió dels models.

<figure id="figure-11">
    <img src="../img/dimensionality-reduction.webp" alt="Reducció de la dimensionalitat">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 11: Reducció de la dimensionalitat</figcaption>
</figure>

Alguns exemples de reducció de la dimensionalitat són:

- __Anàlisi de components principals (PCA)__: reduir el nombre de dimensions d'un conjunt de dades.
- __Visualització de dades__: reduir les dades a un nombre menor de dimensions per a visualitzar-les en 2D o 3D.
- __Reducció de soroll__: eliminar les característiques menys rellevants o redundants.


### Aprenentatge semisupervisat
De vegades, tenim un conjunt de dades on sols algunes de les observacions estan etiquetades.

En aquests casos, podem utilitzar l'__Aprenentatge semisupervisat__ per a combinar les tècniques de SL i UNS.

<figure id="figure-12">
    <img src="../img/semi-supervised-learning.png" alt="Semi-supervised Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 12: Aprenentatge semisupervisat</figcaption>
</figure>


### Aprenentatge per reforçament
L'__Aprenentatge per reforçament (*Reinforcement Learning o RL*)__ és un tipus de ML en el qual
l'aprenentatge es basa en la interacció amb un entorn.

En aquest tipus d'aprenentatge, un agent (robot, cotxe autònom, etc.) ha de prendre decisions
per a maximitzar una recompensa a llarg termini. Quan l'agent pren una decisió correcta, rep una recompensa,
i quan pren una decisió incorrecta, rep un càstig.

<figure id="figure-13">
    <img src="../img/reinforcement-learning.png" alt="Reinforcement Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 13: Aprenentatge per reforçament</figcaption>
</figure>


### Aprenentatge per lots
En l'__Aprenentatge per lots (*Batch Learning*)__, el model és entrenat amb un conjunt de dades fix.

Si volem actualitzar el model amb noves dades, hem de tornar a entrenar-lo des de zero.

<figure id="figure-14">
    <img src="../img/batch-learning.png" alt="Batch Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 14: Aprenentatge per lots</figcaption>
</figure>


### Aprenentatge en línia
En l'__Aprenentatge en línia (*Online Learning*)__, el model és entrenat amb dades que arriben en temps real.

Aquest tipus d'aprenentatge és útil quan les dades són massa grans per a ser processades en memòria o quan
les dades arriben de manera contínua.

<figure id="figure-15">
    <img src="../img/online-learning.png" alt="Online Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 15: Aprenentatge en línia</figcaption>
</figure>


### Aprenentatge basat en models
En l'__Aprenentatge basat en models (*Model-based Learning*)__, existeix un model (normalment matemàtic/estadístic)
que descriu com les dades són transformades en una predicció.

Aquest model és entrenat amb les dades d'entrenament i després utilitzat per a fer prediccions.

<figure id="figure-16">
    <img src="../img/model-learning.png" alt="Model-based Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 16: Aprenentatge basat en models</figcaption>
</figure>


### Aprenentatge basat en instàncies
En l'__Aprenentatge basat en instàncies (*Instance-based Learning*)__, les prediccions
es basen en la similitud entre les observacions d'entrenament i les noves observacions.

Aquest tipus d'aprenentatge és útil quan no es pot construir un model matemàtic/estadístic.

<figure id="figure-17">
    <img src="../img/instance-learning.png" alt="Instance-based Learning">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 17: Aprenentatge basat en instàncies</figcaption>
</figure>


## Prova i validació de models
Una vegada s'ha entrenat un model, és important avaluar la seva precisió i rendiment.

Per a això, es divideixen les dades en dos conjunts: __dades d'entrenament__ i __dades de prova__.

- Les __dades d'entrenament__ són utilitzades per a entrenar el model.
- Les __dades de prova__ són utilitzades per a avaluar el rendiment del model.

!!! important
    És molt important que les dades de prova no hagen segut utilitzades en el procés d'entrenament.

    Estem avaluant si el model __generalitza__ bé el problema o no, per tant, el model no ha de conéixer les dades de prova.

!!! info
    Normalment la proporció entre les dades d'entrenament i les dades de prova és de 80%/20% o 70%/30%, respectivament.

Cada tipus de problema té unes mètriques associades per a avaluar la qualitat del model.


## Principals problemes de l'Aprenentatge Automàtic
L'Aprenentatge Automàtic és una eina molt potent, però també difícil d'utilitzar perquè siga eficient.

Alguns dels principals problemes són:

- __Cantitat insuficient de dades__: per a entrenar un model amb precisió, és necessari un conjunt de dades gran
    que represente correctament el problema.
- __Dades de baixa qualitat__: si les dades tenen errors, valors atípics i soroll, difícilment el model
    podrà fer prediccions correctes.
- __Dades d'entrenament no representatives__: per poder generalitzar correctament el problema, és crucial
    que les dades d'entrenament representen correctament el problema.

    Si utilitzem un conjunt de dades que no és representatiu, el model no podrà fer prediccions correctes i
    ens trobarem en un cas de __mostra esbiaixada__.

A més, és important conéixer els problemes que ens podem trobar en el procés d'entrenament:

- __Sobreajustament (*Overfitting*)__: el model s'ajusta massa bé a les dades d'entrenament i no pot generalitzar
    correctament el problema.

- __Subajustament (*Underfitting*)__: el model no s'ajusta prou bé a les dades d'entrenament i no pot fer prediccions
    correctes.

<figure id="figure-16">
    <img src="../img/overfitting.png" alt="Overfitting and Underfitting">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 16: Sobreajustament i Subajustament</figcaption>
</figure>

Mesurant el rendiment del model amb les dades de prova, podem determinar si el model pateix d'aquests problemes:

- Si el model té un mal rendiment amb les dades d'entrenament i les dades de prova, probablement estiguem davant
    un cas de subajustament.
- Si el model té un bon rendiment amb les dades d'entrenament i un mal rendiment amb les dades de prova, probablement
    estiguem davant un cas de sobreajustament.

El moment de parar l'entrenament del model és quan aquest té un bon rendiment amb les dades d'entrenament i la validació
de les dades de prova comença a empitjorar.

<figure id="figure-17">
    <img src="../img/overfitting-validation.png" alt="Overfitting and Underfitting validation">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 17: Validació Sobreajustament i Subajustament</figcaption>
</figure>

## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/) de César Guijarro Rosaleny
- Material del curs "Iniciació a la Intel·ligència Artificial amb Python" impartit per David Campoy Miñarro
- Artificial general intelligence, Wikipedia: https://en.wikipedia.org/wiki/Artificial_general_intelligence
- Weak artificial intelligence, Wikipedia: https://en.wikipedia.org/wiki/Weak_artificial_intelligence
- Aprenentatge Automàtic, Viquipèdia: https://ca.wikipedia.org/wiki/Aprenentatge_autom%C3%A0tic
- Supervised learning, Wikipedia: https://en.wikipedia.org/wiki/Supervised_learning
- Unsupervised learning, Wikipedia: https://en.wikipedia.org/wiki/Unsupervised_learning
- Reinforcement learning, Wikipedia: https://en.wikipedia.org/wiki/Reinforcement_learning
- Online machine learning, Wikipedia: https://en.wikipedia.org/wiki/Online_machine_learning
- Mostra esbiaixada, Viquipèdia: https://ca.wikipedia.org/wiki/Mostra_esbiaixada
