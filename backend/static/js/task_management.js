// task_management.js


$(function() {
    $(".task-item").draggable({
        revert: "invalid",
        cursor: "move",
        opacity: 0.7,
        helper: "clone",
    });
    $(".column").droppable({
        drop: function(event, ui) {
            var droppedItem = ui.draggable;
            var targetColumn = $(this);
            droppedItem.appendTo(targetColumn);

          var taskId = droppedItem.attr("id").replace("task", "");

          var newStatus = targetColumn.attr("id");

          console.log("Task ID:", taskId);
          console.log("New Status:", newStatus);

          updateTaskStatus(taskId, newStatus);
        }
    });
});


function updateTaskStatus(taskId, newStatus) {
    var csrfToken = $('#csrf-form input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type: "POST",
        url: "/update_task_status/", 
        data: {
            task_id: taskId,
            new_status: newStatus,
            csrfmiddlewaretoken: csrfToken
        },
        success: function(data) {
            console.log(data)
            var taskElement = $('#task' + taskId);
            var targetColumn = $('#' + newStatus);
            
            taskElement.appendTo(targetColumn);
            console.log("Task status updated successfully. New status name:", data.new_status_name);
        },
        error: function(xhr, status, error) {
            console.error("Error updating task status:", error);
            console.error("Server response:", xhr.responseText);

        }
    });
}
