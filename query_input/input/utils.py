import json, os

def write_queries_to_json_file(queries, file_name, create_query_object):
    if os.path.isfile(file_name):
        with open(file_name) as f:
            queries = json.load(f)   
          
    queries.update(create_query_object)
     
    with open(file_name, "w") as f:
        json.dump(queries, f, indent=4)