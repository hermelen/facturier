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
