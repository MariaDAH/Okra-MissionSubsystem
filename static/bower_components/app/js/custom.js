//keep an eye on an uploaded file in sign up form input and fire an event called fileselect when a file is chosen:
$(document).on('change', ':file', function() {

    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);

});



$('document').ready(function(){


    //Test feedback when uploading a file
     $(':file').on('fileselect', function(event, numFiles, label) {

        console.log(numFiles);
        console.log(label);
        $("#filetext").value=label;
    });

    $('#selectimg').on('click', function(){

          var img=$('input:file').val();
          console.log(img);
          $("#avatar").attr('src',img);
          //$("#avatar").append("<object width='100%' height='100%' data="+ img + "></object>")

          $("#avatar").ready(function() {
              var $doc = $("#avatar").contentWindow.document;
              var $body = $("<body>").text("Test");
              $body.insertAfter($doc);
          });
    });

    $("#login").click(function(){

       var section = document.getElementById('mainSection');
       if(section != undefined)
       {
         section.remove();
       }
       $("#searchpnl").hide();
       $("#registerpnl").hide();
       $("#signuppnl").hide();
       $("#loginpnl").slideToggle('slow');

    })

    $("#search").click(function(){

      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
       $("#loginpnl").hide();
       $("#registerpnl").hide();
       $("#signuppnl").hide();
       $("#searchpnl").slideToggle('slow');

    })

    $("#register").click(function(){

      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
       $("#loginpnl").hide();
       $("#searchpnl").hide();
       $("#signuppnl").hide();
       $("#registerpnl").slideToggle('slow');

    })

    $("#signup").click(function(){

      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
      $("#loginpnl").hide();
      $("#searchpnl").hide();
      $("#registerpnl").hide();
      $("#signuppnl").slideToggle('slow');

    })

    document.querySelector("#signup-panel").addEventListener('click',function(event){

        hide = function(){
           loaderDiv.style.display = "none";
           $("#signuppnl").show();
           $("#mainSection").hide();
        };

        var loaderDiv = document.getElementById("loaderDiv");
        loaderDiv.style.display = "block";
        setTimeout(hide, 5000); // 5 seconds

    }, false)


})









