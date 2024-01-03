const loadProduct = (search) => {
    const parent = document.getElementById("product-container");
    parent.innerHTML = "";
    const apiUrl = search ? `https://fakestoreapi.com/products/category/${search}` : 'https://fakestoreapi.com/products';
    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        displayProduct(data)
    })
      .catch((err) => console.log(err));
};

const displayProduct = (products) => {
    const parent = document.getElementById("product-container");
    
    products.forEach((product) => {
        const li = document.createElement("li");
        li.classList.add("col-md-4"); // Bootstrap column class
        li.innerHTML = `
            <div class="card shadow h-100">
                <div class="ratio ratio-16x9">
                    <img
                        src=${product.image}
                        class="card-img-top"
                        loading="lazy"
                        alt="..."
                    />
                </div>
                <div class="card-body p-3 p-xl-5">
                    <h3 class="card-title h5">${product.title}</h3>
                    <p class="card-text">
                        ${product.description.slice(0, 140)}
                    </p>
                    <p> price: $${product.price}</p>
                    <p> Rating: ${product.rating.rate}</p>
                    <a target="_blank" href="productDetails.html?productId=${
                        product.id
                      }" class="btn btn-primary">Details</a>
                </div>
            </div>
        `;
        parent.appendChild(li);
    });
};
const loadCategory = () => {
    fetch("https://fakestoreapi.com/products/categories")
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        data.forEach((item) => {
          const parent = document.getElementById("category");
          const li = document.createElement("li");
          li.classList.add("dropdown-item");
          li.innerHTML = `
          <li onclick="loadProduct('${item}')"> ${item}</li>
            `;
          parent.appendChild(li);
        });
      });
  };
// Calling Functions
loadProduct();
loadCategory();
