function checkPassword() {
    //capture the entered password from the input
   var passwordBoxObject = document.getElementById("passwordBox");
    var passwordEntered = passwordBoxObject.value; console.log("User entered password:", passwordEntered);

    //check if correct
    var sitePassword = "milolovestocode";
    if (passwordEntered == sitePassword)
    {
        //allow navigation
    console.log("Allow!");
 window.location.assign("members.html");   
}
    else{
        //block nav
        console.log("Block!")
        //style rule to incorrect password element
        document.getElementById("incorrect-password").style.color = "DarkOrchid";
        //text to incorrect pw
       document.getElementById("incorrect-password").innerHTML = "Incorrect password. Please try again...";
    
      
    
    }

   
}