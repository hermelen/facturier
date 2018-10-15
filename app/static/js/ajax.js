$('.delete-btn').click(function(){
    var url = $(this).data('url');
    $.ajax({
      url: url,
      type: "POST",
      success: function() {
        console.log('success');
        $(this).remove();
      },
      error: function () {
        console.log('error');
      }
    });
})


$('#line-to-add').hide();
// $('.create-btn').hide();



$('#line-to-add').show();


$(document).ready(function(){
  $('#product_list_form').submit(function(event){
    var url = $(this).attr('action');
    $.ajax({
      url: url,
      type: "POST",
      data: $(this).serializeArray(),
      success: function(response) {
        console.log(response);
        //         $('#tr-'+idButton).remove();
      },
      error: function () {
        console.log('error');
      }
    });
    event.preventDefault();
  });

})
