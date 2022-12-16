$(document).ready(function () {
    document.getElementById("myBtn").style.bottom = "-4rem";
    window.onscroll = function() {onScrollTopButton()};

    console.log("Document ready !");

    document.addEventListener('scroll', function (ev) {
        onScrollHandle();
    }, true)

    document.getElementById("burger").addEventListener("click", togglePanel);
    document.getElementById("panel-outside").addEventListener("click", togglePanel);

    var mobile_link_elems = document.getElementsByClassName("mobile-link");
    for (var i = 0; i < mobile_link_elems.length; i++) {
        mobile_link_elems[i].addEventListener('click', togglePanel, false);
    }

    var burger_elems = document.getElementsByClassName("burger-elem");

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

    var menu_on = 0;
    function togglePanel() {
        menu_on = !menu_on;
        if (menu_on) {
            // show panel
            document.getElementById("panel").classList.add("panel-active");
            // add active class to burger elems
            for (var i = 0; i < burger_elems.length; i++) {
                switch (i) {
                    case (0):
                        burger_elems[0].classList.add("burger-elem-active1");
                    case (1):
                        burger_elems[1].classList.add("burger-elem-active2");
                    case (2):
                        burger_elems[2].classList.add("burger-elem-active3");
                    default: break;
                }
            }
        } else {
            // hide panel
            document.getElementById("panel").classList.remove("panel-active");
            // remove active class to burger elems
            for (var i = 0; i < burger_elems.length; i++) {
                switch (i) {
                    case (0):
                        burger_elems[0].classList.remove("burger-elem-active1");
                    case (1):
                        burger_elems[1].classList.remove("burger-elem-active2");
                    case (2):
                        burger_elems[2].classList.remove("burger-elem-active3");
                    default: break;
                }
            }
        }
        console.log("menu_on :", menu_on);
    }

    function onScrollTopButton() {
        /* Top Button */
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("myBtn").style.bottom = "2rem";
        } else {
            document.getElementById("myBtn").style.bottom = "-4rem";
        }
    }
});