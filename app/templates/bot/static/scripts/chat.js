// collapsible
var coll = document.getElementsByClassName("collapsible");

for (let i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");

    var content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

function getTime() {
  let today = new Date();
  hours = today.getHours();
  minutes = today.getMinutes();

  if (hours < 10) {
    hours = "0" + hours;
  }

  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  let time = hours + ":" + minutes;
  return time;
}

function firstBotMessage() {
  let firstMessage = "Welcome, How can I help you?";
  document.getElementById("botStarterMessage").innerHTML =
    "<p class='botText'><span>" + firstMessage + "</span></p>";

  let time = getTime();

  $("#chat-timestamp").append(time);
  document.getElementById("userInput").scrollIntoView(false);
}

firstBotMessage();

// function getHardResponse(userText) {
//   let botResponse = getBotResponse(userText);
//   let botHTML = "<p class='botText'><span>" + botResponse + "</span></p>";
//   $("#chatBox").append(botHTML);
//   document.getElementById("chatbar-bottom").scrollIntoView(true);
// }

// function getResponse() {
//   let userText = $("#textInput").val();

//   if (userText == "") {
//     userText = "Pressed Enter";
//   }

//   let userHTML = "<p class='userText'><span>" + userText + "</span></p>";

//   $("#textInput").val("");
//   $("#chatBox").append(userHTML);
//   document.getElementById("chatbar-bottom").scrollIntoView(true);

//   setTimeout(() => {
//     getHardResponse(userText);
//   }, 1000);
// }
// function sendButton() {
//   getResponse();
// }
// // enter press
// $("#textInput").keypress(function (e) {
//   if (e.which == 13) {
//     console.log("Nazim");
//     sendButton();
//   }
// });
