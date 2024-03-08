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


    # TODO: FOR NOW, JUST SKIP ALL OF THIS UNTIL I GET TO IT
    if False:
        # ## Replace incorrect life_history_stage values

        # - Simple replacement of "F1_0;_Furcilia_1_0_legs" entry with "F10;_Furcilia_10". Use pandas `replace` on the column
        # - EUPHAUSIA_PACIFICA and THYSANOESSA in `species` column: replace `life_history_stage` based on combined `species` and `life_history_stage` entries
        #   > Calyptopis 1-3 life_history_stage codes. For Euphasia Pacifica, calyptopis life stages are typically coded in life_history_stage as "Cal1;_Calyptopis_1", "Cal2;_Calyptopis_2" and "Cal3;_Calyptopis_3" (same for thysanoessa). But there are a few Euphasia records that include the following codes: "1;_CI", "2;_CII", "3;_CIII". These are the same life_history_stage codes used for copepods, copepodites C1 - C3. My guess is that they're miscoded and should be calyptopis 1-3. Can you confirm?
        # 
        #   Yes, these are miscoded ("1, CI" should be "Cal1, calyptopis 1," and so on).

        def _update_lhs_byspecies(species, lhs_updates):
            """Modifies source_df in place, within the function"""
            sel_species = source_df["species"].isin(species)
            for old_lhs,new_lhs in lhs_updates.items():
                source_df.loc[sel_species & source_df["life_history_stage"].str.startswith(old_lhs), "life_history_stage"] = new_lhs

        source_df["life_history_stage"].replace({"F1_0;_Furcilia_1_0_legs": "F10;_Furcilia_10"}, inplace=True)

        krill_bad_lhs = {
            "1;_CI": "Cal1;_Calyptopis_1", 
            "2;_CII": "Cal2;_Calyptopis_2",
            "3;_CIII": "Cal3;_Calyptopis_3",
        }
        _update_lhs_byspecies(["EUPHAUSIA_PACIFICA", "THYSANOESSA"], krill_bad_lhs)

        # Handle life stage correction SIPHONOPHORA corrections from Amanda
        siphonophora_bad_lhs = {
            "Medusa": "Nectophore", 
            "Unknown": "Nectophore",
        }
        _update_lhs_byspecies(["SIPHONOPHORA"], siphonophora_bad_lhs)


        # ## Perform updates to species (taxa), life_history_stage and density
        # Specific to certain sample_code entries, not across the board.
        # Focused on Jellyfishes, mites and one sinophora record
        
        # If the "new" lhs or density value in Amanda's spreadsheet is the same as the old one,
        # I've entered None rather than repeating the value, for clarity for intent.
        jellyfishes_mites_updates = [
            dict(old=("20120614DBDm2_200", "JELLYFISHES", "Medusa"), new=("HYDROZOA", None, None)),
            dict(old=("20120614DBDm4_200", "JELLYFISHES", "Unknown"), new=("HYDROZOA", "Medusa", None)),
            dict(old=("20120712DBDm4_200", "JELLYFISHES", "Medusa"), new=("CALYCOPHORAE", "Gonophore", None)),
            dict(old=("20120905DBDm4_200", "JELLYFISHES", "Medusa"), new=("HYDROZOA", None, None)),
            dict(old=("20120905DBNm3_200", "JELLYFISHES", "Unknown"), new=("CALYCOPHORAE", "Gonophore", None)),
            dict(old=("20120709UNDm3_200", "JELLYFISHES", "Medusa"), new=("CALYCOPHORAE", "Gonophore", None)),
            dict(old=("20130930UNDm3_200", "MITES", "4;_CIV"), new=("MICROCALANUS", None, None)),
            dict(old=("20120902UNiiNm1_200", "JELLYFISHES", "Medusa"), new=("HYDROZOA", None, None)),
            dict(old=("20120902UNiiNm4_200", "JELLYFISHES", "Medusa"), new=("CALYCOPHORAE", "Bract", 23.52941)),
            dict(old=("20121001UNNm3_200", "SIPHONOPHORA", "Nectophore"), new=("CALYCOPHORAE", "Gonophore", None)), 
            dict(old=("20121001UNNm3_200", "JELLYFISHES", "Medusa"), new=("HYDROZOA", None, None)),
        ]
        # For ("20121001UNNm3_200", "SIPHONOPHORA", "Nectophore"), I changed from the original Medusa lhs 
        # to Nectophore to account for the lhs change already executed in an earlier step.
        # For ("20120614DBDm4_200", "JELLYFISHES", "Unknown") and
        # ("20121001UNNm3_200", "JELLYFISHES", "Medusa"), replaced the assigned "HYDROZOA_Medusa" and 
        # "HYDROMEDUSA", respectively, to "HYDROZOA" b/c those two entries don't resolved with pyworms
        # (are not taxa names per se?)
        # I also ommitted SIPHONOPHORA	Nectophore from Amanda's spreadsheet because, unlike all other entries
        # in the "jellyfishes and mites" tab, the intent wasn't clear

        for upd_record in jellyfishes_mites_updates:
            old, new = upd_record["old"], upd_record["new"]
            # select on the entries from the "old" tuple forming a set of unique combinations of
            # sample_code, species and life_history_stage
            sel = (
                (source_df["sample_code"] == old[0])
                & (source_df["species"] == old[1])
                & (source_df["life_history_stage"] == old[2])
            )
            source_df.loc[sel, "species"] = new[0]
            if new[1] is not None:
                source_df.loc[sel, "life_history_stage"] = new[1]
            if new[2] is not None:
                source_df.loc[sel, "density"] = new[2]


    return source_df.copy()
