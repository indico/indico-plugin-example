$(document).ready(function() {
    var $t = window.$t_example = $T.domain('example');
    $('#js-msg').text($t.gettext('This message was generated using JavaScript'));
    $('#yes-msg').text($T.gettext('Edit'));
});
