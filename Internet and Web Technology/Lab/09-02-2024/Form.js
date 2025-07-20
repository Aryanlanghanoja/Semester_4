function ValidateUser(Event) {
    var Password = document.getElementById('InputPassword').value;
    var ConfimedPassowrd = document.getElementById('Confirm_Password').value;


    if (Password == ConfimedPassowrd) {
        console.log('Welcome');
        alert('Welcome');
    }

    else {
        console.log('Password not match');
        alert('Password not match');
    }
}

function OnFocusEvent() {
    if (document.getElementById('InputPassword').value == '') {
        alert('Please enter password');
    }

    else {
        alert('Welcome');
    }
}