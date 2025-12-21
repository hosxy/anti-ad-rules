import json
from pathlib import Path
import sys

def convert(file_name:str):
    ruleset = {"version": 3,"rules": []}
    domain:list[str] = []
    domain_suffix:list[str] = []
    domain_regex:list[str] =[]

    if Path.cwd().joinpath(file_name + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"),"r") as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#"):
                    continue
                elif i.startswith("full:"):
                    domain.append(i.split(":",1)[1])
                elif i.startswith("regexp:"):
                    domain_regex.append(i.split(":",1)[1])
                else:
                    domain_suffix.append(i)

    if Path.cwd().joinpath(file_name + "-add" + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"),"r") as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#"):
                    continue
                elif i.startswith("full:"):
                    domain.append(i.split(":",1)[1])
                elif i.startswith("regexp:"):
                    domain_regex.append(i.split(":",1)[1])
                else:
                    domain_suffix.append(i)
    if domain:
        ruleset["rules"].append({"domain":domain})
    if domain_suffix:
        ruleset["rules"].append({"domain_suffix":domain_suffix})
    if domain_regex:
        ruleset["rules"].append({"domain_regex":domain_regex})

    with open(Path.cwd().joinpath(file_name + ".json"),"w") as f:
        json.dump(ruleset,f,indent=2)

file_name = sys.argv[1]

convert(file_name)
