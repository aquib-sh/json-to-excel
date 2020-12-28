import os
import sys
import json
import pandas as pd
import numpy as np

#==================== FILENAMES & DIRECTORIES HERE ====================
OUTPUT_DIR        = "outputs"
JSON_INPUT_DIR    = "inputs"

BASE_FILE         = "locale_en.json"
OUTPUT_EXCEL_FILE = "data.xlsx"

EXCEL_OUTPUT_DIR  = os.path.join(OUTPUT_DIR, "excel")
JSON_OUTPUT_DIR   = os.path.join(OUTPUT_DIR, "json")

OUTPUT_EXCEL_PATH = os.path.join(EXCEL_OUTPUT_DIR, OUTPUT_EXCEL_FILE)
#======================================================================

def get_data(files_list):
    """ Returns keys of the base file and holder containing all data. """
    holder = {}
    base_keys = []
    for json_file in files_list:
        with open(os.path.join(JSON_INPUT_DIR, json_file), encoding="utf-8") as f:
            raw_json = json.loads(f.read())
            holder[json_file] = raw_json
    return holder

def get_base_keys(raw_json):
    base_keys = []
    # LEVEL 1
    for key, value in raw_json.items():
        k = key
        # If there is a json inside then add the subkeys with parent reference
        # LEVEL 2
        if type(raw_json[key]) == dict:
            for ckey, cvalue in raw_json[key].items():
                k = key+"."+ckey
                # If there is again JSON at third level then parent will be reference of past 2 parent
                if type(raw_json[key][ckey]) == dict:
                    # LEVEL 3
                    for cckey, ccvalue in raw_json[key][ckey].items():
                        third_level = k+"."+cckey
                        base_keys.append(third_level)
                else:
                    base_keys.append(k)
        else:
            base_keys.append(k)
    return base_keys

def get_raw_name(string):
    raw_name = string.replace("locale_", "").split(".")[0].upper()
    return raw_name

def get_data_frame(base_keys, holder):
    """ Returns the data from files into a nicely formatted DataFrame. """
    data = {}
    data['KEY'] = base_keys
    for key, value in holder.items():
        raw_name = get_raw_name(key)
        registry = {} # maintian register for values which have subdict
        # Level 1
        for ckey, cvalue in holder[key].items():
            if type(holder[key][ckey]) == dict:
                # Level 2
                for cckey, ccvalue in holder[key][ckey].items():
                    fname = ckey + "." + cckey
                    if type(holder[key][ckey][cckey]) == dict:
                        # Level 3
                        for ccckey, cccvalue in holder[key][ckey][cckey].items():
                            sname = fname + "." + ccckey
                            registry[sname] = cccvalue
                    else:    
                        registry[fname] = ccvalue

        # Now append the values by looking into registery
        data[raw_name] = []
        for column in data['KEY']:
            if column in holder[key]:
                data[raw_name].append(holder[key][column])
            elif column in registry:
                data[raw_name].append(registry[column])
            else:
                data[raw_name].append(np.nan)

    # To put EN on the 2nd columnn
    temp = {}
    temp['KEY'] = data['KEY']
    bname = get_raw_name(BASE_FILE)
    temp[bname] = data[bname]
    for item in data:
        if item == bname:
            continue
        else:
            temp[item] = []
            temp[item] = data[item]
    data = temp
    del temp
    df = pd.DataFrame(data)
    return df

def get_data_structure(dataframe):
    """ Returns the basic data structure/skeleton 
        in which values would be inserted. """
    data_struct = {}
    for key in df['KEY']:
        if "." in key:
            temp = key.split(".")
            if temp[0] not in data_struct:
                data_struct[temp[0]] = {}
            if len(temp) == 2:
                data_struct[temp[0]][temp[1]] = np.nan
            elif len(temp) == 3:
                if temp[1] not in data_struct[temp[0]]:
                    data_struct[temp[0]][temp[1]] = {}
                data_struct[temp[0]][temp[1]][temp[2]] = np.nan
        else:
            data_struct[key] = np.nan
    return data_struct

def get_individual_json(df, data_struct, column):
    """ Returns individual column json data. """
    for i in range(0, len(df)):
        current_frame = df.iloc[i]
        key = current_frame['KEY']
        val = current_frame[column]
        
        if key == "n_a":
            if pd.isnull(val):
                val = 'N/A'
        if pd.isnull(val):
            val = current_frame[get_raw_name(BASE_FILE)]
        
        if "." in key:
            temp = key.split(".")
            total = len(temp)
            
            if total == 2:
                if temp[0] not in data_struct:
                    data_struct[temp[0]] = {}
                data_struct[temp[0]][temp[1]] = val
            
            elif total == 3:
                if temp[1] not in data_struct[temp[0]]:
                    data_struct[temp[0]][temp[1]] = {}
                data_struct[temp[0]][temp[1]][temp[2]] = val
        else:
            data_struct[key] = val
            
    return data_struct

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--export-excel": 
            holder = get_data(os.listdir(JSON_INPUT_DIR))
            base_keys = get_base_keys(holder[BASE_FILE])
            df = get_data_frame(base_keys, holder)
            df.to_excel(OUTPUT_EXCEL_PATH, index=False)
            print("[+] Data successfully exported to {}".format(OUTPUT_EXCEL_PATH))

        elif sys.argv[1] == "--export-json":
            df = pd.read_excel(OUTPUT_EXCEL_PATH)
            columns = [item for item in df.keys() if item != 'KEY']
            data_struct = get_data_structure(df)
            
            for column in columns:
                temp_data_struct = data_struct
                json_data = get_individual_json(df, temp_data_struct, column)
                base_filename = ("exported_"+column+".json").lower()
                filename = os.path.join(JSON_OUTPUT_DIR, base_filename)

                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(json_data, fp=f, indent=4, ensure_ascii=False)
                    print("[+] Data successfully exported to {}".format(filename))
    else:
        print("Please provide correct arguments\n--export-excel to export JSON files to Excel\n--export-json to export individual JSON files")
