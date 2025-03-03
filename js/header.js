document.addEventListener('DOMContentLoaded', function() {
    const sliderClose = document.querySelector('.close-header');
    const header = document.querySelector('.nav-menu');

    const headerBtn = document.querySelector('.header-btn');
    const sideMenu = document.getElementById('sidebar');
    const modelsBtn = document.getElementById('models');
    const modelsBtnMain = document.querySelector('.models-main-phone');
    const modelsMenu = document.querySelector('.models');
    const configBtn = document.getElementById('config');
    const configBtnMain = document.querySelector('.config-main-phone');
    const configMenu = document.querySelector('.config');
    const rusakBtn = document.getElementById('rusak');
    const rusakMenu = document.querySelector('.rusak');

    const modelsCloseBtn = document.getElementById('close-model');
    const configCloseBtn = document.getElementById('close-config')
    const rusakCloseBtn = document.getElementById('close-rusak');

    const modelsBtnPc = document.getElementById('models-pc');
    const modelsBtnPcMain = document.querySelector('.models-main-pc')
    const modelsMenuPc = document.querySelector('.models-pc');
    const configBtnPc = document.getElementById('config-pc');
    const configBtnPcMain = document.querySelector('.config-main-pc');
    const configMenuPc = document.querySelector('.config-pc');
    const rusakBtnPc = document.getElementById('rusak-pc');
    const rusakMenuPc = document.querySelector('.rusak-pc');

    function close() {
        modelsBtnPc.classList.remove('open');
        modelsMenuPc.classList.remove('open');
        configMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');
        configBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
        sliderClose.classList.remove('open');
        header.classList.remove('open');
    }

    function headerColor(){
        sliderClose.classList.toggle('open');
        header.classList.toggle('open');
    }

    sliderClose.addEventListener('click', ()=>{
        close();
    });

    headerBtn.addEventListener('click', function() {
        if(header.classList.contains('open') && sideMenu.classList.contains('open')){
            header.classList.remove('open');
        }
        else if (!header.classList.contains('open') && !sideMenu.classList.contains('open')) {
            header.classList.toggle('open');
        }
        this.classList.toggle('open');
        sideMenu.classList.toggle('open');
        modelsMenu.classList.remove('open');
        rusakMenu.classList.remove('open');
        configMenu.classList.remove('open');
    });

    modelsBtn.addEventListener('click', function() {
        modelsMenu.classList.toggle('open');
    });
    modelsBtnMain.addEventListener('click', function() {
        modelsMenu.classList.toggle('open');
        header.classList.toggle('open');
    });
    configBtn.addEventListener('click', function(){
        configMenu.classList.toggle('open');
    });
    configBtnMain.addEventListener('click', function(){
        configMenu.classList.toggle('open');
        header.classList.toggle('open');
    });
    rusakBtn.addEventListener('click', function() {
        rusakMenu.classList.toggle('open');
    });
    modelsCloseBtn.addEventListener('click', function() {
        modelsMenu.classList.remove('open');
        if (!sideMenu.classList.contains('open')) {
            header.classList.toggle('open');
        }
    });
    configCloseBtn.addEventListener('click', function() {
        configMenu.classList.remove('open');
        if (!sideMenu.classList.contains('open')) {
            header.classList.toggle('open');
        }
    });
    rusakCloseBtn.addEventListener('click', function() {
        rusakMenu.classList.remove('open');
    });
    modelsBtnPc.addEventListener('click', function() {
        if (modelsBtnPc.classList.contains('open')) {
            close();
        } else {
            close();
            modelsBtnPc.classList.toggle('open');
            modelsMenuPc.classList.toggle('open');
            headerColor();
        }
    });
    modelsBtnPcMain.addEventListener('click', function() {
        if (modelsBtnPc.classList.contains('open')) {
            close();
        } else {
            close();
            modelsBtnPc.classList.toggle('open');
            modelsMenuPc.classList.toggle('open');
            headerColor();
        }
    });
    configBtnPc.addEventListener('click', function () {
        if (configBtnPc.classList.contains('open')) {
            close();
        } else {
            close();
            configMenuPc.classList.toggle('open');
            configBtnPc.classList.toggle('open');
            headerColor();
        }
    });
    configBtnPcMain.addEventListener('click', function () {
        if (configBtnPc.classList.contains('open')) {
            close();
        } else {
            close();
            configMenuPc.classList.toggle('open');
            configBtnPc.classList.toggle('open');
            headerColor();
        }
    });

    rusakBtnPc.addEventListener('click', function() {
        if ( rusakBtnPc.classList.contains('open')) {
            close();
        } else {
            close();
            rusakMenuPc.classList.toggle('open');
            rusakBtnPc.classList.toggle('open');
            headerColor();
        }
    });
    
    
    const modals = {
        price: document.getElementById('price-modal'),
        call: document.getElementById('call-modal')
    };

    const priceBtn = document.getElementById('price');
    const callBtn = document.getElementById('call');

    if (priceBtn) {
        priceBtn.addEventListener('click', () => {
            modals.price.style.display = 'flex';
        });
    }

    if (callBtn) {
        callBtn.addEventListener('click', () => {
            modals.call.style.display = 'flex';
        });
    }

    document.querySelectorAll('.close-form').forEach(closeBtn => {
        closeBtn.addEventListener('click', function () {
            const modalId = this.getAttribute('data-modal');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });

    window.addEventListener('click', (event) => {
        Object.values(modals).forEach(modal => {
            if (modal && event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });
});
    
    