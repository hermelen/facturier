$('.delete-btn').click(function(){
    var idButton = $(this).attr('id')
    deleteCommand(idButton);
})
function deleteCommand(idButton) {
   var url = $('.delete-btn').attr('action');
   $.ajax({
     url: url,
     type: "POST",
     data: idButton,
     success: function() {
       console.log('success');
         $('#tr-'+idButton).remove();
     },
     error: function () {
       console.log('error');
     }
   });
}

$('#line-to-add').hide();
// $('.create-btn').hide();


$('.add-btn').click(function(){
  // $('.create-btn').show();
  $('#line-to-add').show();
  $('.create-btn').click(function(){
      // createCommand();
  });
});

// function createCommand() {
//   var url = $('.add-btn').attr('action');
//   $.ajax({
//     url: url,
//     type: "POST",
//     data: idButton,
//     success: function() {
//       console.log('success');
//         $('#tr-'+idButton).remove();
//     },
//     error: function () {
//       console.log('error');
//     }
//   });
// }
