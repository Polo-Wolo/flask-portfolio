$(document).ready(function () {
    console.log("Document ready !!!");

    document.addEventListener('scroll', function (ev) {
        onScrollHandle();
    }, true)

    document.getElementById("burger").addEventListener("click", toggleBurger);

    function onScrollHandle() {

        //Get current scroll position
        var currentScrollPos = $(document).scrollTop();

        //Iterate through all node
        $('#navbar > ul > li > a').each(function () {
            var curLink = $(this);
            var refElem = $(curLink.attr('href'));
            //Compare the value of current position and the every section position in each scroll
            if (refElem.position().top <= currentScrollPos && refElem.position().top + refElem.height() > currentScrollPos) {
                //Remove class active in all nav
                //$('#navbar > ul > li').removeClass("active");
                //Add class active
                curLink.parent().addClass("active");
            }
            else {
                curLink.parent().removeClass("active");
            }
        });
    }

    let menu_on = 0;
    function toggleBurger() {
        menu_on = !menu_on;
        /*
        if (menu_on) {
            menu_on = 0;
        } else {
            menu_on = 1;
        }*/
        console.log("menu_on :", menu_on);
    }
});