document.addEventListener("DOMContentLoaded", () => {
  // Base price of the vehicle
  const basePrice = 1000000;

  // Open first section by default
  document.querySelector(".config-title").click();

  // Handle section title clicks
  document.querySelectorAll(".config-title").forEach((title) => {
    title.addEventListener("click", () => {
      const content = title.nextElementSibling;
      title.classList.toggle("active");
      content.classList.toggle("active");
    });
  });

  // Handle option items with radio buttons
  document
    .querySelectorAll('.option-item[data-type="radio"]')
    .forEach((item) => {
      const radio = item.querySelector('input[type="radio"]');
      if (radio) {
        item.addEventListener("click", (e) => {
          if (!e.target.closest(".custom-radio")) {
            radio.checked = true;
            radio.dispatchEvent(new Event("change"));
          }
        });
      }
    });

  // Handle radio button changes
  document.querySelectorAll('input[type="radio"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      const name = radio.getAttribute("name");
      document.querySelectorAll(`input[name="${name}"]`).forEach((r) => {
        const item = r.closest(".option-item");
        if (item) {
          item.classList.toggle("selected", r.checked);
        }
      });

      // Update price when radio selection changes
      calculateTotalPrice();
    });
  });

  // Handle option items with checkboxes
  document.querySelectorAll(".option-item[data-group]").forEach((item) => {
    if (!item.getAttribute("data-type")) {
      item.addEventListener("click", (e) => {
        if (!e.target.closest(".custom-checkbox")) {
          const checkbox = item.querySelector('input[type="checkbox"]');
          if (checkbox) {
            checkbox.checked = !checkbox.checked;
            checkbox.dispatchEvent(new Event("change"));
          }
        }
      });
    }
  });

  // Handle checkbox changes
  document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const item =
        checkbox.closest(".option-item") || checkbox.closest(".kit-item");
      if (item) {
        item.classList.toggle("selected", checkbox.checked);
      }

      // Update price when checkbox selection changes
      calculateTotalPrice();
    });
  });

  // Engine selection
  document.querySelectorAll(".engine-option").forEach((option) => {
    option.addEventListener("click", () => {
      document
        .querySelectorAll(".engine-option")
        .forEach((opt) => opt.classList.remove("selected"));
      option.classList.add("selected");

      // Update price when engine selection changes
      calculateTotalPrice();
    });
  });

  // Tires selection
  document.querySelectorAll(".tires-option").forEach((option) => {
    option.addEventListener("click", () => {
      document
        .querySelectorAll(".tires-option")
        .forEach((opt) => opt.classList.remove("selected"));
      option.classList.add("selected");

      // Update price when tires selection changes
      calculateTotalPrice();
    });
  });

  // Wheelbase selection (new feature)
  document.querySelectorAll(".wheelbase-option").forEach((option) => {
    option.addEventListener("change", () => {
      // Обновить изображение вездехода в зависимости от выбранной колесной базы
      const wheelbaseType = option.value;
      const vehicleImg = document.getElementById("vehicle-img");

      if (wheelbaseType === "8x8") {
        vehicleImg.src =
          "../../img/грузовые вездеходы/К-8 Грузовой 4х2,5/K8gr07.webp";
        document.getElementById("wheelbase-spec").textContent =
          "8×8, постоянный полный привод, две передние оси управляемые";

        // Показать все пассажирские места, кроме 8 и 12
        showAllPassengerOptions();
      } else if (wheelbaseType === "6x6") {
        vehicleImg.src = "../../img/Фото вездехода 6х6.jpg";
        document.getElementById("wheelbase-spec").textContent =
          "6×6, постоянный полный привод, две передние оси управляемые";

        // Ограничить пассажирские места только 8 и 12
        limitPassengerOptions();
      }

      // Добавить анимацию перехода
      vehicleImg.classList.add("image-transition");
      setTimeout(() => {
        vehicleImg.classList.remove("image-transition");
      }, 500);

      // Обновить цену при изменении колесной базы
      calculateTotalPrice();
    });
  });

  // Function to show all passenger options
  function showAllPassengerOptions() {
    document.querySelectorAll(".passenger-option").forEach((option) => {
      const item = option.closest(".option-item");
      const value = Number.parseInt(option.value);

      // Скрыть опции 8 и 12 мест для 8x8
      if (value === 8 || value === 12) {
        item.style.display = "none";
      } else {
        item.style.display = "flex";
      }

      // Если скрытая опция была выбрана, выбрать опцию 18 мест
      if ((value === 8 || value === 12) && option.checked) {
        const eighteenPassengerOption = document.querySelector(
          'input[name="passengers"][value="18"]'
        );
        if (eighteenPassengerOption) {
          eighteenPassengerOption.checked = true;
          eighteenPassengerOption.dispatchEvent(new Event("change"));
        }
      }
    });
  }

  // Function to limit passenger options for 6x6 configuration
  function limitPassengerOptions() {
    document.querySelectorAll(".passenger-option").forEach((option) => {
      const item = option.closest(".option-item");
      const value = Number.parseInt(option.value);

      // Только показать опции 8 и 12 мест для 6x6
      if (value === 8 || value === 12) {
        item.style.display = "flex";
      } else {
        item.style.display = "none";

        // Если скрытая опция была выбрана, выбрать опцию 8 мест
        if (option.checked) {
          const eightPassengerOption = document.querySelector(
            'input[name="passengers"][value="8"]'
          );
          if (eightPassengerOption) {
            eightPassengerOption.checked = true;
            eightPassengerOption.dispatchEvent(new Event("change"));
          }
        }
      }
    });
  }

  // Handle kit expansion
  document.querySelectorAll(".expand-button").forEach((button) => {
    button.addEventListener("click", (e) => {
      e.stopPropagation(); // Prevent event from bubbling up

      button.classList.toggle("active");
      const kitItem = button.closest(".kit-item");
      const components = kitItem.querySelector(".kit-components");
      components.classList.toggle("active");
    });
  });

  // Handle kit header clicks
  document.querySelectorAll(".kit-header").forEach((header) => {
    header.addEventListener("click", (e) => {
      // Ignore clicks on the expand button
      if (e.target.closest(".expand-button") || e.target.closest("svg")) {
        return;
      }

      const kitItem = header.closest(".kit-item");
      const checkbox = kitItem.querySelector('input[type="checkbox"]');

      // Toggle checkbox state
      checkbox.checked = !checkbox.checked;
      checkbox.dispatchEvent(new Event("change"));
    });
  });

  // Calculate total price function
  function calculateTotalPrice() {
    let totalPrice = basePrice;

    // Добавить цену колесной базы (может быть отрицательной для 6x6)
    const selectedWheelbase = document.querySelector(
      'input[name="wheelbase"]:checked'
    );
    if (selectedWheelbase) {
      totalPrice += Number.parseInt(
        selectedWheelbase.getAttribute("data-price")
      );
    }

    // Добавить цену двигателя
    const selectedEngine = document.querySelector(".engine-option.selected");
    if (selectedEngine) {
      totalPrice += Number.parseInt(selectedEngine.getAttribute("data-price"));
    }

    // Добавить цену шин
    const selectedTires = document.querySelector(".tires-option.selected");
    if (selectedTires) {
      totalPrice += Number.parseInt(selectedTires.getAttribute("data-price"));
    }

    // Добавить цену пассажирских мест
    const selectedPassenger = document.querySelector(
      'input[name="passengers"]:checked'
    );
    if (selectedPassenger) {
      totalPrice += Number.parseInt(
        selectedPassenger.getAttribute("data-price")
      );
    }

    // Добавить цены всех отмеченных чекбоксов
    document
      .querySelectorAll('input[type="checkbox"]:checked')
      .forEach((checkbox) => {
        totalPrice += Number.parseInt(checkbox.getAttribute("data-price"));
      });

    // Форматировать цену с пробелами в качестве разделителей тысяч
    const formattedPrice = totalPrice
      .toString()
      .replace(/\B(?=(\d{3})+(?!\d))/g, " ");

    // Обновить отображение цены
    document.getElementById("total-price").textContent = formattedPrice + " ₽";
  }

  // Initialize price calculation
  calculateTotalPrice();

  // Scroll animation for keeping model and specs visible
  window.addEventListener("scroll", handleScroll);

  function handleScroll() {
    const scrollY = window.scrollY;
    const vehicleImage = document.getElementById("vehicle-image");
    const specsSidebar = document.getElementById("specs-sidebar");

    // Определим порог прокрутки, чтобы изменить макет
    const scrollThreshold = 50;

    console.log("Scroll Y:", scrollY); // Логирование для отладки

    if (scrollY > scrollThreshold) {
      // Добавляем класс .scrolled к body для анимации
      document.body.classList.add("scrolled");
    } else {
      // Убираем класс, если прокрутка меньше порога
      document.body.classList.remove("scrolled");
    }

    // Дополнительная отладка для проверки размеров элементов
    console.log(
      "Vehicle Image position:",
      vehicleImage ? vehicleImage.getBoundingClientRect() : "Not found"
    );
    console.log(
      "Specs Sidebar position:",
      specsSidebar ? specsSidebar.getBoundingClientRect() : "Not found"
    );
  }

  // Инициализировать первую секцию как открытую
  const firstSection = document.querySelector(".config-section");
  if (firstSection) {
    const firstTitle = firstSection.querySelector(".config-title");
    const firstContent = firstSection.querySelector(".config-content");
    if (firstTitle && firstContent) {
      firstTitle.classList.add("active");
      firstContent.classList.add("active");
    }
  }

  // Скрыть опции 8 и 12 мест при загрузке страницы, так как по умолчанию выбран 8x8
  showAllPassengerOptions();
});
