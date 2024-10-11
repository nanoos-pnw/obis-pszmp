# Data processing steps and code

2024-10-09

## Summary of the aligned files and processing code

We used Python code consisting of one module, four Jupyter notebooks and a JSON file to transform the source data Excel file to three CSV files "aligned" to the Darwin Core (**DwC**) Event Core with Extended Measurement or Fact (eMoF) extensionn standard. The source data file, `PSZMP_2014-2022_Species_Data_Keister_Lab.xlsx`, was obtained from Keister lab staff and is found in the `sourcedata` directory.

### DwC aligned CSV files

The resulting DwC files are found in the [`aligned_csvs`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/aligned_csvs) directory (as zipped files):

- `DwC_event.csv`: Event file. Each row defines a sampling "event", where each event is described with the event type (under `eventType`), temporal and spatial information (including depth), a unique ID, and its relationship to a "parent" event if applicable. Three event types are defined: "cruise", "stationVisit" (with a cruise parent) and "sample" (with a stationVisit parent). A sample event is the sample collection from each net deployment, where the `eventID` is taken directly from the `Sample Code` column in the original data file and a `samplingProtocol` description is included. 
  - There are 8470 records: 1332 cruises, 3569 station visits and 3569 samples.
- `DwC_occurrence.csv`: Occurrence file. Each row defines a unique taxonomic identification and associated sex and life stage determinations, if present. Each occurrence entry is associated with a "sample" event in `DwC_event.csv` via the `eventID` code. The taxonomic description includes the associated taxonomic match up and details from WoRMS (World Register of Marine Species) based on the `Genus species` column in the original data file, plus a few manual matchups when an automatic matchup could not be made.
  - There are 185737 occurrences.
- `DwC_emof.csv`: eMoF file. The eMoF file provides a flexible and open-ended mechanism for storing additional information about the dataset not found in the Event and Occurrence files, or to provide additional details about information provided in those two files. There are 380462 eMoF records, each classified by a specific type (`measurementType`). Each eMoF type is associated with an external community vocabulary references specifying the measurement type and, when appropriate, the measurement unit. 5 eMoF types are included:
  - density (abundance) measurements: 184026 entries
  - biomass carbon concentration estimates: 185729 entries
  - tow net sampling descriptions: 3569 entries
  - Sampling method descriptions: 3569 entries
  - Sampling net mesh size descriptions: 3569 entries

### Intermediate WoRMS taxonomic match-up file

The processing code creates two intermediate files that are not part of the final DwC-aligned output files, `intermediate_DwC_occurrence_life_history_stage.csv` and `intermediate_DwC_taxonomy.csv`, found at the [root level of this repository](https://github.com/nanoos-pnw/obis-pszmp/). They are used as temporary information passed from one Jupyter notebook to another, or within the same notebook. 
`intermediate_DwC_taxonomy.csv` contains the taxonomic match-up between the original `Genus species` entry and the corresponding, fully fleshed out WoRMS information. There are currently 261 unique taxa found in 288 taxonomy table records.

### Processing code

The processing code consists of a Python module file, four Python Jupyter notebooks and a JSON file, all found at the [root level of this repository](https://github.com/nanoos-pnw/obis-pszmp/).

- **(UPDATE THIS TEXT, ESP. BCO-DMO REF)** [`data_preprocess.py`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/data_preprocess.py). This module serves as "pre-processor" and is called by each Jupyter notebook.  Among other tasks, it reads the BCO-DMO source data file and applies several corrections and parsing steps: insert missing times for 6 samples; interpret timestamps as PDT; correct four `life_history_stage` entry errors (each error may occur in multiple samples); and parse the `life_history_stage` and `sample_code` entries into component strings for further processing.
- [`PSZMP-dwcEvent.ipynb`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/PSZMP-dwcEvent.ipynb). This notebook produces the `DwC_event.csv` file.
- [`PSZMP-dwcTaxonomy.ipynb`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/PSZMP-dwcTaxonomy.ipynb). This notebook produces an intermediate file, `intermediate_DwC_taxonomy.csv`, used later in the `PSZMP-dwcOccurrence.ipynb` notebook.
- [`PSZMP-dwcOccurrence.ipynb`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/PSZMP-dwcOccurrence.ipynb). This notebook produces the `DwC_occurrence.csv` file. It also produces an intermediate table for matching `life_history_stage` to `occurrenceID`, `intermediate_DwC_occurrence_life_history_stage.csv`, used later in the `PSZMP-dwceMoF.ipynb` notebook.
- [`PSZMP-dwceMoF.ipynb`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/PSZMP-dwceMoF.ipynb). This notebook produces the `DwC_emof.csv` file.
- [`common_mappings.json`](https://github.com/nanoos-pnw/obis-pszmp/blob/main/common_mappings.json). JSON file defining dataset information and "mappings" from codes in the source data to more standardized forms. This file is loaded and used by all the notebooks.

The processing code runs in a `conda` Python environment that can be created with the conda environment file `environment-py.yaml`. 
