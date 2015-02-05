$(document).ready(function() {
    var $t = $T.domain('example');
    $('#js-msg').text($t.gettext('This message was generated using JavaScript'));
    $('#yes-msg').text($T.gettext('Edit'));
});
