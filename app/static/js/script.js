$(document).ready(function(){
    $(function() {
        $('#quotation-form div').formset();
    })
    $.fn.editable.defaults.mode = 'inline';
    $('.x-editable').editable();

    $('.x-editable').click(function(){
      $('div.editable-input input' ).keypress(function() {
        // $(this).closest('.single-line').css('background-color', 'blue');
        var container = $(this).closest('.single-line').find('.total-line');
        container.html('toto');
      });
    });
})
