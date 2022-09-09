const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn = document.querySelector('#sign-up-btn');
const container = document.querySelector('.container');
const themeToggler = document.querySelector(".theme-toggler");

sign_up_btn.addEventListener('click', () => {
    container.classList.add('sign-up-mode');
});

sign_in_btn.addEventListener('click', () => {
    container.classList.remove('sign-up-mode');
});

themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeToggler.querySelector('span').classList.toggle('active');
});