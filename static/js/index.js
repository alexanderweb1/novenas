
document.addEventListener('DOMContentLoaded', function () {
    const novena = 'DivinoN'; // cámbialo al nombre que uses para el Cisne

    document.querySelectorAll('.dias__columna').forEach(function (col, index) {
        const dia = index + 1;
        const key = `novena_${novena}_dia_${dia}`;

        if (localStorage.getItem(key) === 'leido') {
            const overlay = col.querySelector('.card__overlay');

            overlay.style.backgroundColor = 'rgba(25, 135, 84, 0.75)';

            if (!overlay.querySelector('.check-leido')) {
                const check = document.createElement('span');
                check.className = 'check-leido';
                check.textContent = '✓ Leído';
                check.style.cssText = 'display:block; color:white; font-weight:bold; margin-top:6px;';
                overlay.appendChild(check);
            }
        }
    });
});
