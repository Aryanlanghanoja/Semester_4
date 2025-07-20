$(document).ready(function () {
    $('.slider').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: true,
        dots: true
    });
});

$('#registrationForm').submit(function (e) {
    e.preventDefault();
    var username = $(this).find('input[name="username"]').val();
    var email = $(this).find('input[name="email"]').val();
    var password = $(this).find('input[name="password"]').val();

    if (username === '') {
        $(this).find('.username-error').text('Please enter a username');
        return;
    }

    if (email === '') {
        $(this).find('.email-error').text('Please enter an email');
        return;
    }

    if (!isValidEmail(email)) {
        $(this).find('.email-error').text('Please enter a valid email');
        return;
    }

    if (password === '') {
        $(this).find('.password-error').text('Please enter a password');
        return;
    }

    this.submit();
});

$('#loginForm').submit(function (e) {
    e.preventDefault();
    var username = $(this).find('input[name="username"]').val();
    var password = $(this).find('input[name="password"]').val();

    if (username === '') {
        $(this).find('.username-error').text('Please enter your username');
        return;
    }

    if (password === '') {
        $(this).find('.password-error').text('Please enter your password');
        return;
    }

    this.submit();
});

function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}