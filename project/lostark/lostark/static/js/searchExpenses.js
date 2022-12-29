const searchField = document.querySelector('#searchField');

searchField.addEventListener('keyup', (e) =>{
    const searchValue = e.target.value;

    if (searchValue.length > 0) {
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
});