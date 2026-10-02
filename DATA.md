# Data

**Structured or not, Claude can read it.** Open datasets, statistics, the City's own how-to pages, and the experience of the people in your team are all fair game.

Ground rules:
- **Public data only.** No personal data in any prototype, ever. Invent realistic fake cases when you need them.
- Respect the terms of use of every site you read.
- Check the **period covered** by each dataset: some series stop years ago. Say so in your README.

---

## 1. Comune di Milano open data portal

**[dati.comune.milano.it](https://dati.comune.milano.it/web/portale-del-dato)**: hundreds of datasets under Creative Commons licences, in CSV, JSON and often GeoJSON. Each dataset page is at `https://dati.comune.milano.it/dataset/<slug>`.

### Curated for the three tracks

**Where the City is: offices and desks** (all tracks)

| Dataset | Slug |
|---|---|
| [Sedi dei servizi anagrafici](https://dati.comune.milano.it/dataset/ds549-sedi-dei-servizi-anagrafici) (registry offices, with coordinates) | `ds549-sedi-dei-servizi-anagrafici` |
| [Sedi municipi nel Comune di Milano](https://dati.comune.milano.it/dataset/ds1299-sedi-municipi-nel-comune-di-milano) | `ds1299-sedi-municipi-nel-comune-di-milano` |
| [Servizio Sociale Professionale Territoriale: le sedi](https://dati.comune.milano.it/dataset/ds1303-servizio-sociale-professionale-territoriale-le-sedi) | `ds1303-servizio-sociale-professionale-territoriale-le-sedi` |
| [Sede dei Sindacati e Patronati](https://dati.comune.milano.it/dataset/ds550_sede-dei-sindacati-e-patronati) | `ds550_sede-dei-sindacati-e-patronati` |

**Who arrives in Milan** (Track 01)

| Dataset | Slug |
|---|---|
| [Iscrizioni anagrafiche per luogo di provenienza (2020–2024)](https://dati.comune.milano.it/dataset/ds1959-popolazione-iscrizioni-anagrafiche-per-luogo-di-provenienza) | `ds1959-popolazione-iscrizioni-anagrafiche-per-luogo-di-provenienza` |
| [Iscrizioni anagrafiche per classi di età (2020–2024)](https://dati.comune.milano.it/dataset/ds1957-popolazione-iscrizioni-anagrafiche-per-classi-di-eta) | `ds1957-popolazione-iscrizioni-anagrafiche-per-classi-di-eta` |
| [Iscrizioni anagrafiche per quartiere (2020–2024)](https://dati.comune.milano.it/dataset/ds1954-popolazione-iscrizioni-anagrafiche-per-quartiere-2020-avanti) | `ds1954-popolazione-iscrizioni-anagrafiche-per-quartiere-2020-avanti` |
| [Stranieri: residenti per cittadinanza (1979–2025)](https://dati.comune.milano.it/dataset/ds74-popolazione-residenti-stranieri-cittadinanza-e-municipio) | `ds74-popolazione-residenti-stranieri-cittadinanza-e-municipio` |
| [Popolazione: residenti per cittadinanza e quartiere](https://dati.comune.milano.it/dataset/ds27-popolazione-residenti-cittadinanza-quartiere-serie-storica) | `ds27-popolazione-residenti-cittadinanza-quartiere-serie-storica` |
| [Proiezioni della popolazione straniera per municipio (2023–2039)](https://dati.comune.milano.it/dataset/ds31-popolazione-proiezioni-popolazione-stranieri-municipio) | `ds31-popolazione-proiezioni-popolazione-stranieri-municipio` |
| [Istruzione: sedi universitarie degli atenei milanesi](https://dati.comune.milano.it/dataset/ds94-infogeo-atenei-sedi-localizzazione) | `ds94-infogeo-atenei-sedi-localizzazione` |

**How services perform: demand and satisfaction** (Tracks 02 and 03)

| Dataset | Slug |
|---|---|
| [Pass per la sosta: richieste allo sportello](https://dati.comune.milano.it/dataset/ds701-pass-per-la-sosta-di-residenti-e-dimoranti-richieste-allo-sportello) | `ds701-pass-per-la-sosta-di-residenti-e-dimoranti-richieste-allo-sportello` |
| [Pass per la sosta: richieste online](https://dati.comune.milano.it/dataset/ds700-pass-per-la-sosta-di-residenti-e-dimoranti-richieste-online) | `ds700-pass-per-la-sosta-di-residenti-e-dimoranti-richieste-online` |
| [Qualità del servizio 2024: pass sosta](https://dati.comune.milano.it/dataset/ds2695_rilevazione-qualita-servizio-richieste-pass-sosta-anno-2024) | `ds2695_rilevazione-qualita-servizio-richieste-pass-sosta-anno-2024` |
| [Qualità del servizio 2022: richieste residenza](https://dati.comune.milano.it/dataset/ds1702-rilevazione-qualita-servizio-richieste-residenza-anno-2022) | `ds1702-rilevazione-qualita-servizio-richieste-residenza-anno-2022` |
| [Qualità del servizio 2021: richieste certificati anagrafici](https://dati.comune.milano.it/dataset/ds1512-rilevazione-qualita-servizio-richieste-certificati-anno-2021) | `ds1512-rilevazione-qualita-servizio-richieste-certificati-anno-2021` |
| [Qualità del servizio 2021: certificati di Stato Civile](https://dati.comune.milano.it/dataset/ds1515-rilevazione-qualita-servizio-richieste-certificati-stato-civile-anno-2021) | `ds1515-rilevazione-qualita-servizio-richieste-certificati-stato-civile-anno-2021` |
| [Qualità del servizio 2021: appuntamenti online](https://dati.comune.milano.it/dataset/ds1511-rilevazione-della-qualita-del-servizio-appuntamenti-on-line-anno-2021) | `ds1511-rilevazione-della-qualita-del-servizio-appuntamenti-on-line-anno-2021` |
| [Qualità del servizio 2021: dichiarazioni TARI](https://dati.comune.milano.it/dataset/ds1587-rilevazione-qualita-servizio-presentaz-dichiaraz-tari-anno-2021) | `ds1587-rilevazione-qualita-servizio-presentaz-dichiaraz-tari-anno-2021` |

The satisfaction surveys often include free-text comments: a good input for Claude to classify and summarise.

**Moving around the city** (accessibility in a physical sense)

| Dataset | Slug |
|---|---|
| [ATM: fermate linee metropolitane](https://dati.comune.milano.it/dataset/ds535_atm-fermate-linee-metropolitane) | `ds535_atm-fermate-linee-metropolitane` |
| [ATM: percorsi linee metropolitane](https://dati.comune.milano.it/dataset/ds539_atm-percorsi-linee-metropolitane) | `ds539_atm-percorsi-linee-metropolitane` |
| [Ambiti della sosta](https://dati.comune.milano.it/dataset/ds83-infogeo-sosta-ambiti-localizzazione) | `ds83-infogeo-sosta-ambiti-localizzazione` |
| [Osservatorio Milano: obiettivi, accessibilità](https://dati.comune.milano.it/dataset/ds640_osservatorio_milano__obiettivi_accessibilita) | `ds640_osservatorio_milano__obiettivi_accessibilita` |
| [Barriere architettoniche negli edifici scolastici statali (a.s. 2020/21)](https://dati.comune.milano.it/dataset/ds1868-accorgimenti-per-superamento-barriere-architettoniche-edifici-scuole-statali-as-2020-2021) | `ds1868-accorgimenti-per-superamento-barriere-architettoniche-edifici-scuole-statali-as-2020-2021` |

This list is a starting point, not a fence. Search the portal for more.

### Querying the portal from code

The portal runs CKAN, so it has a standard JSON API. No key needed.

```bash
# Search datasets
curl "https://dati.comune.milano.it/api/3/action/package_search?q=residenza&rows=20"

# Dataset details, including the download URL of every resource (CSV, JSON, GeoJSON)
curl "https://dati.comune.milano.it/api/3/action/package_show?id=ds549-sedi-dei-servizi-anagrafici"

# Query rows directly, for resources with the datastore active
curl "https://dati.comune.milano.it/api/3/action/datastore_search?resource_id=<resource-id>&limit=5"
```

See [`starter/portal.py`](starter/portal.py) for a tiny helper that searches and downloads.

---

## 2. Other City data portals

- **[MilanoStatistica](https://milanostatistica.comune.milano.it/)**: population, economy and territory statistics.
- **[Linked Open Data portal](https://portalelod.comune.milano.it/home)**: semantic data about the city.

## 3. Public service pages (unstructured)

The knowledge a newcomer or a citizen needs mostly lives in web pages, not datasets. Claude can read them, summarise them and reason over them.

- **[comune.milano.it](https://www.comune.milano.it/)**: how-to pages for every City service (registry, certificates, TARI, parking permits, social services).
- **[yesmilano.it](https://www.yesmilano.it/)**: the city's information for visitors and international students.
- **[atm.it](https://www.atm.it/)**: public transport, including accessibility information for stations.

Save the pages you use (or their URLs and retrieval date) in your repo, so the jury can see your sources.

## 4. What you know

The people in your team, and City staff in the room, know where citizens get stuck. Domain experts are the best dataset here. Write down what they tell you, and use it.
