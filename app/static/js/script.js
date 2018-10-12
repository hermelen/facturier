$(document).ready(function(){
    $(function() {
        $('#quotation-form div').formset();
    })
    $.fn.editable.defaults.mode = 'inline';
    $('.x-editable').editable();

    $('.x-editable').click(function(){
      $('button.editable-submit').click(function() {
        var single_line = $(this).closest('.single-line');
        var total_field = single_line.find('.total-field');
        var price = single_line.find('.price-field').html();
        var quantity = $('div.editable-input input').val();
        var price_dot = price.replace(',', '.');
        var total = price_dot * quantity;
        // var total_comma = total.replace('.', ',');
        total_field.html(total);
      });
    });
})
