(function ($) {
    function initWysiwyg($e) {
        if ($e.parents('.empty-form').length == 0) {  // Don't do empty inlines
            var id = $e.attr('id');
            var settings = $.parseJSON($e.attr('data-wysiwyg-settings'));
            {{ init|safe }}
        }
    }

    $(function () {
        // initialize the WYSIWYG editors on load
        $('textarea.djwysiwyg').each(function () {
            initWysiwyg($(this));
        });

        // initialize the WYSIWYG editor after adding an inline
        // XXX: We don't use jQuery's click event as it won't work in Django 1.4
        document.body.addEventListener("click", function(ev) {
            if(!ev.target.parentNode || ev.target.parentNode.className.indexOf("add-row") === -1) {
                return;
            }
            var $addRow = $(ev.target.parentNode);
            setTimeout(function() {  // We have to wait until the inline is added
                $('textarea.djwysiwyg', $addRow.parent()).each(function () {
                    initWysiwyg($(this));
                });
            }, 0);
        }, true);
    });
}(django.jQuery));
