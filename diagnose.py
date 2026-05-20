#!/usr/bin/env python3
import os
import subprocess

def print_status(component, status, message):
    colors = {"OK": "\033[92m[УСПІХ]\033[0m", "WARN": "\033[93m[УВАГА]\033[0m", "ERROR": "\033[91m[ПОМИЛКА]\033[0m"}
    print(f"{colors.get(status, '[INFO]')} {component.ljust(30)}: {message}")

print("\033[95m=== STARTING ADVANCED INFRASTRUCTURE DIAGNOSIS ===\033[0m\n")

# 1. Перевірка тем і модулів
if os.path.exists("themes"):
    print_status("Physical Themes Folder", "ERROR", "Знайдено папку themes! Вона конфліктує з Go Modules.")
else:
    print_status("Go Modules Theme", "OK", "Фізичних конфліктів немає. Тема керується через Go proxy.")

# 2. Сканування головного конфігу на наявність блоку [author]
config_path = "config/_default/config.toml"
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "[author]" in content or "author =" in content:
        print_status("Config Author Field", "WARN", "Виявлено старе поле author. В Hugo v0.161+ воно має лежати в [params.author].")
    else:
        print_status("Config Author Field", "OK", "Старих полів автора в корені не знайдено.")
else:
    print_status("Core Config", "ERROR", f"Файл {config_path} відсутній!")

# 3. Перевірка контенту для мовних версій
languages = ['uk', 'en', 'de', 'zh', 'ru', 'fr', 'ga', 'tr', 'es']
missing_index = []
for lang in languages:
    idx_path = f"content/{lang}/_index.md"
    if not os.path.exists(idx_path):
        missing_index.append(lang)

if not missing_index:
    print_status("Content Index Files", "OK", "Усі 9 мов мають стартові файли _index.md.")
else:
    print_status("Content Index Files", "WARN", f"Відсутні _index.md для мов: {', '.join(missing_index)}")

# 4. Тест збірки через CLI
print("\n\033[94m[ПРОЦЕС] Запуск тестової збірки сайту через Hugo CLI...\033[0m")
result = subprocess.run(["hugo", "--gc"], capture_output=True, text=True)

if result.returncode != 0:
    print_status("Hugo Site Build", "ERROR", "Hugo не зміг зібрати сайт.")
    if "warnings.html" in result.stderr and ".Author" in result.stderr:
        print("\033[91m[ДІАГНОЗ ШІ]: Підтверджено конфлікт Hugo v0.161 і шаблону warnings.html теми Congo.\033[0m")
else:
    print_status("Hugo Site Build", "OK", "Сайт успішно скомпільовано без помилок!")

print("\n\033[95m=== DIAGNOSIS COMPLETE ===\033[0m")