const loadUserData = () => {
    fetch('https://fakestoreapi.com/users')
        .then(res => res.json())
        .then(data => displayUserData(data))
        .catch(error => console.log(error)); // Add a catch block for error handling
};

const displayUserData = (users) => {
    const parent = document.getElementById('user-container');
    users.forEach(user => {
        const li = document.createElement('li');
        li.classList.add("col-md-4");
        li.innerHTML = `
            <div class="card shadow h-100">
                <div class="card-body p-3 p-xl-5">
                    <h3 class="card-title h5">Name: ${user.name.firstname} ${user.name.lastname}</h3>
                    <p class="card-text">username: ${user.username}</p>
                    <p>Email: ${user.email}</p>
                    <p>Number: ${user.number}</p>
                    <p>Address: ${user.address.street}, ${user.address.city}</p>
                    <a target="_blank" href="userDetails.html?userId=${user.id}" class="btn btn-primary">Details</a>
                </div>
            </div>
        `;
        parent.appendChild(li);
    });
};


loadUserData();
const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
  };
  
const handleRegistration = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");
    const info = {
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
    };
    if (password === confirm_password) {
        document.getElementById("error").innerText = "";
        if (
          /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(
            password
          )
        ) {
          console.log(info);
    
          fetch("https://fakestoreapi.com/users/", {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify(info),
          })
            .then((res) => res.json())
            .then((data) => console.log(data));

        } else {
          document.getElementById("error").innerText =
            "pass must contain eight characters, at least one letter, one number and one special character:";
        }
      } else {
        document.getElementById("error").innerText =
          "password and confirm password do not match";
        alert("password and confirm password do not match");
      }
}
const handleLogin = (event) => {
  event.preventDefault();
  const username = getValue("login-username");
  const password = getValue("login-password");
  console.log(username, password);
  if ((username, password)) {
    fetch("https://testing-8az5.onrender.com/patient/login/", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ username, password }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        if (data.token && data.user_id) {
          localStorage.setItem("token", data.token);
          localStorage.setItem("user_id", data.user_id);
          window.location.href = "index.html";
        }
      });
  }
};
