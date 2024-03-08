# README

- OUTLINE WHAT TO INCLUDE IN THIS INTRO SECTION VS IN THE BACKGROUND SECTION
- ALSO, ADD A BRIEF SECTION ON DATA PROCESSING TO ALIGN TO DWC? MAYBE VERY BRIEFLY, THEN LINK TO `notebooks-notes.md` FOR MORE DETAILS
- INCLUDE SUPER-BRIEF MENTION AND LINK TO THE HOOD CANAL ZOOPLANKTON DATASET REPO

Alignment of Julie Keister's Hood Canal Zooplankton dataset to the OBIS-ENV-DATA Darwin Core standard for submission to OBIS and the MBON Data Portal. University of Washington Pelagic Hypoxia Hood Canal project, Zooplankton dataset. This dataset was previously published to BCO-DMO in a format submitted by the PI that's not aligned to Darwin Core. The dataset we obtain from the BCO-DMO ERDDAP server is the starting point for the Darwin Core alignment.


Hi @psalinasruiz . Great to learn about this Strait of Georgia zooplankton dataset! I am currently working on aligning a similar dataset on the other side of the border in the Salish Sea, in Puget Sound and parts of the Strait of Juan de Fuca. And as it turns out, event the time frame is similar, 2014 - 2022. This dataset is from the Puget Sound Zooplankton Monitoring Program (PSZMP; here's a [recent article about the program](https://www.eopugetsound.org/magazine/ups-and-downs-of-zooplankton-Puget-Sound/HSIL)). We recently published on OBIS a similar but earlier and smaller zooplankton dataset, in Hood Canal (also in Puget Sound), and the work on the PSZMP dataset builds on what we did for that previous dataset. Both of these datasets came from big "horizontal" tables -- one a CSV, the other one an Excel file.


- https://www.eopugetsound.org/magazine/ups-and-downs-of-zooplankton-Puget-Sound/HSIL
- https://vitalsigns.pugetsoundinfo.wa.gov/VitalSign/Detail/35
- https://makingwaves.psp.wa.gov/index.php/2021/12/04/monitoring-the-tiny-creatures-at-the-base-of-the-food-web-can-have-a-big-impact/
- https://marinesurvivalproject.com/research_activity/list/zooplankton-establishing-puget-sound-wide-zooplankton-sampling-program/
- https://green2.kingcounty.gov/marine/Monitoring/Zooplankton
- King County page where their file can be downloaded: https://green2.kingcounty.gov/ScienceLibrary/Document.aspx?ArticleID=556


FROM KC PSZMP DATA DOWNLOAD PAGE

Puget Sound Zooplankton Monitoring Program Dataset (2014 - 2022)

The Puget Sound Zooplankton Monitoring Program began in 2014 (formerly part of the Salish Sea Marine Survival Project) as a collaborative effort involving many tribal, county, state, federal, academic and non-profit entities. The program was developed to address two main research objectives:

1. examine how environmental variability affects Puget Sound’s ecosystem through changes in zooplankton and
2.. measure how the prey field of salmon and other fish varies spatio-temporally and correlates with survival. 

Zooplankton samples were collected on either a monthly or bi-monthly schedule, depending on sampling group and season, at 16 sampling sites across Puget Sound.  Vertical tows deployed a single ring net to sample zooplankton throughout the depth of the water column, and oblique tows deployed a double ring net to sample larger, more motile zooplankton inhabiting the upper portion of the water column (i.e., the primary feeding zone for juvenile salmonids). Samples were processed and analyzed for species biomass, abundances and lengths at the University of Washington. Resulting data associated with the two methods are provided in this excel file.


## Background

IOOS provided NANOOS with special funding to integrate regional biological data into community data resources, specifically **OBIS** (https://obis.org, https://mapper.obis.org) and the **MBON Portal** (https://ioos.noaa.gov/project/bio-data/, https://mbon.ioos.us, https://ioos.github.io/mbon-docs/). This effort is focused on the Hood Canal zooplankton densities dataset Julie Keister (UW) submitted to BCO-DMO in 2017 as part of the project "Consequences of hypoxia on food web linkages in a pelagic marine ecosystem". This alignment work will reorganize the data and metadata into the standards required by those other systems. This "Marine Mammals in Puget Sound" dataset (limited to individual presence) serves as a good example for what the data might look like on OBIS: https://obis.org/dataset/0e80dc63-b47c-423a-8e34-362f3171ea18 and https://mapper.obis.org/?datasetid=0e80dc63-b47c-423a-8e34-362f3171ea18#

### Dataset information
THIS SUBHEADING SEEMS REDUNDANT. REMOVE IT?

Publications

- Winans, A. K., B. Herrmann, and J. E. Keister. 2023. Spatio-temporal variation in zooplankton community composition in the southern Salish Sea: Changes during the 2015–2016 Pacific marine heatwave. *Progress in Oceanography* 214, 103022, https://doi.org/10.1016/j.pocean.2023.103022
- Keister, J. 2017. The Puget Sound Zooplankton Monitoring Program. Zooplankton_Monitoring_Program_plan_2017.pdf. Find where I downloaded this pdf
- Keister, J., Winans, A., and Hermann, B. (2017). Salish Sea Marine Survival Project: Zooplankton Monitoring Program 20142015 Final Report. Washington, DC: University of Washington, School of Oceanography, Seattle.
- Long Live the Kings. December 2019. Puget Sound-wide Zooplankton Monitoring Program. Final Report on NTA 2016-0367. 66pp. https://pugetsoundestuary.wa.gov/wp-content/uploads/2020/06/2016_0367_Final_Report.pdf


## Data source

- Link to obtain the data from the BCO-DMO ERDDAP server in CSV format: https://erddap.bco-dmo.org/erddap/tabledap/bcodmo_dataset_682074.csv


## Remaining tasks

