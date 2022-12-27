const usernameField = document.querySelector('#usernameField');

usernameField.addEventListener('keyup', (event) => {
    console.log("test");

    const usernameVal = event.target.value;
    console.log('usernameVal', usernameVal)


    if (usernameVal.length > 0) {
        fetch("/authentication/validate-username", {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.username_error)
        });
    }
});