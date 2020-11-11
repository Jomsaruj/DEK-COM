function show_comment_reply() {
    var btn = document.getElementById("show-comment-reply");
    var text_area = document.getElementById("comment-reply");
    if (text_area.style.display == "none") {
        text_area.style.display = "";
        btn.innerHTML = "hide..";
    }
    else {
        text_area.style.display = "none";
        btn.innerHTML = "write comment..";
    }
}

function show_subcomment_reply() {
    var btn = document.getElementById("show-subcomment-reply");
    var text_area = document.getElementById("subcomment-reply");
    if (text_area.style.display == "none") {
        text_area.style.display = "";
        btn.innerHTML = "hide..";
    }
    else {
        text_area.style.display = "none";
        btn.innerHTML = "write comment..";
    }
}