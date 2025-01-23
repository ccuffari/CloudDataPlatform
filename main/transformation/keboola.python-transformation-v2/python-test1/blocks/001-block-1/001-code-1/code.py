import pandas as pd
import os
import logging
from datetime import datetime

# Configurazione del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

try:
    # Path di input dal componente OneDrive
    input_file_path = '/data/in/tables/Data.csv'
    logging.info(f"Leggendo il file di input da: {input_file_path}")

    # Verifica se il file di input esiste
    if not os.path.exists(input_file_path):
        logging.error(f"Il file di input non esiste: {input_file_path}")
        raise FileNotFoundError(f"File di input non trovato: {input_file_path}")

    # Leggi il file CSV in un dataframe pandas
    try:
        df = pd.read_csv(input_file_path)
        logging.info("File CSV letto con successo.")
    except Exception as e:
        logging.error(f"Errore durante la lettura del file CSV: {e}")
        raise

    # Rimuovi righe completamente vuote
    try:
        initial_rows = len(df)
        df.dropna(how='all', inplace=True)
        logging.info(f"Rimosse {initial_rows - len(df)} righe completamente vuote.")
    except Exception as e:
        logging.error(f"Errore durante la rimozione delle righe vuote: {e}")
        raise

    # Aggiungi una colonna 'Id' autoincrementale (partendo da 1)
    try:
        df.insert(0, 'Id', range(1, len(df) + 1))
        logging.info("Colonna 'Id' autoincrementale aggiunta con successo.")
    except Exception as e:
        logging.error(f"Errore durante l'aggiunta della colonna 'Id': {e}")
        raise

    # Normalizza le stringhe: prima lettera maiuscola, resto minuscolo
    try:
        string_columns = ['Segment', 'Country', 'Product', 'Discount_Band', 'Month_Name']
        for col in string_columns:
            if col in df.columns:
                df[col] = df[col].str.title()
        logging.info(f"Stringhe normalizzate nelle colonne: {string_columns}")
    except Exception as e:
        logging.warning(f"Errore durante la normalizzazione delle stringhe: {e}")

    # Converti 'Date' in formato DATE compatibile con BigQuery
    try:
        default_date = '2000-01-01'
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce').fillna(default_date)
            df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        logging.info("Colonna 'Date' convertita in formato DATE.")
    except Exception as e:
        logging.error(f"Errore durante la conversione della colonna 'Date': {e}")
        raise

    # Converti 'Year' in intero
    try:
        if 'Year' in df.columns:
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0).astype(int)
        logging.info("Colonna 'Year' convertita in formato intero.")
    except Exception as e:
        logging.error(f"Errore durante la conversione della colonna 'Year': {e}")
        raise

    # Converti 'Month_Number' in intero
    try:
        if 'Month_Number' in df.columns:
            df['Month_Number'] = pd.to_numeric(df['Month_Number'], errors='coerce').fillna(0).astype(int)
        logging.info("Colonna 'Month_Number' convertita in formato intero.")
    except Exception as e:
        logging.error(f"Errore durante la conversione della colonna 'Month_Number': {e}")
        raise

    # Configura il percorso di output
    try:
        output_file_path = '/data/out/tables/tableOutput'
        logging.info(f"Percorso di output configurato: {output_file_path}")

        # Crea la directory di output se non esiste
        output_dir = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(f"Creata la directory di output: {output_dir}")
    except Exception as e:
        logging.error(f"Errore durante la configurazione del percorso di output: {e}")
        raise

    # Salva il dataframe modificato nel nuovo percorso di output
    try:
        df.to_csv(output_file_path, index=False)
        logging.info(f"File salvato con successo in: {output_file_path}")
    except Exception as e:
        logging.error(f"Errore durante il salvataggio del file: {e}")
        raise

except Exception as main_e:
    logging.critical(f"Errore critico nello script: {main_e}", exc_info=True)
