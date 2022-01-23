# **Gruppo coniche**

*Il nostro gruppo per la realizzazione di questo progetto è formato da Gallo, Pala, Corbo, Carotenuto, Minichiello,
Fulgione, Todino e Di Gennaro.*

## **Ruoli**

- Pala: **Gestione e realizzazione del software e addetto ad aggiornare il file .md**
- Corbo: **Gestione e realizzazione del software e addetto ad aggiornare il file .md**
- Carotenuto: **Gestione e realizzazione del software e addetto ad aggiornare il file .md**
- Gallo: **Gestione, realizzazione del software e gestione del ReadMe**
- Minichiello: **Gestione e realizzazione del software e addetto ad aggiornare il file .md**
- Fulgione: **Gestione e realizzazione del software e addetto ad aggiornare il file .md**
- Todino: **Creazione diagramma di flusso e gestione e realizzazione del software**
- Di Gennaro: **Creazione diagramma di flusso e gestione del ReadMe**

## **Organizzazione del gruppo:**

*Prima di andare a lavorare effettivamente sul codice abbiamo stabilito dei giorni e degli orari precisi dove ci saremmo
potuti vedere su Google Meet, questo per avere un organizzazione più efficace e pulita.*

Come si può notare sopra bene o male tutti quanti abbiamo lo stesso ruolo, ma c'è da dire che, in realtà, durante una
riunione Meet ognuno ha un ruolo ben preciso in cui spesso ci si alterna.

- C'è chi, qualora ce ne fosse la necessità, presenta da Youtube un video che potrebbe aiutarci ulteriormente nella
  realizzazione del codice.
- C'è chi, come me in questo caso, che scrive un file ReadMe per spiegare come ci siamo organizzati.
- C'è chi lavora sul codice e lo presenta per rendere tutti partecipi nel lavoro.

In particolare devo dire che la nostra grande dote da gruppo è quella che anche se qualcuno durante la riunione se ne
deve andare perchè ha degli impegni, il gruppo continua a lavorare e la volta prossima verrà fatto un sunto di quello
che è stato fatto in sua assenza.
***

# Alla conquista di Saturno

## **Descrizione del gioco:**

### *Abstract (descrizione delle caratteristiche del gioco):*

È un gioco arcade 2D ambientato nello spazio, nella Via Lattea, dove impersonifichiamo degli alieni a comando di una
navicella e che vogliono conquistare un nuovo pianeta. La loro scelta ricade su Saturno e si dirigono verso esso. La
traiettoria della navicella è decisa dal giocatore, il quale seleziona una conica tra la retta e la parabola e
successivamente inserisce un’equazione della conica selezionata. La navicella si muoverà lungo la lista dei punti
appartenenti alla conica e arriverà nei pressi di Saturno. A questo punto la navicella dovrà schivare i detriti che
compongono gli anelli di Saturno, affinché possa raggiungere la superficie del pianeta. Le abilità del pilota porteranno
alla buona o alla cattiva riuscita della missione aliena.

### *Interfaccia:*

Il gioco comincia con la prima scena, nella quale c’è l’astronave su uno sfondo spaziale, e al giocatore compare un pop
up che gli chiede di selezionare una conica da un elenco che gli viene mostrato. Una volta selezionata la conica, al
giocatore viene chiesto di inserire i parametri dell’equazione della conica selezionata. L’astronave comincerà a
muoversi lungo la lista di punti, che sono i punti che compongono la conica data in input dal giocatore, e l’astronave
continuerà a muoversi finché essa non uscirà dallo schermo.

A questo punto inizia la seconda scena, nella quale si vede l’astronave che si muove verso Saturno e, quando i due
actor (dell’astronave e di Saturno) saranno molto vicini, terminerà la seconda scena.

Inizia la terza scena, nella quale inizia il gioco vero e proprio. Il giocatore deve schivare i proiettili (detriti) che
gli vengono incontro e, se venisse colpito tre volte, perderebbe il gioco e gli comparirebbe la scritta “GAME OVER”. Se
il giocatore riuscisse a non farsi colpire tre volte, vincerebbe il gioco e gli comparirebbe la scritta “YOU WON”.
*Funzionalità*
Il giocatore seleziona da un elenco una conica e inserisce all’interno di una casella di testo un’equazione della conica
scelta. L’equazione della conica rappresenta la traiettoria che compierà la navicella. Appena la navicella si troverà
nei pressi di Saturno cambierà la scena e si dovranno schivare i frammenti più o meno grandi, di cui sono formati gli
anelli di Saturno. In caso il giocatore non venisse colpito più di tre volte dai detriti che gli vengono in contro, egli
avrà terminato il gioco con successo, in caso contrario il gioco terminerà con una scritta “Game Over”.

# ![github-small](https://github.com/renatogallo27/gruppo-coniche/blob/main/images/astro.png)
# ![github-small](https://github.com/renatogallo27/gruppo-coniche/blob/main/images/saturno.png)

### *Requisiti*

#### *Concetti teorici:*

Conoscenza delle caratteristiche delle coniche (in particolare retta e parabola) e della forma delle loro equazioni.

#### *Software:*

Bisogna possedere python e un suo interprete sul proprio computer.

#### *Moduli python:*

Bisogna avere installati sul proprio computer i moduli python: pygame, pgzero, random,
(possibili altri moduli che probabilmente ci serviranno ma di cui adesso non siamo a conoscenza).
