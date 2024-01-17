const loadCategory = () => {
    fetch("https://sunexpress.onrender.com/category/list/")
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        displaycategory(data)
      })
      .catch((err) => console.log(err));
  };
  const displaycategory = (cats) => {
    //   console.log(services);
    cats.forEach((cat) => {
      const parent = document.getElementById("category-container");
      const li = document.createElement("li");
      li.innerHTML = `
                  <div class="p-3">
                  <a target="_blank" onclick="loadCategoryArticle('${cat.name}')" style="cursor: pointer;"> ${cat.name}</a>
                  </div>
        `;
      parent.appendChild(li);
      // Create article container for each category
      
    });
  };


// load article
const loadArticle = () => {
  fetch("https://sunexpress.onrender.com/article/list/")
    .then((res) => res.json())
    .then((data) => 
    {
      displayArticle(data)
      // console.log(data);
    }
    )
    .catch((err) => console.log(err));
};

const displayArticle = (articles) => {
  const parent = document.getElementById("article-container");

  articles.forEach((article) => {
    const col = document.createElement("div");
    col.classList.add("col-md-4");

    const card = document.createElement("div");
    card.classList.add("card", "shadow", "h-100");

    card.innerHTML = `
      <div class="ratio ratio-16x9">
        <img src=${article.image} class="card-img-top" loading="lazy" alt="..." />
      </div>
      <div class="card-body p-3 p-xl-5">
        <h3 class="card-title h5">${article.headline}</h3>
        <h3 class="card-title h5">${article.id}</h3>
        <p class="card-text">${article.body.slice(0, 50)}</p>
        <button > <a target="_blank" href="artDetails.html?articleId=${
          article.id
        }">Details</a> </button>
      </div>
    `;

    col.appendChild(card);
    parent.appendChild(col);
  });
};
loadCategory()
loadArticle()