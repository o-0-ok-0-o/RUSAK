document.addEventListener('DOMContentLoaded', function() {
    const elements = {
        sliderClose: document.querySelector('.close-header'),
        header: document.querySelector('.nav-menu'),
        headerBtn: document.querySelector('.header-btn'),
        sideMenu: document.getElementById('sidebar'),
        menus: {
            models: {
                btn: document.getElementById('models'),
                btnMain: document.querySelector('.models-main-phone'),
                menu: document.querySelector('.models'),
                closeBtn: document.getElementById('close-model')
            },
            config: {
                btn: document.getElementById('config'),
                btnMain: document.querySelector('.config-main-phone'),
                menu: document.querySelector('.config'),
                closeBtn: document.getElementById('close-config')
            },
            rusak: {
                btn: document.getElementById('rusak'),
                menu: document.querySelector('.rusak'),
                closeBtn: document.getElementById('close-rusak')
            }
        },
        pcMenus: {
            models: {
                btn: document.getElementById('models-pc'),
                menu: document.querySelector('.models-pc')
            },
            config: {
                btn: document.getElementById('config-pc'),
                menu: document.querySelector('.config-pc')
            },
            rusak: {
                btn: document.getElementById('rusak-pc'),
                menu: document.querySelector('.rusak-pc')
            }
        },
        modals: {
            price: document.getElementById('price-modal'),
            call: document.getElementById('call-modal')
        }
    };

    function closeMenus() {
        Object.values(elements.menus).forEach(({ menu }) => menu?.classList.remove('open'));
        Object.values(elements.pcMenus).forEach(({ btn, menu }) => {
            btn?.classList.remove('open');
            menu?.classList.remove('open');
        });
        elements.sideMenu.classList.remove('open');
        elements.headerBtn.classList.remove('open');
        elements.sliderClose.classList.remove('open');
        elements.header.classList.remove('open');
    }

    function toggleMenu(menu) {
        const { btn, menu: menuEl } = elements.pcMenus[menu];
        if (btn.classList.contains('open')) {
            closeMenus();
        } else {
            closeMenus();
            btn.classList.add('open');
            menuEl.classList.add('open');
            elements.sliderClose.classList.add('open');
            elements.header.classList.add('open');
        }
    }

    elements.sliderClose.addEventListener('click', closeMenus);

    elements.headerBtn.addEventListener('click', function() {
        if (this.classList.contains('open')) {
            closeMenus();
        } else {
            closeMenus();
            elements.sideMenu.classList.add('open');
            elements.header.classList.add('open');
            elements.headerBtn.classList.add('open');
        }
    });

    Object.values(elements.menus).forEach(({ btn, btnMain, menu, closeBtn }) => {
        btn?.addEventListener('click', () => menu.classList.toggle('open'));
        btnMain?.addEventListener('click', () => {
            menu.classList.toggle('open');
            elements.header.classList.toggle('open');
        });
        closeBtn?.addEventListener('click', () => {
            menu.classList.remove('open');
            if (!elements.sideMenu.classList.contains('open')) {
                elements.header.classList.remove('open');
            }
        });
    });

    Object.entries(elements.pcMenus).forEach(([key, { btn, btnMain }]) => {
        btn?.addEventListener('click', () => toggleMenu(key));
        btnMain?.addEventListener('click', () => toggleMenu(key));
    });

    document.getElementById('price').addEventListener('click', () => {
        elements.modals.price.style.display = 'flex';
    });
    document.getElementById('call').addEventListener('click', () => {
        elements.modals.call.style.display = 'flex';
    });

    document.querySelectorAll('.close-form').forEach(closeBtn => {
        closeBtn.addEventListener('click', function () {
            elements.modals[this.dataset.modal].style.display = 'none';
        });
    });

    window.addEventListener('click', (event) => {
        Object.values(elements.modals).forEach(modal => {
            if (event.target === modal) modal.style.display = 'none';
        });
    });
});