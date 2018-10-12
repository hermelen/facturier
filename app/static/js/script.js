$(document).ready(function(){

    $('#quotation-form div').formset();


    $.fn.editable.defaults.mode = 'inline';
    $('.x-editable').editable();

    var total_initial = 0;

    var each_line = $('.single-line').each(function(){
      var single_line = $(this).closest('.single-line');
      var total_field = single_line.find('.total-field');
      var price = single_line.find('.price-field').html();
      var quantity = single_line.find('.td-editable a').html();
      var price_dot = price.replace(',', '.');
      var total = (price_dot * quantity).toFixed(2);
      var str_total = total.toString()
      var total_comma = str_total.replace('.', ',');
      total_field.html(total_comma);

      total_initial += (price_dot * quantity);
    });

    total_initial = total_initial.toFixed(2).toString();
    total_initial = total_initial.replace('.', ',');

    $('.total').html(total_initial);




    $('.x-editable').click(function(){
      var total_quotation = 0
      $('button.editable-submit').click(function() {
        var single_line = $(this).closest('.single-line');
        var total_field = single_line.find('.total-field');
        var price = single_line.find('.price-field').html();
        var quantity = $('div.editable-input input').val();
        var price_dot = price.replace(',', '.');
        var total = (price_dot * quantity).toFixed(2);
        var str_total = total.toString()
        var total_comma = str_total.replace('.', ',');
        total_field.html(total_comma);

        var each_line = $('.single-line').each(function(){
          var single_line = $(this).closest('.single-line');
          var total = single_line.find('.total-field').html();
          total = total.replace(',','.');
          total_quotation += parseFloat(total);
          console.log(total_quotation);
        });

        total_quotation = total_quotation.toFixed(2);
        total_quotation = total_quotation.replace('.', ",");
        $('.total').html(total_quotation);
      });
    });
})
