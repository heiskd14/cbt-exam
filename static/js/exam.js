let calcDisplay = '';

function updateTimer() {
    fetch('/time_check')
        .then(response => response.json())
        .then(data => {
            const remaining = data.remaining;
            const minutes = Math.floor(remaining / 60);
            const seconds = remaining % 60;
            
            const timerElement = document.getElementById('timer');
            if (timerElement) {
                timerElement.textContent = `Time Left: ${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
                
                if (remaining <= 0) {
                    alert('Time is up! Submitting exam...');
                    document.querySelector('form[action*="submit"]').submit();
                } else {
                    setTimeout(updateTimer, 1000);
                }
            }
        });
}

function submitAnswer(optionIndex) {
    const formData = new FormData();
    formData.append('option', optionIndex);
    
    fetch('/answer', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const options = document.querySelectorAll('.option');
            options.forEach(opt => opt.classList.remove('selected'));
            options[optionIndex].classList.add('selected');
        }
    });
}

function toggleCalculator() {
    const calc = document.getElementById('calculator');
    if (calc.style.display === 'none') {
        calc.style.display = 'block';
    } else {
        calc.style.display = 'none';
    }
}

function calcBtn(value) {
    calcDisplay += value;
    document.getElementById('calc-display').value = calcDisplay;
}

function calcClear() {
    calcDisplay = '';
    document.getElementById('calc-display').value = '';
}

function calcBackspace() {
    calcDisplay = calcDisplay.slice(0, -1);
    document.getElementById('calc-display').value = calcDisplay;
}

function calcEquals() {
    try {
        const result = eval(calcDisplay);
        calcDisplay = String(result);
        document.getElementById('calc-display').value = calcDisplay;
    } catch (e) {
        document.getElementById('calc-display').value = 'Error';
        calcDisplay = '';
    }
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
        const prevBtn = document.querySelector('button[type="submit"][name*="prev"]');
        if (prevBtn && !prevBtn.disabled) {
            prevBtn.closest('form').submit();
        }
    } else if (e.key === 'ArrowRight') {
        const nextBtn = document.querySelector('button[type="submit"][name*="next"]');
        if (nextBtn && !nextBtn.disabled) {
            nextBtn.closest('form').submit();
        }
    } else if (['a', 'A'].includes(e.key)) {
        const option = document.querySelector('input[name="option"][value="0"]');
        if (option) {
            option.checked = true;
            submitAnswer(0);
        }
    } else if (['b', 'B'].includes(e.key)) {
        const option = document.querySelector('input[name="option"][value="1"]');
        if (option) {
            option.checked = true;
            submitAnswer(1);
        }
    } else if (['c', 'C'].includes(e.key)) {
        const option = document.querySelector('input[name="option"][value="2"]');
        if (option) {
            option.checked = true;
            submitAnswer(2);
        }
    } else if (['d', 'D'].includes(e.key)) {
        const option = document.querySelector('input[name="option"][value="3"]');
        if (option) {
            option.checked = true;
            submitAnswer(3);
        }
    } else if (['s', 'S'].includes(e.key)) {
        const submitBtn = document.querySelector('form[action*="submit"] button');
        if (submitBtn && confirm('Do you want to submit all subjects and continue?')) {
            submitBtn.closest('form').submit();
        }
    }
});

if (document.getElementById('timer')) {
    updateTimer();
}
