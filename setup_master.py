import os
import re

# Колірна палітра для звіту
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

def setup():
    print(f"\n{G}💥 MASTER SETUP v5.0: INFRASTRUCTURE REPAIR & LLM OPTIMIZATION 💥{W}\n")

    domain = "cyber-hub-1705.pages.dev"
    repo = "9315223-cyber/1705"

    # 1. Створення/Оновлення static/llms.txt (згідно з стандартами Cloudflare)
    print(f"{B}🔧 Генерація маніфесту llms.txt...{W}")
    with open("static/llms.txt", "w", encoding='utf-8') as f:
        f.write(f"# Congo Enterprise Hub\n\n## Context\nHigh-performance multilingual marketing hub.\n\n## Language Matrix\n/en/, /uk/, /de/, /fr/, /es/, /ru/, /zh/, /tr/, /ga/")

    # 2. Виправлення помилки в _middleware.ts (видалення PagesFunction типів)
    print(f"{B}🔧 Виправлення захисного щита Edge Functions...{W}")
    os.makedirs("functions", exist_ok=True)
    with open("functions/_middleware.ts", "w", encoding='utf-8') as f:
        f.write("export async function onRequest(context) {\n"
                "  const ua = (context.request.headers.get('user-agent') || '').toLowerCase();\n"
                "  const blocked = ['gptbot', 'chatgpt-user', 'bytespider', 'claudebot'];\n"
                "  if (blocked.some(bot => ua.includes(bot))) return new Response('Forbidden', {status: 403});\n"
                "  return await context.next();\n}")

    # 3. Санація Sveltia CMS (Видалення хардкоду Codespaces)
    update_file("static/admin/config.yml", r'^  repo: .*', f'  repo: {repo}')
    update_file("static/admin/config.yml", r'^site_url: .*', f'site_url: "https://{domain}"')

    # 4. Лікування Nesting Bug (Ізоляція 9 мов)
    lang_cfg = "config/_default/languages.toml"
    langs = ['en', 'uk', 'de', 'fr', 'es', 'ru', 'zh', 'tr', 'ga']
    for l in langs:
        update_file(lang_cfg, rf'\[{l}\]\n(?!.*contentDir)', f'[{l}]\n  contentDir = "content/{l}"\n')

    print(f"\n{G}🚀 УСПІХ: Помилки в _middleware виправлено, інфраструктура готова!{W}")

if __name__ == "__main__":
    setup()
    