const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn = document.querySelector('#sign-up-btn');
const container = document.querySelector('.container');
const themeTogglerOne = document.querySelector(".theme-togglerOne");
const themeTogglerTwo = document.querySelector(".theme-togglerTwo");

sign_up_btn.addEventListener('click', () => {
    container.classList.add('sign-up-mode');
});

sign_in_btn.addEventListener('click', () => {
    container.classList.remove('sign-up-mode');
});

themeTogglerOne.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeTogglerOne.querySelector('span').classList.toggle('active');
});

themeTogglerTwo.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeTogglerTwo.querySelector('span').classList.toggle('active');
});