const editButton = document.querySelectorAll(".edit")
const editForm = document.querySelectorAll(".ed-form")
const inputSearch = document.querySelector(".search-input")
const grids = document.querySelectorAll(".grid")

editButton.forEach((btn) =>{
    btn.addEventListener("click",() =>{
        editForm.forEach((form) =>{
            form.style.display = "block"
        })
    })
})

inputSearch.addEventListener("input",function(){
    const query = this.value.toLowerCase()
    grids.forEach((grid) =>{
        const contentElement = grid.querySelector(".test")
        const title = contentElement ? contentElement.textContent.toLowerCase() : ""
        grid.style.display = title.includes(query) ? '' : 'none';
    })
})