//메인 헤더 쉐도우 기능 추가
$(window).scroll(function () {
  $( "#main-nav" ).css('box-shadow', '0 3px 13px 0 rgba(2, 3, 3, 0.16)');
});


//모바일 적용 시 햄버거 메뉴 클릭 버튼 활성화
$(document).ready(function () {
    $('.burger').click(function () {
        $('.navbar-menu').toggleClass('active')
    })
})