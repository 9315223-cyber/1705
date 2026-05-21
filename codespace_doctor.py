#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Congo Hub - Daily Environment Doctor
"""
import os
import subprocess

def run_doctor():
    print("🔍 [DOCTOR] Перевірка портів та конфігурації хмари...")
    
    # Визначаємо URL для Codespaces
    codespace_name = os.getenv("CODESPACE_NAME", "local")
    domain = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "app.github.dev")
    
    if codespace_name != "local":
        cloud_url = f"https://{codespace_name}-1313.{domain}/"
        cmd = f"hugo server --bind=0.0.0.0 --baseURL={cloud_url} --appendPort=false"
    else:
        cmd = "hugo server --baseURL=http://localhost:1313/"
        
    print(f"🚀 Запуск: {cmd}")
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print("\n🛑 Роботу зупинено.")

if __name__ == "__main__":
    run_doctor()
