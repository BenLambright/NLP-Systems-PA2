document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("toggleButton").addEventListener("click", function () {
        var commentBox = document.getElementById("hiddenForm")
        if (commentBox.style.display === "none" || commentBox.style.display === "") {
            commentBox.style.display = "block";
        } else {
            commentBox.style.display = "none";
        }
    })
    }
);
