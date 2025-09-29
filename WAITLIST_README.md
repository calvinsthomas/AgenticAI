# Waitlist Landing Page

A modern, responsive waitlist landing page for "The Next Generation Product" with email signup functionality.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Email Validation**: Client-side validation with user-friendly error messages
- **Success Feedback**: Animated success message after successful signup
- **Keyboard Support**: Press Enter to submit the form
- **Modern UI**: Purple gradient theme with smooth animations
- **Local Storage**: Emails are stored locally (in production, would connect to a backend)

## Files

- `index.html` - Main landing page structure
- `styles.css` - Responsive CSS styling with purple gradient theme
- `script.js` - Email validation and form submission functionality
- `.replit` - Replit configuration for easy deployment
- `replit.nix` - Nix configuration for dependencies

## Running Locally

1. Open the project in a web browser by serving the files:
   ```bash
   python3 -m http.server 8000
   ```
2. Visit `http://localhost:8000` in your browser

## Running on Replit

1. Import this project to Replit
2. Click "Run" button
3. The website will be served automatically

## Features Implemented

✅ **Landing Page Design**
- Purple gradient background matching the original design
- Centered layout with responsive typography
- Modern card-based feature section

✅ **Email Signup Form**
- Email input with placeholder text
- "Join Waitlist" button with hover effects
- Form validation for email format
- Success message display

✅ **Feature Cards**
- Lightning Fast - Speed and efficiency messaging
- Secure by Design - Security-focused messaging  
- Powerful Features - Advanced capabilities messaging
- Purple circular icons with white symbols

✅ **Responsive Design**
- Mobile-first approach
- Stacked layout on smaller screens
- Proper spacing and typography scaling

✅ **Interactive Features**
- Email validation with error messages
- Loading state during form submission
- Success notification with auto-dismiss
- Keyboard navigation support (Enter to submit)
- Duplicate email detection

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Customization

To customize the landing page:

1. **Colors**: Edit the CSS custom properties in `styles.css`
2. **Content**: Update the text content in `index.html`
3. **Features**: Modify the feature cards section
4. **Backend Integration**: Replace localStorage with actual API calls in `script.js`