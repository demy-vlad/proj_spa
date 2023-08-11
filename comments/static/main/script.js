document.addEventListener('DOMContentLoaded', function() {
    const openButton = document.getElementById('open-comment-form');
    const openButton2 = document.querySelectorAll('.open-comment-button');
    const popup = document.getElementById('comment-popup');
    const closeButton = document.getElementById('close-button');
    const closeErrorButton = document.getElementById('close-error-button');
    const form = document.getElementById('comment-form');
    const errorPopup = document.getElementById('error-popup');

    openButton.addEventListener('click', function() {
        popup.style.display = 'block';
    });

    openButton2.forEach(openButton2 => {
        openButton2.addEventListener('click', function() {
            var formId = this.getAttribute('data-form-id');
            var form = document.getElementById('comment-form-' + formId);
            if (form) {
                form.style.display = 'block';
            }
        });
    });

    closeButton.addEventListener('click', function() {
        popup.style.display = 'none';
    });

    form.addEventListener('submit', function(event) {
        const username = document.getElementById('user_name').value;
        const email = document.getElementById('email').value;
        const text = document.getElementById('text').value;

        if (!username || !email || !text) {
            event.preventDefault();
            errorPopup.style.display = 'block';
        }
    });

    closeErrorButton.addEventListener('click', function() {
        errorPopup.style.display = 'none';
    });
});