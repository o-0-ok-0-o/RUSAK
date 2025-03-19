// Находим видеоплеер и кнопки управления
const video = document.querySelector('video');
const playButton = document.querySelector('#playButton');
const muteButton = document.querySelector('#muteButton');
const volumeSlider = document.querySelector('#volumeSlider');
const speedSlider = document.querySelector('#speedSlider');
const fullscreenButton = document.querySelector('#fullscreenButton');
const rewindButton = document.querySelector('#rewindButton');
const forwardButton = document.querySelector('#forwardButton');
const progressBar = document.querySelector('#progressBar');
const currentTimeDisplay = document.querySelector('#currentTime');
const durationDisplay = document.querySelector('#duration');

// Проверка доступности видео
if (!video) {
    console.error('Видео не найдено! Проверьте, что элемент <video> присутствует в HTML.');
}

// Функция для воспроизведения или паузы видео
function togglePlayPause() {
    if (video.paused) {
        video.play();
        playButton.innerText = '⏸️';
    } else {
        video.pause();
        playButton.innerText = '▶️';
    }
}

// Функция для включения/отключения звука
function toggleMute() {
    video.muted = !video.muted;
    muteButton.innerText = video.muted ? '🔇' : '🔊';
}

// Функция для изменения громкости
function changeVolume() {
    video.volume = volumeSlider.value;
}

// Функция для изменения скорости воспроизведения
function changeSpeed() {
    video.playbackRate = speedSlider.value;
}

// Функция для переключения полноэкранного режима
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        video.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
}

// Функция для перемотки видео назад
function rewindVideo() {
    video.currentTime -= 10;
}

// Функция для перемотки видео вперёд
function forwardVideo() {
    video.currentTime += 10;
}

// Функция для обновления прогресс-бара и времени
function updateProgress() {
    if (!isNaN(video.duration)) {
        const progress = (video.currentTime / video.duration) * 100;
        progressBar.value = progress;
        currentTimeDisplay.innerText = formatTime(video.currentTime);
        durationDisplay.innerText = formatTime(video.duration);
    }
}

// Функция для форматирования времени в mm:ss
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

// Функция для установки текущего времени видео через прогресс-бар
function setVideoProgress() {
    const newTime = (progressBar.value / 100) * video.duration;
    video.currentTime = newTime;
}

// Добавление обработчиков событий к кнопкам и элементам
playButton.addEventListener('click', togglePlayPause);
muteButton.addEventListener('click', toggleMute);
volumeSlider.addEventListener('input', changeVolume);
speedSlider.addEventListener('input', changeSpeed);
fullscreenButton.addEventListener('click', toggleFullscreen);
rewindButton.addEventListener('click', rewindVideo);
forwardButton.addEventListener('click', forwardVideo);
video.addEventListener('timeupdate', updateProgress);
progressBar.addEventListener('input', setVideoProgress);
