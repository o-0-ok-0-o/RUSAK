document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.nav-menu');
    const headerBtn = document.querySelector('.header-btn');
    const sideMenu = document.getElementById('sidebar');

    headerBtn.addEventListener('click', function() {
        this.classList.toggle('open');
        sideMenu.classList.toggle('open');
        header.classList.toggle('open');
    });
});