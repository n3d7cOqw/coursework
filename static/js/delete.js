
const container = document.querySelector(".container");

container.addEventListener("click", function (e){
    if (e.target.id === "deleteButton"){
        let id = e.target.getAttribute("data-id");
        let name = e.target.getAttribute("data-name");
        let surname = e.target.getAttribute("data-surname");
        const deleteLabel = document.querySelector("#DeleteLabel")
        deleteLabel.innerHTML = `Видалення контакту ${name} ${surname}`
        const deleteForm = document.querySelector("#deleteForm");
            deleteForm.action = `delete-record/${id}`;

    }
})