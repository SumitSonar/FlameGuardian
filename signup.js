
var firebaseConfig = {
    apiKey: "AIzaSyDqiTI80l91w3UxOnXWAyf5k5az2HuuBt8",
    authDomain: "login-ac410.firebaseapp.com",
    databaseURL: "https://login-ac410-default-rtdb.firebaseio.com",
    projectId: "login-ac410",
    storageBucket: "login-ac410.appspot.com",
    messagingSenderId: "531038238814",
    appId: "1:531038238814:web:33efd07aeb145567455ccf"
  };
  
  firebase.initializeApp(firebaseConfig);
  function signUpUser(username, email, password) {
    firebase.auth().createUserWithEmailAndPassword(email, password)
  .then((userCredential) => {
      // User is signed up
      var user = userCredential.user;
      console.log('User signed up:', user);
      alert('Sign-up successful!');
    })
  .catch((error) => {
      // An error occurred while signing up the user
      var errorCode = error.code;
      var errorMessage = error.message;
      console.log('Error signing up user:', errorCode, errorMessage);
    });
  }
  document.getElementById('signup-form').addEventListener('submit', (event) => {
    event.preventDefault();
  
    var username = document.querySelector('#username').value;
    var email = document.querySelector('#emailid').value;
    var password = document.querySelector('#password').value;
  
    signUpUser(username, email, password);
  });