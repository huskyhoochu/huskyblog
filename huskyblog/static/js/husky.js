//모바일 적용 시 햄버거 메뉴 클릭 버튼 활성화
$(document).ready(function () {
    $('.burger').click(function () {
        $('.navbar-menu').toggleClass('active')
    })
})