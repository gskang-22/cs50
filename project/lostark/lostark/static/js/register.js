const usernameField = document.querySelector('#usernameField');

usernameField.addEventListener('keyup', (event) => {
    console.log("test");

    const usernameVal = event.target.value;
    console.log('usernameVal', usernameVal)

    fetch("/authentication/validate-username", {
        
    });
    .then(response)
});
