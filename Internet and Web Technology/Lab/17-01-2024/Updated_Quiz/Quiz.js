var data = [
    {
        question: "This Is First Question" ,
        answers: [
            "Answer1 Option1",
            "Answer1 Option2",
            "Answer1 Option3",
            "Answer1 Option4"
        ],
        Correect_Answer : 1
    },
    {
        question: "This Is Second Question" ,
        answers: [
        "Answer2 Option1",
        "Answer2 Option2",
        "Answer2 Option3",
        "Answer2 Option4"
        ],
        Correect_Answer : 2
    },
    {
        question: "This Is Third Question" ,
        answers: [
        "Answer3 Option1",
        "Answer3 Option2",
        "Answer3 Option3",
        "Answer3 Option4"
        ],
        Correect_Answer : 3
    },
    {
        question: "This Is Fourth Question" ,
        answers: [
        "Answer4 Option1",
        "Answer4 Option2",
        "Answer4 Option3",
        "Answer4 Option4"
        ],
        Correect_ANswer : 4
    },
    {
        question: "This Is Fifth Question" ,
        answers: [
        "Answer5 Option1",
        "Answer5 Option2",
        "Answer5 Option3",
        "Answer5 Option4"
        ],
        Correect_ANswer : 5
    }
];

currentIndex = 0;

function DisplayQuiz() {

}

function onClickeNextButton() {
    currentIndex++;
}

function onClickePreviousButton() {
    currentIndex--;

}

function onClickCheckAnswer() {

}