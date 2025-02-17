document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.nav-menu');
    const headerBtn = document.querySelector('.header-btn');
    const sideMenu = document.getElementById('sidebar');
    const modelsBtn = document.getElementById('models');
    const modelsMenu = document.querySelector('.models');
    const configBtn = document.getElementById('config');
    const configMenu = document.querySelector('.config');
    const shopperBtn = document.getElementById('shopper');
    const shopperMenu = document.querySelector('.shopper');
    const ownerBtn = document.getElementById('owner');
    const ownerMenu = document.querySelector('.owner');
    const rusakBtn = document.getElementById('rusak');
    const rusakMenu = document.querySelector('.rusak');

    const modelsCloseBtn = document.getElementById('close-model');
    const configCloseBtn = document.getElementById('close-config')
    const shopperCloseBtn = document.getElementById('close-shopper');
    const ownerCloseBtn = document.getElementById('close-owner');
    const rusakCloseBtn = document.getElementById('close-rusak');

    const modelsBtnPc = document.getElementById('models-pc');
    const modelsMenuPc = document.querySelector('.models-pc');
    const configBtnPc = document.getElementById('config-pc');
    const configMenuPc = document.querySelector('.config-pc');
    const shopperBtnPc = document.getElementById('shopper-pc');
    const shopperMenuPc = document.querySelector('.shopper-pc');
    const ownerBtnPc = document.getElementById('owner-pc');
    const ownerMenuPc = document.querySelector('.owner-pc');
    const rusakBtnPc = document.getElementById('rusak-pc');
    const rusakMenuPc = document.querySelector('.rusak-pc');

    headerBtn.addEventListener('click', function() {
        this.classList.toggle('open');
        sideMenu.classList.toggle('open');
        header.classList.toggle('open');
        modelsMenu.classList.remove('open');
        shopperMenu.classList.remove('open');
        ownerMenu.classList.remove('open');
        rusakMenu.classList.remove('open');
        configMenu.classList.remove('open');
    });

    modelsBtn.addEventListener('click', function() {
        modelsMenu.classList.toggle('open');
    });
    configBtn.addEventListener('click', function(){
        configMenu.classList.toggle('open');
    });
    shopperBtn.addEventListener('click', function() {
        shopperMenu.classList.toggle('open');
    });
    ownerBtn.addEventListener('click', function() {
        ownerMenu.classList.toggle('open');
    });
    rusakBtn.addEventListener('click', function() {
        rusakMenu.classList.toggle('open');
    });

    modelsCloseBtn.addEventListener('click', function() {
        modelsMenu.classList.remove('open');
    });
    configCloseBtn.addEventListener('click', function() {
        configMenu.classList.remove('open');
    });
    shopperCloseBtn.addEventListener('click', function() {
        shopperMenu.classList.remove('open');
    });
    ownerCloseBtn.addEventListener('click', function() {
        ownerMenu.classList.remove('open');
    });
    rusakCloseBtn.addEventListener('click', function() {
        rusakMenu.classList.remove('open');
    });


    modelsBtnPc.addEventListener('click', function() {
        modelsMenuPc.classList.toggle('open');
        modelsBtnPc.classList.toggle('open');
        if (!header.classList.contains('open')) {
            header.classList.add('open');
        }
        configMenuPc.classList.remove('open');
        shopperMenuPc.classList.remove('open');
        ownerMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        configBtnPc.classList.remove('open');
        shopperBtnPc.classList.remove('open');
        ownerBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    configBtnPc.addEventListener('click', function () {
        configMenuPc.classList.toggle('open');
        configBtnPc.classList.toggle('open');
        if (!header.classList.contains('open')) {
            header.classList.add('open');
        }
        modelsMenuPc.classList.remove('open');
        shopperMenuPc.classList.remove('open');
        ownerMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        modelsBtnPc.classList.remove('open');
        shopperBtnPc.classList.remove('open');
        ownerBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    shopperBtnPc.addEventListener('click', function() {
        shopperMenuPc.classList.toggle('open');
        shopperBtnPc.classList.toggle('open');
        if (!header.classList.contains('open')) {
            header.classList.add('open');
        }
        configMenuPc.classList.remove('open');
        modelsMenuPc.classList.remove('open');
        ownerMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        configBtnPc.classList.remove('open');
        modelsBtnPc.classList.remove('open');
        ownerBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    ownerBtnPc.addEventListener('click', function() {
        ownerMenuPc.classList.toggle('open');
        ownerBtnPc.classList.toggle('open');
        if (!header.classList.contains('open')) {
            header.classList.add('open');
        }
        configMenuPc.classList.remove('open');
        modelsMenuPc.classList.remove('open');
        shopperMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');
        
        configBtnPc.classList.remove('open');
        modelsBtnPc.classList.remove('open');
        shopperBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    rusakBtnPc.addEventListener('click', function() {
        rusakMenuPc.classList.toggle('open');
        rusakBtnPc.classList.toggle('open');
        if (!header.classList.contains('open')) {
            header.classList.add('open');
        }
        configMenuPc.classList.remove('open');
        modelsMenuPc.classList.remove('open');
        shopperMenuPc.classList.remove('open');
        ownerMenuPc.classList.remove('open');

        configBtnPc.classList.remove('open');
        modelsBtnPc.classList.remove('open');
        shopperBtnPc.classList.remove('open');
        ownerBtnPc.classList.remove('open');
    });
    setInterval(function() {
        const menus = [modelsMenu, shopperMenu, ownerMenu, rusakMenu, modelsMenuPc, shopperMenuPc, ownerMenuPc, rusakMenuPc, configMenuPc, sideMenu];
        const isAnyMenuOpen = menus.some(menu => menu.classList.contains('open'));
        if (!isAnyMenuOpen) {
            header.classList.remove('open');
        }
    }, 10);
});