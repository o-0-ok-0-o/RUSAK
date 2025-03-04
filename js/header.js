document.addEventListener("DOMContentLoaded", () => {
    // Cache DOM elements using a structured object
    const elements = {
      // Header elements
      sliderClose: document.querySelector(".close-header"),
      header: document.querySelector(".nav-menu"),
      headerBtn: document.querySelector(".header-btn"),
      sideMenu: document.getElementById("sidebar"),
  
      // Mobile menu elements
      mobile: {
        models: {
          btn: document.getElementById("models"),
          btnMain: document.querySelector(".models-main-phone"),
          menu: document.querySelector(".models"),
          closeBtn: document.getElementById("close-model"),
        },
        config: {
          btn: document.getElementById("config"),
          btnMain: document.querySelector(".config-main-phone"),
          menu: document.querySelector(".config"),
          closeBtn: document.getElementById("close-config"),
        },
        rusak: {
          btn: document.getElementById("rusak"),
          menu: document.querySelector(".rusak"),
          closeBtn: document.getElementById("close-rusak"),
        },
      },
  
      // PC menu elements
      pc: {
        models: {
          btn: document.getElementById("models-pc"),
          btnMain: document.querySelector(".models-main-pc"),
          menu: document.querySelector(".models-pc"),
        },
        config: {
          btn: document.getElementById("config-pc"),
          btnMain: document.querySelector(".config-main-pc"),
          menu: document.querySelector(".config-pc"),
        },
        rusak: {
          btn: document.getElementById("rusak-pc"),
          menu: document.querySelector(".rusak-pc"),
        },
        news: {
          btn: document.getElementById("news-pc"),
          menu: document.querySelector(".news-pc"),
        },
        video: {
          btn: document.getElementById("video-pc"),
          menu: document.querySelector(".video-pc"),
        },
        review: {
          btn: document.getElementById("review-pc"),
          menu: document.querySelector(".review-pc"),
        },
      },
  
      // Modals
      modals: {
        price: document.getElementById("price-modal"),
        call: document.getElementById("call-modal"),
      },
      modalTriggers: {
        price: document.getElementById("price"),
        call: document.getElementById("call"),
      },
      closeFormBtns: document.querySelectorAll(".close-form"),
    }
  
    // Helper functions
    function toggleClass(element, className) {
      if (element) element.classList.toggle(className)
    }
  
    function removeClass(element, className) {
      if (element) element.classList.remove(className)
    }
  
    function closeAllPcMenus() {
      // Get all PC menu items
      const pcMenuItems = Object.values(elements.pc)
  
      // Remove 'open' class from all PC menu buttons and menus
      pcMenuItems.forEach((item) => {
        removeClass(item.btn, "open")
        removeClass(item.menu, "open")
      })
  
      // Reset header state
      removeClass(elements.sliderClose, "open")
      removeClass(elements.header, "open")
    }
  
    function toggleHeaderColor() {
      toggleClass(elements.sliderClose, "open")
      toggleClass(elements.header, "open")
    }
  
    function handlePcMenuClick(menuItem) {
      if (menuItem.btn.classList.contains("open")) {
        closeAllPcMenus()
      } else {
        closeAllPcMenus()
        toggleClass(menuItem.btn, "open")
        toggleClass(menuItem.menu, "open")
        toggleHeaderColor()
      }
    }
  
    function showModal(modal) {
      if (modal) modal.style.display = "flex"
    }
  
    function hideModal(modal) {
      if (modal) modal.style.display = "none"
    }
  
    // Event listeners
    // Close button
    elements.sliderClose.addEventListener("click", closeAllPcMenus)
  
    // Header button
    elements.headerBtn.addEventListener("click", function () {
      const { header, sideMenu } = elements
      const mobileMenus = Object.values(elements.mobile).map((item) => item.menu)
  
      if (header.classList.contains("open") && sideMenu.classList.contains("open")) {
        removeClass(header, "open")
      } else if (!header.classList.contains("open") && !sideMenu.classList.contains("open")) {
        toggleClass(header, "open")
      }
  
      toggleClass(this, "open")
      toggleClass(sideMenu, "open")
  
      // Close all mobile menus
      mobileMenus.forEach((menu) => removeClass(menu, "open"))
    })
  
    // Mobile menu event listeners
    // Setup mobile menu interactions
    Object.entries(elements.mobile).forEach(([key, item]) => {
      // Main button click
      if (item.btn) {
        item.btn.addEventListener("click", () => toggleClass(item.menu, "open"))
      }
  
      // Main phone button click
      if (item.btnMain) {
        item.btnMain.addEventListener("click", () => {
          toggleClass(item.menu, "open")
          toggleClass(elements.header, "open")
        })
      }
  
      // Close button click
      if (item.closeBtn) {
        item.closeBtn.addEventListener("click", () => {
          removeClass(item.menu, "open")
  
          // Toggle header if sidebar is not open (only for models and config)
          if ((key === "models" || key === "config") && !elements.sideMenu.classList.contains("open")) {
            toggleClass(elements.header, "open")
          }
        })
      }
    })
  
    // PC menu event listeners
    // Setup PC menu interactions
    Object.values(elements.pc).forEach((item) => {
      // Main button click
      if (item.btn) {
        item.btn.addEventListener("click", () => handlePcMenuClick(item))
      }
  
      // Main PC button click (if exists)
      if (item.btnMain) {
        item.btnMain.addEventListener("click", () => handlePcMenuClick(item))
      }
    })
  
    // Modal event listeners
    // Open modals
    Object.entries(elements.modalTriggers).forEach(([key, trigger]) => {
      if (trigger) {
        trigger.addEventListener("click", () => showModal(elements.modals[key]))
      }
    })
  
    // Close modals with close buttons
    elements.closeFormBtns.forEach((closeBtn) => {
      closeBtn.addEventListener("click", function () {
        const modalId = this.getAttribute("data-modal")
        hideModal(document.getElementById(modalId))
      })
    })
  
    // Close modals on outside click
    window.addEventListener("click", (event) => {
      Object.values(elements.modals).forEach((modal) => {
        if (modal && event.target === modal) {
          hideModal(modal)
        }
      })
    })
  })
  
  