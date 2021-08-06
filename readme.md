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

### YARN
Yet-Another-Resource-Negotiator, è un framework che permette la creazione di applicazioni per il calcolo distribuito,
gestendo le risorse del cluster.
Gestisce come schedulare i lavori, alloca le risorse del cluster alle applicazioni in esecuzione, decide come gestire le
priorità quando avvengono delle contese per la richiesta delle risorse disponibili. Inoltre monitora l'esecuzione e il completamento
dei lavori svolti.

### MapReduce
Paradigma che lavora secondo il principio _divide et impera_ cioè suddivisione in piccole parti di un 
problema complesso su di una quantità di dati enorme che vengono processate in autonomia e una volta che le singole 
parti completano il processo i risultati parziali vengono ridotti a un risultato finale.
MapReduce permette la creazione di applicazioni che sono in grado di elaborare grandi quantità di dati in parallelo.
E' possibile elaborare efficientemente Big data grazie a un sistema distribuito, per fare questo bisogna eseguire un job 
MapReduce che si suddivide in cinque fasi:
- Input, dati su HDFS.
- Funzione Map, grazie alla quale i dati in input sono trasformati in una coppia chiave valore (K, V).
- Operazione di Shuffle, processo che trasferisce l'output della funzione map alla funzione di reduce, assegnando un 
  intervallo di chiavi a ogni nodo reducer.
- Funzione Reduce, per ogni chiave vengono elaborati i valori che sono associati, creando come output una o più coppie 
  di (K, V). I valori che presentano le stesse chiavi vengono raggruppati.
- Il risultato viene scritto su di un file in HDFS.

#### Architettura
Sono presenti due componenti:
- JobTracker:
    gestisce la CPU, la memoria e la vita del job. Il JobTracker partiziona i singoli job ai nodi che contengono i dati
    che devono essere elaborati, se il nodo che contiene i dati non può elaborare il job allora viene privilegiato il 
    nodo che si trova nello stesso rack (collezione di server).
- TaskTracker:
    sono le singole componenti comandate dal JobTracker e che sui singoli nodi eseguono i task impartiti.

Le applicazioni che usano MapReduce sono implementate nel linguaggio Java grazie alla costruzione di interfacce o classi
astratte.

___
## SPARK

___
## DB Distribuiti
La gestione di una grande mole di dati presenta dei vincoli nei RDBMS:
- Vincoli di grandezza
- Vincoli di performance
- Vincoli di affidabilità

### Vincoli di taglia
Una base dati distribuita non viene allocata su di un unico server ma vengono sparsi su diversi nodi di un sistema 
distribuito.
Il partizionamento dei dati può essere effettuato perseguendo una delle seguenti strategie:
- Partizionamento verticale
- Partizionamento orizzontale

**Partizionamento verticale** i dati sono distribuiti usando tabelle diverse che sono allocate su server divsersi.

**Partizionamento orizzontale** il DB viene replicato su piu server mantenendo la stessa struttura.

### Vincoli di performance

Il numero di richieste che un DBMS può servire può essere aumentato a piacimento predisponendo un sistema distribuito
dove server differenti rispondono alle stesse richieste.
Questa soluzione è possibile grazie alla replicazione dei dati e dei servizi.
La replicazione deve prevedere una strategia in cui ogni nodo, che è responsabile di una replica, sia aggiornato alla 
versione più recente.
- Allineamento sincrono: le modifiche su di un nodo viene subito notificata a tutti i nodi.
- Allineamento asincrono: le modifiche su di un nodo vengono conservate e rilasciate con cadenza preiodica.

Le richieste da parte dei client devono essere indirizzate in modo efficiente, cosi da
evitare che alcuni server siano sovraccaricati e altri no.

- Client based: ogni client sceglie quale server contattare.
- Proxy based: ogni client invia una richiesta al proxy che la indirizza al server, seguendo un certo criterio.

### Transazioni
Quando si eseguono più operazioni contemporaneamente potrebbero verificarsi dei rischi nel caso in cui queste operazioni
vengono eseguite contemporaneamente.
I DBMS supportano il costrutto delle transazioni ovvero un raggruppamento di query SQL.

Una transazione può avere due risultati:

__Successo__: tutte le istruzioni vengono eseguite.

__Fallimento__: almeno una delle istruzioni non viene eseguita correttamente. In tal caso viene avviata una
procedura di __Roll back__ che annulla le operazioni eseguite dell'istruzione e riporta il sistema allo
stato precedente la transazione.

## Tipi di DB NoSQL

### Column-Based
I dati vengono conservati su colonne, ogni attributo di una relazione rappresenta una tabella a cui viene assegnato un _id_.
Attributi diversi riferiti alla stessa occorrenza vengono memorizzati con lo stesso _id_.


|  id |  nome |   
|---|---|
|  1 | Gino  |  
|  2 | Ugo   |
|  3 | Pino  | 
|  4 | Gino  |
|  5 | Gino  |
|  6 | Ugo   |
|  7 | Ugo   |
|  8 | Ugo   |

|  id |  cognome | 
|---|---|
|  1 | Rossi   |
|  2 | Bianchi |
|  3 | Rollo   | 
|  4 | Rossi   |
|  5 | Rossi   |
|  6 | Bianchi |
|  7 | Bianchi |
|  8 | Bianchi |

Tutti i record che presentano lo stesso valore vengono aggregati per ridurre la dimensione occupata.

| id | nome |
|---|---|
|1 | Gino|
|2 | Ugo |
|3 | Pino|
|4-5| Gino|
|6-8| Ugo|

| id | Cognome |
|---| ---|
|  1 | Rossi   |
|  2 | Bianchi |
|  3 | Rollo   | 
|  4-5 | Rossi   |
|  6-8| Bianchi |

### Key-Value 

I dati vengono conservati in strutture tabellari che prendono il nome di Hash-Table
come coppie di Key-Value (K-V).
Quando si vuole accedere a un valore bisogna indicarne la chiave. In fase di inserimento non è previsto nessun
vincolo di struttura, il valore inserito può essere atomico o aggregato.
Sarà l'applicazione che analizzerà la struttura del valore che si intende inserire.

![Tabella](https://upload.wikimedia.org/wikipedia/commons/5/5b/KeyValue.PNG)

### Document-Based

Questo modello di DB si basa sul concetto di documento.
I documenti vengono organizzati in raccolte di documenti e sono identificabili mediante una
chiave univoca, la loro struttura risulta essere flessibile.
All'interno di un documento i dati sono organizzati secondo gli attributi che vengono organizzati
come coppie (K-V), vengono supportati più valori per lo stesso attributo.

> {id:\
> type:\
> author:\
> title:\
> tags: ['aaa','bbb']\
> }

### Graph-DB
Il DB è basato sul modello di grafo, sono presenti nodi e archi.

__Nodi__: sono presenti le istanze delle entità. Viene identificato da un id univoco
e possiede gli attributi che descrivono un'entità.

__Archi__: relazioni tra nodi. Ogni arco possiede un id univoco e l'id del nodo origine
e del nodo destinazione, inoltre possiede degli attributi.
\
\
\
_Esempi di script per la connessione e l'esecuzione di query in Neo4J_

In Java è necessario aggiungere le dipendenze sul proprio file pom.
### Python
~~~
# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>", 
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

MATCH (p:Product)-[:PART_OF]->(:Category)-[:PARENT*0..]->
(:Category {categoryName:$category})
RETURN p.productName as product

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
      category="Dairy Products").data())

driver.close()
~~~
### Java
~~~
import org.neo4j.driver.*;
import static org.neo4j.driver.Values.parameters;

public class Example {

  public static void main(String...args) {

    Driver driver = GraphDatabase.driver("bolt://<HOST>:<BOLTPORT>",
              AuthTokens.basic("<USERNAME>","<PASSWORD>"));

    try (Session session = driver.session(SessionConfig.forDatabase("neo4j"))) {

      String cypherQuery =
        "MATCH (p:Product)-[:PART_OF]->(:Category)-[:PARENT*0..]->" +
        "(:Category {categoryName:$category})" +
        "RETURN p.productName as product";

      var result = session.readTransaction(
        tx -> tx.run(cypherQuery, 
                parameters("category","Dairy Products"))
            .list());
    }
    driver.close();
  }
}
~~~
