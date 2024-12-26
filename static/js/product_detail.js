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
        body: JSON.stringify({ product_id: 2 }),
    })
    .then(res => res.json())
    .then(data =>{
        console.log(data)
    })
    .catch(er=>{
        console.error('Fetch',er)
    })
})