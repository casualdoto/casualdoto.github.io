document.addEventListener('DOMContentLoaded', function() {
    // Получаем текущий язык из localStorage или используем язык по умолчанию
    const currentLang = localStorage.getItem('language') || 'ru';
    
    // Устанавливаем класс для body, чтобы CSS мог реагировать на язык
    document.documentElement.setAttribute('lang', currentLang);
    
    // Показываем элементы текущего языка и скрываем остальные
    updateLanguageDisplay(currentLang);
    
    // Инициализируем переключатель языка
    const langSwitcher = document.getElementById('language-switcher');
    if (langSwitcher) {
        langSwitcher.value = currentLang;
        langSwitcher.addEventListener('change', function() {
            const newLang = this.value;
            localStorage.setItem('language', newLang);
            document.documentElement.setAttribute('lang', newLang);
            updateLanguageDisplay(newLang);
        });
    }
});

// Функция для обновления отображения элементов в зависимости от языка
function updateLanguageDisplay(lang) {
    // Показываем элементы текущего языка
    document.querySelectorAll(`.lang-${lang}`).forEach(el => {
        el.style.display = 'block';
    });
    
    // Скрываем элементы других языков
    document.querySelectorAll('.lang-content').forEach(el => {
        if (!el.classList.contains(`lang-${lang}`)) {
            el.style.display = 'none';
        }
    });
    
    // Текст кнопки переключения обновляется автоматически через CSS
} 