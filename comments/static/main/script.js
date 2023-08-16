document.addEventListener('DOMContentLoaded', function() {
    const openButton = document.getElementById('open-comment-form');
    const openButton2 = document.querySelectorAll('.open-comment-button');
    var openButtons = document.querySelectorAll('.emoji-button');
    var popup = document.getElementById('comment-popup');
    var closeButton = document.getElementById('close-button');
    var parentCommentIdInput = document.getElementById('parent_comment_id');
    var form = document.getElementById('comment-form');
    var errorPopup = document.getElementById('error-popup');
    var closeErrorButton = document.getElementById('close-error-button');


    openButtons.forEach(function(openButton) {
        openButton.addEventListener('click', function() {
            var commentId = openButton.getAttribute('data-comment-id');
            if (commentId) {
                parentCommentIdInput.value = commentId;
            } else {
                parentCommentIdInput.value = '';
            }
            var errorPopup = document.getElementById('error-popup');
            if (errorPopup) {
                errorPopup.style.display = 'none';
            }
            popup.style.display = 'block';
        });
    });


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
        const file = document.getElementById('file').value;

        if (!username || !email || !text || !file) {
            event.preventDefault();
            errorPopup.style.display = 'block';
        }
    });

    closeErrorButton.addEventListener('click', function() {
        errorPopup.style.display = 'none';
    });
    const submitButton9 = document.getElementById('submit-button');

    // Деактивируем кнопку при загрузке страницы
    // submitButton9.disabled = true;

    // Обработка успешной проверки капчи
    function onCaptchaSuccess() {
        submitButton9.disabled = false;
    }

    // Обработка сброса капчи
    function onCaptchaExpire() {
        submitButton9.disabled = true;
    }

    // Инициализация hCaptcha
    const hcaptchaContainer = document.getElementById('hcaptcha-container');
    if (hcaptchaContainer) {
        hcaptchaContainer.addEventListener('h-captcha-success', function () {
            onCaptchaSuccess();
        });
        hcaptchaContainer.addEventListener('h-captcha-expired', function () {
            onCaptchaExpire();
        });
    }


}); 