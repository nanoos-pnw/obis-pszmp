# README

Alignment of Julie Keister's Hood Canal Zooplankton dataset to the OBIS-ENV-DATA Darwin Core standard for submission to OBIS and the MBON Data Portal. University of Washington Pelagic Hypoxia Hood Canal project, Zooplankton dataset. This dataset was previously published to BCO-DMO in a format submitted by the PI that's not aligned to Darwin Core. The dataset we obtain from the BCO-DMO ERDDAP server is the starting point for the Darwin Core alignment.

## Background

IOOS provided NANOOS with special funding to integrate regional biological data into community data resources, specifically **OBIS** (https://obis.org, https://mapper.obis.org) and the **MBON Portal** (https://ioos.noaa.gov/project/bio-data/, https://mbon.ioos.us, https://ioos.github.io/mbon-docs/). This effort is focused on the Hood Canal zooplankton densities dataset Julie Keister (UW) submitted to BCO-DMO in 2017 as part of the project "Consequences of hypoxia on food web linkages in a pelagic marine ecosystem". This alignment work will reorganize the data and metadata into the standards required by those other systems. This "Marine Mammals in Puget Sound" dataset (limited to individual presence) serves as a good example for what the data might look like on OBIS: https://obis.org/dataset/0e80dc63-b47c-423a-8e34-362f3171ea18 and https://mapper.obis.org/?datasetid=0e80dc63-b47c-423a-8e34-362f3171ea18#

### Dataset information

- BCO-DMO Dataset 682074: [Zooplankton densities collected from a seasonally hypoxic fjord on R/V Clifford A Barnes cruises from 2012-2013 (Pelagic Hypoxia project)](https://www.bco-dmo.org/dataset/682074). ERDDAP dataset: https://erddap.bco-dmo.org/erddap/tabledap/bcodmo_dataset_682074.html. A description of each data column is found in the "Parameters" section in https://www.bco-dmo.org/dataset/682074
- BCO-DMO Project 557504: [Consequences of hypoxia on food web linkages in a pelagic marine ecosystem (PelagicHypoxia)](https://www.bco-dmo.org/project/557504)
- Publications
  - Li, L., J.E. Keister, T.E. Essington and J. Newton. 2019. Vertical distributions and abundances of life stages of the euphausiid Euphausia pacifica in relation to oxygen and temperature in a seasonally hypoxic fjord. Journal of Plankton Research 41(2): 188–202, [doi:10.1093/plankt/fbz009](https://doi.org/10.1093/plankt/fbz009)
  - Related, more recent paper: Moriarty, P. E.,  Essington, T. E.,  Horne, J. K.,  Keister, J. E.,  Li, L.,  Parker-Stetter, S. L., and  Sato, M..  2020.  Unexpected food web responses to low dissolved oxygen in an estuarine fjord. *Ecological Applications*  30(8):e02204. [doi:10.1002/eap.2204](https://doi.org/10.1002/eap.2204)

## Data source

- Link to obtain the data from the BCO-DMO ERDDAP server in CSV format: https://erddap.bco-dmo.org/erddap/tabledap/bcodmo_dataset_682074.csv
- For convenience, I pre-fetched the dataset in January 2020 using that request url, and stored the csv file locally in the `sourcedata` folder: [bcodmo_dataset_682074_data.csv](https://github.com/nanoos-pnw/obis-keisterhczoop/blob/main/sourcedata/bcodmo_dataset_682074_data.csv)

## Other

- **TODO:** Move relevant content from `IOOSbiodata_DCalignment_PEF.md` to this file.
- List and briefly discuss other, relevant datasets I used for reference and guidance
- Great reference from Stace Beaulieu: "the best published example that I know of for getting zooplankton data into OBIS, using the 3 tables (event, occurrence, emof):" [Mortelmans, Jonas, et al. (2019) LifeWatch observatory data: Zooplankton
observations in the Belgian part of the North Sea. Geoscience Data Journal, 6: 76–84. DOI:10.1002/gdj3.68](https://doi.org/10.1002/gdj3.68). The dataset itself is described (hosted?) at https://doi.org/10.14284/329


## Remaining tasks

- [Submit request to add new life stage terms to S11 NERC vocab](https://github.com/nanoos-pnw/obis-keisterhczoop/issues/1)
