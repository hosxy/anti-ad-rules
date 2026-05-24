import json
import sys
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import SingleQuotedScalarString


def convert_json(file_name: str):
    ruleset = {"version": 3, "rules": []}
    domain: list[str] = []
    domain_suffix: list[str] = []
    domain_regex: list[str] = []

    if Path.cwd().joinpath(file_name + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"), "r",encoding='utf-8') as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#") or len(i) == 0:
                    continue
                elif i.startswith("full:"):
                    domain.append(i.split(":", 1)[1])
                elif i.startswith("regexp:"):
                    domain_regex.append(i.split(":", 1)[1])
                else:
                    domain_suffix.append(i)

    if Path.cwd().joinpath(file_name + "-add" + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"), "r",encoding='utf-8') as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#") or len(i) == 0:
                    continue
                elif i.startswith("full:"):
                    domain.append(i.split(":", 1)[1])
                elif i.startswith("regexp:"):
                    domain_regex.append(i.split(":", 1)[1])
                else:
                    domain_suffix.append(i)
    if domain:
        ruleset["rules"].append({"domain": domain})
    if domain_suffix:
        ruleset["rules"].append({"domain_suffix": domain_suffix})
    if domain_regex:
        ruleset["rules"].append({"domain_regex": domain_regex})

    with open(Path.cwd().joinpath(file_name + ".json"), "w") as f:
        json.dump(ruleset, f, indent=2)

def convert_yaml(file_name: str):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)

    ruleset = {"payload":[]}
    domain: list[SingleQuotedScalarString] = []

    if Path.cwd().joinpath(file_name + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"), "r",encoding='utf-8') as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#") or len(i) == 0:
                    continue
                elif i.startswith("regexp:"):
                    continue
                elif i.startswith("full:"):
                    domain.append(SingleQuotedScalarString(i.split(":", 1)[1]))
                else:
                    domain.append(SingleQuotedScalarString("+."+i))

    if Path.cwd().joinpath(file_name + "-add" + ".txt").exists():
        with open(Path.cwd().joinpath(file_name + ".txt"), "r",encoding='utf-8') as f:
            content = f.read().splitlines()
            for i in content:
                if i.startswith("#") or len(i) == 0:
                    continue
                elif i.startswith("regexp:"):
                    continue
                elif i.startswith("full:"):
                    domain.append(SingleQuotedScalarString(i.split(":", 1)[1]))
                else:
                    domain.append(SingleQuotedScalarString("+." + i))

    if domain:
        ruleset["payload"].extend(domain)
    with open(Path.cwd().joinpath(file_name + ".yaml"), "w") as f:
        yaml.dump(ruleset, f)
        #yaml.dump(ruleset, sys.stdout)

file_name = sys.argv[1]

convert_json(file_name)
convert_yaml(file_name)
