# Progetto Basi di Dati: Piattaforma Gestione Viaggi Aerei

Ecco una TODO list dettagliata in formato Markdown per aiutarti a organizzare il lavoro del tuo progetto universitario, basata sulla consegna che hai fornito.

## Fase 1: Pianificazione e Progettazione

    [ ] Leggere attentamente e comprendere tutti i requisiti del progetto e i punti oscuri da chiarire col docente.

    [ ] Discutere e definire l'ambito esatto del progetto, identificando le funzionalità obbligatorie e quelle opzionali/di miglioramento da implementare.

    [] Scegliere il DBMS da utilizzare (Postgres consigliato).

    [ ] Progettare lo schema della base di dati a livello concettuale (E/R o notazione del corso).

    [ ] Progettare lo schema della base di dati a livello logico (relazionale) a partire dal modello concettuale.

    [ ] Documentare la progettazione concettuale e logica, includendo commenti e rispettando la notazione del Modulo 1 del corso.

    [ ] Pianificare la struttura del backend (Flask routes, modelli SQLAlchemy, logica di business).

    [ ] Pianificare la struttura del frontend (pagine HTML, stili CSS, interazione utente).

    [ ] Definire le principali query necessarie per le funzionalità richieste (ricerca voli, statistiche compagnie, ecc.).

    [ ] (Opzionale, se ci si concentra su questi aspetti) Identificare i punti specifici in cui applicare integrità dei dati, sicurezza e ottimizzazioni di performance.

## Fase 2: Implementazione del Database

    [ ] Installare e configurare il DBMS scelto.

    [ ] Creare il database.

    [ ] Implementare lo schema logico nel DBMS (creazione tabelle, definizione tipi di dato, chiavi primarie/esterne).

    [ ] Implementare i vincoli di integrità (CHECK, UNIQUE, NOT NULL) a livello di schema basati sul design logico.

    [ ] Scrivere uno script (SQL o altro) per la creazione completa dello schema del database.

    [ ] Creare dati artificiali significativi per testare tutte le funzionalità.

    [ ] Scrivere uno script per l'inserimento dei dati artificiali nel database.

    [ ] (Miglioramento) Implementare eventuali trigger o altre regole di integrità a livello di database.

    [ ] (Miglioramento) Definire ruoli e permessi a livello di database (se rilevante per la sicurezza).

    [ ] (Miglioramento) Creare gli indici necessari per le query identificate come frequenti o critiche per le performance.

    [ ] (Miglioramento) Creare eventuali viste materializzate per aggregazioni o dati di uso frequente.

## Fase 3: Implementazione del Backend (Python, Flask, SQLAlchemy)

    [ ] Configurare l'ambiente di sviluppo Python con le dipendenze necessarie.

    [ ] Installare le librerie Flask e SQLAlchemy (o Flask-SQLAlchemy).

    [ ] Configurare la connessione al database tramite SQLAlchemy.

    [ ] Definire i modelli SQLAlchemy corrispondenti alle tabelle del database.

    [ ] Implementare le route Flask per gestire le richieste HTTP e le interazioni con il database:

        [ ] Route per la pagina principale e la ricerca voli (accessibile anche a utenti anonimi).

        [ ] Route per la registrazione e il login degli utenti (Compagnie e Passeggeri).

        [ ] Logica di ricerca voli, inclusa la gestione delle soste intermedie (almeno 2 ore di scalo).

        [ ] Logica per l'ordinamento dei risultati della ricerca voli in base a vari parametri (costo, tempo, numero di soste, ecc.).

        [ ] Route per la visualizzazione del dettaglio del volo e la selezione di posti ed extra.

        [ ] Logica per il processo di acquisto biglietti.

        [ ] Logica per l'aggiornamento automatico della disponibilità posti dopo un acquisto.

        [ ] Route e logica per l'area riservata delle Compagnie Aeree:

            [ ] Gestione dell'inserimento di nuove tratte servite.

            [ ] Visualizzazione delle statistiche (numero passeggeri per volo, guadagno totale, tratte richieste).

        [ ] (Opzionale/Miglioramento) Route e logica per l'area riservata dei Passeggeri (es. visualizzazione biglietti acquistati).

    [ ] (Miglioramento) Implementare la gestione delle transazioni per garantire l'atomicità delle operazioni critiche (es. acquisto biglietto).

    [ ] (Miglioramento) Implementare politiche di autorizzazione basate sui ruoli utente (Compagnia, Passeggero, Anonimo).

    [ ] (Miglioramento) Implementare difese contro XSS e SQL injection (validazione input, uso corretto di ORM/Expression Language).

    [ ] Assicurarsi di utilizzare SQLAlchemy ORM o Expression Language per astrarre dal dialetto SQL specifico del DBMS.

## Fase 4: Implementazione del Frontend (HTML, CSS, Optional JS)

    [ ] Creare la struttura di base delle pagine HTML richieste.

    [ ] Implementare la pagina di ricerca voli con i campi di input necessari.

    [ ] Implementare la pagina dei risultati della ricerca, mostrando le alternative e le opzioni di ordinamento.

    [ ] Implementare la pagina di dettaglio del volo (mostrare layout posti, opzioni extra).

    [ ] Implementare le pagine di Login e Registrazione.

    [ ] Implementare la pagina di conferma acquisto biglietto.

    [ ] Implementare le pagine per l'area riservata delle Compagnie Aeree (form per inserire tratte, pagine per visualizzare statistiche).

    [ ] Utilizzare un framework CSS esistente (W3.CSS, Bootstrap, o altro) o riutilizzare il frontend sviluppato per il corso "Tecnologie e applicazioni web".

    [ ] Applicare stili CSS per garantire un'interfaccia utente minimale ma chiara e funzionale.

    [ ] (Opzionale) Aggiungere codice JavaScript per migliorare l'esperienza utente (es. validazione form lato client, aggiornamenti dinamici senza ricaricare la pagina).

## Fase 5: Test e Refinamento

    [ ] Testare lo script di creazione e popolamento del database per verificare che funzioni correttamente.

    [ ] Testare tutte le funzionalità implementate nel backend (endpoints API) utilizzando vari scenari e dati artificiali.

    [ ] Testare il flusso utente completo sul frontend, simulando le azioni di utenti anonimi, passeggeri e compagnie.

    [ ] Verificare l'integrità dei dati in scenari complessi (es. acquisti simultanei, operazioni che coinvolgono più tabelle).

    [ ] Verificare la sicurezza dell'applicazione (es. tentativi di accesso non autorizzato, validazione input).

    [ ] Verificare le performance delle query principali, soprattutto quelle utilizzate nella ricerca voli e nelle statistiche.

    [ ] Debuggare e correggere eventuali errori riscontrati durante i test.

    [ ] Rifinire l'interfaccia utente e l'esperienza complessiva per renderla più intuitiva.

## Fase 6: Documentazione

    [ ] Redigere la relazione di progetto in formato PDF.

    [ ] Scrivere l'Introduzione della relazione (descrizione ad alto livello dell'applicazione, struttura del documento).

    [ ] Descrivere dettagliatamente le Funzionalità principali fornite dall'applicazione.

    [ ] Presentare la Progettazione concettuale e logica della base di dati, spiegandola e motivandola, includendo i diagrammi con la notazione del corso.

    [ ] Descrivere una selezione delle Query principali implementate all'interno dell'applicazione, utilizzando una sintassi SQL opportuna.

    [ ] Descrivere le Principali scelte progettuali relative a integrità, sicurezza, performance, astrazione dal DBMS, motivandole adeguatamente.

    [ ] Includere Ulteriori informazioni rilevanti (scelte tecnologiche specifiche, librerie usate, ecc.).

    [ ] Aggiungere l'Appendice sul Contributo al progetto, specificando il ruolo e il lavoro svolto da ciascun membro del gruppo.

    [ ] Assicurarsi che il codice del progetto sia opportunamente strutturato e commentato per favorirne la manutenibilità e leggibilità.

## Fase 7: Consegna

    [ ] Rivedere tutti i materiali da consegnare (codice sorgente, script database, relazione PDF).

    [ ] Preparare il pacchetto del progetto secondo le istruzioni di consegna fornite dall'università.

    [ ] Consegnare il progetto entro la scadenza stabilita.
