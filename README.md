# Medie registro (axios) per ISIS Bernocchi

#### DISCLAIMER
_QUESTO SOFTWARE NON E' IN ALCUN MODO AFFILIATO CON AXIOS ITALIA E RELATIVI BRAND, SOCIETA' E PRODOTTI. NON E' INTESO COME UNA MODIFICA DEL SUDDETTO SERVIZIO "REGISTRO ELETTRONICO" MA E' INTESO COME UNO SCRIPT PER AUTOMATIZZARE IL PROCESSO DI CALCOLO DELLE MEDIE TOTALI.
CONTATTO PER RECLAMI E RIMOZIONE: andrea (at) andreasau (dot) it_

### Prerequisiti
avere installato _python3_ ed il packet manager _pip_

### Installazione
per installare il modulo _selenium_ eseguire da terminale (nella cartella dello script) il seguente comando:
```bash
pip install selenium
```

### Configurazione account
Modificare le prime due righe dello script come segue
```py
userid = "TUO_USER_ID""
password = "TUA_PASSWORD"
```

### Eseguire lo script
Da terminale eseguire:
```bash
python3 main.py
```
ed attendere la stampa della media!
```shell
andrea@andrea-ubuntu:~/medieRegistro$ python3 main.py 
Hai  40  voti
La media dei voti e' :  8.74375
```

(dati riferiti al quadrimeste in corso!)

