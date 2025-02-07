import streamlit as st
import pandas as pd

# Funzione per caricare i dati (eventualmente si può usare @st.cache_data in Streamlit 1.18+)
@st.cache_data(show_spinner=False)
def load_data():
    # Assicurati che il file "Cloud_Data_Platform.csv" sia nella stessa cartella dello script.
    df = pd.read_csv("CDP_generator.csv", encoding='latin-1')  # or 'iso-8859-1', 'cp1252')
    return df

# Ordine predefinito delle dimensioni (come da indice)
DIMENSION_ORDER = [
    "Data Ingestion",
    "Data Landing",
    "Data Manipulation & Orchestration",
    "Data Warehouse / Data Lake / Lakehouse",
    "Data Governance",
    "Data Security",
    "Data Visualization",
    "CI/CD"
]

# Carica i dati
df = load_data()

# Imposta la pagina Streamlit
st.set_page_config(page_title="Cloud Data Platform Builder", layout="wide")

st.title("Cloud Data Platform Builder Dashboard")
st.write("Questa dashboard guida l'utente nella scelta delle soluzioni per costruire una Cloud Data Platform. "
         "Seleziona uno o più provider cloud e rispondi alle domande per ciascuna dimensione per scoprire le risorse consigliate.")

# Selezione dei provider (multiselect)
provider_options = sorted(df["Cloud Provider"].unique())
selected_providers = st.sidebar.multiselect("Seleziona Cloud Provider", provider_options, default=provider_options)

if not selected_providers:
    st.warning("Seleziona almeno un provider dal menu laterale!")
    st.stop()

# Creiamo un dizionario per memorizzare le scelte dell'utente
selections = {}  # struttura: { provider: { dimensione: { question: selected_scenario } } }

# Per organizzare il layout, creiamo una sezione per ogni dimensione in ordine predefinito.
st.header("Configurazione per Dimensione")
for dim in DIMENSION_ORDER:
    # Filtra i dati per la dimensione corrente e per i provider selezionati
    df_dim = df[(df["Dimensione"] == dim) & (df["Cloud Provider"].isin(selected_providers))]
    if df_dim.empty:
        continue

    with st.container():
        st.subheader(f"Dimensione: {dim}")
        # Se vogliono visualizzare i dati per ciascun provider, possiamo usare delle tab
        tabs = st.tabs(selected_providers)
        for i, prov in enumerate(selected_providers):
            with tabs[i]:
                st.markdown(f"**Provider: {prov}**")
                # Inizializza il dizionario per il provider e dimensione se non esiste
                selections.setdefault(prov, {}).setdefault(dim, {})
                # Filtra per il provider corrente
                df_provider = df_dim[df_dim["Cloud Provider"] == prov]
                # Per ogni domanda (raggruppata per "Actual Question") nella dimensione per questo provider
                for question, group in df_provider.groupby("Actual Question"):
                    st.markdown(f"**Domanda:** {question}")
                    # Le opzioni sono i valori unici della colonna "Scenario/Answer Proposal"
                    options = group["Scenario/Answer Proposal"].unique().tolist()
                    # Usa un radio button per la selezione
                    user_choice = st.radio(f"Seleziona la casistica per la domanda sopra ({prov}, {dim}):", options, key=f"{prov}_{dim}_{question}")
                    selections[prov][dim][question] = user_choice
                    # Una volta scelto, mostriamo la risorsa corrispondente
                    # Filtra la riga che corrisponde alla scelta effettuata
                    row = group[group["Scenario/Answer Proposal"] == user_choice]
                    if not row.empty:
                        resource = row.iloc[0]["Recommended Resource"]
                        justification = row.iloc[0]["Justification"]
                        doc_link = row.iloc[0]["Documentation Link"]
                        st.info(f"**Risorsa Consigliata:** {resource}\n\n*Motivazione:* {justification}\n\n[Documentazione]({doc_link})")
                    st.markdown("---")

# Sezione di riepilogo/infrastrutturale
st.header("Schema Infrastrutturale")

# Per ogni provider selezionato, raggruppa le scelte per dimensione e mostra le risorse finali
for prov in selected_providers:
    st.subheader(f"Provider: {prov}")
    resource_summary = []
    for dim in DIMENSION_ORDER:
        if dim in selections.get(prov, {}):
            dim_summary = []
            for question, answer in selections[prov][dim].items():
                # Trova la riga corrispondente per ottenere la risorsa
                row = df[(df["Dimensione"] == dim) &
                         (df["Cloud Provider"] == prov) &
                         (df["Actual Question"] == question) &
                         (df["Scenario/Answer Proposal"] == answer)]
                if not row.empty:
                    resource = row.iloc[0]["Recommended Resource"]
                    dim_summary.append(f"- **{question}**: {resource}")
            if dim_summary:
                resource_summary.append(f"**{dim}:**\n" + "\n".join(dim_summary))
    if resource_summary:
        st.markdown("\n\n".join(resource_summary))
        st.markdown("---")

st.markdown("### Nota:")
st.markdown("Le risorse e le scelte sono determinate in base alle risposte fornite per ciascuna dimensione e per ogni provider selezionato. Utilizza i filtri laterali e le opzioni per personalizzare la configurazione della tua Cloud Data Platform.")

