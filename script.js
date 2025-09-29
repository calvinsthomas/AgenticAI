document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('waitlist-form');
    const emailInput = document.getElementById('email');
    const modal = document.getElementById('success-modal');
    const closeModal = document.getElementById('close-modal');
    
    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const email = emailInput.value.trim();
        
        // Validate email
        if (!email) {
            showError('Please enter your email address.');
            return;
        }
        
        if (!emailRegex.test(email)) {
            showError('Please enter a valid email address.');
            return;
        }
        
        // Check for duplicate emails (simple localStorage check)
        if (isEmailAlreadyRegistered(email)) {
            showError('This email is already registered on the waitlist.');
            return;
        }
        
        // Submit to waitlist
        addToWaitlist(email);
        showSuccessModal();
        form.reset();
    });
    
    // Close modal functionality
    closeModal.addEventListener('click', function() {
        hideSuccessModal();
    });
    
    // Close modal when clicking outside
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            hideSuccessModal();
        }
    });
    
    // Close modal with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            hideSuccessModal();
        }
    });
    
    function showError(message) {
        // Create or update error message
        let errorDiv = document.querySelector('.error-message');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.style.cssText = `
                color: #ef4444;
                background: #fef2f2;
                padding: 0.75rem 1rem;
                border-radius: 0.5rem;
                margin-top: 1rem;
                border: 1px solid #fecaca;
                text-align: center;
                font-size: 0.9rem;
            `;
            form.appendChild(errorDiv);
        }
        errorDiv.textContent = message;
        
        // Remove error after 5 seconds
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
        }, 5000);
        
        // Focus back on email input
        emailInput.focus();
    }
    
    function addToWaitlist(email) {
        // Get existing waitlist from localStorage
        let waitlist = JSON.parse(localStorage.getItem('waitlist') || '[]');
        
        // Add new entry
        const entry = {
            email: email,
            timestamp: new Date().toISOString(),
            id: Date.now().toString(36) + Math.random().toString(36).substr(2)
        };
        
        waitlist.push(entry);
        
        // Save back to localStorage
        localStorage.setItem('waitlist', JSON.stringify(waitlist));
        
        // Log for debugging (remove in production)
        console.log('Added to waitlist:', entry);
        console.log('Total waitlist entries:', waitlist.length);
    }
    
    function isEmailAlreadyRegistered(email) {
        const waitlist = JSON.parse(localStorage.getItem('waitlist') || '[]');
        return waitlist.some(entry => entry.email.toLowerCase() === email.toLowerCase());
    }
    
    function showSuccessModal() {
        modal.style.display = 'block';
        // Prevent body scroll when modal is open
        document.body.style.overflow = 'hidden';
    }
    
    function hideSuccessModal() {
        modal.style.display = 'none';
        // Restore body scroll
        document.body.style.overflow = '';
    }
    
    // Enhanced email input behavior
    emailInput.addEventListener('input', function() {
        // Remove any existing error messages when user starts typing
        const errorDiv = document.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
    });
    
    // Add some visual feedback for the email input
    emailInput.addEventListener('blur', function() {
        const email = emailInput.value.trim();
        if (email && !emailRegex.test(email)) {
            emailInput.style.borderColor = '#ef4444';
        } else {
            emailInput.style.borderColor = '#e2e8f0';
        }
    });
    
    // Debug function to view waitlist (remove in production)
    window.viewWaitlist = function() {
        const waitlist = JSON.parse(localStorage.getItem('waitlist') || '[]');
        console.table(waitlist);
        return waitlist;
    };
    
    // Debug function to clear waitlist (remove in production)
    window.clearWaitlist = function() {
        localStorage.removeItem('waitlist');
        console.log('Waitlist cleared');
    };
});