import { showChart } from "./statChart.js";

document.addEventListener("DOMContentLoaded", function () {
    const modalTag = document.getElementById("exampleModal");
    const formMessage = document.getElementById("invalid-form-message-container");

    // Check if formMessage contains any content (message rendered by Django)
    if (formMessage && formMessage.innerText.trim().length > 0) {
      const modal = new bootstrap.Modal(modalTag);
      modal.show();
    }
  });

document.addEventListener("DOMContentLoaded", function () {
    var toggler = document.getElementsByClassName("caret");

    for (var i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function () {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("caret-down");
      });
    }
  });

// pass job id on button click (add form)
// document.addEventListener("DOMContentLoaded", function () {
//     const addNoteBtn = document.getElementsByClassName("add-note-btn")
//     const addNoteForm = document.getElementById("note-form")
//     for (let i = 0; i < addNoteBtn.length; i++){
//     addNoteBtn[i].addEventListener("click",()=>{
//     link = addNoteBtn.item(i).getAttribute("href")
//     addNoteForm.action = `${link}`
//     })
// }    
// })

function openJobModal(id, title, company, url, location,status, description,modalTitle, formAction) {
    document.getElementById('jobFormModalLabel').innerText = modalTitle;
    document.getElementById('id_title').value = title;
    document.getElementById('id_company').value = company;
    document.getElementById('id_location').value = location;
    document.getElementById('id_url').value = url;
    document.getElementById('id_status').value = status;
    document.getElementById('id_description').value = description;
    document.getElementById('job-form').action = formAction;

    const submitBtn = document.getElementById('job-form-submit-btn')
    if (id){
      submitBtn.innerHTML = 'Update'
    }else{
      submitBtn.innerHTML = 'Add'
    }

    // Show modal (bootstrap 5)
    let jobModal = new bootstrap.Modal(document.getElementById('jobFormModal'));
    jobModal.show();
}


function openNoteModal(id, note, modalTitle, formAction){
  document.getElementById('noteFormModalLabel').innerText = modalTitle
  document.getElementById('id_note').value = note
  document.getElementById('note-form').action = formAction

  const submitBtn = document.getElementById('note-form-submit-btn')
  if (id){
    submitBtn.innerHTML = 'Update'
  }else{
    submitBtn.innerHTML = 'Add Note'
  }

  let noteModal = new bootstrap.Modal(document.getElementById('noteFormModal'));
  noteModal.show();
}

function deleteWarning(){
 return  confirm('Are you sure?')
}

const totalJobs = document.getElementById("stat-total-jobs")
if ( totalJobs!==null ){
showChart();
}

const deleteJob = document.getElementById('delete-job-btn')
if(deleteJob){
deleteJob.addEventListener('click', (e) => {
  if (!deleteWarning()) {
    e.preventDefault()
    return;
  }
})
}

const deleteNote = document.getElementById("delete-note-btn")
if(deleteNote){
deleteNote.addEventListener('click', (e) => {
  if (!deleteWarning()) {
    e.preventDefault()
    return;
  }
})
}

window.openJobModal = openJobModal;
window.openNoteModal = openNoteModal;