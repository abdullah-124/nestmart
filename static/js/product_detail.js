const thumbnail = document.querySelectorAll('.thumbnail')
const main_image = document.getElementById('main_image')

thumbnail.forEach(t =>{
    t.addEventListener('click',()=>{
        main_image.src = t.src
        
    })
})