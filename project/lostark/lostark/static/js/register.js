const usernameField = document.querySelector('#usernameField');
const feedbackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const emailFeedbackArea = document.querySelector(".emailFeedbackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const emailSuccessOutput = document.querySelector(".emailSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
console.log(showPasswordToggle);
const passwordField = document.querySelector("#passwordField");
const submitBtn = document.querySelector(".submit-btn");

showPasswordToggle.addEventListener('click', (e) => {
    if (showPasswordToggle.textContent == 'SHOW') {
        showPasswordToggle.textContent = 'HIDE';
        passwordField.setAttribute("type", "text");
    } else {
        showPasswordToggle.textContent = 'SHOW';
        passwordField.setAttribute("type", "password");
    }
});

emailField.addEventListener('keyup', (event) => {
    const emailVal = event.target.value;
    emailSuccessOutput.style.display = 'block';
    if (emailVal.length == 0) {
        emailSuccessOutput.style.display = 'none';
    };
    emailSuccessOutput.textContent = `Checking ${emailVal}`

    emailField.classList.remove("is-invalid");
    emailFeedbackArea.style.display = 'none';

    if (emailVal.length > 0) {
        fetch("/authentication/validate-email", {
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            emailSuccessOutput.style.display = 'none';
            if (data.email_error) {
                submitBtn.disabled = true;
                emailField.classList.add("is-invalid");
                emailFeedbackArea.style.display = 'block';
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`
            } else if (feedbackArea.style.display == 'none') {
                submitBtn.removeAttribute('disabled');
            };
        });
    }
})


usernameField.addEventListener('keyup', (event) => {

    const usernameVal = event.target.value;
    usernameSuccessOutput.style.display = 'block';
    if (usernameVal.length == 0) {
        usernameSuccessOutput.style.display = 'none';
    };
    usernameSuccessOutput.textContent = `Checking ${usernameVal}`

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = 'none';

    if (usernameVal.length > 0) {
        fetch("/authentication/validate-username", {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            usernameSuccessOutput.style.display = 'none';
            if (data.username_error) {
                submitBtn.disabled = true;
                usernameField.classList.add("is-invalid");
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`
            } else if (emailFeedbackArea.style.display == 'none') {
                submitBtn.removeAttribute('disabled');
            };
        });
    }
});