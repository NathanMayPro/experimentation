import yaml


if __name__ == "__main__":
    import os
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    for k,v in cfg.items():
        if isinstance(v, str):
            os.system(f"export {k}={v}")
            print(k,v)
    import os
    
    print(os.environ.get("name"))