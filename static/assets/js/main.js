
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
document.addEventListener("DOMContentLoaded", function () {
    const addNoteBtn = document.getElementsByClassName("add-note-btn")
    const addNoteForm = document.getElementById("note_form")
    for (let i = 0; i < addNoteBtn.length; i++){
    addNoteBtn[i].addEventListener("click",()=>{
    link = addNoteBtn.item(i).getAttribute("href")
    addNoteForm.action = `${link}`
    })
}    
})

