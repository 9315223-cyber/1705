export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);

  // Перехоплюємо потік ТІЛЬКИ на головному корені сайту "/"
  if (url.pathname === "/") {
    // Зчитуємо гео-дані безпосередньо з IP-адреси клієнта на рівні мережі Cloudflare
    const country = request.cf?.country?.toLowerCase();

    // Матриця мовного відповідності (Твоя карта 9 мов)
    const countryToLocale = {
      ua: "/uk/",
      de: "/de/",
      fr: "/fr/",
      es: "/es/",
      cn: "/zh/",
      tw: "/zh/",
      tr: "/tr/",
      ie: "/ga/",
      ru: "/ru/"
    };

    // Визначаємо мову: якщо країни немає в списку, віддаємо "/uk/", як вказано в нашому config.toml
    const targetLocale = countryToLocale[country] || "/uk/";

    // Повертаємо швидкий 302-редірект. 
    // ВАЖЛИВО: Використовуємо 302 (тимчасовий), щоб не руйнувати кеш користувачів, які подорожують
    return Response.redirect(new URL(targetLocale, request.url), 302);
  }

  // Якщо користувач переходить по внутрішнім сторінкам (/uk/about чи /en/posts), хмара просто віддає статику
  return next();
}
