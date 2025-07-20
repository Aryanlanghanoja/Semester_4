// Get DOB and Addmission Date and Find That User is Eligible for Profeessional Years.

function ChecckElibibility() {
    var DOB = document.getElementById('DOB').value;
    var AddmissionDate = document.getElementById('Addmission_Date').value;
    var ReferenceDate = new Date(DOB.getFullYear() + '12-31');
    DOB = new Date(DOB);
    AddmissionDate = new Date(AddmissionDate);
    
    var Years = DOB.getFullYear() - ReferenceDate.getFullYear();

    if (Years == 0 && DOB.getMonth() < AddmissionDate.getMonth()) {
        Years--;
    }
    if (Years == 0 && DOB.getDate() < AddmissionDate.getDate()) {
        Years--;
    }

    // if (Years >= 18) {
    //     alert("You are not eligible for Profeessional Years");
    // } else {
    //     alert("You are eligible for Profeessional Years");
    // }
}

// Task - 0 :- Calculate Age ;
// Task - 1 :- Check Aligibility For Addmissions You HAve to Take Reference Date of The as 31st December of the Addmission Year if the Person is 17 or more he/she is Eligible
// Task- 2:-  Display After How may years the person is eligible