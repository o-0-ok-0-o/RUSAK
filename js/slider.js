let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const indicators = document.querySelectorAll('.indicator');
const totalSlides = slides.length;
let autoSlideInterval;
let isDragging = false; // Флаг, что ЛКМ зажата

// Функция для отображения слайда и сброса анимации индикатора
function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === index);
  });
  indicators.forEach((indicator, i) => {
    indicator.classList.remove('active');
    void indicator.offsetWidth; // перезапуск анимации
    if (i === index) {
      indicator.classList.add('active');
    }
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  showSlide(currentSlide);
}

// Автоматическая смена слайдов каждые 5 секунд
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
  // Проверяем, что нажата именно левая кнопка мыши (e.button === 0)
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

// Универсальная функция обработки жеста (для мыши и тач)
function handleGesture(startX, endX) {
  if (startX === null || endX === null) return;
  const diffX = startX - endX;
  // Порог 50px для переключения слайда
  if (Math.abs(diffX) > 50) {
    if (diffX > 0) {
      nextSlide();
    } else {
      prevSlide();
    }
  }
}