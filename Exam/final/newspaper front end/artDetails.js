const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("articleId");
    // console.log(param);
    // loadTime(param);
    fetch(`https://sunexpress.onrender.com/article/list/${param}`)
      .then((res) => res.json())
      .then((data) => {
        // console.log(data);
        displayDetails(data)
    });

};


const displayDetails = (article) => {
    // console.log(article);
    const parent = document.getElementById("art-details");
    const div = document.createElement("div");
    const publishingTime = new Date(article.publishing_time);
    div.classList.add("art-details-container");
    div.innerHTML = `
    <p class='text-Indigo'>${publishingTime.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
      })}</p>
      <div class="article-img">
      <img src=${article.image} alt="" />
    </div>
    <div class="doc-info">
      <h1>${article.headline} </h1>
      
  
      <p class="w-50">
      ${article.body}
      </p>
  
      <h4 class='text-primary'>${article.category} </h4>
      <h6 class='text-warning'>${article.editor} </h6>
      
    </div>
      `;
    parent.appendChild(div);
};

getparams()