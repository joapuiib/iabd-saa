---
template: document.html
title: Xarxes neuronals
icon: material/book-open-variant
comments: true
tags:
    - xarxes neuronals
    - neural networks (NN)
    - aprenentatge profund
    - deep learning
    - deep neural networks (DNN)
    - backpropagation
    - perceptró
    - xarxes neuronals convolucionals (CNN)
    - xarxes neuronals recurrents (RNN)
---

*[IA]: Intel·ligència Artificial
*[ML]: Machine Learning
*[DNN]: Deep Neural Networks
*[NN]: Neural Networks
*[CNN]: Convolutional Neural Networks
*[RNN]: Recurrent Neural Networks


## Xarxes Neuronals
Les __xarxes neuronals (*neural networks o NN*)__ són un model
computacional inspirat en el funcionament del cervell dels organismes
vius: un conjunt de neurones interconnectades entre sí, que s'activen
quan reben un estímul i treballen col·lectivament per resoldre un
problema.

Aquest model ha revolucionat el camp del Aprenentatge Automàtica (ML)
en els últims anys.

### Perceptró
Les xarxes neuronals estan compostes per __neurones artificials__, que són
l'element bàsic d'aquest model. La neurona artificial esta inspirada en
la neurona natural, que és la cèl·lula bàsica del cervell dels animals.

<figure id="figure-1">
    <img src="../img/neurona.png" alt="Neurona natural">
    <figcaption class="attribution">Mauro Lanari, Wikimedia Commons</figcaption>
    <figcaption>FIgura 1: Neurona natural</figcaption>
</figure>

La __neurona artificial__, també anomenada __perceptró__, és
la unitat bàsica d'una xarxa neuronal. Aquesta rep un __conjunt d'entrades__
(*inputs*), que són ponderades per uns __pesos__ (*weights*) i sumades
amb un __sesg__ (*bias*).

L'__eixida__ (*output*) de la neurona es calcula aplicant una __funció
d'activació__ a la suma ponderada de les entrades.

<figure id="figure-2">
    <img src="../img/perceptron.png" alt="Perceptró">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 2: Perceptró</figcaption>
</figure>

L'eixida d'un perceptró es linear respecte a les entrades, per tant, no
podria resoldre problemes no lineals. Per evitar aquesta limitació,
s'han afegit les __funcions d'activació__, que permeten a les xarxes
neuronals resoldre problemes més complexos.

Les __funcions d'activació__ són funcions no lineals que s'apliquen a
abans de l'eixida de la neurona.

<figure id="figure-3">
    <img src="../img/activation.jpeg" alt="Funcions d'activació">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 3: Funcions d'activació</figcaption>
</figure>

!!! note
    Existeixes moltes funcions d'activació, que caldrà seleccionar
    segons el problema a resoldre.

## Xarxes neuronals profundes (DNN)
Les __xarxes neuronals profundes (*Deep Neural Networks o DNN*)__ són
un tipus de xarxes neuronals, en les quals es connecten múltiples capes
de neurones entre sí.

Aquesta estructura permet modelar relacions més complexes entre les
dades, i per tant, resoldre problemes més complicats.

!!! note
    Realment, el que defineix el DNN no és el nombre de capes, siní el
    processament de les dades de manera jeràrquica. Cada capa extrau característiques
    més abstractes de les dades que la capa anterior arribant
    a la resposta final.

<figure id="figure-4">
    <img src="../img/deep-learning-process.png" alt="Procés d'una xarxa neuronal profunda">
    <figcaption class="attribution">https://wwww.quantamagazine.org</figcaption>
    <figcaption>Figura 4: Procés d'una xarxa neuronal profunda</figcaption>
</figure>

La primera capa s'anomena __capa d'entrada__, que tindrà tantes neurones
com entrades tinguen les nostres dades.

!!! example
    Si volem predir el preu d'una casa, les entrades podrien ser:

    - Metres quadrats
    - Nombre de dormitoris
    - Nombre de banys
    - Barri

    En aquest cas, la capa d'entrada tindria 4 neurones.

De la mateixa manera, l'última capa s'anomena __capa d'eixida__, que
tindrà tantes neurones com resultats esperem obtindre.

!!! example
    En el problema anterior, l'exida que esperem és el preu de la casa.

    Per tant, la capa d'eixida tindria una sola neurona.

Les capes intermèdies s'anomenen __capa ocultes__ que estan connctades entre sí,
de manera que l'eixida d'una capa és l'entrada de la següent. El nombre de neurones
en aquestes capes depèn del problema a resoldre.

<figure id="figure-5">
    <img src="../img/dnn.png" alt="Xarxa neuronal profunda">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 5: Xarxa neuronal profunda</figcaption>
</figure>

### Retropropagació (backpropagation)
La __retropropagació (*backpropagation*)__ és un algoritme d'aprenentatge
supervisat que s'utilitza per entrenar xarxes neuronals.

Aquest algoritme ajusta els pesos de les connexions entre les neurones
per minimitzar l'error entre l'eixida de la xarxa i l'eixida esperada.

El funcionament és el següent:

- S'envia un conjunt de dades a la xarxa, i es calcula l'eixida de la xarxa.
- Es compara l'eixida de la xarxa amb l'eixida esperada, i es calcula l'__error__.
- L'error es propaga cap enrere a través de la xarxa, ajustant els pesos de les connexions.

<figure id="figure-6">
    <img src="../img/backpropagation.png" alt="Retropropagació">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 6: Retropropagació</figcaption>
</figure>

Aquest procés es repeteix moltes vegades de manera iterativa, reduint
l'error de la xarxa fins a arribar a un valor acceptable.

!!! note
    La retropropagació és un algoritme computacionalment intensiu, i
    requereix una gran quantitat de dades per a ser efectiu.


## Tipus de xarxes neuronals
Hi ha molts tipus de xarxes neuronals, cadascuna dissenyada per a
resoldre un tipus de problema concret.


### Xarxes neuronals convolucionals (CNN)
Les __xarxes neuronals convolucionals (*Convolutional Neural Networks o CNN*)__
són un tipus de xarxes neuronals especialment dissenyades per a processar
imatges.

Les primeres capes d'una CNN són __capes de convolució__, que apliquen
s'encarreguen d'extraure característiques de xicotetes regions de la
imatge (lines, curves, textures, etc.).

<figure id="figure-7">
    <img src="../img/cnn.jpg" alt="Xarxa neuronal convolucional">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 7: Xarxa neuronal convolucional</figcaption>
</figure>


### Xarxes neuronals recurrents (RNN)
Les __xarxes neuronals recurrents (*Recurrent Neural Networks o RNN*)__
són un tipus de xarxes neuronals dissenyades per a processar seqüències
de dades, com textos, temps, etc.

Aquest tipus de xarxes tenen __connexions cícliques__ entre les neurones,
de manera que l'eixida de la xarxa pot ser utilitzada com a entrada en
la següent iteració.

<figure id="figure-8">
    <img src="../img/rnn.png" alt="Xarxa neuronal recurrent">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 8: Xarxa neuronal recurrent</figcaption>
</figure>


### Xarxes neuronals generatives adversàries (GAN)
Les __xarxes neuronals generatives adversàries (*Generative Adversarial Networks o GAN*)__
són un tipus de xarxes neuronals dissenyades per a generar dades noves
a partir de dades existents.

Aquest tipus de xarxes estan compostes per dues xarxes neuronals:

- __Generador__: Aquesta xarxa genera dades noves a partir de dades existents.
- __Discriminador__: Aquesta xarxa intenta distingir entre les dades reals
    i les dades generades pel generador.

La tasca del generador és enganyar el discriminador, i la tasca del
discriminador és diferençiar entre les dades reals i les dades generades.

Quan el discriminador descarta les dades generades pel generador, aquest
aprén de l'error i millora la seua capacitat per a generar dades noves.

En canvi, quan el discriminador no pot distingir entre les dades reals i
les dades generades, el discriminador aprén de l'error i millora la seua
capacitat per a distingir entre les dades reals i les dades generades.

<figure id="figure-9">
    <img src="../img/gan.png" alt="Xarxa neuronal generativa adversària">
    <figcaption class="attribution">Autor desconegut</figcaption>
    <figcaption>Figura 9: Xarxa neuronal generativa adversària</figcaption>
</figure>

## Recursos addicionals
- [¿Qué es una Red Neuronal? Parte 1 : La Neurona | DotCSV](https://www.youtube.com/watch?v=MRIv2IwFTPg&list=PL-Ogd76BhmcB9OjPucsnc2-piEE96jJDQ){:target="_blank"}
- [¿Qué es una Red Neuronal? Parte 2 : La Red | DotCSV](https://www.youtube.com/watch?v=uwbHOpp9xkc&list=PL-Ogd76BhmcB9OjPucsnc2-piEE96jJDQ&index=2){:target="_blank"}
- [Jugando con Redes Neuronales - Parte 2.5 | DotCSV](https://www.youtube.com/watch?v=FVozZVUNOOA&list=PL-Ogd76BhmcB9OjPucsnc2-piEE96jJDQ&index=3){:target="_blank"}
- [¿Qué es una Red Neuronal? Parte 3 : Backpropagation | DotCSV](https://www.youtube.com/watch?v=eNIqz_noix8&list=PL-Ogd76BhmcB9OjPucsnc2-piEE96jJDQ&index=4){:target="_blank"}
- [A Friendly Introduction to Generative Adversarial Networks (GANs)](https://www.youtube.com/watch?v=8L11aMN5KY8){:target="_blank"}

## Bibliografia
- [Material del mòdul "Sistemes d'Aprenentatge Automàtic"](https://cesguiro.es/) de César Guijarro Rosaleny
- Retropropagacio, Wikipedia: https://ca.wikipedia.org/wiki/Retropropagaci%C3%B3
