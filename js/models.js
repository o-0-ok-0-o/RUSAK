// Обработка кликов по заголовкам секций
document.querySelectorAll('.config-title').forEach(title => {
    title.addEventListener('click', () => {
        const content = title.nextElementSibling;
        title.classList.toggle('active');
        content.classList.toggle('active');
    });
});

// Обработка выбора опций
document.querySelectorAll('.option-item').forEach(item => {
    const radio = item.querySelector('input[type="radio"]');
    if (radio) {
        item.addEventListener('click', (e) => {
            if (!e.target.closest('.custom-radio')) {
                radio.checked = true;
                radio.dispatchEvent(new Event('change'));
            }
        });
    } else {
        item.addEventListener('click', (e) => {
            if (!e.target.closest('.custom-checkbox')) {
                const checkbox = item.querySelector('input[type="checkbox"]');
                if (checkbox) {
                    checkbox.checked = !checkbox.checked;
                    checkbox.dispatchEvent(new Event('change'));
                }
            }
        });
    }
});

// Обработка радио кнопок
document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener('change', () => {
        const name = radio.getAttribute('name');
        document.querySelectorAll(`input[name="${name}"]`).forEach(r => {
            const item = r.closest('.option-item');
            if (item) {
                item.classList.toggle('selected', r.checked);
            }
        });
    });
});

// Обработка чекбоксов
document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        const item = checkbox.closest('.option-item');
        if (item) {
            item.classList.toggle('selected', checkbox.checked);
        }
    });
});

// Engine selection
document.querySelectorAll('.engine-option').forEach(option => {
    option.addEventListener('click', () => {
        document.querySelectorAll('.engine-option').forEach(opt => 
            opt.classList.remove('selected'));
        option.classList.add('selected');
    });
});

// При загрузке страницы открываем первую секцию
document.querySelector('.config-title').click();