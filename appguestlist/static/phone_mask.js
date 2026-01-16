document.addEventListener('DOMContentLoaded', function () {
    const phoneInput = document.querySelector('#id_telephone');

    if (phoneInput) {
        phoneInput.addEventListener('input', function () {
            let value = phoneInput.value.replace(/\D/g, '').slice(0, 10);
            let formatted = '';

            if (value.length > 0) formatted += value.slice(0, 2);
            if (value.length > 2) formatted += '-' + value.slice(2, 4);
            if (value.length > 4) formatted += '-' + value.slice(4, 6);
            if (value.length > 6) formatted += '-' + value.slice(6, 8);
            if (value.length > 8) formatted += '-' + value.slice(8, 10);

            phoneInput.value = formatted;
        });
    }
});
