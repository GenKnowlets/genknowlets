import json
import os
import nanopub_constants as np_cnt
import datetime

def list_json_files_on_folder(folder_path):
    filepaths = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"): 
            filepath = os.path.join(folder_path, filename)
            filepaths.append(filepath)
    return filepaths

def extract_dict_from_file(filepath):
    readmode = "r"
    with open(filepath, readmode) as f:
        d = json.load(f)
        # print(json.dumps(d, indent = 3))
    return d

def convert_dict_to_rdf(dict_input):

    nanopubs = []

    for link in dict_input["assembly"]["links"]:

        np_prefixes = np_cnt.prefixes
        np_head = np_cnt.head  
        assembly_id = link["report"]["bioSample"]["url"].split("/")[-1]
        np_assertions = np_cnt.assertion.format(
            assembly_id=assembly_id,        
            taxonomy_link=link["report"]["taxonomyUrl"],
            organism_name=link["report"]["organismName"],
        )    
        np_prov = np_cnt.provenance.format(
            biosample_link=link["report"]["bioSample"]["url"],      
            institution=link["report"]["submitter"],        
            collected_at=link["report"]["bioSample"]["collectionDate"],
            publication_link=dict_input["doi"],       
            submitted_at=link["report"]["date"],
        )    
        np_pubinfo = np_cnt.pubinfo.format(
            created_datetime=str(datetime.datetime.now()),      
            creator_id="123"
        )
        nanopub = np_prefixes + "\n" + np_head + "\n"
        nanopub += np_assertions + "\n" + np_prov + "\n"
        nanopub += np_pubinfo

        nanopubs.append(nanopub)
    
    return nanopubs
    
def convert_rdf_to_file(nanopubs, filepath):
    writemode = "w"
    output_folder = "../output"

    for i in range(len(nanopubs)):
        filename = filepath.split("/")[-1]
        filename_without_extension = filename.split(".")[0]
        output_path = f"{output_folder}/{filename_without_extension}_{i}.rdf"
        with open(output_path, writemode) as f:
            f.write(nanopubs[i])
            f.close()

input_folder = "../input"

files_to_convert = list_json_files_on_folder(input_folder)

for filepath in files_to_convert:
    
    print(f"Reading {filepath}")
    file_as_dict = extract_dict_from_file(filepath) 
    
    try:
        quant_samples = len(file_as_dict["assembly"]["links"])
        print(f"Found {quant_samples} samples.")
    except:
        print("Assembly links not found.")
        continue
    nanopubs = convert_dict_to_rdf(file_as_dict)
    # print(nanopubs)
    convert_rdf_to_file(nanopubs, filepath)
    print(f"Finished converting {filepath}")