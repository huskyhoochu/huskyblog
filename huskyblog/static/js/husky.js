//메인 헤더 블러 기능 추가
$(window).scroll(function () {
  $( "#main-nav" ).addClass( "blurredclass" );
});


//모바일 적용 시 햄버거 메뉴 클릭 버튼 활성화
$(document).ready(function () {
    $('.burger').click(function () {
        $('.navbar-menu').toggleClass('active')
    })
})