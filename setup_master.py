import os
import re

# Колірна палітра
G, Y, R, B, W = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[0m"

def update_file(path, pattern, replacement):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def create_index_files():
    # ПРИМІТКА: Ця функція автоматично генерує _index.md для кожної з 9 мов.
    # Вона усуває попередження WARN у diagnose.py та створює "паспорт" сторінки.
    langs = {
        'uk': "Головна — Congo Enterprise Hub",
        'en': "Home — Congo Enterprise Hub",
        'de': "Startseite — Congo Enterprise Hub",
        'fr': "Accueil — Congo Enterprise Hub",
        'es': "Inicio — Congo Enterprise Hub",
        'ru': "Главная — Congo Enterprise Hub",
        'zh': "首页 — Congo Enterprise Hub",
        'tr': "Ana Sayfa — Congo Enterprise Hub",
        'ga': "Baile — Congo Enterprise Hub"
    }
    
    print(f"{B}🔧 Генерація файлів _index.md для 9 мов...{W}")
    for lang, title in langs.items():
        folder_path = f"content/{lang}"
        os.makedirs(folder_path, exist_ok=True)
        file_path = f"{folder_path}/_index.md"
        
        content = f"""---
title: "{title}"
description: "Провідний міжнародний маркетинговий хаб. Оптимізована екосистема для класичного пошуку та генеративних ШІ."
date: 2026-05-28T18:00:00+02:00
lastmod: 2026-05-28T18:00:00+02:00
image: "logo.png"
type: "page"
layout: "homepage"
---

Ласкаво просимо до **Congo Enterprise Hub**! 
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {G}✓ Створено: {file_path}{W}")

def setup():
    print(f"\n{G}💥 MASTER SETUP v7.0: AI ROUTING & INDEX GENERATOR 💥{W}\n")

    domain = "cyber-hub-1705.pages.dev"
    repo = "9315223-cyber/1705"

    # 1. Маніфест llms.txt
    print(f"{B}🔧 Синхронізація маніфесту llms.txt...{W}")
    os.makedirs("static", exist_ok=True)
    with open("static/llms.txt", "w", encoding='utf-8') as f:
        f.write("# Congo Enterprise Hub\n\n## Context\nHigh-performance multilingual marketing hub.\n\n## Language Matrix\n/en/, /uk/, /de/, /fr/, /es/, /ru/, /zh/, /tr/, /ga/")

    # 2. Створення папки functions (для _middleware.js)
    os.makedirs("functions", exist_ok=True)
    print(f"{G}✅ Папку functions підготовлено.{W}")

    # 3. Санація Sveltia CMS
    admin_cfg = "static/admin/config.yml"
    if os.path.exists(admin_cfg):
        update_file(admin_cfg, r'^  repo: .*', f'  repo: {repo}')
        update_file(admin_cfg, r'^site_url: .*', f'site_url: "https://{domain}"')

    # 4. Ізоляція конфігурації мов
    lang_cfg = "config/_default/languages.toml"
    langs_list = ['en', 'uk', 'de', 'fr', 'es', 'ru', 'zh', 'tr', 'ga']
    if os.path.exists(lang_cfg):
        for l in langs_list:
            update_file(lang_cfg, rf'\[{l}\]\n(?!.*contentDir)', f'[{l}]\n  contentDir = "content/{l}"\n')

    # 5. ГЕНЕРАЦІЯ 9 МОВНИХ ФАЙЛІВ
    create_index_files()

    print(f"\n{G}🚀 УСПІХ: Інфраструктура повністю налаштована!{W}")

if __name__ == "__main__":
    setup()
    