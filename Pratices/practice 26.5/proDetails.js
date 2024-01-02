const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("productId");
    // loadTime(param);
    fetch(`https://fakestoreapi.com/products/${param}`)
      .then((res) => res.json())
      .then((data) => displayDetails(data));
  };

  const displayDetails = (product) => {
    console.log(product);
    const parent = document.getElementById("product-details");
    const div = document.createElement("div");
    div.classList.add("product-details-container");
    div.innerHTML = `
      <div class="card-img">
      <img class='w-100' style='max-width: 300px;' src=${product.image} alt="" />
    </div>
    <div class="card-info">
      <h1>${product.title} </h1>
      
  
      <p class="w-50">
        ${product.description}
      </p>
  
      <h4>Fees: ${product.price} BDT</h4>
      
    </div>
    // <a href="#">Back to Home</a>
      `;
    parent.appendChild(div);
  };

getparams();