$(document).ready(function () {
    $("#cards-box").html("");
    showArticles();
});

function openClose() {
    // id 값 post-box의 display 값이 block 이면(= 눈에 보이면)
    if ($("#post-box").css("display") == "block") {
        // post-box를 가리고
        $("#post-box").hide();
        // 다시 버튼을 클릭하면, 박스 열기를 할 수 있게 텍스트 바꿔두기
        $("#btn-post-box").text("Posting Box Open");
    } else {
        // 아니면(눈에 보이지 않으면) post-box를 펴라
        $("#post-box").show();
        // 다시 버튼을 클릭하면, 박스 닫기를 할 수 있게 텍스트 바꿔두기
        $("#btn-post-box").text("Posting Box Close");
    }
}

function postArticle() {
    // 1. user가 입력한 데이터를 #post-url과 #post-comment에서 가져오기
    let url = $('#post-url').val();
    let comment = $('#post-comment').val();

    //2. memo에 POST 방식으로 메모 생성 요청하기 
    $.ajax({
        type: "POST",
        url: "/memo",
        data: {
            url_give: url,
            comment_give :comment
        },
        success: function (response) { // 성공하면
            if (response["result"] == "success") {
                alert("포스팅 성공!");
                //3. 성공 시, 페이지 새로고침하기
                window.location.reload();
            } else{
                alert("서버오류!")
            }
        }
    })
}

function showArticles() {
    $.ajax({
        type: "GET",
        url: "/memo",
        data: {},
        success: function (response) {
            let articles = response["articles"];
            for(let i = 0; i < articles.length; i++){
                makeCard(articles[i]["url"], articles[i]["title"], articles[i]["desc"], articles[i]["comment"], articles[i]["image"])
            }
        }
    })
}

function makeCard(url, title, desc, comment, image) {
    let temp_html = `<div class="card">
                        <img class="card-img-top" src="${image}" alt="Card image cap">
                        <div class="card-body">
                            <a href="${url}" target="_blank" class="card-title">${title}</a>
                            <p class="card-text">${desc}</p>
                            <p class="card-text comment">${comment}</p>
                        </div>
                    </div>`;
    $("#cards-box").append(temp_html);

}