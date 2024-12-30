const thumbnail = document.querySelectorAll('.thumbnail')
const main_image = document.getElementById('main_image')

thumbnail.forEach(t => {
    t.addEventListener('click', () => {
        main_image.src = t.src
        console.log('ee');

    })
})

// add to wishlist feature
const add_wishlist_btn = document.getElementById('add_wishlist_btn')
add_wishlist_btn.addEventListener('click', () => {
    const product_id = add_wishlist_btn.getAttribute('data-product-id')
    // const formData = new FormData();
    // formData.append('product_id', product_id);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    console.log(product_id)
    // fetching for add product to wishlist
    fetch(` http://127.0.0.1:8000/wishlist/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product_id: product_id }),
    })
    .then(res => res.json())
    .then(data =>{
        show_modal(data)
    })
    .catch(er=>{
        console.error('Fetch',er)
    })
})

const show_modal = (data)=>{
    const modal = new bootstrap.Modal(document.getElementById('successModal'))
    const modal_massage = document.getElementById('modal_massage')
    if(data.type){
        modal_massage.innerHTML = `
            <i style="font-size:52px" class="bi bi-check2-circle text-success"></i>
            <h6 class="text-${data.type}">${data.message}</h6>
            `
    }
    else{
        modal_massage.innerHTML = `<h6 class="text-danger">Something went wrong!!!</h6>`
    }
    modal.show()
    setTimeout(() => {
        modal.hide()
        window.location.reload()
    }, 1500);
}