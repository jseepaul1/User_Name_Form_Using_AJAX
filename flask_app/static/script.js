var jsonForm = document.getElementById("json_form");
// e is the javascript event happening when we submit a form
jsonForm.onsubmit = function (e) {
// e.preventDefault() is a method that stops the default nature of javascript.
  e.preventDefault();
// create formData object from js and send it through a fetch post request.
  var form = new FormData(jsonForm);
// fetch collects data from the specific endpoint
  fetch("/create/user", { method: "POST", body: form })
    .then((response) => response.json())
    .then((data) => {
// accessing the user table in the html by the id
      var usernames = document.getElementById("user_table");
// inserting a row using js
      var row = usernames.insertRow();
// table-active is the same class used in the table in the html
      row.classList.add('table-active');
      row.insertCell(0).innerHTML = data["user_name"];
      row.insertCell(1).innerHTML = data["email"];
    });
};

