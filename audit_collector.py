import json, os

def get_data():
    # Тепер ми бачимо повну архітектуру
    files = [
        'config/_default/config.toml', 
        'config/_default/languages.toml', 
        'config/_default/params.toml', 
        'static/admin/config.yml'
    ]
    
    data = {}
    for f in files:
        if os.path.exists(f):
            with open(f, 'r', encoding='utf-8') as file:
                data[f] = file.read()
        else:
            data[f] = "MISSING"
            
    print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    get_data()