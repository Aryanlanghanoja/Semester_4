var data = [
  {
    question: "This is first question",
    answers: ["ans1 opt1", "ans1 opt2", "ans1 opt3", "ans1 opt4"],
    correct_opt: 1,
  },
  {
    question: "This is second question",
    answers: ["ans2 opt1", "ans2 opt2", "ans2 opt3", "ans2 opt4"],
    correct_opt: 2,
  },
  {
    question: "This is third question",
    answers: ["ans3 opt1", "ans3 opt2", "ans3 opt3", "ans3 opt4"],
    correct_opt: 3,
  },
  {
    question: "This is fourth question",
    answers: ["ans4 opt1", "ans4 opt2", "ans4 opt3", "ans4 opt4"],
    correct_opt: 4,
  },
];

var currInd = 0;
var response = [];
displayQuiz();

function displayQuiz() {
  document.getElementById("labelQuestion").innerText = data[currInd]["question"];
  let optHtml = "";
  data[currInd]["answers"].forEach((answer, index) => {
    optHtml +=
      ' <div class="ans-opt" id="opt_' +
      (index + 1) +
      '">' +
      '<input type="radio" name="options" value="' +
      (index + 1) +
      '"';
    
    if (response[currInd] && response[currInd]["res"] == index + 1) {
      optHtml += 'checked = "checked"';
    }

    optHtml += ">" + 
      answer +
      "</div>";
  });

  document.getElementById("answer").innerHTML = optHtml;

  if (currInd == 0) {
    document.getElementById("btnPrev").style.display = "none";
  } else {
    document.getElementById("btnPrev").style.display = "inline";
  }

  if (currInd == data.length - 1) {
    document.getElementById("btnNext").style.display = "none";
    document.getElementById("btnCheckResult").style.display = "inline";
  } else {
    document.getElementById("btnNext").style.display = "inline";
    document.getElementById("btnCheckResult").style.display = "none";
  }
}

function onClickNext() {
  checkAnswer();
  currInd++;
  displayQuiz();
}

function onClickPrev() {
  currInd--;
  displayQuiz();
}

function checkAnswer() {
  var val = document.querySelector('input[type="radio"]:checked').value;
  if (val == data[currInd]["correct_opt"]) {
    response[currInd] = { res: val, istrue: true };

    alert("Good work");
  } else {
    response[currInd] = { res: val, istrue: false };
    alert("Oops you miss");
  }
}

function onClickResult() {
  checkAnswer();
  var html = "";
  response.forEach((resp, index) => {
    html +=
      "<p>Ques " +
      (index + 1) +
      ": option selected :" +
      resp.res +
      " istrue: " +
      resp.istrue +
      " </p>";
  });
  document.getElementById("displayresult").innerHTML = html;
}


function addQuestion() {
  let newquestion = document.getElementById('txtQuestion').value;
  let option1 = document.getElementById('txtOpt1').value;
  let option2 = document.getElementById('txtOpt2').value;
  let option3 = document.getElementById('txtOpt3').value;
  let option4 = document.getElementById('txtOpt4').value;
  let correctopt = parseInt(document.getElementById('corrAns').value);
  data.push ({ question: newquestion, answers: [option1, option2, option3, option4 ], correct_opt: correctopt });
}



