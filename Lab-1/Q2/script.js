let currentInput = '';

function appendNumber(number) {
    currentInput += number;
    $('#result').val(currentInput);
}

function appendOperator(operator) {
    if (currentInput && !isNaN(parseInt(currentInput.slice(-1)))) {
        currentInput += operator;
        $('#result').val(currentInput);
    }
}

function appendDecimal() {
    if (!currentInput.includes('.') || /[+\-*\/]$/.test(currentInput)) {
        currentInput += '.';
        $('#result').val(currentInput);
    }
}

function clearDisplay() {
    currentInput = '';
    $('#result').val('');
}

function calculateResult() {
    try {
        const calculated = eval(currentInput);
        $('#result').val(calculated);
        currentInput = calculated.toString();
    } catch {
        $('#result').val('Error');
        currentInput = '';
    }
}