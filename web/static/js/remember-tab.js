$(function() {
    $('a[data-toggle="tab"]').on('click', function(e) {
        window.localStorage.setItem('activeTab', $(e.target).attr('href'));
    });
    let activeTab = window.localStorage.getItem('activeTab');
    if (activeTab) {
        $('#myTab a[href="' + activeTab + '"]').tab('show');
    }
});