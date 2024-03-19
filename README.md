# README

2024-03-19

This repository contains all the elements involved in the transformation of a Puget Sound zooplankton data from its original format to the standardized format used for integration into the [Ocean Biodiversity Information System (OBIS)](https://obis.org). Collection and analysis of the dataset ("Puget Sound Zooplankton Monitoring Program") is led by the Principal Investigator, Julie Keister, [ORCID 0000-0002-9385-5889](https://orcid.org/0000-0002-9385-5889), University of Washington / NOAA. 

The goal of the project captured in this repository is to transform this dataset into the [Darwin Core (DwC) standard format](https://ioos.github.io/bio_data_guide/intro.html) for submission to OBIS. This processing workflow starts with the reorganization and reformatting ("alignment") of a dataset's data to *DwC - [Event Core](https://manual.obis.org/formatting.html#when-to-use-event-core) with [Extended Measurement or Fact (eMoF) extension](https://manual.obis.org/data_format.html#obis-holds-more-than-just-species-occurrences-the-env-data-approach)* (also known as OBIS-ENV-DATA), the data standard used by OBIS.

The alignment work is supported by the [Northwest Association of Networked Ocean Observing Systems (NANOOS)](https://www.nanoos.org), the Regional Association of the national [US Integrated Ocean Observing System (IOOS)](https://ioos.noaa.gov) for the US Pacific Northwest. It is being carried out by Emilio Mayorga, [ORCID 0000-0003-2574-4623](https://orcid.org/0000-0003-2574-4623), University of Washington.


## Dataset description

**NOTE:** This text currently is copied from the program description found in the [zooplankton dataset download page from the King County Marine and Sediment Assessment Group](https://green2.kingcounty.gov/ScienceLibrary/Document.aspx?ArticleID=556). Currently it includes only small edits. It will be overhauled in the near future.

The **Puget Sound Zooplankton Monitoring Program** is an ongoing program that began in 2014 (formerly part of the Salish Sea Marine Survival Project) as a collaborative effort involving many tribal, county, state, federal, academic and non-profit entities. The program was developed to address two main research objectives:

1. Examine how environmental variability affects Puget Sound’s ecosystem through changes in zooplankton and
2. Measure how the prey field of salmon and other fish varies spatio-temporally and correlates with survival. 

Zooplankton samples were collected on either a monthly or bi-monthly schedule, depending on sampling group and season, at 16 sampling sites across Puget Sound.  Vertical tows deployed a single ring net to sample zooplankton throughout the depth of the water column, and oblique tows deployed a double ring net to sample larger, more motile zooplankton inhabiting the upper portion of the water column (i.e., the primary feeding zone for juvenile salmonids). Samples were processed and analyzed for species biomass, abundances and lengths at the University of Washington. Resulting data associated with the two methods are provided in this excel file.

To read more about this zooplankton monitoring program, see:

- [The ups and downs of zooplankton in Puget Sound - 2023-Oct. - Salish Sea Currents magazine](https://www.eopugetsound.org/magazine/ups-and-downs-of-zooplankton-Puget-Sound/HSIL)
- [Zooplankton Vital Sign - Puget Sound Parntership](https://vitalsigns.pugetsoundinfo.wa.gov/VitalSign/Detail/35)
- [Monitoring the tiny creatures at the base of the food web can have a big impact - 2021-Dec. - Making Waves magazine](https://makingwaves.psp.wa.gov/index.php/2021/12/04/monitoring-the-tiny-creatures-at-the-base-of-the-food-web-can-have-a-big-impact/)
- [Zooplankton Monitoring Program - King County Marine and Sediment Assessment Group](https://green2.kingcounty.gov/marine/Monitoring/Zooplankton)
- [Zooplankton: a Puget Sound-wide sampling program - Salish Sea Marine Survival Project](https://marinesurvivalproject.com/research_activity/list/zooplankton-establishing-puget-sound-wide-zooplankton-sampling-program/)


## Data alignment

The starting point data file for OBIS Darwin Core alignment was obtained in Excel format from Keister Lab staff. (A similar version of this data file [can be downloaded as an Excel file](https://green2.kingcounty.gov/ScienceLibrary/Document.aspx?ArticleID=556) from the [King County Marine and Sediment Assessment Group](https://green2.kingcounty.gov/marine/)). Starting with the source Excel file, we performed the following revisions and corrections, based on more recent information from the PI's lab:
- Timestamps were clearly encoded as local Pacific time, either PST (UTC-8) or PDT (UTC-7) depending on the date.
- Removed records where both `Genus species` and `Life History Stage` are coded as "unknown".
- Fixed a `Sampling Group` error.
- Updated or corrected several taxa assignments. 

These steps and data alignments work was implemented in Python code. See [`notebooks-notes.md`](notebooks-notes.md) for details.


## Funding

This zooplankton monitoring program is funded by **(to be filled in)**. The transformation and publication of this dataset in OBIS is supported by the [Northwest Association of Networked Ocean Observing Systems (NANOOS)](https://www.nanoos.org).


## Bibliography

- Winans, A. K., B. Herrmann, and J. E. Keister. 2023. Spatio-temporal variation in zooplankton community composition in the southern Salish Sea: Changes during the 2015–2016 Pacific marine heatwave. *Progress in Oceanography* 214, 103022, https://doi.org/10.1016/j.pocean.2023.103022
- Keister, J. 2017. The Puget Sound Zooplankton Monitoring Program. Zooplankton_Monitoring_Program_plan_2017.pdf. (*A url will be included later*)
- Keister, J., Winans, A., and Hermann, B. 2017. Salish Sea Marine Survival Project: Zooplankton Monitoring Program 20142015 Final Report. Washington, DC: University of Washington, School of Oceanography, Seattle.
- Long Live the Kings. December 2019. Puget Sound-wide Zooplankton Monitoring Program. Final Report on NTA 2016-0367. 66pp. https://pugetsoundestuary.wa.gov/wp-content/uploads/2020/06/2016_0367_Final_Report.pdf
