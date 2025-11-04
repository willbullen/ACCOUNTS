// Dropdown menu functionality
document.addEventListener('DOMContentLoaded', function() {
    // Handle all dropdown toggles
    document.querySelectorAll('[data-dropdown-toggle]').forEach(function(toggle) {
        const dropdownId = toggle.getAttribute('data-dropdown-toggle');
        const dropdown = document.getElementById(dropdownId);
        
        if (dropdown) {
            toggle.addEventListener('click', function(e) {
                e.stopPropagation();
                
                // Close other dropdowns
                document.querySelectorAll('[data-dropdown]').forEach(function(otherDropdown) {
                    if (otherDropdown !== dropdown) {
                        otherDropdown.classList.add('hidden');
                    }
                });
                
                // Toggle current dropdown
                dropdown.classList.toggle('hidden');
            });
        }
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function() {
        document.querySelectorAll('[data-dropdown]').forEach(function(dropdown) {
            dropdown.classList.add('hidden');
        });
    });
    
    // Prevent dropdown from closing when clicking inside
    document.querySelectorAll('[data-dropdown]').forEach(function(dropdown) {
        dropdown.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    });
});
