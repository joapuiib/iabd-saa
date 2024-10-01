---
template: programacio.html
title: Programació didàctica
subtitle:
- "5072 - Sistemes d'Aprenentatge Automàtic"
- "Curs d'especialitazció: Intel·ligència Artificial i Big Data"
icon: material/book
alias: programacio
# title: "IABD - Sistemes d'Aprenentatge Automàtic"
# description: Intel·ligència Artificial i Big Data
---

{% set examens = 40 %}
{% set practiques = 60 %}

{% if false %}
## Unitats didàctiques
##### 1a avaluació
- __UD1__: Introducció a la Intel·ligència Artificial
    - IA forta i IA dèbil
    - IA vs Machine Learning
    - Machine Learning:
        - Tipus (regressió, classificació, clustering)
        - Supervisat, no supervisat, reforç
        - Conjunts de dades
- __UD2__: Estadística
- __UD3__: Manipulació i visualicació de dades
    - Pandas
    - Numpy (?)
    - Plotnine
    - Anàlisi de les dades
- __UD4__: Regressió
    - Regressió linial
    - Regressió ML

##### 2a avaluació
- __UD5__: Preprocessament de dades
    - Normalització
    - Reducció de la dimensionalitat
    - Regularització
- __UD6__: Classificació
    - Validació
    - Mètriques
    - Tipus de classificadors
    - Models
- __UD7__: Clustering
{% endif %}

_Control de versions:_

| Data | Descripció |
| --- | --- |
| 2024-09-18 | Primera versió |
| 2024-09-24 | Correccions a l'apartat Avaluació |
| 2024-10-01 | Proposta de millora del curs anterior |

## 1. Propostes de millora del curs anterior
Les propostes de millora del curs anterior i les accions realitzades són les següents:

- __Incorporar conceptes d'estadística bayesiana, sobretot en les mètriques dels models de classificació.__

    En la mesura del possible, es tractarà d'introduïr algun concepte d'estadística bayesiana.

## 2. Marc normatiu
- [Llei Orgànica 3/2022, de 31 de març, d'ordenació i integració de la Formació
    Professional](https://www.boe.es/eli/es/lo/2022/03/31/3)

- [Reial decret 279/2021, de 20 d'abril, pel qual s'estableix el Curs d'especialització
    en Intel·ligència Artificial i Big Data i es fixen els aspectes bàsics del
    currículum.](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2021-7686)

- [RESOLUCIÓ de 8 d’agost de 2024, de la Secretaria Autonòmica d’Educació, per la qual es dicten instruccions sobre
    ordenació acadèmica i d’organització dels centres que impartixen Formació Professional durant el curs 2024-2025 a la
    Comunitat Valenciana](https://dogv.gva.es/datos/2024/08/14/pdf/2024_8407_va.pdf)

## 3. Contextualització
- __Codi__: 5072
- __Durada__: 90 hores
- __Crèdits ECTS__: 5

 Aquest mòdul professional conté la informació necessària per a dur a terme les funcions d'analitzar i
 relacionar les tècniques d'aprenentatge automàtic amb la predicció de comportaments futurs que
 permeten a les organitzacions i empreses l'eficiència operativa.

 Les funcions esmentades anteriorment inclouen aspectes com ara:

- Caracteritzar sistemes d'aprenentatge automàtic.
- Fer prediccions de comportaments futurs utilitzant models d'aprenentatge automàtic.

La formació del mòdul contribueix a assolir els objectius generals
a), b), c), d), e), f), g), j), k), m), n), ñ), o) i p),
així com les competències professionals i socials
a), c), d), e), f), g), j), k), m), n), ñ), o), p), q), r) i s) del curs d'especialització.

Les línies d'actuació en el procés d'ensenyament-aprenentatge que permeten assolir els objectius del mòdul estan relacionades amb:

- La caracterització de sistemes d'aprenentatge automàtic.
- L'aplicació d'aquests sistemes d'aprenentatge automàtic en la presa de decisions a les organitzacions i empreses.


## 5. Continguts
##### Bloc 1 - Caracterització de la Intel·ligència Artificial forta i dèbil

- Intel·ligència Artificial Dèbil:
    - Característiques i aplicacions.
    - Avantatges i inconvenients.
    - Usos i possibilitats.

- Intel·ligència Artificial Forta:
    - Característiques i aplicacions.
    - Avantatges i inconvenients.
    - Usos i possibilitats.

##### Bloc 2 Determinació de sistemes d'aprenentatge automàtic (Machine Learning):
- Classificació de sistemes d'aprenentatge automàtic: Supervisat i no supervisat.
- Principals tècniques per desenvolupar l'aprenentatge automàtic:
    Xarxes neuronals, aprenentatge inductiu, raonament basat en casos, entre altres.
- Algoritmes o models aplicats a l'aprenentatge automàtic:
    - Algoritmes de classificació.
    - Algoritmes de detecció d'anomalies.
    - Algoritmes de regressió.
    - Algoritmes de clustering.
    - Algoritmes de reforç de l'aprenentatge.
    - Arbres i regles de decisió.
    - Altres algoritmes relacionats amb l'aprenentatge automàtic.
- Procediments del Machine Learning: Dades, identificació de patrons i presa de decisions.
- Eines d'aprenentatge automàtic.
- Aplicacions del Machine Learning.

##### Bloc 3: Algoritmes aplicats a l'aprenentatge supervisat i optimització del model:
- Determinació d'elements i eines d'aprenentatge supervisat.
- Dades etiquetades.
- Variables d'entrada (input data). Etiquetes de sortida.
- Plataformes d'aprenentatge automàtic supervisat.
- Fases de l'aprenentatge automàtic:
    - Selecció de l'algoritme d'aprenentatge supervisat.
    - Selecció de dades.
    - Construcció del model.
    - Validació del model.
    - Ajust de característiques o paràmetres.
    - Implementació del model proposat.
    - Verificació del model de prova.
    - Optimització del model.

##### Bloc 4: Aplicació de tècniques d'aprenentatge no supervisat:
- Tècniques d'aprenentatge no supervisat.
- Algoritmes d'aprenentatge no supervisat: Agrupació de clústers, reducció de dimensió, entre altres.
- Determinació d'elements i eines d'aprenentatge no supervisat.
- Plataformes d'aprenentatge automàtic no supervisat.
- Fases de l'aprenentatge automàtic no supervisat.

##### Bloc 5: Aplicació de models computacionals de xarxes neuronals i comparació amb altres models:
- Aprenentatge automàtic versus aprenentatge profund.
- Com aprèn una xarxa neuronal.
- Models de xarxes neuronals artificials: Xarxes neuronals convolucionals (CNN).

##### Bloc 6: Valoració de la qualitat dels resultats obtinguts en la pràctica amb sistemes d'aprenentatge automàtic:
- Capacitat de generalització.
- Test.
- Validació.
- Matriu de confusió.

## 6. Distribució temporal
{% include "./programacio/components/_distribucio_temporal.html" %}

## 7. Metodologia didàctica
Aquest mòdul és sobretot pràctic.
Considerem que la manera millor manera d’aprendre és realitzant
i resolguent els problemes de manera pràctica.

Es realitzaran breus explicacions dels continguts combinats
amb molts exemples resolts, afavorint la participació activa
de l’alumnat (exposició participativa).

A mesura que es va avançant en la unitat,
es proporcionaran activitats que vagen augmentant progressivament
de dificultat.

## 8. Avaluació
### 8.1. Criteris d'avaluació
Els resultats d'aprenentatge i els seus corresponents criteris d'avaluació del mòdul professional són:

1. Caracteritza la Intel·ligència Artificial forta i dèbil, determinant-ne els usos i possibilitats.

    a. S'han determinat les especificitats de la Intel·ligència Artificial forta i dèbil.
    b. S'han establert les barreres entre la Intel·ligència Artificial i l'aprenentatge automàtic (Machine Learning).
    c. S'han diferenciat els àmbits d'aplicació de la Intel·ligència Artificial forta i dèbil.
    d. S'han identificat els problemes als quals pot fer front la Intel·ligència Artificial dèbil.
    e. S'han identificat els problemes als quals pot fer front la Intel·ligència Artificial forta.
    f. S'han reconegut els avantatges que proporciona cada tipus en la resolució de problemes.

2. Determina tècniques i eines de sistemes d'aprenentatge automàtic (Machine Learning), testant-ne l'aplicabilitat per a la resolució de problemes.

    a. S'han identificat els principis dels sistemes d'aprenentatge automàtic.
    b. S'han determinat tipus i usos dels sistemes d'aprenentatge automàtic.
    c. S'han determinat tècniques i eines de sistemes d'aprenentatge automàtic.
    d. S'han trobat diferències entre els tipus de sistemes d'aprenentatge automàtic.
    e. S'han associat tècniques i eines a cada tipus de sistema d'aprenentatge automàtic.

3. Aplica algoritmes d'aprenentatge supervisat, optimitzant el resultat del model i minimitzant els riscos associats.

    a. S'han proporcionat les dades etiquetades al model.
    b. S'han seleccionat les dades d'entrada, ja siguin per a la fase d'entrenament, fase de validació o fase de test, entre altres.
    c. S'han utilitzat les dades en la fase d'entrenament per a la construcció del model aplicant les característiques rellevants obtingudes.
    d. S'ha avaluat el model amb les dades obtingudes en la fase de validació.
    e. S'han ajustat les dades d'aprenentatge supervisat en la fase d'ajust per millorar el rendiment de les diferents característiques o paràmetres.
    f. S'ha implementat el model per fer prediccions sobre noves dades.
    g. S'han detectat i minimitzat els riscos associats al model.
    h. S'ha optimitzat el model d'aprenentatge supervisat validant dades de prova.

4. Aplica tècniques d'aprenentatge no supervisat relacionant-les amb els tipus de problemes que tracten de resoldre.

    a. S'han caracteritzat els tipus de problemes que l'aprenentatge no supervisat tracta de resoldre.
    b. S'han caracteritzat les tècniques d'aprenentatge no supervisat utilitzades per a la resolució d'aquests tipus de problemes.
    c. S'han aplicat algoritmes utilitzats en l'aprenentatge no supervisat.
    d. S'ha optimitzat el model d'aprenentatge no supervisat validant dades de prova.

5. Aplica models computacionals de xarxes neuronals comparant-los amb altres mètodes d'intel·ligència artificial.

    a. S'han avaluat els models neuronals per triar el més adequat per a cada classe de problema.
    b. S'han aplicat tècniques d'aprenentatge profund (deep learning) per entrenar xarxes neuronals.
    c. S'han comparat les xarxes neuronals artificials amb altres mètodes d'intel·ligència artificial.
    d. S'ha reconegut una xarxa neuronal entrenada a partir d'un conjunt de dades.

6. Valora la qualitat dels resultats obtinguts en la pràctica amb sistemes d'aprenentatge automàtic integrant els principis fonamentals de la computació.

    a. S'ha valorat la conveniència dels algoritmes proposats per resoldre els problemes plantejats.
    b. S'ha avaluat l'aplicació pràctica dels principis i tècniques bàsiques dels sistemes intel·ligents.
    c. S'han integrat els principis fonamentals de la computació en la pràctica per seleccionar, valorar i crear nous desenvolupaments tecnològics.
    d. S'han desenvolupat sistemes i aplicacions informàtiques que utilitzen tècniques dels sistemes intel·ligents.
    e. S'han desenvolupat tècniques d'aprenentatge computacional dedicades a l'extracció automàtica d'informació a partir de grans volums de dades.


### 8.2. Procediments i instruments de qualificació

<figure id="figure-1">
    <img src="../img/diagrama_convocatories.png" alt="Diagrama de convocatòries">
    <figcaption class="attribution">CIPFP Mislata</figcaption>
    <figcaption>Figura 1: Diagrama de convocatòries</figcaption>
</figure>

#### 8.2.1. Avaluació contínua
L’avaluació es realitzarà amb els següents instruments d'avaliació:

- __Exàmens__: Exàmens de caràcter pràctic sobre 
    els continguts de cada avaluació.
- __Pràctiques__: Treball teòric o pràctic, on s’avalua el 
    treball diari i els continguts que s’estan treballant.

Tots els instruments d'avaluació s'han d'entregar a temps i ha de complir amb els requisits d'entrega.
Si aquest no s'entrega en temps i forma, es considerarà com a no presentat.

La manca d'autenticitat en l'autoria o d'originalitat de les proves d'avaluació; la còpia o el plagi;
l'intent fraudulent d'obtenir un resultat acadèmic millor; la col·laboració, l'encobriment o l'afavoriment de la còpia,
o la utilització de material, aplicacions o dispositius no autoritzats durant l'avaluació, entre d'altres,
són conductes irregulars que poden tenir conseqüències acadèmiques i disciplinàries greus. 

D'una banda, si es detecta alguna d'aquestes conductes irregulars, pot comportar el suspens en les activitats
avaluables o en la qualificació final de l'assignatura. 

D'altra banda, i d'acord amb la normativa acadèmica, les conductes irregulars en l'avaluació, a més de comportar el suspens de l'assignatura,
poden donar lloc a la incoació d'un procediment disciplinari i a l'aplicació, si escau, de la sanció corresponent.

##### Qualificació
La __nota de cada avaluació ($A_i$)__ es calcularà de la següent manera:

- __Nota de l'examen ($E_i$):__ Nota de l'exàmen realitzat
    en l'avaluació. Comptara un __{{ examens }}%__.
- __Nota de pràctiques ($P_i$):__ Nota mitjana de les 
    pràctiques realitzades en l’avaluació.
    Comptarà un __{{ practiques }}%__.

$$
A_i = 0.4 \times E_i + 0.6 \times P_i
$$

Perquè un alumne supere una avaluació, la qualificació 
d’aquesta ha de ser igual o superior a 5.

$$
A_i \ge 5
$$

La __qualificació del mòdul ($M$)__ es calcularà mitjançant la mitjana 
de la nota de totes les avaluacions. En cas que alguna avaluació 
no estiga superada, la qualificació del mòdul serà com a màxim un 4.

$$
M = \frac{A_1 + A_2}{2}\\\
$$

Per norma general les notes s'arredoniran amb la fòrmula general: __>.5__.
No obstant això, en l'interval $[4, 5)$ la nota s'arredonirà a 5 sols a partir de 4.75.


#### 8.2.2. Convocatòria ordinària
Abans de finalitzar el curs, els alumnes amb alguna avaluació
suspesa tenen el dret a presentar-se a la examen de convocatòria
ordinària. Aquesta examen té com a objectiu superar
cada avaluació suspesa per separat.

També es permet que estudiants que hagen aprovat un trimestre, es presenten
a per millorar la seua nota. En aquest cas, la nota de la convocatòria ordinària
serà la que es té en compte (on es pot donar el cas que baixe la nota o no s'aprove).
Es donarà l'opció de no entregar la examen si es creu que aquesta empijorarà
el resltat anterior.

En la convocatòria, es mantindran les notes de les avaluacions
__aprovades__ en l'avalaució contínua. Per a superar la convocatòria ordinària:

- La mitjana total de les notes de les avaluacions ha de ser __superior o igual a 5__.
- La nota de cada avalucio ha de ser __superior o igual a 5__.


#### 8.2.3 Convocatòria extraordinària
L’alumnat que no supere el mòdul en la convocatòria ordinària, 
té dret a la convocatòria extraordinària, que tractarà els continguts de tot el curs,
independentment de les avaluacions aprovades anteriorment.


#### 8.2.4 Avaluació de la pràctica docent
Al final del curs es realitzarà un qüestionari per avaluar la pràctica docent i la qualitat dels materials i el procés d'aprenentatge.

### 8.3 Criteris d’avaluació mínims per superar el mòdul
Per poder superar el mòdul, l’alumnat haurà de:

- Superar els __exàmens__ que es realitzaran en cada de les avaluacions. 
  Per poder superar cada avaluació, __la mitjana dels exàmens
  haurà de ser major o igual que 5.__
- Superar les __pràctiques__ realitzades en cada avaluació. 
  Per poder superar cada avaluació, __la mitjana de les pràctiques
  haurà de ser major o igual que 5.__
- Tindre un comportament adequat a l’aula i complir les 
  normes de convivència.
- __Superar cada avaluació per separat.__


### 8.4. Quadre resum
{% include "./programacio/components/_quadre_resum.html" %}


## 9. Materials i recursos didàctics

- Pantalla digital
- Pissarra
- Plataforma educativa: __Aules__: Publicació de material, continguts, activitats, correccions i rúbriques.
- Ordinadors amb Windows.
- Accès a internet.
- Correu corporatiu.
- Entorns de desenvolupament integrats: __PyCharm__, __Google Colab__.
- Eines de control de versions: __Git__
- Llocs d'allotjament de repositoris Git: __GitHub__


## 10. Activitats complementàries i extraescolars
No s'ha contemplat cap activitat complementaria específica per aquest mòdul professional.


## 11. Temes transversals
Els temes transversals a tractar al mòdul professional al llarg del curs estan relacionats
amb el desenvolupament de les capacitats de relacions socials i comunicatives dels alumnes,
enteses com un complement necessari i important a incloure en qualsevol titulació de tipus tècnica.

Els temes transversals concrets a tractar són els següents:

- Desenvolupar habilitats de relació social i interpersonal.
- Potenciar les actituds comunicatives, de negociació i de treball en grup.
- Fomentar la motivació.
- Saber afrontar conflictes provocats per les limitacions
    tecnològiques sempre presents en un entorn tecnològic tan dinàmic i en continua evolució
    com és el sector informàtic.


## 12. Mesures de resposta educativa per a la inclusió
Es tindrà en compte a l'alumnat que necessite més atenció, de manera que
es garantirà l'accessibilitat a tots els mitjans comuns.

Accions que es portaran a terme:

- Elaboració d'__exercicis complementaris__ per aquells estudiants que ho precisen,
    tant de suport com d'aprofundiment en la matèria.
- Estimulació del treball en grup de manera remota. La composició dels grups
    serà supervisada pel docent per aconseguir grups amb nivells heterogenis.
- Facilitar la accessibilitat dels materials i recursos didàctics.
- Flexibilització en les temporitzacions de les activitats
    (realització d'exàmens, entrega de pràctiques, treball personal, etc.).

