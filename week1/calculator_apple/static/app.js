let display = document.getElementById('display');
let currentInput = '';

function appendNumber(num) {
  if (currentInput === '0') currentInput = '';
  currentInput += num;
  display.innerText = currentInput;
}

function appendOperator(op) {
  if (currentInput === '') return;
  currentInput += ` ${op} `;
  display.innerText = currentInput;
}

function clearDisplay() {
  currentInput = '';
  display.innerText = '0';
}

function calculate() {
  try {
    currentInput = eval(currentInput).toString();
    display.innerText = currentInput;
  } catch {
    display.innerText = 'Error';
  }
}
