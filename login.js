const largeBox = document.querySelector('.large-box');
const loginLink = document.querySelector('.login-link'); 
const registerLink = document.querySelector('.register-link');

registerLink.addEventListener('click', () => {
    largeBox.classList.add('active');
});