// Email validation function
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Join waitlist function
function joinWaitlist() {
    const emailInput = document.getElementById('email');
    const email = emailInput.value.trim();
    const successMessage = document.getElementById('success-message');
    const joinBtn = document.getElementById('join-btn');
    
    // Validate email
    if (!email) {
        alert('Please enter your email address.');
        emailInput.focus();
        return;
    }
    
    if (!isValidEmail(email)) {
        alert('Please enter a valid email address.');
        emailInput.focus();
        return;
    }
    
    // Disable button and show loading state
    joinBtn.disabled = true;
    joinBtn.innerHTML = 'Joining... <i class="fas fa-spinner fa-spin"></i>';
    
    // Simulate API call delay
    setTimeout(() => {
        // Store email in localStorage (in a real app, this would be sent to a server)
        const waitlistEmails = JSON.parse(localStorage.getItem('waitlistEmails') || '[]');
        
        // Check if email already exists
        if (waitlistEmails.includes(email)) {
            alert('This email is already on the waitlist!');
            joinBtn.disabled = false;
            joinBtn.innerHTML = 'Join Waitlist <i class="fas fa-arrow-right"></i>';
            return;
        }
        
        // Add email to waitlist
        waitlistEmails.push(email);
        localStorage.setItem('waitlistEmails', JSON.stringify(waitlistEmails));
        
        // Show success message
        successMessage.classList.remove('hidden');
        
        // Clear form
        emailInput.value = '';
        
        // Reset button
        joinBtn.disabled = false;
        joinBtn.innerHTML = 'Join Waitlist <i class="fas fa-arrow-right"></i>';
        
        // Hide success message after 3 seconds
        setTimeout(() => {
            successMessage.classList.add('hidden');
        }, 3000);
        
        console.log('Email added to waitlist:', email);
        console.log('Total waitlist emails:', waitlistEmails.length);
    }, 1000);
}

// Add enter key support for email input
document.getElementById('email').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        joinWaitlist();
    }
});

// Close success message when clicking outside
document.addEventListener('click', function(e) {
    const successMessage = document.getElementById('success-message');
    if (!successMessage.classList.contains('hidden') && !successMessage.contains(e.target)) {
        successMessage.classList.add('hidden');
    }
});

// Add some animation when page loads
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.hero h1, .hero-subtitle, .waitlist-form, .feature-card');
    
    elements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            el.style.transition = 'all 0.6s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 100);
    });
});