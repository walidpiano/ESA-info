$('document').ready(function(){

    $.ajaxSetup ({
        // Disable caching of AJAX responses
        cache: false
    });


    window.onscroll = function() {myFunction()};
    var header = document.getElementById("header-to-stick");
    var sticky = header.offsetTop;

    function myFunction() {
        if (window.pageYOffset >= sticky) {
            header.classList.add("sticky");
        }
        else
        {
            header.classList.remove("sticky");
        }
    }
})