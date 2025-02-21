let currentSlide = 1; // Начинаем со 2-го (т.к. 1-й - копия последнего)
const slidesContainer = document.querySelector('.slides-container');
const indicators = document.querySelectorAll('.indicator');
const totalSlides = 3; // Количество оригинальных слайдов
let autoSlideInterval;
let isDragging = false; // Флаг зажатой ЛКМ

// Устанавливаем стартовую позицию (чтобы скрыть копию последнего слайда)
slidesContainer.style.transform = `translateX(-100vw)`;

// Функция смены слайдов
function showSlide(index) {
    slidesContainer.style.transition = "transform 0.5s ease-in-out";
    slidesContainer.style.transform = `translateX(-${index * 100}vw)`;
    
    indicators.forEach((indicator, i) => {
        indicator.classList.remove('active');
        void indicator.offsetWidth; // Перезапуск анимации индикатора
        if (i === (index - 1) % totalSlides) {
            indicator.classList.add('active');
        }
    });
}

// Функция для плавного перехода между 1-м и последним слайдом
function handleLoop() {
    if (currentSlide === totalSlides + 1) {
        setTimeout(() => {
            slidesContainer.style.transition = "none";
            currentSlide = 1;
            slidesContainer.style.transform = `translateX(-100vw)`;
        }, 500);
    } else if (currentSlide === 0) {
        setTimeout(() => {
            slidesContainer.style.transition = "none";
            currentSlide = totalSlides;
            slidesContainer.style.transform = `translateX(-${totalSlides * 100}vw)`;
        }, 500);
    }
}

// Функции для переключения слайдов
function nextSlide() {
    if (currentSlide < totalSlides + 1) {
        currentSlide++;
    }
    showSlide(currentSlide);
    handleLoop();
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
    }
    showSlide(currentSlide);
    handleLoop();
}

// Автопрокрутка слайдов
function startAutoSlide() {
    autoSlideInterval = setInterval(nextSlide, 5000);
}

function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

startAutoSlide();

// Обработка свайпов на тач-устройствах
let touchStartX = null;
let touchEndX = null;
const slider = document.getElementById('slider');

slider.addEventListener('touchstart', (e) => {
    stopAutoSlide();
    touchStartX = e.changedTouches[0].screenX;
}, false);

slider.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleGesture(touchStartX, touchEndX);
    startAutoSlide();
}, false);

// Обработка мышиных событий (только при зажатой ЛКМ)
let mouseStartX = null;
let mouseEndX = null;

slider.addEventListener('mousedown', (e) => {
    if (e.button !== 0) return;
    stopAutoSlide();
    mouseStartX = e.screenX;
    isDragging = true;
}, false);

slider.addEventListener('mouseup', (e) => {
    if (!isDragging) return;
    mouseEndX = e.screenX;
    handleGesture(mouseStartX, mouseEndX);
    isDragging = false;
    startAutoSlide();
}, false);

slider.addEventListener('mouseleave', (e) => {
    if (!isDragging) return;
    mouseEndX = e.screenX;
    handleGesture(mouseStartX, mouseEndX);
    isDragging = false;
    startAutoSlide();
}, false);

// Универсальная функция обработки жеста (свайп)
function handleGesture(startX, endX) {
    if (startX === null || endX === null) return;
    const diffX = startX - endX;
    if (Math.abs(diffX) > 50) {
        if (diffX > 0) {
            nextSlide();
        } else {
            prevSlide();
        }
    }
}