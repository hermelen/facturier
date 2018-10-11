$(document).ready(function(){
    $(function() {
        $('#quotation-form div').formset();
    })
    $.fn.editable.defaults.mode = 'inline';
    $('.x-editable').editable();

    $('.x-editable').click(function(){
      $('div.editable-input input' ).keypress(function() {
        // $(this).closest('.single-line').css('background-color', 'blue');
        console.log($(this).closest('.single-line:nth-child(3)'));
      });
    });
})
