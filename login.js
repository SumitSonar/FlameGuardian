var firebaseConfig = {
  apiKey: "AIzaSyA1jFY3ICziwgugwsBhNrZENmpa3wpVr7s",
  authDomain: "flameguardian-4f0d4.firebaseapp.com",
  databaseURL: "https://flameguardian-4f0d4-default-rtdb.firebaseio.com",
  projectId: "flameguardian-4f0d4",
  storageBucket: "flameguardian-4f0d4.appspot.com",
  messagingSenderId: "882450188876",
  appId: "1:882450188876:web:38f86c88762b3217edc2e9",
  measurementId: "G-3ZLXL3N1T2"
};
  
  firebase.initializeApp(firebaseConfig);
  function logInUser(email, password) {
    firebase.auth().signInWithEmailAndPassword(email, password)
  .then((userCredential) => {
      // User is logged in
      var user = userCredential.user;
      console.log('User logged in:', user);
      alert('Login successful!');
    })
  .catch((error) => {
      // An error occurred while logging in the user
      var errorCode = error.code;
      var errorMessage = error.message;
      console.log('Error logging in user:', errorCode, errorMessage);
    });
  }
  document.getElementById('login-form').addEventListener('submit', (event) => {
    event.preventDefault();
  
    var email = document.querySelector('#emailid').value;
    var password = document.querySelector('#password').value;
  
    logInUser(email, password);
  });