# Data processing code

2024-02-14. Emilio Mayorga

## Summary of the aligned files and processing code

We use Python code consisting of one module and four Jupyter notebooks to transform the source data Excel file to three CSV files "aligned" to the Darwin Core (DwC) extended Measurement or Fact (eMoF) standard. The source data file was obtained from ... and is called `PSZMP_2014-2022_Species_Data_Keister_Lab.xlsx` and is found in the `sourcedata` directory.

### DwC eMoF aligned CSV files

The resulting DwC eMoF files are found in the `aligned_csvs` directory:

- `DwC_event.csv`: Event file. Each row defines a sampling "event", where each event is described with the event type (under `eventType`), temporal and spatial information (including depth), a unique ID, and its relationship to a "parent" event if applicable. Three event types are defined: "cruise", "stationVisit" (with a cruise parent) and "sample" (with a stationVisit parent). A sample event is the sample collection from each net deployment, where the `eventID` is taken directly from the `Sample Code` column in the original data file and a `samplingProtocol` description is included. 
  - There are XX cruises, XX station visits and XX samples.
- `DwC_occurrence.csv`: Occurrence file. Each row defines a unique taxonomic identification and associated sex and life stage determinations, if present. Each occurrence entry is associated with a "sample" event in `DwC_event.csv` via the `eventID` code. The taxonomic description includes the associated taxonomic match up and details from WoRMS (World Register of Marine Species) based on the `Genus species` column in the original data file, plus XX manual matchups when an automatic matchup could not be made.
  - There are XX occurrences.
- `DwC_emof.csv`: eMoF file. The eMoF file provides a flexible and open-ended mechanism for storing additional information about the dataset not found in the Event and Occurrence files, or to provide additional details about information provided in those two files. Each eMoF type is associated with an external community vocabulary references specifying the measurement type and, when appropriate, the measurement unit. 4 eMoF types are included:
  - density measurements: XX entries
  - multinet sampling descriptions: XX entries
  - Sampling method descriptions: XX entries
  - Sampling net mesh size descriptions: XX entries

### Intermediate WoRMS taxonomic match-up file

The processing code creates two intermediate files that are not part of the final DwC-aligned output files: `intermediate_DwC_occurrence_life_history_stage.csv` and `intermediate_DwC_taxonomy.csv`. They are used as temporary information passed from one Jupyter notebook to another, or within the same notebook.

`intermediate_DwC_taxonomy.csv` contains the taxonomic match-up between the original `Genus species` entry and the corresponding, fully fleshed out WoRMS information. Currently it contains XX entries (NOTE: there may be cases where different source `Genus species` entries are matched to the same WoRMS taxa).

### Processing code

**TODO: ADD MENTION OF `common_mappings.json`**

The processing code consists of four Python Jupyter notebooks, a Python module file and a JSON file.

- `data_preprocess.py`. This module serves as "pre-processor" and is called by each Jupyter notebook.  It reads the source data file and applies several corrections and parsing steps: (TO BE FILLED OUT).
- `PSZMP-dwcEvent.ipynb`. This notebook produces the `DwC_event.csv` file.
- `PSZMP-dwcTaxonomy.ipynb`. This notebook produces an intermediate file,  `intermediate_DwC_taxonomy.csv`, used later in the `PSZMP-dwcOccurrence.ipynb` notebook.
- `PSZMP-dwcOccurrence.ipynb`. This notebook produces the `DwC_occurrence.csv` file.
- `PSZMP-dwceMoF.ipynb`. This notebook produces the `DwC_emof.csv` file.
- `common_mappings.json`

The processing code runs in a `conda` Python environment that can be created with the conda environment file `environment-py.yaml`. 
