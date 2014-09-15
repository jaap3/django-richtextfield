/*
The following JS variables are available from the calling function:

$e: jQuery wrapped textarea to be replaced
id: The `id` attribute of this textarea
default_settings: `DJRICHTEXTFIELD_CONFIG['settings']` as a JS object
custom_settings: The parsed value of `data-field-settings`
settings: Merge of `default_settings` and `custom_settings`
*/
if (!CKEDITOR.instances[id]) {
    CKEDITOR.replace(id, settings);
}
