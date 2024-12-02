const thumbnail = document.querySelectorAll('.thumbnail')
const main_image = document.getElementById('main_image')

thumbnail.forEach(t =>{
    t.addEventListener('click',()=>{
        main_image.src = t.src
        
    })
})

// add product to wishlist
const add_wishlist = document.getElementById('add_wishlist')
add_wishlist.addEventListener('click',async()=>{
    product_id = add_wishlist.getAttribute('data-product-id')
    console.log(product_id)
    try {
        const response = await fetch("/wishlist/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                // "X-CSRFToken": getCSRFToken(),
            },
        body: JSON.stringify({ product_id: product_id }),
        });

        const data = await response.json();
        if (response.ok) {
            console.log('addedd')
        } else {
            alert(data.error || "Something went wrong!");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
})

// Helper function to fetch the CSRF token
function getCSRFToken() {
    const cookieValue = document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
    return cookieValue || "";
}