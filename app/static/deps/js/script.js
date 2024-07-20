document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('modal');
    var span = document.getElementsByClassName('close')[0];
    var editLinks = document.getElementsByClassName('edit-link');
    var form = document.getElementById('edit-form');

    for (var i = 0; i < editLinks.length; i++) {
        editLinks[i].onclick = function() {
            var row = this.getAttribute('data-row');
            var tableRow = document.querySelector('tbody tr:nth-child(' + row + ')');
            var column1 = tableRow.cells[0].innerText;
            var column2 = tableRow.cells[1].innerText;

            document.getElementById('column1').value = column1;
            document.getElementById('column2').value = column2;

            modal.style.display = 'block';
        }
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    form.onsubmit = function(event) {
        event.preventDefault();

        var row = document.querySelector('tbody tr:nth-child(' + row + ')');
        row.cells[0].innerText = document.getElementById('column1').value;
        row.cells[1].innerText = document.getElementById('column2').value;

        // Здесь можно добавить код для отправки данных на сервер и обновления базы данных

        modal.style.display = 'none';
    }
});