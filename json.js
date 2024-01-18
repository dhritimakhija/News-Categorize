function signin() {
  var email = document.getElementById("signinEmail").value;
  var password = document.getElementById("signinPassword").value;

  if (email === "" || password === "") {
    alert("Please fill in all fields.");
  } else {
    // Perform signin logic here
    // Simulating a successful sign-in for demonstration purposes
    alert("Sign In successful for user: " + username);
    window.location.href = "link.html"; // Redirect to the link entry page
  }
}

function submitLink() {
  var linkInput = document.getElementById("linkInput").value;
  if (linkInput === "") {
    alert("Please enter a link.");
  } else {
    // Perform link submission logic here
    alert("Link submitted: " + linkInput);
  }
}
