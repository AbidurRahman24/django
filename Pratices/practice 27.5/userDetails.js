const getUserparams = () => {
    const param = new URLSearchParams(window.location.search).get("userId");
    // loadTime(param);
    fetch(`https://fakestoreapi.com/users/${param}`)
      .then((res) => res.json())
      .then((data) => displayUserDetails(data));
  };

  const displayUserDetails = (user) => {
    console.log(user);
    const parent = document.getElementById("user-details");
    const div = document.createElement("p");
    div.innerHTML = `
    <div class="text-center">
    Single user Details here
      <h1 >Name: ${user.name.firstname} ${user.name.lastname}  </h1>
      <p>UserName: ${user.username} </p>
      <p>Email ${user.email} </p>
      <p>Address: ${user.address.street} ${user.address.city}</p>
      `;
    parent.appendChild(div);
  };

getUserparams();