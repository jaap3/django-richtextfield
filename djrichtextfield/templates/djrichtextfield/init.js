(function ($) {
    var default_settings = {{ default_settings }};

    function initField($e) {
        if ($e.parents('.empty-form').length == 0) {  // Don't do empty inlines
            var id = $e.attr('id');
            var custom_settings = {};
            if ($e.attr('data-field-settings')) {
                custom_settings = $.parseJSON($e.attr('data-field-settings'));
            }
            var settings = $.extend({}, default_settings, custom_settings);
            {% include init_template %}
        }
    }

    $(function () {
        // initialize the editors on load
        $('textarea.djrichtextfield').each(function () {
            initField($(this));
        });

        // initialize the editor after adding an inline
        // XXX: We don't use jQuery's click event as it won't work in Django 1.4
        document.body.addEventListener("click", function(ev) {
            if(!ev.target.parentNode || ev.target.parentNode.className.indexOf("add-row") === -1) {
                return;
            }
            var $addRow = $(ev.target.parentNode);
            setTimeout(function() {  // We have to wait until the inline is added
                $('textarea.djrichtextfield', $addRow.parent()).each(function () {
                    initField($(this));
                });
            }, 0);
        }, true);
    });
}(django.jQuery));
