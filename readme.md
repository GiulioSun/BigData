# Strumenti per i BigData
## Tipi di Big data

Per essere definiti Big data i dati devono presentare una 
o piu delle tre caratteristiche riportate di seguito:

* Volume 
* Velocità
* Varietà

*Per big data quindi si intende quel tipo di dati che risultano difficili da gestire
e analizzare utilizzando le tecnologie di gestione dei dati tradizionali, ovvero RDBMS.*

Sono diverse le tipologie di dato che si presentano idonei per la definizione di Big data,
nel nostro caso utilizzeremo categorie di dati afferenti alle seguenti aree:

* Financial data
* Social Network

___

## Big data Life Cycle 
* Data ingestion (Acquisizione)
* Storage (Conservazione) 
* Transformation (Trasformazione)

### Data ingestion

Indichiamo i casi più rilevanti di acquisizione dei dati. Dati provenienti da RDBMS o da API (Application Programming 
Interface).
Hadoop mette a disposizione strumenti che permettono il trasferimento e la gestione dei dati raccolti da queste due 
fattispecie come ad esempio _Sqoop_ e _Kafka_.
Per approfondimenti:
- https://kafka.apache.org/
- https://sqoop.apache.org/

### Storage

La gestione e la conservazione di Big data strutturati o semi strutturati è possibile grazie ad Hadoop e ai DB NoSQL.

**Hadoop** è un framework open source scalabile creato per il calcolo distribuito, permette alle applicazioni di 
lavorare con un numero elevato di nodi e di dati che possono essere strutturati o semi strutturati
I software per il calcolo distribuito permettono la suddivisione delle operazioni su di un sistema di computer che
sono connessi tra di loro attraverso una rete.

**DB NoSQL** sono strumenti che non usano il concetto di modello relazionale, non richiedono uno schema fisso
(schemaless), sono open source e scalabili.

### Trasformation
Grazie al paradigma MapReduce, strumento nativo di Hadoop, è possibile la trasformazione e l'analisi dei dati.

___

## Hadoop
Hadoop nasce come gestore di calcoli ed elaborazioni di Big data. Questo framework è composto da diversi componenti:

### HDFS
Permette l'accesso ai dati, permette la ridondanza delle informazioni nei vari cluster gestendo eventuali 
guasti su di un nodo. I dati ammessi non devono rispettare degli schemi preimpostati.
HDFS organizza i file secondo una struttura gerarchica.
Un cluster è composto da diverse tipi di nodi.

**NameNode** è un'applicazione che gestisce il file system controllando l'accesso ai file, l'apertura, la chiusura e il
cambiamento dei nomi dei file. Gestisce come i dati siano distribuiti sui Data node, sia come debbano essere replicati 
sugli stessi, questo garantisce l'affidabilità di tutto il sistema.
Il nameNode verifica la funzionalità di tutti i nodi e la strategia di ripristino in caso di guasti di un nodo.

**DataNode** sono applicazioni situate sui nodi del cluster, hanno il compito di gestire fisicamente lo storage. Eseguono
le richieste del client, quindi la creazione, la cancellazione, la replica o le operazioni di lettura dei dati.



**YARN** permette la creazione di applicazioni per il calcolo distribuito, gestendo le risorse del cluster.

**MapReduce** paradigma che lavora secondo il principio _divide et impera_ cioè suddivisione in piccole parti di un 
problema complesso su di una quantità di dati enorme che vengono processate in autonomia e una volta che le singole 
parti completano il processo i risultati parziali vengono ridotti a un risultato finale.


