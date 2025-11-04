// Table search functionality for shadcn/ui data tables

document.addEventListener('DOMContentLoaded', function() {
    // Get all search inputs
    const searchInputs = document.querySelectorAll('[id$="-search"]');
    
    searchInputs.forEach(input => {
        if (!input) return;
        
        // Get the table associated with this search input
        const table = input.closest('.rounded-lg').querySelector('table');
        if (!table) return;
        
        const tbody = table.querySelector('tbody');
        if (!tbody) return;
        
        // Add input event listener for real-time search
        input.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const rows = tbody.querySelectorAll('tr');
            
            rows.forEach(row => {
                // Skip empty state rows
                if (row.querySelector('td[colspan]')) {
                    return;
                }
                
                const text = row.textContent.toLowerCase();
                
                if (text.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
            
            // Show "no results" message if all rows are hidden
            const visibleRows = Array.from(rows).filter(row => 
                row.style.display !== 'none' && !row.querySelector('td[colspan]')
            );
            
            if (visibleRows.length === 0 && searchTerm) {
                // Check if no results row already exists
                let noResultsRow = tbody.querySelector('.no-results-row');
                if (!noResultsRow) {
                    noResultsRow = document.createElement('tr');
                    noResultsRow.className = 'no-results-row';
                    const colspan = rows[0]?.querySelectorAll('td').length || 8;
                    noResultsRow.innerHTML = `
                        <td colspan="${colspan}" class="px-4 py-8 text-center text-gray-400">
                            <p class="text-sm">No results found for "${searchTerm}"</p>
                        </td>
                    `;
                    tbody.appendChild(noResultsRow);
                }
                noResultsRow.style.display = '';
            } else {
                // Remove no results row if it exists
                const noResultsRow = tbody.querySelector('.no-results-row');
                if (noResultsRow) {
                    noResultsRow.style.display = 'none';
                }
            }
        });
    });
});
