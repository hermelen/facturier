$(document).ready(function(){
$('.delete-btn').click(function(){
    var parent = $(this).parents('.single-line');
    var url = $(this).data('url');
    $.ajax({
      url: url,
      type: "POST",
      data:parent,
      success: function() {
        parent.remove();
        console.log('success');
      },
      error: function () {
        console.log('error');
      }
    });
})

$('#line-to-add').hide();
$('#line-to-add').show();


  $('#product_list_form').submit(function(event){
    var url = $(this).attr('action');
    $.ajax({
      url: url,
      type: "POST",
      data: $(this).serializeArray(),
      success: function(response) {
        $('#line-to-add').before(
            `<tr class="single-line" id="tr-${ response.id }">
                <th scope="row">${ response.productName }</th>
                <td class="td-editable"><a class="x-editable-quantity" data-url="${ response.editable_data_url }">${ response.quantity }</a></td>
                <td class="price-field">${ response.price }</td>
                <td class="total-field">${ response.price*response.quantity }</td>
                <td class="operations">
                    <button data-url="${ response.del_button_data_url }" type="button" class="btn btn-warning delete-btn">Delete</button>
                </td>
            </tr>`)

        $('input').val(''); // empty input field
        $('select').prop('selectedIndex',0); // reset select field
        console.log(response);
      },
      error: function () {
        console.log('error');
      }
    });
    event.preventDefault();
  });
})



// function deleteCommand(svCommandId) {
//             var url = $('#service_command_form').attr('action') + svCommandId;
//             $.ajax({
//                 url: url,
//                 type: "DELETE",
//                 dataType: "json",
//                 beforeSend: function (xhr) {
//                     xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
//                 },
//                 success: function () {
//                     $('#service_command_' + svCommandId).remove();
//                     addMessage("Deleted data successfully");
//                 },
//                 error: function () {
//                     addMessage("Delete failed!");
//                 }
//             });
