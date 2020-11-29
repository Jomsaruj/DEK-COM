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

function show_subcomment_reply(_show) {
    var btn = _show;
    var text_area = btn.parentElement.nextElementSibling;
    console.log(text_area)
    if (text_area.style.display == "none") {
        text_area.style.display = "";
        btn.innerHTML = "hide..";
    }
    else {
        text_area.style.display = "none";
        btn.innerHTML = "reply comment..";
    }
}

function show_more_coomet() {
    var comment_list = document.querySelectorAll(".comment-list");
    var show_count = 0;
    for (i=0; i<comment_list.length; i++) {
        if (comment_list[i].style.display == "none") {
            comment_list[i].style.display = "";
            show_count++;
        }
        if (show_count >= 5) {
            break;
        }
    }
}

function add_tag() {
    var tag_name = document.getElementById("tag-input").value.trim();
    document.getElementById("tag-input").value = "";
    if (String(tag_name).length === 0) {
        return;
    }
    var num = document.getElementById("tags-container").childElementCount;
    var tag = document.createElement("input");
    tag.setAttribute("type", "text");
    tag.setAttribute("name", "tag[" + String(num) + "]");
    tag.setAttribute("value", tag_name);
    tag.style.display = "none";
    
    var tag_display = document.createElement("div");
    tag_display.classList.add("tag-display");
    tag_display.id = tag_name;
    tag_display.innerHTML = `<label>` + tag_name + `</label><div onclick="delete_tag('` + tag_name +`')">&#10006;</div>`;

    if (document.getElementById("tags-container").childElementCount < 7) {
        var exist_tag = document.getElementById(tag_name);
        if (!document.getElementById("tags-container").contains(document.getElementById(tag_name))) {
            tag_display.append(tag);
            document.getElementById("tags-container").append(tag_display);
        }
    }


}

function delete_tag(tag_id) {
    var tag = document.getElementById(tag_id);
    document.getElementById("tags-container").removeChild(tag);
}

function add_choice() {
    var num = document.getElementById("choices-container").childElementCount;
    var choice = document.createElement("input");
    choice.setAttribute("name", "choice[" + String(num) + "]");

    var color = document.createElement("input");
    color.setAttribute("type", "color")
    color.setAttribute("name", "color[" + String(num) + "]");
    
    var choice_display = document.createElement("div");
    choice_display.classList.add("choice-display");
    choice_display.id = 'choice' + String(num)
    choice_display.append(choice, color);
    choice_display.innerHTML += `<div onclick="delete_choice('choice` + String(num) + `')">  &#10006;</div>`;

    document.getElementById("choices-container").append(choice_display);
} 


function delete_choice(choice_id) {
    var choice = document.getElementById(choice_id);
    document.getElementById("choices-container").removeChild(choice);
}

function show_candidate(_this) {
    var candidates = _this.nextElementSibling.nextElementSibling;
    var text = _this.children[0]
    if (candidates.style.display == "none") {
        candidates.style.display = "";
        text.innerHTML = "Hide candidates"
    }
    else {
        candidates.style.display = "none";
        text.innerHTML = "Show candidates"
    }
}