/*
The following JS variables are available from the calling function:

$e: jQuery wrapped textarea to be replaced
id: The value of the id attribute of this textarea
settings: The parsed JSON data attribute of the textarea
*/
if (!CKEDITOR.instances[id]) {
    CKEDITOR.replace(id, settings);
}
