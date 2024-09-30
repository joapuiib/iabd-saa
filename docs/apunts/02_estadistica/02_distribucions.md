---
template: document.html
title: Distribucions de probabilitat
icon: material/book-open-variant
comments: true
tags:
---

## Distribucions de probabilitat
En probabilitats i estadistica, una __distibució de probabilitat__ és una funció que indica la probabilitat que una __variable aleatòria__ prenga un valor determinat.

Una __variable aleatòria__ és una funció que assigna un valor numèric a cada resultat possible d'un __experiment aleatori__.

!!! example "Variable aleatòria: Catan"
    En el joc de taula Catan, el resultat de llançar dos daus és una variable aleatòria.

    Considerem l'__experiència aleatòria__ del llançament de dos daus. El conjunt de resultats possibles és:

    $$\Omega = \{(1,1), (1,2), \ldots, (1,6), (2,1), (2,2), \ldots, (5,6), (6,6)\}$$

    on cada parell $(i,j)$ representa el resultat obtingut en cada dau.

    La variable aleatòria $X$, que assigna a cada possible resultat la suma dels dos daus, és:

    $$X((i,j)) = i+j$$

    Els valors posibles de la variable aleatòria $X$ són:

    $$X = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$$

### Distribució de probabilitat discreta
Una distribució de probabilitat és __discreta__ si la variable aleatòria és també discreta, és a dir,
si la variable aleatòria pren valors en un conjunt __finit o numerable__.

!!! example "Catan"
    En l'example anterior, la variable aleatòria $X$ és discreta, ja que pren valors en un conjunt finit.

    Per calcular la distribució de probabilitat de la variable aleatòria $X$,
    hem de calcular la probabilitat de cada valor possible de la variable aleatòria.

    El nombre total de resultats possibles és $6 \times 6 = 36$.

    | Suma $i$ | Resultats $\{X = i\}$ | Probabilitat $P(X = i)$ |
    |----------|-----------------------|-------------------------|
    | 2        | $\{(1,1)\}$           | $\frac{1}{36} \approx 0.0278$ |
    | 3        | $\{(1,2), (2,1)\}$    | $\frac{2}{36} \approx 0.0556$ |
    | 4        | $\{(1,3), (2,2), (3,1)\}$ | $\frac{3}{36} \approx 0.0833$ |
    | 5        | $\{(1,4), (2,3), (3,2), (4,1)\}$ | $\frac{4}{36} \approx 0.1111$ |
    | 6        | $\{(1,5), (2,4), (3,3), (4,2), (5,1)\}$ | $\frac{5}{36} \approx 0.1389$ |
    | 7        | $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$ | $\frac{6}{36} \approx 0.1667$ |
    | 8        | $\{(2,6), (3,5), (4,4), (5,3), (6,2)\}$ | $\frac{5}{36} \approx 0.1389$ |
    | 9        | $\{(3,6), (4,5), (5,4), (6,3)\}$ | $\frac{4}{36} \approx 0.1111$ |
    | 10       | $\{(4,6), (5,5), (6,4)\}$ | $\frac{3}{36} \approx 0.0833$ |
    | 11       | $\{(5,6), (6,5)\}$ | $\frac{2}{36} \approx 0.0556$ |
    | 12       | $\{(6,6)\}$ | $\frac{1}{36} \approx 0.0278$ |

    ```mermaid
    xychart-beta
        title "Distribució de probabilitat la suma de dos daus"
        x-axis "Suma dels dos daus" [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y-axis "Probabilitat en %" 0 --> 20
        bar [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    ```

#### Distribució de Bernoulli
La __distribució de Bernoulli__ és una distribució de probabilitat discreta que modela 
un experiment aleatori amb dos possibles resultats: __èxit o fracàs__.

- Quan és __èxit__, la variable aleatòria pren el valor 1.
- Quan és __fracàs__, la variable aleatòria pren el valor 0.

La distribució de Bernoulli depèn de dos paràmetres:

- La probabilitat d'èxit $p$.
- La probabilitat de fracàs $q$.

On sempre es compleix que $p + q = 1$.

La funció de probabilitat de la distribució de Bernoulli és:

$$P(X = x) = \begin{cases}
    p & \text{si } x = 1 \\
    q & \text{si } x = 0 \\
    0 & \text{altrament}
\end{cases}$$

O escrit com a fòrmula, on $x \in \{0, 1\}$:

$$P(X = x) = p^x \cdot (1 - p)^{1-x}$$

!!! example "Llançament d'una moneda"
    En el llançament d'una moneda equilibrada, la variable aleatòria $X$ que indica si el resultat
    és cara o creu és una variable de Bernoulli, on $p = q = 0.5$.


#### Distribució binomial
La __distribució binomial__ és una distribució de probabilitat discreta que modela
el nomre d'èxits en una seqüència de $n$ experiments amb una probabilitat d'èxit $p$.

$$X \sim B(n, p)$$

És a dir, la distribució binomial modela el nombre de vegades que es repeteix un esdeveniment de Bernoulli.

La funció de probabilitat de la distribució binomial és la probabilitat de obtindre exactament $k$ èxits
en $n$ experiments:

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n-k}$$

on el [coeficient binomial](https://ca.wikipedia.org/wiki/Coeficient_binomial), és el
nombre de combinacions en què es poden escollir $k$ elements d'un conjunt de $n$ elements:

$$\binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}$$

!!! example "Dau igual a 6"
    En el llançament d'un dau equilibrat, la variable aleatòria $X$ que indica si el resultat
    és un 6 és una variable de Bernoulli, on $p = \frac{1}{6}$.

    Si llancem el dau 10 vegades, la variable aleatòria $Y$ que indica el nombre de vegades que ha sortit un 6
    és una variable binomial amb $n = 10$ i $p = \frac{1}{6}$.

    $$X \sim B(10, \frac{1}{6})$$

    La probabilitat de no treure cap 6 és:

    $$P(Y = 0) = \binom{10}{0} \cdot \left(\frac{1}{6}\right)^0 \cdot \left(1 - \frac{1}{6}\right)^{10} \approx 0.16151$$

    ```mermaid
    xychart-beta
        title "Distribució de probabilitat de llançar un dau 10 vegades"
        x-axis "Nombre de 6" [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y-axis "Probabilitat en %" 0 --> 35
        bar [16.151, 32.301, 29.071, 15.505, 5.427, 1.302, 0.217, 0.025, 0.002, 0.000, 0.000]
    ```

#### Distribució de Poisson
La __distribució de Poisson__ és una distribució de probabilitat discreta que modela
el nombre d'ocurrències d'un esdeveniment en un interval de temps o espai, sempre
i quan aquestes ocurrències siguin independents i la seva freqüència siga constant
independentment del temps des de l'última ocurrència.

La funció de probabilitat de la distribució de Poisson és:

$$P(X = k) = \frac{\lambda^k \cdot e^{-\lambda}}{k!}$$

on $\lambda$ és la mitjana del nombre (o el nombre esperat) d'ocurrències
en l'interval.

!!! example "Central 112"
    La central d'emergències 112 rep una mitjana de 5 trucades per minut.

    La variable aleatòria $X$ que indica el nombre de trucades que rep la central en un minut
    és una variable de Poisson amb $\lambda = 5$ si les trucades són independents.

    La probabilitat que la central rebi exactament 3 trucades en un minut és:

    $$P(X = 3) = \frac{5^3 \cdot e^{-5}}{3!} \approx 0.14037$$

    ```mermaid
    xychart-beta
        title "Distribució de probabilitat de trucades a la central 112"
        x-axis "Nombre de trucades" [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y-axis "Probabilitat en %" 0 --> 20
        bar [0.674, 3.369, 8.422, 14.037, 17.546, 17.546, 14.621, 10.444, 6.527, 3.626, 1.813, 0.825, 0.347]
    ```

    La probabilitat __acumulada__ de rebre $x$ o menys trucades en un minut és:

    $$F(x)=P(X≤x)$$

    ```mermaid
    xychart-beta
        title "Distribució de probabilitat acumulada de trucades a la central 112"
        x-axis "Nombre de trucades" [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y-axis "Probabilitat en %" 0 --> 100
        line [0.674, 4.043, 12.465, 26.502, 44.048, 61.594, 76.215, 86.659, 93.186, 96.812, 98.625, 99.450, 99.797]
    ```


### Distribució de probabilitat contínua
Una distribució de probabilitat és __contínua__ si la variable aleatòria és contínua, és a dir,
si la variable aleatòria pren valors en un conjunt __no numerable__ (infinit) de valors.

En aquest cas, la funció de probabilitat és una __funció de densitat de probabilitat__,
que indica la probabilitat que la variable aleatòria prengui un valor en un interval.

$$P(a \leq X \leq b) = \int_a^b f(x) \, dx$$

!!! note
    La probabilitat que la variable aleatòria prenga un valor exacte és sempre zero.

#### Distribució uniforme contínua
La __distribució uniforme contínua__ és una distribució de probabilitat contínua que modela
una variable aleatòria que pren valors en un interval amb la mateixa probabilitat.

La funció de densitat de probabilitat de la distribució uniforme és:

$$
f(x) = \begin{cases}
    \frac{1}{b-a} & \text{si } a \leq x \leq b \\
    0 & \text{altrament}
\end{cases}
$$

![Distribució uniforme contínua](img/uniform_distribution.png){: .center style="max-height: 300px"}

La funció de distribució de probabilitat acumulada és:

$$
F(x) = \begin{cases}
    0 & \text{si } x < a \\
    \frac{x-a}{b-a} & \text{si } a \leq x \leq b \\
    1 & \text{si } x > b
\end{cases}
$$

![Distribució uniforme contínua acumulat](img/uniform_distribution_accumulated.png){: .center style="max-height: 300px"}


!!! example "Fabricació de llapis"
    En una fàbrica de llapis, la longitud dels llapis és una variable aleatòria contínua
    que segueix una distribució uniforme en l'interval $[10, 20]$ cm.

    La probabilitat que un llapis fabricat tinga una longitud entre 15 i 17 cm és:

    $$P(15 \leq X \leq 17) = F(17) - F(15) = \frac{17-10}{20-10} - \frac{15-10}{20-10} = \frac{7}{10} - \frac{5}{10} = \frac{2}{10} = 0.2$$
    

#### Distribució normal
La __distribució normal__ és una distribució de probabilitat contínua que modela
variables aleatòries que segueixen una distribució simètrica al voltant d'un valor mitjà,
on existeiex poc valors extrems i molts valors prop del mitjà.

És el model més comú en estadística, ja que existeixen moltes variables associades
a fenòmens naturals que segueixen aquesta distribució.

Aquesta distribució es caracteritza per una _campana de Gauss_ a partir d'un __valor mitjà $\mu$__,
sobre el qual el 50% dels valors queda a cada costat, i una __desviació estàndard $\sigma$__.

$$X \sim N(\mu, \sigma)$$

La funció de densitat de probabilitat de la distribució normal és:

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

![Distribució normal](img/normal.png){: .center style="max-height: 300px"}

Alguna de les propietats de la distribució normal són:

- La mitjana, la mediana i la moda coincideixen.
- És simètrica respecte al valor mitjà.
    - L'interval $[\mu - \sigma, \mu + \sigma]$ conté el 68.27% dels valors.
    - L'interval $[\mu - 2\sigma, \mu + 2\sigma]$ conté el 95.45% dels valors.
    - L'interval $[\mu - 3\sigma, \mu + 3\sigma]$ conté el 99.73% dels valors.

!!! example "Alçada d'una població"
    L'alçada d'una població segueix una distribució normal amb una mitjana de 170 cm i una desviació estàndard de 10 cm.

    !!! note
        Aquest càlcul es pot fer mitjançant [__unitats tipificades (standard-score)__](#unitat-tipificada-standard-score)
        i la [__taula de la distribució normal__](https://en.wikipedia.org/wiki/Standard_normal_table#Cumulative_(less_than_Z)){:target="_blank"}.

    La probabilitat que una persona triada a l'atzar tinga una alçada entre 160 i 180 cm és:

    $$P(160 \leq X \leq 180) = 0.6826$$

    La probabilitat que una persona triada a l'atzar tinga una alçada entre 150 i 190 cm és:

    $$P(150 \leq X \leq 190) = 0.9544$$

    ```mermaid
    xychart-beta
        title "Distribució de probabilitat de l'alçada d'una població"
        x-axis "Alçada en cm" [140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
        y-axis "" 0 --> 5
        line [0.044318, 0.175283, 0.539910, 1.295176, 2.419707, 3.520653, 3.989423, 3.520653, 2.419707, 1.295176, 0.539910, 0.175283, 0.044318]
    ```

#### Unitat tipificada (standard-score)
La __unitat tipificada (*standard-score o z-score*)__
és una mesura que serveix per comparar una observació
dins d'una distribució estadística.

Aquesta unitat indiquen el nombre de desviacions típiques que una observació
està per damunt o per davall de la mitjana.

La unitat tipificada es calcula com:

$$z = \frac{x - \mu}{\sigma}$$

!!! example "Unitat tipificada de l'alçada"
    Donada una població amb una mitjana de 170 cm i una desviació estàndard de 10 cm,
    calculem les unitats tipificades de les alçades 160 i 180 cm.

    1. Per a $x = 160$ cm:

        $$z_1 = \frac{160 - 170}{10} = -1$$

    2. Per a $x = 180$ cm:
        
        $$z_2 = \frac{180 - 170}{10} = 1$$
    

#### Distribució normal estàndard
La __distribució normal estàndard__ és cas especial d'una distribució normal, que té una mitjana $\mu = 0$
i una desviació estàndard $\sigma = 1$.

$$X \sim N(0, 1)$$

Aquesta distribució és molt important en estadística, ja que permet calcular
la probabilitat acumulada de qualsevol distribució normal utilitzant les [__unitats tipificades__](#unitat-tipificada-standard-score)
i consultat la [__taula de la distribució normal__](https://en.wikipedia.org/wiki/Standard_normal_table#Cumulative_(less_than_Z)){:target="_blank"}.

Aquesta taula indica la __probabilitat acumulada__ de trobar un valor menor que $z$
en una distribució normal estàndard.

!!! example "Càlcul de probabilitats alçada d'una població"
    Calculem la probabilitat que una persona tinga una alçada entre 160 i 180 cm.

    Utilitzant les unitats tipificades $z_1 = -1$ i $z_2 = 1$,
    podem calcular la probabilitat acumulada de trobar un valor entre $z_1$ i $z_2$:

    $$P(-1 \leq Z \leq 1) = P(Z \leq 1) - P(Z \leq -1)$$

    Consultem la taula de la distribució normal estàndard:

    $$P(Z \leq 1) = 0.8413$$

    $$P(Z \leq -1) = 0.1587$$

    Per tant:

    $$P(-1 \leq Z \leq 1) = 0.8413 - 0.1587 = 0.6826$$






## Bibliografia
- [Distribució de probabilitat, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_de_probabilitat)
- [Variable aleatòria, Viquipèdia](https://ca.wikipedia.org/wiki/Variable_aleat%C3%B2ria)
- [Distribució de Bernoulli, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_de_Bernoulli)
- [Distribució binomial, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_binomial)
- [Distribució de Poisson, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_de_Poisson)
- [Distribució uniforme contínua, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_uniforme_cont%C3%ADnua)
- [Distribució normal, Viquipèdia](https://ca.wikipedia.org/wiki/Distribuci%C3%B3_normal)
