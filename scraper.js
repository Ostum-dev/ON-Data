const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

async function scrape() {
    try {
        // 1. ضع رابط صفحة الأنميات هنا
        const url = 'https://example-anime-site.com'; 
        const { data } = await axios.get(url);
        const $ = cheerio.load(data);
        const animes = [];

        // 2. هنا يتم الكشط: استبدل .anime-card وما بداخلها بما يناسب الموقع
        $('.anime-card').each((i, el) => {
            const title = $(el).find('.title-class').text().trim();
            const link = $(el).find('a').attr('href');
            const img = $(el).find('img').attr('src');
            
            if (title) {
                animes.push({ title, link, img });
            }
        });

        // 3. حفظ البيانات في ملف json ليستخدمه موقعك
        fs.writeFileSync('data.json', JSON.stringify(animes, null, 2));
        console.log('Scraping finished successfully.');

    } catch (error) {
        console.error('Error during scraping:', error);
    }
}

scrape();
