document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const vehicleImageContainer = document.getElementById("vehicle-image-container")
  const stickyColumn = document.getElementById("sticky-column")
  const specsPanel = document.getElementById("specs-panel")
  const pricePanel = document.getElementById("price-panel")
  const configSections = document.querySelectorAll(".config-section")
  const vehicle8x8Image = document.getElementById("vehicle-8x8")
  const vehicle6x6Image = document.getElementById("vehicle-6x6")
  const specValues = document.querySelectorAll(".spec-value")

  // Variables for scroll animation
  let isScrolling = false
  let scrollTimeout
  let initialConfigTop
  let initialImageHeight
  let initialRightColumnWidth

  // Initialize values
  function initializeValues() {
    initialConfigTop = vehicleImageContainer.offsetTop
    initialImageHeight = vehicleImageContainer.offsetHeight
    initialRightColumnWidth = stickyColumn.offsetWidth
  }

  // Call once on load
  initializeValues()

  // Handle window resize
  window.addEventListener("resize", initializeValues)

  // Scroll event handler
  window.addEventListener("scroll", () => {
    if (!isScrolling) {
      isScrolling = true
      requestAnimationFrame(handleScroll)
    }

    clearTimeout(scrollTimeout)
    scrollTimeout = setTimeout(() => {
      isScrolling = false
    }, 100)
  })

  // Handle scroll animation
  function handleScroll() {
    const scrollY = window.scrollY
    const engineSectionTop = document.querySelector(".config-section").getBoundingClientRect().top
    const windowHeight = window.innerHeight

    // When scrolling down past the initial position
    if (scrollY > initialConfigTop) {
      // Make the right column sticky
      stickyColumn.classList.add("sticky")

      // Make the vehicle image sticky and resize it
      vehicleImageContainer.classList.add("sticky")

      // Make specs panel scrollable when in sticky mode
      specsPanel.classList.add("sticky-compact")

      // Adjust the config section width
      document.querySelector(".vehicle-config").style.width = "65%"
    } else {
      // Reset everything when scrolling back up
      stickyColumn.classList.remove("sticky")
      vehicleImageContainer.classList.remove("sticky")
      specsPanel.classList.remove("sticky-compact")
      document.querySelector(".vehicle-config").style.width = ""
    }

    isScrolling = false
  }

  // Handle section title clicks
  document.querySelectorAll(".config-title").forEach((title) => {
    title.addEventListener("click", () => {
      const content = title.nextElementSibling
      title.classList.toggle("active")
      content.classList.toggle("active")
    })
  })

  // Open first section by default
  document.querySelector(".config-title").click()

  // Handle wheelbase selection
  const wheelbaseOptions = document.querySelectorAll('input[name="wheelbase"]')
  wheelbaseOptions.forEach((option) => {
    option.addEventListener("change", function () {
      const wheelbaseValue = this.value

      // Update vehicle image
      if (wheelbaseValue === "8x8") {
        vehicle8x8Image.classList.add("active-image")
        vehicle6x6Image.classList.remove("active-image")
      } else {
        vehicle8x8Image.classList.remove("active-image")
        vehicle6x6Image.classList.add("active-image")
      }

      // Update specs based on wheelbase
      specValues.forEach((spec) => {
        const specType = spec.getAttribute("data-spec")
        if (wheelbaseValue === "8x8") {
          spec.textContent = spec.getAttribute("data-value-8x8")
        } else {
          spec.textContent = spec.getAttribute("data-value-6x6")
        }
      })

      // Show/hide passenger options based on wheelbase
      const passengerOptions = document.querySelectorAll(".option-item[data-wheelbase]")
      passengerOptions.forEach((option) => {
        const allowedWheelbases = option.getAttribute("data-wheelbase").split(" ")
        if (allowedWheelbases.includes(wheelbaseValue)) {
          option.classList.remove("hidden")
        } else {
          option.classList.add("hidden")
          // Uncheck if it was selected but now hidden
          const radio = option.querySelector('input[type="radio"]')
          if (radio && radio.checked) {
            // Find first available option and select it
            const firstAvailable = document.querySelector(
              `.option-item[data-wheelbase*="${wheelbaseValue}"] input[type="radio"]`,
            )
            if (firstAvailable) {
              firstAvailable.checked = true
              firstAvailable.dispatchEvent(new Event("change"))
            }
          }
        }
      })

      // Update price calculation
      calculateTotalPrice()
    })
  })

  // Handle engine selection
  document.querySelectorAll(".engine-option").forEach((option) => {
    option.addEventListener("click", () => {
      document.querySelectorAll(".engine-option").forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")
      calculateTotalPrice()
    })
  })

  // Handle tires selection
  document.querySelectorAll(".tires-option").forEach((option) => {
    option.addEventListener("click", () => {
      document.querySelectorAll(".tires-option").forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")
      calculateTotalPrice()
    })
  })

  // Handle radio button options
  document.querySelectorAll('input[type="radio"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      const name = radio.getAttribute("name")
      document.querySelectorAll(`input[name="${name}"]`).forEach((r) => {
        const item = r.closest(".option-item")
        if (item) {
          item.classList.toggle("selected", r.checked)
        }
      })
      calculateTotalPrice()
    })
  })

  // Handle checkbox options
  document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const item = checkbox.closest(".option-item") || checkbox.closest(".kit-item")
      if (item) {
        item.classList.toggle("selected", checkbox.checked)
      }
      calculateTotalPrice()
    })
  })

  // Handle kit expansion buttons
  document.querySelectorAll(".expand-button").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.stopPropagation() // Prevent event bubbling

      const kitItem = button.closest(".kit-item")
      const components = kitItem.querySelector(".kit-components")

      // Toggle active state
      button.classList.toggle("active")
      components.classList.toggle("active")
    })
  })

  // Handle kit header clicks
  document.querySelectorAll(".kit-header").forEach((header) => {
    header.addEventListener("click", (e) => {
      // Ignore clicks on expand button
      if (e.target.closest(".expand-button") || e.target.closest("svg")) {
        return
      }

      const kitItem = header.closest(".kit-item")
      const checkbox = kitItem.querySelector('input[type="checkbox"]')

      // Toggle checkbox state
      checkbox.checked = !checkbox.checked
      checkbox.dispatchEvent(new Event("change"))
    })
  })

  // Calculate total price
  function calculateTotalPrice() {
    const basePrice = 1000000 // Base price of the vehicle
    let totalPrice = basePrice

    // Add selected engine price
    const selectedEngine = document.querySelector(".engine-option.selected")
    if (selectedEngine) {
      totalPrice += Number.parseInt(selectedEngine.getAttribute("data-price"))
    }

    // Add selected tires price
    const selectedTires = document.querySelector(".tires-option.selected")
    if (selectedTires) {
      totalPrice += Number.parseInt(selectedTires.getAttribute("data-price"))
    }

    // Add selected wheelbase adjustment (could be negative)
    const selectedWheelbase = document.querySelector('input[name="wheelbase"]:checked')
    if (selectedWheelbase) {
      totalPrice += Number.parseInt(selectedWheelbase.getAttribute("data-price"))
    }

    // Add selected radio options
    document.querySelectorAll('input[type="radio"]:checked').forEach((radio) => {
      if (radio.name !== "wheelbase") {
        // Skip wheelbase as it's already counted
        totalPrice += Number.parseInt(radio.getAttribute("data-price") || 0)
      }
    })

    // Add selected checkbox options
    document.querySelectorAll('input[type="checkbox"]:checked').forEach((checkbox) => {
      totalPrice += Number.parseInt(checkbox.getAttribute("data-price") || 0)
    })

    // Update price display
    document.querySelector(".total-price").textContent = new Intl.NumberFormat("ru-RU").format(totalPrice) + " ₽"
  }

  // Initial price calculation
  calculateTotalPrice()
})
document.addEventListener("DOMContentLoaded", () => {
  // Initialize configuration sections
  initConfigSections()

  // Initialize wheelbase selection
  initWheelbaseSelection()

  // Initialize engine and tires selection
  initEngineAndTiresSelection()

  // Initialize radio and checkbox options
  initRadioAndCheckboxOptions()

  // Initialize kit expansion
  initKitExpansion()

  // Initialize scroll behavior
  initScrollBehavior()

  // Calculate initial price
  calculateTotalPrice()

  // Open first section by default
  const firstSection = document.querySelector(".config-title")
  if (firstSection) {
    firstSection.click()
  }
})

// Initialize configuration sections
function initConfigSections() {
  const configTitles = document.querySelectorAll(".config-title")

  configTitles.forEach((title) => {
    title.addEventListener("click", () => {
      const content = title.nextElementSibling
      if (content && content.classList.contains("config-content")) {
        title.classList.toggle("active")
        content.classList.toggle("active")
      }
    })
  })
}

// Initialize wheelbase selection
function initWheelbaseSelection() {
  const wheelbaseRadios = document.querySelectorAll('input[name="wheelbase"]')

  wheelbaseRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      updateVehicleImage(this.value)
      updateSpecifications(this.value)
      updatePassengerOptions(this.value)
      calculateTotalPrice()
    })
  })
}

// Update vehicle image based on wheelbase selection
function updateVehicleImage(wheelbaseValue) {
  const vehicle8x8 = document.getElementById("vehicle-8x8")
  const vehicle6x6 = document.getElementById("vehicle-6x6")

  if (!vehicle8x8 || !vehicle6x6) return

  if (wheelbaseValue === "8x8") {
    vehicle8x8.classList.add("active-image")
    vehicle6x6.classList.remove("active-image")
  } else {
    vehicle8x8.classList.remove("active-image")
    vehicle6x6.classList.add("active-image")
  }
}

// Update specifications based on wheelbase selection
function updateSpecifications(wheelbaseValue) {
  const specValues = document.querySelectorAll(".spec-value")

  specValues.forEach((spec) => {
    const value8x8 = spec.getAttribute("data-value-8x8")
    const value6x6 = spec.getAttribute("data-value-6x6")

    if (wheelbaseValue === "8x8" && value8x8) {
      spec.textContent = value8x8
    } else if (wheelbaseValue === "6x6" && value6x6) {
      spec.textContent = value6x6
    }
  })
}

// Update passenger options based on wheelbase selection
function updatePassengerOptions(wheelbaseValue) {
  const passengerOptions = document.querySelectorAll(".option-item[data-wheelbase]")
  let firstAvailableChecked = false

  passengerOptions.forEach((option) => {
    const allowedWheelbases = option.getAttribute("data-wheelbase").split(" ")
    const radio = option.querySelector('input[type="radio"]')

    if (allowedWheelbases.includes(wheelbaseValue)) {
      option.classList.remove("hidden")

      // If this is the first available option and no other option is checked, check it
      if (
        !firstAvailableChecked &&
        radio &&
        !document.querySelector(`input[name="${radio.name}"]:checked:not(.hidden)`)
      ) {
        radio.checked = true
        radio.dispatchEvent(new Event("change"))
        firstAvailableChecked = true
      }
    } else {
      option.classList.add("hidden")

      // If this option was checked but is now hidden, uncheck it
      if (radio && radio.checked) {
        radio.checked = false
      }
    }
  })

  // Ensure at least one option is selected
  const passengerRadios = document.querySelectorAll('input[name="passengers"]')
  const anyChecked = Array.from(passengerRadios).some((radio) => radio.checked)

  if (!anyChecked && passengerRadios.length > 0) {
    // Find first visible option
    const firstVisible = document.querySelector(
      `.option-item[data-wheelbase*="${wheelbaseValue}"] input[name="passengers"]`,
    )
    if (firstVisible) {
      firstVisible.checked = true
      firstVisible.dispatchEvent(new Event("change"))
    }
  }
}

// Initialize engine and tires selection
function initEngineAndTiresSelection() {
  // Engine selection
  const engineOptions = document.querySelectorAll(".engine-option")
  engineOptions.forEach((option) => {
    option.addEventListener("click", () => {
      engineOptions.forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")
      calculateTotalPrice()
    })
  })

  // Tires selection
  const tiresOptions = document.querySelectorAll(".tires-option")
  tiresOptions.forEach((option) => {
    option.addEventListener("click", () => {
      tiresOptions.forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")
      calculateTotalPrice()
    })
  })
}

// Initialize radio and checkbox options
function initRadioAndCheckboxOptions() {
  // Radio buttons
  const radioButtons = document.querySelectorAll('input[type="radio"]')
  radioButtons.forEach((radio) => {
    radio.addEventListener("change", () => {
      const name = radio.getAttribute("name")
      document.querySelectorAll(`input[name="${name}"]`).forEach((r) => {
        const item = r.closest(".option-item")
        if (item) {
          item.classList.toggle("selected", r.checked)
        }
      })
      calculateTotalPrice()
    })
  })

  // Checkboxes
  const checkboxes = document.querySelectorAll('input[type="checkbox"]')
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const item = checkbox.closest(".option-item") || checkbox.closest(".kit-item")
      if (item) {
        item.classList.toggle("selected", checkbox.checked)
      }
      calculateTotalPrice()
    })
  })
}

// Initialize kit expansion
function initKitExpansion() {
  // Kit expansion buttons
  const expandButtons = document.querySelectorAll(".expand-button")
  expandButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.stopPropagation()

      const kitItem = button.closest(".kit-item")
      if (!kitItem) return

      const components = kitItem.querySelector(".kit-components")
      if (!components) return

      button.classList.toggle("active")
      components.classList.toggle("active")
    })
  })

  // Kit header clicks
  const kitHeaders = document.querySelectorAll(".kit-header")
  kitHeaders.forEach((header) => {
    header.addEventListener("click", (e) => {
      if (e.target.closest(".expand-button") || e.target.closest("svg")) {
        return
      }

      const kitItem = header.closest(".kit-item")
      if (!kitItem) return

      const checkbox = kitItem.querySelector('input[type="checkbox"]')
      if (!checkbox) return

      checkbox.checked = !checkbox.checked
      checkbox.dispatchEvent(new Event("change"))
    })
  })
}

// Initialize scroll behavior
function initScrollBehavior() {
  const vehicleImageContainer = document.getElementById("vehicle-image-container")
  const stickyColumn = document.getElementById("sticky-column")
  const specsPanel = document.getElementById("specs-panel")

  if (!vehicleImageContainer || !stickyColumn || !specsPanel) return

  let initialConfigTop = vehicleImageContainer.getBoundingClientRect().top + window.scrollY
  let isScrolling = false
  let scrollTimeout

  // Update initial values on window resize
  window.addEventListener("resize", () => {
    initialConfigTop = vehicleImageContainer.getBoundingClientRect().top + window.scrollY
  })

  // Handle scroll event
  window.addEventListener("scroll", () => {
    if (!isScrolling) {
      isScrolling = true
      requestAnimationFrame(handleScroll)
    }

    clearTimeout(scrollTimeout)
    scrollTimeout = setTimeout(() => {
      isScrolling = false
    }, 100)
  })

  function handleScroll() {
    const scrollY = window.scrollY

    if (scrollY > initialConfigTop) {
      // Make elements sticky
      stickyColumn.classList.add("sticky")
      vehicleImageContainer.classList.add("sticky")
      specsPanel.classList.add("sticky-compact")
      document.querySelector(".vehicle-config").style.width = "65%"
    } else {
      // Reset elements
      stickyColumn.classList.remove("sticky")
      vehicleImageContainer.classList.remove("sticky")
      specsPanel.classList.remove("sticky-compact")
      document.querySelector(".vehicle-config").style.width = ""
    }

    isScrolling = false
  }
}

// Calculate total price
function calculateTotalPrice() {
  const basePrice = 1000000 // Base price of the vehicle
  let totalPrice = basePrice

  try {
    // Add selected engine price
    const selectedEngine = document.querySelector(".engine-option.selected")
    if (selectedEngine) {
      const enginePrice = Number.parseInt(selectedEngine.getAttribute("data-price") || 0)
      if (!isNaN(enginePrice)) {
        totalPrice += enginePrice
      }
    }

    // Add selected tires price
    const selectedTires = document.querySelector(".tires-option.selected")
    if (selectedTires) {
      const tiresPrice = Number.parseInt(selectedTires.getAttribute("data-price") || 0)
      if (!isNaN(tiresPrice)) {
        totalPrice += tiresPrice
      }
    }

    // Add selected wheelbase adjustment
    const selectedWheelbase = document.querySelector('input[name="wheelbase"]:checked')
    if (selectedWheelbase) {
      const wheelbasePrice = Number.parseInt(selectedWheelbase.getAttribute("data-price") || 0)
      if (!isNaN(wheelbasePrice)) {
        totalPrice += wheelbasePrice
      }
    }

    // Add selected radio options
    document.querySelectorAll('input[type="radio"]:checked').forEach((radio) => {
      if (radio.name !== "wheelbase") {
        // Skip wheelbase as it's already counted
        const radioPrice = Number.parseInt(radio.getAttribute("data-price") || 0)
        if (!isNaN(radioPrice)) {
          totalPrice += radioPrice
        }
      }
    })

    // Add selected checkbox options
    document.querySelectorAll('input[type="checkbox"]:checked').forEach((checkbox) => {
      const checkboxPrice = Number.parseInt(checkbox.getAttribute("data-price") || 0)
      if (!isNaN(checkboxPrice)) {
        totalPrice += checkboxPrice
      }
    })

    // Update price display
    const totalPriceElement = document.querySelector(".total-price")
    if (totalPriceElement) {
      totalPriceElement.textContent = new Intl.NumberFormat("ru-RU").format(totalPrice) + " ₽"
    }
  } catch (error) {
    console.error("Error calculating price:", error)
  }
}

