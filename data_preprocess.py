#!/usr/bin/env python
# coding: utf-8

# # Data pre-processing. PSZMP
# 
# 
# 3/1. 2/16,12,9,6. 1/31, 2024

from pathlib import Path

import pandas as pd


def read_and_parse_sourcedata(test_n_rows=None):
    """
    Read, parse and pre-process source Excel data.
    """

    # TODO: In the long run, the Excel file name and sheet name should be
    #   arguments to read_and_parse_sourcedata(). They could be placed in common_mappings.json
    excel_file_name = "PSZMP_2014-2022_Species_Data_Keister_Lab.xlsx"
    excel_sheet_name = "PSZMP 2014-22 Density & Biomass"

    # ## Read the Excel file
    data_pth = Path(".")
    sourcexlsdata_pth = data_pth / "sourcedata" / excel_file_name
    
    read_kwargs = dict(
        sheet_name=excel_sheet_name,
        header=0, 
        dtype={'Sample Date':str, 'Sample Time':str},
        engine='openpyxl',
    )
    if test_n_rows:
        # For testing, select a fixed number of rows to process
        read_kwargs['nrows'] = test_n_rows

    source_df = pd.read_excel(sourcexlsdata_pth, **read_kwargs)

    # ## Parse the date & time columns into a datetime type
    # Amanda & BethElLee said times are local clock times -- PST or PDT, 
    # depending on the date. Assign the correct UTC offset (-7 or -8) or DST status.
    
    # https://www.hacksoft.io/blog/handling-timezone-and-dst-changes-with-python
    # Adapt this code if the .dt.tz_localize("US/Pacific") strategy fails?
    # PACIFIC_TZ = pytz.timezone('US/Pacific')
    # dt_pdt = datetime.fromisoformat("2021-06-15T15:00:00-00:00").astimezone(PACIFIC_TZ)
    # dt_pdt.dst().seconds / 3600  # When DST is on, this will be 1.0; otherwise, 0.0

    # .dt.tz_localize("US/Pacific") will assign the correct UTC offset (-07:00 or -08:00)
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-zone-handling
    source_df["time"] = pd.to_datetime(
        source_df["Sample Date"].str.split(' ').str[0] + source_df["Sample Time"], 
        format="%Y-%m-%d%H:%M:%S"
    ).dt.tz_localize("US/Pacific")

    # ## Set Nan Day_Night to "U", unassigned
    source_df.loc[source_df["Day_Night"].isnull(), "Day_Night"] = "U"

    # ## Change negative "Max Tow Depth (m)" values to positive value
    # Assume the negative sign is a mistake. The only negative value present
    # (for the 2014-2022 dataset) is -10.0, for sample_code == '070819SKETV1038'
    depth_col = "Max Tow Depth (m)"
    source_df.loc[source_df[depth_col] < 0, depth_col] = -1 * source_df[depth_col][source_df[depth_col] < 0]

    # ## Homogenize station names, to use the same case
    station_corrections_updates = {
        "Cow2D2": "COW2D2",
        "Cow3V2": "COW3V2",
        "sketd": "SKETD",
        "Wat1S": "WAT1S",
        "Wat1V": "WAT1V",
    }
    source_df["Station"].replace(station_corrections_updates, inplace=True)

    # ## Fix a Sampling Group error identified by Amanda
    sel = (source_df["Station"] == "SARAD") & (source_df["Sampling Group"] == "NIT")
    source_df.loc[sel, "Sampling Group"] = "NOAA/STIL"

    # ## Create lowercase versions of taxa and life history stage columns
    # This will make downstream processing much more convenient
    source_df["Genus species_lc"] = source_df["Genus species"].str.lower()
    source_df["Life History Stage_lc"] = source_df["Life History Stage"].str.lower()

    # ## Remove records where both "Genus species_lc" and "Life History Stage_lc" are "unknown"
    # Per recommendation from Amanda & BethElLee
    source_df = source_df[
        ~((source_df["Genus species_lc"] == "unknown") & (source_df["Life History Stage_lc"] == "unknown"))
    ].copy()

    # ## Replace outdated/incorrect taxa with updated, corrected ones from Amanda & BethElLee
    taxa_corrections_updates = {
        'barnacles': 'cirripedia',
        'cancrid- c. prod/ g. oreg': 'cancridae',
        # For these two, pyworms failed to make a match. So, fix it here
        'cancridae lg': 'cancridae',
        'cancridae sm': 'cancridae',
        'crabs': 'pleocyemata',
        'chaet/euphaus egg': 'animalia',
        'fish': 'teleostei',
        'forage fish': 'teleostei',
        'hydromedusa': 'hydrozoa',
        'limnomedusa': 'limnomedusae',
        'mites': 'halacaroidea',
        'narcomedusida': 'narcomedusae',
        'pseudocalanus lg': 'pseudocalanus',
        'pseudocalanus sm': 'pseudocalanus',
        'physonect': 'physonectae',
        'scolecithricidae': 'scolecitrichidae',
        'scyphomedusa': 'scyphozoa',
        'triconia (tiny)': 'triconia',
        'worm': 'annelida',
        'unknown': 'animalia',
    }
    source_df["Genus species_lc"].replace(taxa_corrections_updates, inplace=True)

    # ## Parse life_history_stage
    source_df[['lhs_0', 'lhs_1']] = pd.DataFrame(
        source_df["Life History Stage_lc"].str.split(',').to_list(), 
        index=source_df.index
    )

    return source_df.copy()
