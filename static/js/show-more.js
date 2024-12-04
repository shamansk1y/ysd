document.addEventListener('DOMContentLoaded', () => {
    const showMoreBtn = document.getElementById('show-more-btn');
    let itemsToShow = 12; // Количество товаров, которые отображаем за раз

    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', () => {
            // Обновляем список скрытых товаров каждый раз, когда нажимается кнопка
            const hiddenItems = document.querySelectorAll('.product-item.hidden');
            let visibleCount = 0;

            // Показываем следующие товары
            for (let i = 0; i < hiddenItems.length; i++) {
                if (visibleCount >= itemsToShow) break;
                hiddenItems[i].classList.remove('hidden');
                visibleCount++;
            }

            // Если все товары показаны, скрываем кнопку
            if (document.querySelectorAll('.product-item.hidden').length === 0) {
                showMoreBtn.style.display = 'none';
            }
        });
    }
});
