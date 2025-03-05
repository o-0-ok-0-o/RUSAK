document.addEventListener('DOMContentLoaded', function() {
    // Base price
    const BASE_PRICE = 1000000;
    let totalPrice = BASE_PRICE;
    
    // Initialize selected options
    const selectedOptions = {
        engine: 'cummins', // Default engine
        tires: 'rusak',    // Default tires
        passengers: '24',  // Default passenger option
        cabin: [],         // Selected cabin options
        chassis: [],       // Selected chassis options
        service: [],       // Selected service options
        kits: []           // Selected kit options
    };
    
    // Format price in rubles
    function formatPrice(price) {
        return new Intl.NumberFormat('ru-RU', {
            style: 'currency',
            currency: 'RUB',
            maximumFractionDigits: 0
        }).format(price).replace('₽', '₽');
    }
    
    // Update total price based on selected options
    function updateTotalPrice() {
        let price = BASE_PRICE;
        
        // Add engine price
        const engineElement = document.querySelector(`.engine-option.selected`);
        if (engineElement) {
            price += parseInt(engineElement.dataset.price);
        }
        
        // Add tire price
        const tireElement = document.querySelector(`.tires-option.selected`);
        if (tireElement) {
            price += parseInt(tireElement.dataset.price);
        }
        
        // Add passenger option price
        const passengerInput = document.querySelector(`input[name="passengers"]:checked`);
        if (passengerInput) {
            price += parseInt(passengerInput.dataset.price);
        }
        
        // Add cabin options prices
        document.querySelectorAll(`input[data-group="cabin"]:checked`).forEach(input => {
            price += parseInt(input.dataset.price);
        });
        
        // Add chassis options prices
        document.querySelectorAll(`input[data-group="chassis"]:checked`).forEach(input => {
            price += parseInt(input.dataset.price);
        });
        
        // Add service options prices
        document.querySelectorAll(`input[data-group="service"]:checked`).forEach(input => {
            price += parseInt(input.dataset.price);
        });
        
        // Add kit prices
        document.querySelectorAll(`.kit-item input:checked`).forEach(input => {
            price += parseInt(input.dataset.price);
        });
        
        // Update the displayed price
        totalPrice = price;
        document.querySelector('.total-price').textContent = formatPrice(price);
        
        // Debug - log the current price calculation
        console.log('Updated price:', price);
    }
    
    // Toggle section expansion
    document.querySelectorAll('.config-title').forEach(title => {
        title.addEventListener('click', () => {
            title.classList.toggle('active');
            const content = title.nextElementSibling;
            content.classList.toggle('active');
        });
    });
    
    // Engine selection
    document.querySelectorAll('.engine-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.engine-option').forEach(opt => 
                opt.classList.remove('selected'));
            option.classList.add('selected');
            selectedOptions.engine = option.dataset.id;
            updateTotalPrice();
        });
    });
    
    // Tire selection
    document.querySelectorAll('.tires-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.tires-option').forEach(opt => 
                opt.classList.remove('selected'));
            option.classList.add('selected');
            selectedOptions.tires = option.dataset.id;
            updateTotalPrice();
        });
    });
    
    // Radio button options (passengers)
    document.querySelectorAll('input[type="radio"][name="passengers"]').forEach(radio => {
        radio.addEventListener('change', () => {
            // Update selected state for the parent option item
            document.querySelectorAll('.option-item[data-group="passengers"]').forEach(item => {
                item.classList.remove('selected');
            });
            radio.closest('.option-item').classList.add('selected');
            
            selectedOptions.passengers = radio.value;
            updateTotalPrice();
        });
        
        // Make the entire option item clickable
        const optionItem = radio.closest('.option-item');
        if (optionItem) {
            optionItem.addEventListener('click', (e) => {
                if (!e.target.closest('.custom-radio')) {
                    radio.checked = true;
                    
                    // Trigger the change event
                    const changeEvent = new Event('change');
                    radio.dispatchEvent(changeEvent);
                }
            });
        }
    });
    
    // Checkbox options (cabin, chassis, service)
    document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
        // Initial setup of checkbox state in the data model
        if (checkbox.checked) {
            const group = checkbox.dataset.group;
            if (group && selectedOptions[group]) {
                selectedOptions[group].push(checkbox.id);
            } else if (checkbox.closest('.kit-item')) {
                const kitId = checkbox.closest('.kit-item').dataset.kitId;
                selectedOptions.kits.push(kitId);
            }
        }
        
        checkbox.addEventListener('change', () => {
            console.log('Checkbox changed:', checkbox.id, 'Checked:', checkbox.checked);
            
            // Handle different types of checkbox containers
            const kitItem = checkbox.closest('.kit-item');
            const optionItem = checkbox.closest('.option-item');
            
            const group = checkbox.dataset.group;
            
            // Update UI state based on checkbox container type
            if (kitItem) {
                kitItem.classList.toggle('selected', checkbox.checked);
                
                // Update kits array
                const kitId = kitItem.dataset.kitId;
                if (checkbox.checked) {
                    if (!selectedOptions.kits.includes(kitId)) {
                        selectedOptions.kits.push(kitId);
                    }
                } else {
                    selectedOptions.kits = selectedOptions.kits.filter(id => id !== kitId);
                }
            } else if (optionItem) {
                optionItem.classList.toggle('selected', checkbox.checked);
                
                // Update the appropriate group array
                if (group && selectedOptions[group]) {
                    if (checkbox.checked) {
                        if (!selectedOptions[group].includes(checkbox.id)) {
                            selectedOptions[group].push(checkbox.id);
                        }
                    } else {
                        selectedOptions[group] = selectedOptions[group].filter(id => id !== checkbox.id);
                    }
                }
            }
            
            // Log the current state to debug
            console.log('Updated selectedOptions:', JSON.stringify(selectedOptions));
            
            // Update the price based on the new selection
            updateTotalPrice();
        });
    });
    
    // Make checkbox label click work properly
    document.querySelectorAll('.custom-checkbox').forEach(checkboxLabel => {
        checkboxLabel.addEventListener('click', (e) => {
            const checkbox = checkboxLabel.querySelector('input[type="checkbox"]');
            if (checkbox) {
                // Let the default behavior handle the checkbox toggle
                // but make sure the change event is properly dispatched
                setTimeout(() => {
                    const changeEvent = new Event('change');
                    checkbox.dispatchEvent(changeEvent);
                }, 10);
            }
        });
    });
    
    // Make option items clickable for checkboxes
    document.querySelectorAll('.option-item').forEach(item => {
        const checkbox = item.querySelector('input[type="checkbox"]');
        if (checkbox) {
            item.addEventListener('click', (e) => {
                // Prevent clicking on the checkbox itself from triggering this
                if (!e.target.closest('.custom-checkbox') && !e.target.matches('input[type="checkbox"]')) {
                    checkbox.checked = !checkbox.checked;
                    
                    // Trigger the change event
                    const changeEvent = new Event('change');
                    checkbox.dispatchEvent(changeEvent);
                }
            });
        }
    });
    
    // Kit header click handler
    document.querySelectorAll('.kit-header').forEach(header => {
        header.addEventListener('click', (e) => {
            // Ignore clicks on the checkbox itself or the expand button
            if (e.target.closest('.custom-checkbox') || 
                e.target.matches('input[type="checkbox"]') || 
                e.target.closest('.expand-button') || 
                e.target.closest('svg')) {
                return;
            }
            
            const kitItem = header.closest('.kit-item');
            const checkbox = kitItem.querySelector('input[type="checkbox"]');
            
            // Toggle checkbox state
            checkbox.checked = !checkbox.checked;
            
            // Update kit item selected state
            kitItem.classList.toggle('selected', checkbox.checked);
            
            // Trigger change event
            const changeEvent = new Event('change');
            checkbox.dispatchEvent(changeEvent);
        });
    });
    
    // Kit expand buttons
    document.querySelectorAll('.kit-header .expand-button').forEach(button => {
        button.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent event bubbling
            
            button.classList.toggle('active');
            const kitItem = button.closest('.kit-item');
            const components = kitItem.querySelector('.kit-components');
            
            components.classList.toggle('active');
        });
    });
    
    // Initialize the configurator
    function initConfigurator() {
        // Open the first section by default
        const firstSection = document.querySelector('.config-title');
        if (firstSection) {
            firstSection.classList.add('active');
            firstSection.nextElementSibling.classList.add('active');
        }
        
        // Set initial selected states based on checked inputs
        document.querySelectorAll('input[type="radio"]:checked').forEach(radio => {
            const optionItem = radio.closest('.option-item');
            if (optionItem) {
                optionItem.classList.add('selected');
            }
        });
        
        document.querySelectorAll('input[type="checkbox"]:checked').forEach(checkbox => {
            const kitItem = checkbox.closest('.kit-item');
            const optionItem = checkbox.closest('.option-item');
            
            if (kitItem) {
                kitItem.classList.add('selected');
            } else if (optionItem) {
                optionItem.classList.add('selected');
            }
        });
        
        // Calculate initial price
        updateTotalPrice();
    }
    
    // Initialize the configurator when the page loads
    initConfigurator();
    
    // Get quote button
    document.querySelector('.get-quote-btn').addEventListener('click', () => {
        alert('Ваш запрос на коммерческое предложение отправлен!');
    });
});