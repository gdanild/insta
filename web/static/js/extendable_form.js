(function(){
let answerHTML = `
<input name = "q{name}" class="form-control question_input" placeholder="Ответ {answer}">
<div class="answer_icon"></div>
<div class="delete">
 <span class="glyphicon glyphicon-remove"></span>
</div>
<div class="invalid-feedback"> <strong>Ошибка:</strong> данное поле не может быть пустым</div>
`;

function on_click()
{
    if (num_questions > 2) answer_filed.removeChild(this.parentElement);
    num_questions = answer_filed.children.length;
    for (let i = 0; i < num_questions; i ++)
    {
        answer_filed.children[i].firstElementChild.placeholder = "Ответ " + (i+1);
        answer_filed.children[i].firstElementChild.name = "q" + (i+ 1);
    }
}
let num_questions = 2;
let answer_filed = $("#answers_field")[0];
function update_el(){
    let buttons = $(".delete");
    for (let e = 0; e < buttons.length; e ++){
        buttons[e].onclick = on_click;
    }
}
update_el();
$("#add_answer").on('click', function(){
    num_questions ++;
    let elem = document.createElement("div");
    elem.classList.add('form-group');
    elem.innerHTML = answerHTML.replace("{answer}", num_questions).replace("{name}", num_questions);
    answer_filed.appendChild(elem);
    update_el();
});
$("#send_question").on('submit', function () {
    let questions = $(".question_input");
    let success = true;
    for (let e = 0; e < questions.length; e ++){
       if (questions[e].value.match(/^\s*$/i) != null) {
            questions[e].value = '';
            success = false;
            questions[e].classList.add('is-invalid');
       }
       else{
        this.classList.remove('is-invalid');
       }
    }
    return success;
});
})();
