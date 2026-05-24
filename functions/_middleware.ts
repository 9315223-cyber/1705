// =====================================================================
// CONGO ENTERPRISE — EDGE BOT SHIELD (_middleware.ts)
// Захист на рівні Cloudflare Pages Functions (Lighthouse 100/100)
// =====================================================================

export const onRequest: PagesFunction = async (context) => {
  const userAgent = context.request.headers.get("user-agent") || "";

  // Список найбільш агресивних ШІ-скреперів та ботів 2026 року
  const blockedBots = [
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-Web",
    "PerplexityBot",
    "Bytespider", // Скрепер від Bytedance
    "CCBot",      // Common Crawl
    "Diffbot",
    "FacebookBot",
    "Google-Extended",
    "Amazonbot",
    "ClaudeCode"
  ];

  // Перевірка: якщо User-Agent містить рядок зі списку — блокуємо
  const isBlocked = blockedBots.some((bot) => 
    userAgent.toLowerCase().includes(bot.toLowerCase())
  );

  if (isBlocked) {
    return new Response(
      "Access Denied: AI Scraping and Unauthorized Bot Activity Blocked by Congo Enterprise Shield.",
      { 
        status: 403, 
        headers: { "Content-Type": "text/plain" } 
      }
    );
  }

  // Якщо це звичайний користувач або дозволений бот — продовжуємо завантаження
  return await context.next();
};
