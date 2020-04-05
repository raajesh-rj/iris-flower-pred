// $(document).ready(function() {
//     $('.response').hide();
//     $("#iris_form").submit(function() { // catch the form's submit event
//         $.ajax({ // create an AJAX call...
//             data: $(this).serialize(), // get the form data
//             type: $(this).attr('POST'), 
//             success: function(response) { // on success..
//                 $(".response").show();
//                 $(".response").html(response); // update the DIV
//             }
//         });
//         return false;
//     });
// });