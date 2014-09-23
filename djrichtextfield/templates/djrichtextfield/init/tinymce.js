function fixCallbacks(settings) {
    /* Takes a settings object. Converts known callback keys to global
     * window functions. */
    var callback, callbacks = [
        'setup', 'init_instance_callback', 'color_picker_callback',
        'file_picker_callback', 'file_browser_callback'
    ];
    while (callback = callbacks.pop()) {
        if (callback in settings && window[settings[callback]]) {
            settings[callback] = window[settings[callback]];
        }
    }
    return settings;
}
if (!tinymce.editors[id]) {
    settings.selector = "#" + id;
    tinymce.init(fixCallbacks(settings));
}
