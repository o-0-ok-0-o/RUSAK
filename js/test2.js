document.addEventListener("DOMContentLoaded", () => {
  // Base price of the vehicle
  const basePrice = 1000000

  // Open first section by default
  document.querySelector(".config-title").click()

  // Handle section title clicks
  document.querySelectorAll(".config-title").forEach((title) => {
    title.addEventListener("click", () => {
      const content = title.nextElementSibling
      title.classList.toggle("active")
      content.classList.toggle("active")
    })
  })

  // Handle option items with radio buttons
  document.querySelectorAll('.option-item[data-type="radio"]').forEach((item) => {
    const radio = item.querySelector('input[type="radio"]')
    if (radio) {
      item.addEventListener("click", (e) => {
        if (!e.target.closest(".custom-radio")) {
          radio.checked = true
          radio.dispatchEvent(new Event("change"))
        }
      })
    }
  })

  // Handle radio button changes
  document.querySelectorAll('input[type="radio"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      const name = radio.getAttribute("name")
      document.querySelectorAll(`input[name="${name}"]`).forEach((r) => {
        const item = r.closest(".option-item")
        if (item) {
          item.classList.toggle("selected", r.checked)
        }
      })

      // Update price when radio selection changes
      calculateTotalPrice()
    })
  })

  // Handle option items with checkboxes
  document.querySelectorAll(".option-item[data-group]").forEach((item) => {
    if (!item.getAttribute("data-type")) {
      item.addEventListener("click", (e) => {
        if (!e.target.closest(".custom-checkbox")) {
          const checkbox = item.querySelector('input[type="checkbox"]')
          if (checkbox) {
            checkbox.checked = !checkbox.checked
            checkbox.dispatchEvent(new Event("change"))
          }
        }
      })
    }
  })

  // Handle checkbox changes
  document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const item = checkbox.closest(".option-item") || checkbox.closest(".kit-item")
      if (item) {
        item.classList.toggle("selected", checkbox.checked)
      }

      // Update price when checkbox selection changes
      calculateTotalPrice()
    })
  })

  // Engine selection
  document.querySelectorAll(".engine-option").forEach((option) => {
    option.addEventListener("click", () => {
      document.querySelectorAll(".engine-option").forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")

      // Update price when engine selection changes
      calculateTotalPrice()
    })
  })

  // Tires selection
  document.querySelectorAll(".tires-option").forEach((option) => {
    option.addEventListener("click", () => {
      document.querySelectorAll(".tires-option").forEach((opt) => opt.classList.remove("selected"))
      option.classList.add("selected")

      // Update price when tires selection changes
      calculateTotalPrice()
    })
  })

  // Wheelbase selection (new feature)
  document.querySelectorAll(".wheelbase-option").forEach((option) => {
    option.addEventListener("change", () => {
      // Update vehicle image based on wheelbase selection
      const wheelbaseType = option.value
      const vehicleImg = document.getElementById("vehicle-img")
      const vehicleImgFixed = document.getElementById("vehicle-img-fixed")

      if (wheelbaseType === "8x8") {
        vehicleImg.src = "../../img/грузовые вездеходы/К-8 Грузовой 4х2,5/K8gr07.webp"
        vehicleImgFixed.src = "../../img/грузовые вездеходы/К-8 Грузовой 4х2,5/K8gr07.webp"
        document.getElementById("wheelbase-spec").textContent =
          "8×8, постоянный полный привод, две передние оси управляемые"

        // Show all passenger options
        showAllPassengerOptions()
      } else if (wheelbaseType === "6x6") {
        vehicleImg.src = "../../img/Фото вездехода 6х6.jpg"
        vehicleImgFixed.src = "../../img/Фото вездехода 6х6.jpg"
        document.getElementById("wheelbase-spec").textContent =
          "6×6, постоянный полный привод, две передние оси управляемые"

        // Limit passenger options for 6x6
        limitPassengerOptions()
      }

      // Add transition animation
      vehicleImg.classList.add("image-transition")
      vehicleImgFixed.classList.add("image-transition")
      setTimeout(() => {
        vehicleImg.classList.remove("image-transition")
        vehicleImgFixed.classList.remove("image-transition")
      }, 500)

      // Update price when wheelbase selection changes
      calculateTotalPrice()
    })
  })

  // Function to show all passenger options
  function showAllPassengerOptions() {
    document.querySelectorAll(".passenger-option").forEach((option) => {
      const item = option.closest(".option-item")
      item.style.display = "flex"
    })
  }

  // Function to limit passenger options for 6x6 configuration
  function limitPassengerOptions() {
    document.querySelectorAll(".passenger-option").forEach((option) => {
      const item = option.closest(".option-item")
      const value = Number.parseInt(option.value)

      // Only show 8 and 12 passenger options for 6x6
      if (value === 8 || value === 12) {
        item.style.display = "flex"
      } else {
        item.style.display = "none"

        // If a hidden option was selected, select the 8-passenger option
        if (option.checked) {
          const eightPassengerOption = document.querySelector('input[name="passengers"][value="8"]')
          if (eightPassengerOption) {
            eightPassengerOption.checked = true
            eightPassengerOption.dispatchEvent(new Event("change"))
          }
        }
      }
    })
  }

  // Handle kit expansion
  document.querySelectorAll(".expand-button").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.stopPropagation() // Prevent event from bubbling up

      button.classList.toggle("active")
      const kitItem = button.closest(".kit-item")
      const components = kitItem.querySelector(".kit-components")
      components.classList.toggle("active")
    })
  })

  // Handle kit header clicks
  document.querySelectorAll(".kit-header").forEach((header) => {
    header.addEventListener("click", (e) => {
      // Ignore clicks on the expand button
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

  // Calculate total price function
  function calculateTotalPrice() {
    let totalPrice = basePrice

    // Add engine price
    const selectedEngine = document.querySelector(".engine-option.selected")
    if (selectedEngine) {
      totalPrice += Number.parseInt(selectedEngine.getAttribute("data-price"))
    }

    // Add tires price
    const selectedTires = document.querySelector(".tires-option.selected")
    if (selectedTires) {
      totalPrice += Number.parseInt(selectedTires.getAttribute("data-price"))
    }

    // Add passenger option price
    const selectedPassenger = document.querySelector('input[name="passengers"]:checked')
    if (selectedPassenger) {
      totalPrice += Number.parseInt(selectedPassenger.getAttribute("data-price"))
    }

    // Add all checked checkboxes prices
    document.querySelectorAll('input[type="checkbox"]:checked').forEach((checkbox) => {
      totalPrice += Number.parseInt(checkbox.getAttribute("data-price"))
    })

    // Format the price with spaces as thousand separators
    const formattedPrice = totalPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")

    // Update the price display
    document.getElementById("total-price").textContent = formattedPrice + " ₽"
  }

  // Initialize price calculation
  calculateTotalPrice()

  // Scroll animation for keeping model and specs visible
  window.addEventListener("scroll", handleScroll)

  function handleScroll() {
    const scrollY = window.scrollY
    const vehicleImageContainer = document.getElementById("vehicle-image-container")
    const vehicleImgFixed = document.getElementById("vehicle-img-fixed")
    const specsSidebar = document.getElementById("specs-sidebar")

    // Define the scroll threshold where the layout changes
    const scrollThreshold = 100

    if (scrollY > scrollThreshold) {
      // Add scrolled class to body for CSS transitions
      document.body.classList.add("scrolled")

      // Ensure the fixed image has the same source as the main image
      const mainImg = document.getElementById("vehicle-img")
      if (mainImg && vehicleImgFixed) {
        vehicleImgFixed.src = mainImg.src
      }
    } else {
      // Remove scrolled class when scrolling back up
      document.body.classList.remove("scrolled")
    }
  }

  // Initialize the first section as open
  const firstSection = document.querySelector(".config-section")
  if (firstSection) {
    const firstTitle = firstSection.querySelector(".config-title")
    const firstContent = firstSection.querySelector(".config-content")
    if (firstTitle && firstContent) {
      firstTitle.classList.add("active")
      firstContent.classList.add("active")
    }
  }
})

