document.addEventListener('DOMContentLoaded', function() {
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

    headerBtn.addEventListener('click', function() {
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
    });
    configBtn.addEventListener('click', function(){
        configMenu.classList.toggle('open');
    });
    configBtnMain.addEventListener('click', function(){
        configMenu.classList.toggle('open');
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
    rusakCloseBtn.addEventListener('click', function() {
        rusakMenu.classList.remove('open');
    });


    modelsBtnPc.addEventListener('click', function() {
        modelsMenuPc.classList.toggle('open');
        modelsBtnPc.classList.toggle('open');
        configMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        configBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    modelsBtnPcMain.addEventListener('click', function() {
        modelsMenuPc.classList.toggle('open');
        modelsBtnPc.classList.toggle('open');
        configMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        configBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    configBtnPc.addEventListener('click', function () {
        configMenuPc.classList.toggle('open');
        configBtnPc.classList.toggle('open');
        modelsMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        modelsBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });
    configBtnPcMain.addEventListener('click', function () {
        configMenuPc.classList.toggle('open');
        configBtnPc.classList.toggle('open');
        modelsMenuPc.classList.remove('open');
        rusakMenuPc.classList.remove('open');

        modelsBtnPc.classList.remove('open');
        rusakBtnPc.classList.remove('open');
    });

    rusakBtnPc.addEventListener('click', function() {
        rusakMenuPc.classList.toggle('open');
        rusakBtnPc.classList.toggle('open');
        configMenuPc.classList.remove('open');
        modelsMenuPc.classList.remove('open');
        configBtnPc.classList.remove('open');
        modelsBtnPc.classList.remove('open'); 
    });
});