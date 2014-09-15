if (!tinymce.editors[id]) {
    settings.selector = "#" + id;
    tinymce.init(settings);
}
