function deleteCommand(svCommandId) {
           var url = $('.delete-btn').attr('action');
           $.ajax({
               url: url,
               type: "DELETE",
               dataType: "json",
               beforeSend: function (xhr) {
                   xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
               },
               success: function () {
                   $('#service_command_' + svCommandId).remove();
                   addMessage("Deleted data successfully");
               },
               error: function () {
                   addMessage("Delete failed!");
               }
           });
