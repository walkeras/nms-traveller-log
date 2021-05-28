
// On page load
$(document).ready(function(){
    // Dynamically add 'sortBy' param to Systems page navigation links when they are clicked
    $("#systems .page-link").bind("click", function() {
        let href = $(this).attr('href');
        $(this).attr('href', href + '&sortBy=' + $('#systemSortBy').children("option:selected").val());
    });

    // Dynamically add 'category' param to Gallery page navigation links when they are clicked
    $("#gallery .page-link").bind("click", function() {
        let href = $(this).attr('href');
        $(this).attr('href', href + '&' + getGalleryParams());
    });

    // Sort Systems immediately when sort option changed
    $("#systemSortBy").change(function() {
        $("#systemSortByForm").submit()
    });

    // Set Game Session cookie immediately when option changed
    $("#gameSession").change(function() {
        document.cookie = "game_session=" + $("#gameSession").children("option:selected").val() + ";path=/";
    });
    

    // Gallery category view buttons
    $("#galleryViewForm .toggle-btn").each(function(idx) {
        $(this).bind("click", function() {
            if ( $(this).attr('id') === 'gallery_view_all') return;
            if ( $(this).attr('id') === 'gallery_view_submit') return;
            // Toggle presence of 'data' attribute to keep button state
            if ( $(this).attr('data')) {
                $(this).removeAttr('data').removeClass("btn-success").addClass("btn-outline-secondary")
            } else {
                $(this).attr('data', 'on').removeClass("btn-outline-secondary").addClass("btn-success")
            };
            // Un-set "All" button if any category button is currently enabled
            let btn_enabled = false;
            $("#galleryViewForm :button").each(
                function(idx) {
                    if ( $(this).attr('id') === 'gallery_view_all') return;
                    if ( $(this).attr('data') ) {
                        btn_enabled = true;
                    }
                }
            );
            if (btn_enabled) {
                $("#gallery_view_all").removeClass("btn-success").addClass("btn-outline-secondary")
            } else {
                $("#gallery_view_all").removeClass("btn-outline-secondary").addClass("btn-success")
            }
        });
    });

    $("#gallery_view_submit").bind("click", function(){
        let href = $('#galleryViewForm').attr('href') + "?" + getGalleryParams();        
        $('#galleryViewForm').attr('href', href);
        $('#galleryViewForm').prop('action', href);
        window.location = href;
        return false;
    });
    
});

function getGalleryParams() {
    let params = ''
    $("#galleryViewForm .toggle-btn").each(
        function(idx) {
            if ( $(this).attr('id') === 'gallery_view_all') return '';

            if ( $(this).attr('data') ) {
                if (!params.includes('category')) {
                    params += 'category=' + $(this).val();
                } else {
                    params += ' ' + $(this).val();
                }
            }
        }
    );
    return params;
}
