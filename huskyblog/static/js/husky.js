//메인 헤더 쉐도우 기능 추가
$(window).scroll(function () {
  $( "#main-nav" ).css('box-shadow', '0 3px 13px 0 rgba(2, 3, 3, 0.16)');
});


//모바일 적용 시 햄버거 메뉴 클릭 버튼 활성화
$(document).ready(function () {
    $('.burger').click(function () {
        $('.navbar-menu').toggleClass('active')
    })
});

//타일 박스 애니메이션

$(window).ready(function () {
    $('#tile-box').hide()
});

$(window).scroll(function(){
	if($(window).scrollTop() > 300){
		$('#tile-box').fadeIn('1000');
	}else if($(window).scrollTop() < 300){
		$('#tile-box').fadeOut('1000');
	}
});

// 마크다운 적용
$(document).ready(function () {
    $('#post-article').each(function () {
        var content = $('#post-article').text();
        var markedContent = marked(content);
        $(this).html(markedContent)
    })
});

//highlights.js
$(document).ready(function() {
    $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);
    });
});
