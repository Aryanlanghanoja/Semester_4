// var data = [
//     {
//         question: "This Is First Question" ,
//         answers: [
//             "Answer1 Option1",
//             "Answer1 Option2",
//             "Answer1 Option3",
//             "Answer1 Option4"
//         ],
//         Correect_Answer : 1
//     },
//     {
//         question: "This Is Second Question" ,
//         answers: [
//         "Answer2 Option1",
//         "Answer2 Option2",
//         "Answer2 Option3",
//         "Answer2 Option4"
//         ],
//         Correect_Answer : 2
//     },
//     {
//         question: "This Is Third Question" ,
//         answers: [
//         "Answer3 Option1",
//         "Answer3 Option2",
//         "Answer3 Option3",
//         "Answer3 Option4"
//         ],
//         Correect_Answer : 3
//     },
//     {
//         question: "This Is Fourth Question" ,
//         answers: [
//         "Answer4 Option1",
//         "Answer4 Option2",
//         "Answer4 Option3",
//         "Answer4 Option4"
//         ],
//         Correect_ANswer : 4
//     },
//     {
//         question: "This Is Fifth Question" ,
//         answers: [
//         "Answer5 Option1",
//         "Answer5 Option2",
//         "Answer5 Option3",
//         "Answer5 Option4"
//         ],
//         Correect_ANswer : 5
//     }
// ];

// var currentindex = 0;
// displayQuiz();
// function displayQuiz() {
//     document.getElementById('labelquestion').innerHTML = data[currentindex]['question'];

//     let OptionHTML = '';
    
//     OptionHTML += data[currentindex]['answers'].forEach((answer ,index) => {
//         '<div class="ans-opt" id="optfirst">' +
//             '<input type="radio" name="options" id=" ' +(index + 1) + '">' + answer + '</div>'
//     })

//     document.getElementById('answer').innerHTML = OptionHTML;
// }

// document.getElementById('labelquestion').innerText = data[currentindex]['question'];

// function onClickeNext() {
//     currentindex++;
//     displayQuiz();
// }

// function onClickePrev() {
//     currentindex--;
//     displayQuiz();
// }

// function onClickCheckAnswer() {

// }

document.getElementsByClassName('result').style.display = none;

var data = [
    {
        question: "This Is First Question" ,
        answers: [
            "Answer1 Option1",
            "Answer1 Option2",
            "Answer1 Option3",
            "Answer1 Option4"  
        ],
        Correct_Answer : 1
    },
    {
        question: "This Is Second Question" ,
        answers: [
        "Answer2 Option1",
        "Answer2 Option2",
        "Answer2 Option3",
        "Answer2 Option4"  
        ],
        Correct_Answer : 2
    },
    {
        question: "This Is Third Question" ,
        answers: [
        "Answer3 Option1",
        "Answer3 Option2",
        "Answer3 Option3",
        "Answer3 Option4"  
        ],
        Correct_Answer : 3
    },
    {
        question: "This Is Fourth Question" ,
        answers: [
        "Answer4 Option1",
        "Answer4 Option2",
        "Answer4 Option3",
        "Answer4 Option4"  
        ], 
        Correct_Answer : 4
    }
];

var AtLastDisplay = [
    {
        Correctanswer: "",
        is_Correcr: ""
    },
    {
        Correctanswer: "",
        is_Correcr: ""
    },
    {
        Correctanswer: "",
        is_Correcr: ""
    },
    {
        Correctanswer: "",
        is_Correcr: ""
    }
];

var currentindex = 0;
var Score = 0;
displayQuiz();

function displayQuiz() {
    document.getElementById('labelquestion').innerHTML = data[currentindex]['question'];

    let OptionHTML = '';

    OptionHTML += data[currentindex]['answers'].map((answer, index) => {
        return '<div class="ans-opt" id="optfirst">' + 
            '<input type="radio" name="options" value="' + (index + 1) + '">' + answer + '</div>';
    }).join('');

    document.getElementById('answer').innerHTML = OptionHTML;
}

function onClickeNext() {
    var selectedRadioButton = document.querySelector('input[type="radio"]:checked');

    if (selectedRadioButton) {
        var radioButtonsValue = selectedRadioButton.value;

        if (radioButtonsValue == data[currentindex]['Correct_Answer']) {
            AtLastDisplay[currentindex]['is_Correcr'] = true;
            Score++;
        } else {
            AtLastDisplay[currentindex]['is_Correcr'] = false;
        }

        AtLastDisplay[currentindex]['Correctanswer'] = data[currentindex]['answers'][data[currentindex]['Correct_Answer']];

        currentindex++;

        if (currentindex == data.length) {
            alert('Quiz Over');
            document.getElementsByClassName('result').style.display = block;

            let result_display = '';

            

        } else {
            displayQuiz();
        }
    } else {
        alert('Please select an answer before proceeding.');
    }
}


function onClickePrev() {
    currentindex--;
    displayQuiz();
}

// function onClickCheckAnswer() {
//     var radioButtons = document.querySelector('input[type="radio"]:checked').value;
    
//     if (radioButtons == data[currentindex]['Correct_Answer']) {
//         alert("Perfect Answer");
//     }

//     else {
//         alert("Better Luck Next Time");
//     }

// }
