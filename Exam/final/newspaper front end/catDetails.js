const loadCategoryArticle = (search) => {
  document.getElementById("cat-details").innerHTML = "";
    console.log(search);
    fetch(`https://sunexpress.onrender.com/article/list/?search=${
        search
      }`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        // window.open(`catDetails.html?search=${search}`, '_blank');
        displayCategoryArticle(data)
      })
      .catch((err) => console.log(err));
};
const displayCategoryArticle = (catArticles) => {
    console.log(catArticles);
    catArticles?.forEach((catArticle) => {
      // console.log(doctor);
      const parent = document.getElementById("cat-details");
      const div = document.createElement("div");
      div.classList.add("doc-card");
      div.innerHTML = `
          <img class="doc-img" src=${catArticle.image} alt="" />
                <h4>${catArticle?.headline}</h4>
               
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis,
                  numquam!
                </p>
  
                
          `;
  
      parent.appendChild(div);
    });
  };

loadCategoryArticle()














// const getCatparams = () => {
//     const param = new URLSearchParams(window.location.search).get("catId");
//     console.log(param);
//     // loadTime(param);
//     fetch(`https://sunexpress.onrender.com/category/list/${param}`)
//       .then((res) => res.json())
//       .then((data) => {
//         console.log(data);
//         displayDetails(data)});
  
//     // fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
//     //   .then((res) => res.json())
//     //   .then((data) => doctorReview(data));
// };


// getCatparams()