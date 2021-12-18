$("#emailmodif").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this);
    $.ajax({
           type: "POST",
           url: "/modify",
           data: form.serialize(), // serializes the form's elements.
           success: function(data)
           {
                $("#emailSpan").text(data.email);
                $("#CloseModal").click(); // close modal
                $("#email").placeholder = data.email;
                $("#email").value = data.email;

           }
    });
});











/*$("#emailmodif").on( "submit", function(e) {
    var dataString = $(this).serialize();
    alert(dataString);
    console.log('error');
    return false;
    $.ajax({
      type: "POST",
      url: "/modify",
      data: dataString,
      success: function () {
        $("#contact_form").html("<div id='message'></div>");
        $("#message")
          .html("<h2>Contact Form Submitted!</h2>")
          .append("<p>We will be in touch soon.</p>")
          .hide()
          .fadeIn(1500, function () {
            $("#message").append(
              "<img id='checkmark' src='images/check.png' />"
            );
          });
      }
    });
    e.preventDefault();
});
*/