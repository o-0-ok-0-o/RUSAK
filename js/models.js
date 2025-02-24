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
    item.addEventListener('click', (e) => {
        if (!e.target.closest('.sub-options')) {
            const checkbox = item.querySelector('input[type="checkbox"]');
            if (checkbox) {
                checkbox.checked = !checkbox.checked;
                item.classList.toggle('selected', checkbox.checked);
            }
        }
    });
});

// Предотвращаем двойное срабатывание при клике на чекбокс
document.querySelectorAll('.custom-checkbox, .custom-radio').forEach(control => {
    control.addEventListener('click', (e) => {
        e.stopPropagation();
    });
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

// Engine selection
document.querySelectorAll('.engine-option').forEach(option => {
    option.addEventListener('click', () => {
        document.querySelectorAll('.engine-option').forEach(opt => 
            opt.classList.remove('selected'));
        option.classList.add('selected');
    });
});

// Связывание чекбоксов подкачки колес
const suspensionMain = document.getElementById('suspension');
const suspensionSub1 = document.getElementById('suspension_1');
const suspensionSub2 = document.getElementById('suspension_2');

[suspensionSub1, suspensionSub2].forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        suspensionMain.checked = suspensionSub1.checked || suspensionSub2.checked;
        const item = suspensionMain.closest('.option-item');
        if (item) {
            item.classList.toggle('selected', suspensionMain.checked);
        }
    });
});

suspensionMain.addEventListener('change', () => {
    if (!suspensionMain.checked) {
        suspensionSub1.checked = false;
        suspensionSub2.checked = false;
    }
});

// При загрузке страницы открываем первую секцию
document.querySelector('.config-title').click();