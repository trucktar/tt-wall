$(function () {
  $('[data-toggle="tooltip"]').tooltip();

  $('[data-toggle="tooltip"]').click(function () {
    $("input#imageLink").get(0).select();
    document.execCommand("copy");
  });

  $("#image-modal").on("show.bs.modal", function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal

    var imageUrl = button.data("imageurl");
    var imageName = button.data("imagename");
    var imageDesc = button.data("imagedesc");

    var modal = $(this);
    modal.find("#image").attr("src", imageUrl);
    modal.find("#imageName").text(imageName);
    modal.find("#imageDesc").text(imageDesc);
    modal.find("#imageLink").val(imageUrl);
  });
});
