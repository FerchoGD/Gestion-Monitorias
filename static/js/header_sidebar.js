$(document).ready(function () {
    $("#sidebarButton").click(function () {
        $(".sideBar").toggleClass("activeSideBar");
        $(".darkscreen").toggleClass("active");
    });

    $("#sidebarButtonResp").click(function () {
        $(".sideBar").toggleClass("activeSideBar");
        $(".darkscreen").toggleClass("active");
    });

    $("#closeSideBar").click(function () {
        if ($(".sideBar").hasClass("activeSideBar")) {
            $(".sideBar").removeClass("activeSideBar");
            $(".darkscreen").removeClass("active");
        }
    });

    $(".darkscreen").click(function () {
        if ($(".sideBar").hasClass("activeSideBar")) {
            $(".sideBar").removeClass("activeSideBar");
            $(".darkscreen").removeClass("active");
        }
    });

    $("#closeSessionButton").click(function(){
    	if ($(".sideBar").hasClass("activeSideBar")) {
            $(".sideBar").removeClass("activeSideBar");
            $(".darkscreen").removeClass("active");
        }
    });

    $('.modalAlert').on('hide.bs.modal', function (e) {
    	if (e.target.id != "closeSessionModal") {
			$(".darkscreen").removeClass("active");
		}else{
			$("#closeSessionModal").modal('hide');
		}
	})
});

$(document).ready(function () {
    $('.subField').hide();
    //use event delegation since classes are changed dynamically
    $('#sideBarListMenu').on('click', '.buttonShow', function () {
        //remove the show class and assign hidden
        $('.subField').find('buttonShow').toggleClass('buttonHide buttonShow');
        $(this).toggleClass('buttonHide buttonShow');
        //the subfield is a child of the pare  nt not the next sibling
        $(this).siblings('.subField').show('slow');
    });
    $('#sideBarListMenu').on('click', '.buttonHide', function () {
        $(this).toggleClass('buttonHide buttonShow');
        $(this).siblings('.subField').hide('slow');
    });
});
