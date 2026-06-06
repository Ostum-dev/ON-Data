// فتح القائمة الجانبية
document.getElementById('menu-btn').addEventListener('click', () => {
    document.getElementById('sidebar').classList.toggle('active');
});

// تحميل البيانات
async function loadAnime() {
    const response = await fetch('data.json');
    const animes = await response.json();
    const container = document.getElementById('anime-container');

    animes.forEach(anime => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <img src="${anime.img}" alt="${anime.title}">
            <h3>${anime.title}</h3>
            <button onclick="watchExternally('${anime.link}')">مشاهدة بمشغل خارجي</button>
        `;
        container.appendChild(card);
    });
}

// وظيفة المشغل الخارجي
function watchExternally(url) {
    // يفتح الرابط في تطبيق خارجي إذا كان المتصفح يدعم ذلك
    window.location.href = `intent:${url}#Intent;scheme=http;package=com.mxtech.videoplayer.ad;end`;
}

loadAnime();
