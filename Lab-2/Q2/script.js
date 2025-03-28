const form = document.getElementById('employeeForm');
const tableBody = document.querySelector('#employeeTable tbody');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const employeeId = document.getElementById('employeeId').value.trim();
    const employeeName = document.getElementById('employeeName').value.trim();
    const department = document.getElementById('department').value;

    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${employeeId}</td>
        <td>${employeeName}</td>
        <td>${department}</td>
      `;

    tableBody.appendChild(row);
    form.reset();
});