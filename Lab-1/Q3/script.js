let backgroundColor = "red";
let fontFace = "Arial";
let borderStyle = "none";
let defaultPicture = false;
let greetingText = "";

function populateFields() {
    backgroundColor = $("#bg-color").val();
    fontFace = $("#font-face").val();
    defaultPicture = $("#default-picture").is(":checked");
    greetingText = $("#greeting-text").val();

    if ($("#border-style-none").is(":checked"))
        borderStyle = "none";
    else if ($("#border-style-double").is(":checked"))
        borderStyle = "double";
    else if ($("#border-style-solid").is(":checked"))
        borderStyle = "solid";
}

function generateCard() {
    $("#birthday-card").css({
        "background-color": backgroundColor,
        "font-family": fontFace,
        "border": borderStyle
    });

    $("#birthday-text").text(greetingText);

    if (defaultPicture)
        $("#birthday-img").attr("src", "image.jpg");
}

$("button").click(() => {
    event.preventDefault();
    populateFields();
    generateCard();
});
