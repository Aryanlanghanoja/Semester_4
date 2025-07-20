var Blog = [];

function btnreset() {
    document.getElementById('inputname').value = '';
    document.getElementById('inputtitle').value = '';
    document.getElementById('inputurl').value = '';
    document.getElementById('inputdescription').value = '';
}

function btnsubmit() {
    var authorName = document.getElementById('inputname').value;
    var blogTitle = document.getElementById('inputtitle').value;
    var imageUrl = document.getElementById('inputurl').value;
    var blogDescription = document.getElementById('inputdescription').value;

    if (authorName == '' || blogTitle == '' || imageUrl == '' || blogDescription == '') {
        alert("Enter Approriate Details for Blog....");
    }

    else {

        var new_blog = `
        <div id="Blog">
                <h2 id="title">
                    <center>${blogTitle}</center>
                </h2>
            <div id="AuthorName">
                <b>Author Name :- </b>${authorName}
            </div>
            <div id="Image">
                <center>
                <img src="${imageUrl}" alt="Blog Image" height="300px" width="500px">
                </center>
            </div>
            <div id="Description">
                <p>${blogDescription}</p>
            </div>
        </div>
    `;

        Blog = [new_blog, ...Blog];
        document.getElementById('Container').innerHTML = Blog;

        document.getElementById('inputname').value = '';
        document.getElementById('inputtitle').value = '';
        document.getElementById('inputurl').value = '';
        document.getElementById('inputdescription').value = '';
    }
}
