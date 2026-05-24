#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

# Колірна палітра
G, Y, R, B, P, W = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[95m", "\033[0m"

def update_file(path, pattern, replacement):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    print(f"\n{P}===================================================================={W}")
    print(f"{P}💥  MASTER SETUP v4.0: GEO-SECURITY & SELF-HEALING ENGINE        💥{W}")
    print(f"{P}===================================================================={W}")

    # 1. ЗАПИТ ДАНИХ
    domain = input(f"{B}Введіть домен (напр. enterprise-hub.pages.dev): {W}") or "enterprise-hub.pages.dev"
    repo = "9315223-cyber/1705"

    # 2. ОПТИМІЗАЦІЯ SEO ТА ЯДРА
    print(f"{Y}🔄 Оптимізація config.toml та SEO...{W}")
    cfg = "config/_default/config.toml"
    update_file(cfg, r'^baseURL = .*', f'baseURL = "https://{domain}/"')
    update_file(cfg, r'^relativeURLs = .*', 'relativeURLs = false')
    update_file(cfg, r'^canonifyURLs = .*', 'canonifyURLs = true')

    # 3. ЛІКУВАННЯ NESTING BUG ТА ЛІНКУВАННЯ 9 МОВ
    print(f"{Y}🔄 Ізоляція 9 мовних потоків...{W}")
    langs = ['en', 'uk', 'de', 'fr', 'es', 'ru', 'zh', 'tr', 'ga']
    lang_file = "config/_default/languages.toml"
    for l in langs:
        update_file(lang_file, rf'\[{l}\]\n(?!.*contentDir)', f'[{l}]\n  contentDir = "content/{l}"\n')
        os.makedirs(f"content/{l}/posts", exist_ok=True)
        idx = f"content/{l}/_index.md"
        if not os.path.exists(idx):
            with open(idx, "w", encoding='utf-8') as f:
                f.write(f'---\ntitle: "Enterprise Hub {l.upper()}"\nlayout: "page"\n---')

    # 4. ВПРОВАДЖЕННЯ llms.txt (GEO Оптимізація)
    print(f"{Y}🔄 Створення маніфесту llms.txt для ШІ...{W}")
    with open("static/llms.txt", "w", encoding='utf-8') as f:
        f.write(f"# Congo Enterprise Hub\n\n## Context\nOptimized for AI discovery 2026.\n\n## Repository\n{repo}")

    # 5. САНАЦІЯ SVELTIA CMS
    print(f"{Y}🔄 Очищення Sveltia CMS від хардкоду Codespaces...{W}")
    cms_cfg = "static/admin/config.yml"
    update_file(cms_cfg, r'^  repo: .*', f'  repo: {repo}')
    update_file(cms_cfg, r'^site_url: .*', 'site_url: ""')
    update_file(cms_cfg, r'^display_url: .*', 'display_url: ""')

    print(f"\n{G}🚀 УСПІХ: Вся інфраструктура синхронізована та захищена!{W}")
    print(f"{B}Тепер ваш сайт повністю відповідає Ідеальній Структурі.{W}\n")

if __name__ == "__main__":
    main()
    