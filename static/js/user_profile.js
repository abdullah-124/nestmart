// console.log('i am from user profile.js')
const form_elements = document.querySelectorAll('input')
const submit_button = document.getElementById('submit_btn')
function enable_submit() {
    submit_button.disabled = false
}
form_elements.forEach(element => {
    element.addEventListener('input', enable_submit)
})
// suggest location on typing
const location_input = document.getElementById('location_input')
const suggestions_box = document.getElementById('suggestions_box')
let debounceTimeout
function fetch_suggestions(query) {
    let url = `https://maps.gomaps.pro/maps/api/place/autocomplete/json?input=<${query}>&key=AlzaSyccNxQvfcj06z_blIxi2VTBj9l7ViHMKGx`
    console.log(url)
    fetch(url).then(res => res.json())
        .then(data => {
            suggestions_box.innerHTML = ''
            // console.log(data.predictions)
            data.predictions.forEach(l => {
                const li = document.createElement('li')
                li.classList.add('suggestion_list')
                li.textContent = l.description
                suggestions_box.appendChild(li)
                li.addEventListener('click', ()=>{
                    location_input.value = l.description;
                    suggestions_box.innerHTML = '';
                })

            })
        })
}
location_input.addEventListener('input', () => {
    const query = location_input.value
    console.log(query);

    if (query.length >= 3) {
        clearTimeout(debounceTimeout)
        debounceTimeout = setTimeout(() => fetch_suggestions(query), 1000);
    }
    else {
        suggestions_box.innerHTML = ''
    }
})

// VALIDATION FOR PROFILE IMAGAE WHILE UPLOAD
const profile_photo_input = document.getElementById('photo_upload')
const upload_msg = document.getElementById('upload_msg')
const MAX_MB_SIZE =  1024*1024
const allowedTypes = ["image/jpeg", "image/png"];

profile_photo_input.addEventListener('change',function(e){
    const profile_photo = e.target.files[0]
    console.log('size',profile_photo.size)
    if(profile_photo.size > MAX_MB_SIZE){
        upload_msg.innerText = 'file size grater than 1mb'
        upload_msg.classList.add('text-danger')
        e.target.value = ''
    }
    else if (!allowedTypes.includes(profile_photo.type)){
        upload_msg.innerText = "Invalid file type. Only(jpg/png)"
        upload_msg.classList.add('text-danger')
        e.target.value = ''
    }
    else {
        upload_msg.innerText = profile_photo.name;
        upload_msg.classList.add('text-success')
    }
    e.preventDefault()
})