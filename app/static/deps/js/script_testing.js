document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('modal');
  const openModalBtn = document.getElementById('modal-open-btn');
  const modalEdit = document.getElementById('modal-edit');
  const closeModalBtn = document.querySelector('.close-btn');
  const closeEditBtn = document.querySelector('.close-edit');
  const form = document.getElementById('add-student-form');


  openModalBtn.addEventListener('click', () => {
    form.reset();
    editingRow = null;
    modal.style.display = 'block';
  });

  closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  closeEditBtn.addEventListener('click', () => {
    modalEdit.style.display = 'none';
  });



  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });


  function formatDate(dateString) {
    const dateObj = new Date(dateString);
    const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
    return dateObj.toLocaleDateString('ru-RU', options);
  }

});
