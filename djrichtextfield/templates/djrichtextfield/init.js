(function (d) {
    var default_settings = {{ default_settings }};

    function initField(field) {
        if (field.closest('.empty-form')) return;  // Don't do empty inlines
        var id = field.id;
        var custom_settings = {};
        if (field.dataset.fieldSettings) {
            custom_settings = JSON.parse(field.dataset.fieldSettings);
        }
        var settings = Object.assign({}, default_settings, custom_settings);
        {% include init_template %}
    }

    function initFields(parent) {
        var richTextFields = parent.querySelectorAll('textarea.djrichtextfield');
        for (var i = 0; i < richTextFields.length; i++) {
            initField(richTextFields[i])
        }
    }

    addEventListener('DOMContentLoaded', function () {
        initFields(d);

        d.body.addEventListener('click', function(evt) {
            // initialize the editor after adding an inline
            var addRow = evt.target.closest('.add-row');
            if(!addRow) return;
            setTimeout(function() {
                initFields(addRow.parentNode);
            }, 0);
        }, true);
    });
})(document);
