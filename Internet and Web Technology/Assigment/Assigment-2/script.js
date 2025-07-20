function generateTable() {
  var rows = parseInt(document.getElementById('rows').value);
  var columns = parseInt(document.getElementById('columns').value);
  var tableContainer = document.getElementById('table-container');
  var generateBtn = document.getElementById('generate-btn');
  var submitBtn = document.getElementById('submit-btn');

  submitBtn.classList.remove('d-none');
  submitBtn.disabled = false;
  generateBtn.disabled = true;
  generateBtn.style.display = 'none';
  tableContainer.innerHTML = '';

  var table = document.createElement('table');
  table.classList.add('table', 'table-bordered');

  for (var i = 0; i < rows; i++) {
    var row = table.insertRow();
    for (var j = 0; j < columns; j++) {
      var cell = row.insertCell();
      var input = document.createElement('input');
      input.type = 'text';
      input.classList.add('form-control');
      cell.appendChild(input);
    }
  }

  tableContainer.appendChild(table);
}

function submitData() {
  var inputs = document.querySelectorAll('input[type="text"]');
  var isValid = true;

  inputs.forEach(function(input) {
    if (input.value.trim() === '') {
      isValid = false;
      input.classList.add('is-invalid');
    } else {
      input.classList.remove('is-invalid');
    }
  });
    
  if (!isValid) {
    alert('Please Fill All Fields');
  }
}
