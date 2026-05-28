export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);
  const userAgent = (request.headers.get("user-agent") || "").toLowerCase();

  // ПРИМІТКА: Цей список синхронізовано з файлом static/robots.txt
  // Якщо бот є у цьому списку, ми відключаємо гео-перенаправлення, щоб він міг просканувати всі 9 мов.
  const aiBots = ["gptbot", "chatgpt-user", "google-extended", "deepseekspider", "claudebot", "perplexitybot", "applebot"];
  const isAiBot = aiBots.some(bot => userAgent.includes(bot));

  if (isAiBot) {
    return next(); // Бот проходить вільно
  }

  // ПРИМІТКА: Працює тільки для головної сторінки сайту (домену).
  if (url.pathname === "/") {
    const country = request.cf?.country?.toLowerCase();

    // ПРИМІТКА: Матриця мов. Ключі (ua, de...) - це країни з Cloudflare. 
    // Значення (/uk/, /de/...) відповідають папкам контенту, які ми створили у config.toml.
    const countryToLocale = {
      ua: "/uk/", de: "/de/", at: "/de/", ch: "/de/",
      fr: "/fr/", be: "/fr/", es: "/es/", mx: "/es/",
      cn: "/zh/", tw: "/zh/", tr: "/tr/", ie: "/ga/",
      ru: "/ru/", by: "/ru/", kz: "/ru/"
    };

    const targetLocale = countryToLocale[country] || "/uk/";

    // ПРИМІТКА: 302 редірект вказує ШІ, що це тимчасове перенаправлення для людини.
    return Response.redirect(new URL(targetLocale, request.url), 302);
  }

  return next();
}
